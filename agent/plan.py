from typing import Optional
from pydantic import BaseModel, Field
from analyze import Code, llm
from codes import codes_block

class SubQuery(BaseModel):
    text: str
    code: Optional[Code] = None

class Plan(BaseModel):
    sub_queries: list[SubQuery] = Field(min_length=1, max_length=4)

structured_llm = llm.with_structured_output(Plan, method="json_schema")


PLAN_PROMPT = """
You turn a legal question into search queries for a database of TUNISIAN legal codes.
The codes are written in French, so every query you write MUST be in French,
whatever language the question is in (fr, ar or en). Translate the legal idea
into the French legal term a Tunisian code would use.

How many queries:
- Simple question about one legal idea: ONE query.
- Question that mixes several ideas or several areas of law: one query per idea,
  at most 4. Each query searches ONE idea only.

How to write a query:
- 2 to 8 words, only the legal concepts. Like a keyword search, not a sentence.
- Use French legal vocabulary only. No English words, even for foreign concepts:
  write "sentence arbitrale", not "award".
- Use the term the law itself would use (e.g. "bail", "préavis", "héritier").
- NEVER write an article number. Only keep a number if the user wrote one in
  the question (e.g. the user asks about "article 40"); then keep it as the user wrote it.
- NEVER add filler: no "article relatif à", no "alinéa", no "selon la jurisprudence",
  no "conformément à la loi", and no words copied from this prompt.
- Do not invent facts that are not in the question.

__CODES__

The code field:
- Set code to an allowed code only when exactly one allowed code clearly contains
  the answer to that query.
- If more than one allowed code could contain the answer, set code to null.
- If the allowed list is empty, set code to null.
- Never use a code that is not in the allowed list.

Examples (illustration only):

Question: "Quelle est la responsabilité du dirigeant ?"
Allowed codes: ["societes", "commerce"]
Queries:
- {text: "responsabilité du dirigeant", code: null}

Question: "My neighbour built a wall on my land, what can I do?"
Allowed codes: ["droits_reels"]
Queries:
- {text: "construction sur le terrain d'autrui", code: "droits_reels"}

Question: "Mon employeur ne m'a pas payé et je veux porter plainte"
Allowed codes: ["travail", "procedure_civile"]
Queries:
- {text: "paiement du salaire par l'employeur", code: "travail"}
- {text: "action en justice pour créance de salaire", code: "procedure_civile"}

Bad query: "article relatif à la capacité de l'alinéa 2 selon la jurisprudence"
Good query: "capacité de contracter du mineur"

Fill in the structured result only. No other text.
"""
PLAN_PROMPT = PLAN_PROMPT.replace("__CODES__", codes_block())


def make_plan(question: str, language: str, target_codes: list) -> Plan:
    user_msg = (
        f"Question: {question}\n"
        f"Question language: {language}\n"
        f"Allowed codes: {target_codes}"
    )
    return structured_llm.invoke([("system", PLAN_PROMPT), ("human", user_msg)])