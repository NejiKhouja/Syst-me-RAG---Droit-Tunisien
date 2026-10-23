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

- clear: you can tell which area of Tunisian law applies. The exact answer may
  depend on details (type of offence, amount, circumstances); the answer will
  explain those variants. Examples: "What are the legal working hours?",
  "How is a company founded?".
- ambiguous: the question does not say what kind of situation it is about, and
  the answer would come from DIFFERENT areas of law depending on that.
  Ask for that one missing fact. Examples: "How long do I have to file a
  complaint?" (penal, civil or labor?), "Can I get my deposit back?" (rent,
  sale or job?). Missing details such as an amount or a date do NOT make a
  question ambiguous.
- out_of_scope: not about Tunisian law (other countries, general knowledge,
  weather, medical advice, and so on). Example: "How do I cook couscous?".

Rules:
- If you hesitate only because details are missing but the area of law is clear,
  choose clear. If you hesitate because the question could belong to different
  areas of law, choose ambiguous.
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