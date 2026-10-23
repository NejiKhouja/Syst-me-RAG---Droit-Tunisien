from typing import Literal, Optional
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


Code = Literal[
    "arbitrage", "obligations_contrats", "commerce", "droit_international_prive",
    "droits_reels", "protection_enfant", "nationalite", "penal",
    "procedure_civile", "procedure_penale", "societes", "statut_personnel",
    "travail", "constitution",
]

class Analysis(BaseModel):
    reasoning: str = Field(description="One short sentence explaining the intent choice")
    language: Literal["fr","ar", "en"] 
    intent: Literal["clear", "ambiguous", "out_of_scope"]
    target_codes: list[Code] = Field(default_factory=list)
    clarification_question : Optional[str] = None
    

llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0)
structured_llm = llm.with_structured_output(Analysis, method="json_schema")
SYSTEM_PROMPT = """
You analyze questions for a legal assistant that covers TUNISIAN law only.
All questions concern Tunisia, so never ask which country or jurisdiction.
- If only ONE area of law applies, the question is "clear", even when the exact answer depends on the facts (type of offence, amount, circumstances). The answer will explain the variants.
- If you hesitate between clear and ambiguous, choose clear.
Classify the question's intent:

- clear: the question can be answered from one area of Tunisian law, or the
  answer would be the same whichever situation the user is in.
  Examples: "What are the legal working hours?", "How is a company founded?".
- ambiguous: the question could fall under SEVERAL different areas of law and
  the answer would DIFFER between them, or a key fact is missing that changes
  the answer. Examples: "How long do I have to file a complaint?" (penal,
  civil, or labor?), "Am I entitled to compensation?" (for what?).
- out_of_scope: not about Tunisian law (other countries, general knowledge,
  weather, medical advice, and so on). Example: "How do I cook couscous?".

Rules:
- Set target_codes to every code that could apply (empty if out_of_scope).
- If ambiguous, write ONE short clarification_question in the user's language
  that asks for the missing fact. Otherwise leave it null.
- Detect the language of the question (fr, ar or en).
- Fill in the structured result only. No other text.

Allowed codes: arbitrage, obligations_contrats, commerce, droit_international_prive,
droits_reels, protection_enfant, nationalite, penal, procedure_civile,
procedure_penale, societes, statut_personnel, travail, constitution.
"""
def analyze(question: str, language_hint: str | None = None) -> Analysis:
    system = SYSTEM_PROMPT
    if language_hint:
        system += f"\nThe conversation language is '{language_hint}'. Write clarification_question in that language."
    return structured_llm.invoke([("system", system), ("human", question)])