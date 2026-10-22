
import re
import logging
import textwrap
from pathlib import Path
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from config import DB_DIR, DATA_DIR, EMBEDDING_MODEL, LLM_MODEL, GROQ_API_KEY, SUBQUERY_N
from loaders import load_all_documents
from splitter import split_by_article
from retriever import hybrid_retrieve, detect_arabic, detect_english
from translate import rewrite_query, generate_subqueries
from reranker import rerank

logger = logging.getLogger(__name__)

_embeddings: HuggingFaceEmbeddings | None = None


def get_embeddings() -> HuggingFaceEmbeddings:
    global _embeddings
    if _embeddings is None:
        logger.info("Loading embedding model: %s", EMBEDDING_MODEL)
        _embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    return _embeddings


_SYSTEM_PROMPT = textwrap.dedent("""
    You are an expert Tunisian legal assistant. Legal source documents are written in French or Arabic.
    Users may submit questions in French, Arabic, or English.

    STRICT GROUNDING RULES — violating any of these is an error:
    1. Base your answer EXCLUSIVELY on the provided context passages.
       Never add information, penalties, dates, or article numbers not present in the context.
    2. If the context does not contain enough information to answer, say so explicitly.
       Do NOT guess, infer, or use general legal knowledge.
    3. If context passages are in a different language from the question, translate only
       the parts you cite — do not paraphrase beyond what the text says.
    4. Respond in the SAME language as the user's question.

    REQUIRED RESPONSE STRUCTURE
    Use the section labels that match your response language:

    **Direct Answer / Réponse directe / الإجابة المباشرة:**
    One or two sentences directly answering the question.

    **Applicable Articles / Articles applicables / الفصول المنطبقة:**
    For each relevant article: state the article number, source code, and summarise its content.
    Be exhaustive — list every relevant article found in the context.

    **Source(s):**
    Name(s) of the source document(s).

    **Explanation / Explication / شرح:**
    Brief legal explanation of how the cited articles answer the question.
    Highlight any important conditions, exceptions, or cross-references found in the context.

    ── Context ──────────────────────────────────────────────────────────────────
    {context}
""").strip()

_PROMPT = ChatPromptTemplate.from_messages([
    ("system", _SYSTEM_PROMPT),
    ("human", "{input}"),
])

_ARTICLE_RE = re.compile(r"\b\d+\b")


def _is_complex(question: str) -> bool:
    if _ARTICLE_RE.search(question):
        return False
    return len(question.split()) >= 4


# ── Vectorstore management ───────────────────────────────────────────────────
def build_vectorstore(folder: Path = DATA_DIR) -> Chroma:
    docs   = load_all_documents(folder)
    chunks = split_by_article(docs)
    logger.info("Embedding %d chunks → ChromaDB at '%s'", len(chunks), DB_DIR)
    return Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        persist_directory=str(DB_DIR),
        ids=[c.metadata["chunk_id"] for c in chunks],
    )


def load_vectorstore() -> Chroma:
    return Chroma(
        persist_directory=str(DB_DIR),
        embedding_function=get_embeddings(),
    )


def step_rewrite(question: str) -> str:
    return rewrite_query(question)


def step_subqueries(french_query: str, n: int = SUBQUERY_N) -> list[str]:
    return generate_subqueries(french_query, n=n)


def step_retrieve(
    vectorstore: Chroma,
    question: str,
    french_query: str,
    sub_queries: list[str],
    law_type: str | None,
) -> list[Document]:
    article_match = _ARTICLE_RE.search(question)
    if article_match:
        from retriever import _direct_lookup, MMR_K
        docs = _direct_lookup(vectorstore, article_match.group(0), law_type, MMR_K)
        if docs:
            logger.debug("Direct article lookup hit: %s", article_match.group(0))
            return docs

    all_queries = [french_query] + sub_queries
    return hybrid_retrieve(vectorstore, all_queries, question, law_type)


def step_rerank(french_query: str, candidates: list[Document]) -> list[Document]:
    return rerank(french_query, candidates)


def step_generate(question: str, docs: list[Document]) -> str:
    context_blocks = [
        f"[{doc.metadata.get('source', 'unknown')} — Article {doc.metadata.get('article', '?')}]\n"
        f"{doc.page_content}"
        for doc in docs
    ]
    context = "\n\n---\n\n".join(context_blocks)
    llm = ChatGroq(api_key=GROQ_API_KEY, model_name=LLM_MODEL, temperature=0.1)
    return (_PROMPT | llm | StrOutputParser()).invoke({
        "context": context,
        "input":   question,
    })


def ask_question(
    vectorstore: Chroma,
    question: str,
    law_type: str | None = None,
) -> tuple[str, list[Document]]:
    is_arabic  = detect_arabic(question)
    is_english = detect_english(question)

    french_query = step_rewrite(question)
    logger.info("Rewritten query: %r", french_query)

    sub_queries: list[str] = []
    if _is_complex(question):
        sub_queries = step_subqueries(french_query)
        logger.info("Sub-queries: %s", sub_queries)

    candidates = step_retrieve(vectorstore, question, french_query, sub_queries, law_type)

    if not candidates:
        if is_arabic:
            msg = "لم يتم العثور على معلومات ذات صلة في الوثائق."
        elif is_english:
            msg = "No relevant information found in the legal documents."
        else:
            msg = "Aucune information pertinente trouvée dans les documents juridiques."
        return msg, []
    docs = step_rerank(french_query, candidates)
    answer = step_generate(question, docs)

    return answer, docs
