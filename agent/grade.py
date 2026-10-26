from pydantic import BaseModel
from analyze import llm
from llm_retry import invoke_with_retry

GRADE_CHARS = 500     # characters of each article shown to the model


class Grade(BaseModel):
    enough: bool
    relevant_ids: list[str] = []
    missing: str = ""

structured_llm = llm.with_structured_output(Grade, method="json_schema")


GRADE_PROMPT = """
You check whether articles retrieved from the TUNISIAN legal codes are enough to answer a legal question.
The question may be in French, Arabic or English; the articles are in French.

Each article is shown as: [chunk id] source, article number, then the start of its text
(cut after __CHARS__ characters, so the end of a long article may be missing).

enough:
- true only if the articles shown contain the article(s) that state the rule answering the question:
  the condition, right, obligation, penalty or time limit the question asks about.
- Generic, definitional or procedural articles alone are not enough. An article that only defines a term,
  announces a chapter, refers to other texts or describes a procedure around the rule does not state the rule.
- An article that states the rule is enough even if some details (amounts, exceptions) are elsewhere.
- Do not lean towards true or towards false: decide from what the articles actually say.

relevant_ids:
- The chunk ids of the articles that help answer the question, copied exactly as shown.
  Only ids that were shown. Empty list if none helps.

missing:
- If enough is false: ONE short French legal phrase (2 to 8 words) naming the rule that is missing.
  No article number, no sentence.
- If enough is true: an empty string.

Example (illustration only):
Question: "Quelle est la peine pour la pêche sans permis ?"
Articles shown: one defines the fishing gear, one lists the authorities that deliver permits.
Result: enough = false, relevant_ids = [], missing = "sanction de la pêche sans permis"

Fill in the structured result only. No other text.
""".replace("__CHARS__", str(GRADE_CHARS))


def format_evidence(evidence: dict, chars: int = GRADE_CHARS) -> str:
    """evidence: chunk_id -> {source, article, law_type, text}."""
    blocks = []
    for cid, e in evidence.items():
        text = " ".join((e.get("text") or "").split())[:chars]
        blocks.append(f"[{cid}] {e.get('source')}, article {e.get('article')}\n{text}")
    return "\n\n".join(blocks) if blocks else "(no articles retrieved)"


def grade(question: str, evidence: dict) -> Grade:
    user_msg = f"Question: {question}\n\nArticles:\n{format_evidence(evidence)}"
    g = invoke_with_retry(structured_llm, [("system", GRADE_PROMPT), ("human", user_msg)], "Grade")
    g.relevant_ids = [i for i in g.relevant_ids if i in evidence]      # keep only ids that were shown
    return g
