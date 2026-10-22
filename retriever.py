import re
import logging
from langchain_chroma import Chroma
from langchain_core.documents import Document

from config import MMR_K, BM25_K, RERANK_POOL, FUSION, RRF_K

logger = logging.getLogger(__name__)

_ARABIC_RE       = re.compile(r"[؀-ۿ]")
_FRENCH_ACCENTS  = re.compile(r"[éèêëàâùûôîïçœæ]", re.IGNORECASE)
_EN_MARKERS      = {
    "the", "what", "are", "is", "does", "how", "can", "which", "who",
    "when", "where", "define", "explain", "what's", "i", "my", "do",
}


def detect_arabic(text: str) -> bool:
    arabic = sum(1 for _ in _ARABIC_RE.finditer(text))
    return arabic > len(text) * 0.2


def detect_english(text: str) -> bool:
    if detect_arabic(text):
        return False
    if _FRENCH_ACCENTS.search(text):
        return False
    return bool(set(text.lower().split()) & _EN_MARKERS)


# BM25 (fallback)
try:
    from langchain_community.retrievers import BM25Retriever as _BM25Cls
    _BM25_AVAILABLE = True
except ImportError:
    _BM25_AVAILABLE = False
    logger.warning(
        "rank_bm25 not installed — BM25 retrieval disabled. "
        "Run: pip install rank_bm25"
    )

_bm25_instance = None   # built once per process from the Chroma corpus


def _get_bm25(vectorstore: Chroma):
    global _bm25_instance
    if not _BM25_AVAILABLE:
        return None
    if _bm25_instance is not None:
        return _bm25_instance
    try:
        result = vectorstore._collection.get(include=["documents", "metadatas"])
        if not result["documents"]:
            logger.warning("Chroma collection is empty — BM25 index not built")
            return None
        docs = [
            Document(page_content=text, metadata=meta)
            for text, meta in zip(result["documents"], result["metadatas"])
        ]
        # Use k * 4 internally so post-hoc domain filtering still leaves enough
        _bm25_instance = _BM25Cls.from_documents(docs, k=BM25_K * 4)
        logger.info("BM25 index built from %d documents", len(docs))
        return _bm25_instance
    except Exception as exc:
        logger.warning("BM25 index build failed (%s) — semantic-only mode", exc)
        return None


def _build_filter(law_type: str | None, article_num: str | None = None) -> dict | None:
    parts: list[dict] = []
    if law_type:
        parts.append({"law_type": {"$eq": law_type}})
    if article_num:
        parts.append({"article": {"$eq": article_num}})
    if not parts:
        return None
    return parts[0] if len(parts) == 1 else {"$and": parts}


def _deduplicate(docs: list[Document]) -> list[Document]:
    """Remove duplicate chunks by chunk_id (fallback: source + article). Preserves first-seen order."""
    seen: set = set()
    out:  list[Document] = []
    for doc in docs:
        key = doc.metadata.get("chunk_id") or (doc.metadata.get("source"), doc.metadata.get("article"))
        if key not in seen:
            seen.add(key)
            out.append(doc)
    return out


def _semantic_search(
    vectorstore: Chroma,
    query: str,
    law_type: str | None,
    k: int,
) -> list[Document]:
    docs = vectorstore.similarity_search(query, k=k, filter=_build_filter(law_type))
    if not docs and law_type:
        logger.debug("Domain filter '%s' returned nothing — retrying without filter", law_type)
        docs = vectorstore.similarity_search(query, k=k)
    return docs


def _bm25_search(bm25, query: str, law_type: str | None, k: int) -> list[Document]:
    candidates = bm25.invoke(query)
    if law_type:
        candidates = [d for d in candidates if d.metadata.get("law_type") == law_type]
    return candidates[:k]


def _direct_lookup(
    vectorstore: Chroma,
    article_num: str,
    law_type: str | None,
    k: int,
) -> list[Document]:
    query = f"Article {article_num}"
    # Try with full filter first (domain + article number)
    docs = vectorstore.similarity_search(
        query, k=k, filter=_build_filter(law_type, article_num)
    )
    if docs:
        return docs
    # Relax to domain-only
    docs = vectorstore.similarity_search(query, k=k, filter=_build_filter(law_type))
    return docs


def _doc_key(doc: Document):
    return doc.metadata.get("chunk_id") or (doc.metadata.get("source"), doc.metadata.get("article"))


def _fuse(ranked_lists: list[list[Document]]) -> list[Document]:
    """Merge ranked lists into one candidate order.
    rrf: reciprocal rank fusion, score(d) = sum over lists of 1 / (RRF_K + rank), so a chunk that several
    sources rank highly beats one that a single source ranks first. roundrobin: rank 1 of every list, then rank 2, ..."""
    if FUSION == "roundrobin":
        merged: list[Document] = []
        for rank in range(max((len(l) for l in ranked_lists), default=0)):
            for l in ranked_lists:
                if rank < len(l):
                    merged.append(l[rank])
        return merged
    scores: dict = {}
    first: dict = {}
    for l in ranked_lists:
        for rank, doc in enumerate(l, 1):
            key = _doc_key(doc)
            scores[key] = scores.get(key, 0.0) + 1.0 / (RRF_K + rank)
            first.setdefault(key, doc)
    return [first[k] for k in sorted(scores, key=lambda k: -scores[k])]


def hybrid_retrieve(
    vectorstore: Chroma,
    queries: list[str],
    original_query: str,
    law_type: str | None = None,
) -> list[Document]:
    # One ranked list per evidence source, then a round-robin merge (rank 1 of every list, rank 2 ...)
    # so that truncating to RERANK_POOL keeps the best of each source instead of only the first source.
    ranked_lists: list[list[Document]] = []

    for query in queries:
        docs = _semantic_search(vectorstore, query, law_type, k=MMR_K)
        ranked_lists.append(docs)
        logger.debug("semantic(%r): %d docs", query[:60], len(docs))

    bm25 = _get_bm25(vectorstore)
    if bm25:
        bm25_docs = _bm25_search(bm25, queries[0], law_type, k=BM25_K)
        ranked_lists.append(bm25_docs)
        logger.debug("BM25(%r): %d docs", queries[0][:60], len(bm25_docs))

    if detect_arabic(original_query) or detect_english(original_query):
        orig_docs = _semantic_search(vectorstore, original_query, law_type, k=10)
        ranked_lists.append(orig_docs)
        logger.debug("multilingual fallback: %d docs", len(orig_docs))

    merged = _fuse(ranked_lists)

    deduped = _deduplicate(merged)
    if RERANK_POOL:
        deduped = deduped[:RERANK_POOL]
    logger.debug(
        "hybrid_retrieve: %d raw -> %d unique | %d queries",
        len(merged), len(deduped), len(queries),
    )
    return deduped


def retrieve(
    vectorstore: Chroma,
    question: str,
    law_type: str | None = None,
    k: int = MMR_K,
    search_query: str | None = None,
) -> list[Document]:
    article_match = re.search(r"\b(\d+)\b", question)
    if article_match:
        docs = _direct_lookup(vectorstore, article_match.group(1), law_type, k)
        if docs:
            return docs

    primary = search_query or question
    return hybrid_retrieve(vectorstore, [primary], question, law_type)
