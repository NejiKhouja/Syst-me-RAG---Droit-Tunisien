from pydantic import BaseModel, Field
from analyze import llm
from plan import SubQuery
from codes import codes_block
from grade import format_evidence
from llm_retry import invoke_with_retry


class Reformulation(BaseModel):
    sub_queries: list[SubQuery] = Field(min_length=1, max_length=3)

structured_llm = llm.with_structured_output(Reformulation, method="json_schema")


REFORMULATE_PROMPT = """
You write NEW search queries for a database of TUNISIAN legal codes, because the searches so far did not
find the article that answers the question.

You get: the question and its language, the queries already tried, the articles retrieved so far
(chunk id, source, article number, start of the text) and `missing`, a short phrase naming the rule
that was not found.

Write 1 to 3 queries that look for the missing rule:
- Every query is in French, whatever the language of the question.
- 2 to 8 words, only the legal concepts. Like a keyword search, not a sentence.
- Each query must differ from every query already tried (the same words in another order do not count
  as different).
- Reuse the exact legal terms you see in the retrieved articles: they show how the codes name things.
  Prefer the code's word over an everyday word.
- NEVER write an article number. Only keep a number if the user wrote one in the question; then keep it
  as the user wrote it.
- NEVER add filler: no "article relatif à", no "alinéa", no "selon la jurisprudence",
  no "conformément à la loi", and no words copied from this prompt.
- Do not invent facts that are not in the question.

__CODES__

The code field:
- Set code to a code only when exactly one code clearly contains the missing rule.
- Otherwise set code to null.
- Never use a code that is not in the list above.

Example (illustration only):
Question: "Mon voisin fait du bruit toute la nuit, que risque-t-il ?"
Already tried: ["bruit du voisin la nuit"]
Retrieved articles speak of "tapage nocturne" and of the "tranquillité des habitants".
missing: "sanction du tapage nocturne"
Queries:
- {text: "tapage nocturne troublant la tranquillité", code: null}

Fill in the structured result only. No other text.
""".replace("__CODES__", codes_block())


def reformulate(question: str, language: str, tried_queries: list, evidence: dict, missing: str) -> Reformulation:
    user_msg = (
        f"Question: {question}\n"
        f"Question language: {language}\n"
        f"Already tried: {list(tried_queries)}\n"
        f"missing: {missing}\n\n"
        f"Retrieved articles:\n{format_evidence(evidence)}"
    )
    return invoke_with_retry(structured_llm, [("system", REFORMULATE_PROMPT), ("human", user_msg)], "Reformulate")
