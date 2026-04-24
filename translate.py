
import logging
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from config import GROQ_API_KEY, LLM_MODEL, SUBQUERY_N

logger = logging.getLogger(__name__)

_llm_precise:  ChatGroq | None = None   # temperature=0.0  (deterministic rewrite)
_llm_creative: ChatGroq | None = None   # temperature=0.3  (diverse sub-queries)


def _get_llm(temperature: float = 0.0) -> ChatGroq:
    global _llm_precise, _llm_creative
    if temperature == 0.0:
        if _llm_precise is None:
            _llm_precise = ChatGroq(
                api_key=GROQ_API_KEY, model_name=LLM_MODEL, temperature=0.0
            )
        return _llm_precise
    if _llm_creative is None:
        _llm_creative = ChatGroq(
            api_key=GROQ_API_KEY, model_name=LLM_MODEL, temperature=0.3
        )
    return _llm_creative


# In-process caches
_rewrite_cache:  dict[str, str]       = {}
_subquery_cache: dict[str, list[str]] = {}


_REWRITE_PROMPT = ChatPromptTemplate.from_messages([
    ("system", (
        "You are a Tunisian legal search expert specialising in document retrieval. "
        "Rewrite the user's question as a precise French legal search query. "
        "Rules:\n"
        "  • Translate to French if the question is in Arabic or English.\n"
        "  • Use exact Tunisian legal vocabulary: peine, sanction, emprisonnement, "
        "    disposition, alinéa, capacité, consentement, etc.\n"
        "  • Reference the relevant code when obvious: Code Pénal, Code du Travail, "
        "    Constitution, Code du Statut Personnel, Code des Obligations et Contrats.\n"
        "  • Expand colloquial terms into their formal legal equivalents.\n"
        "  • Output ONLY the rewritten French query — no explanation, no preamble."
    )),
    ("human", "{question}"),
])

_SUBQUERY_PROMPT = ChatPromptTemplate.from_messages([
    ("system", (
        "You are a Tunisian legal expert. "
        "Given a French legal search query, generate {n} distinct, focused sub-queries in French "
        "to ensure comprehensive retrieval of all relevant legal articles. "
        "Each sub-query must target a different legal angle "
        "(e.g. definition, conditions, penalties, procedure, exceptions). "
        "Output exactly {n} lines — one sub-query per line. "
        "No numbering, no bullet points, no explanation."
    )),
    ("human", "{query}"),
])


def rewrite_query(question: str) -> str:

    if question in _rewrite_cache:
        return _rewrite_cache[question]
    try:
        result = (
            _REWRITE_PROMPT | _get_llm(0.0) | StrOutputParser()
        ).invoke({"question": question}).strip()
        logger.debug("rewrite_query: %r → %r", question, result)
        _rewrite_cache[question] = result
        return result
    except Exception as exc:
        logger.warning("Query rewrite failed (%s) — using original", exc)
        return question


def generate_subqueries(french_query: str, n: int = SUBQUERY_N) -> list[str]:
    cache_key = f"{french_query}:{n}"
    if cache_key in _subquery_cache:
        return _subquery_cache[cache_key]
    try:
        raw = (
            _SUBQUERY_PROMPT | _get_llm(0.3) | StrOutputParser()
        ).invoke({"query": french_query, "n": n}).strip()

        # Strip any accidental numbering or bullet characters the LLM may add
        subs = [
            line.strip().lstrip("0123456789.-•) ")
            for line in raw.splitlines()
            if line.strip()
        ]
        subs = [s for s in subs if len(s) > 5][:n]

        if not subs:
            return [french_query]

        logger.debug("generate_subqueries(%r): %s", french_query, subs)
        _subquery_cache[cache_key] = subs
        return subs
    except Exception as exc:
        logger.warning("Sub-query generation failed (%s) — using primary query", exc)
        return [french_query]


def to_french(question: str) -> str:
    return rewrite_query(question)
