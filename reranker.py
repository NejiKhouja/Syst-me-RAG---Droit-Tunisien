import logging
from langchain_core.documents import Document
from sentence_transformers import CrossEncoder

from config import RERANKER_MODEL, RERANK_TOP_K

logger = logging.getLogger(__name__)

_reranker: CrossEncoder | None = None


def get_reranker() -> CrossEncoder:
    global _reranker
    if _reranker is None:
        logger.info("Loading cross-encoder: %s", RERANKER_MODEL)
        _reranker = CrossEncoder(RERANKER_MODEL, max_length=512)
    return _reranker


def rerank(query: str, docs: list[Document], top_k: int = RERANK_TOP_K) -> list[Document]:
    if not docs:
        return docs

    try:
        reranker = get_reranker()
        pairs    = [(query, doc.page_content) for doc in docs]
        scores   = reranker.predict(pairs)

        ranked = sorted(zip(scores, docs), key=lambda x: x[0], reverse=True)
        top    = [doc for _, doc in ranked[:top_k]]

        logger.debug(
            "Reranked %d → %d docs | top score=%.3f | bottom kept=%.3f",
            len(docs), top_k, ranked[0][0], ranked[top_k - 1][0],
        )
        return top

    except Exception as exc:
        logger.warning("Reranking failed (%s) — returning original order", exc)
        return docs[:top_k]
