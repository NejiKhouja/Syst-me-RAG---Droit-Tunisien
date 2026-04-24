import sys
import io
import logging
from dataclasses import dataclass

# Force UTF-8 output so Arabic text prints correctly on Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

from pipeline import load_vectorstore, step_rewrite, step_subqueries, step_retrieve, step_rerank, _is_complex

logging.basicConfig(level=logging.WARNING)


@dataclass
class TestCase:
    question:          str
    law_type:          str | None
    expected_articles: set[str]
    description:       str
    language:          str


TEST_CASES: list[TestCase] = [
    # French
    TestCase("Quelle est la peine pour le vol ?",                            "penal",               {"258","260","261","262"}, "Theft penalty",         "fr"),
    TestCase("Qu'est-ce que le meurtre ?",                                   "penal",               {"201","202","203"},       "Homicide definition",   "fr"),
    TestCase("Quelle est la peine pour la corruption ?",                     "penal",               {"84","85","86"},          "Corruption penalty",    "fr"),
    TestCase("Que dit l'article 24 sur le droit à la vie ?",                 "constitution",        {"24"},                   "Right to life",         "fr"),
    TestCase("Quels sont les droits fondamentaux ?",                         "constitution",        {"24","25","26"},          "Fundamental rights",    "fr"),
    TestCase("Que dit l'article 13 sur la garde à vue ?",                    "procedure_penale",    {"13"},                   "Custody article",       "fr"),
    TestCase("Quelle est la durée légale du travail ?",                      "travail",             {"79","85"},               "Working hours",         "fr"),
    TestCase("Quelles sont les conditions de licenciement ?",                "travail",             {"14","16","23"},          "Dismissal conditions",  "fr"),
    TestCase("Quelles sont les conditions du mariage ?",                     "statut_personnel",    {"5","8","14"},            "Marriage conditions",   "fr"),
    TestCase("Comment se déroule le divorce ?",                              "statut_personnel",    {"29","30","31"},          "Divorce",               "fr"),
    TestCase("Quelles sont les conditions de validité d'un contrat ?",       "obligations_contrats",{"2","3"},                 "Contract validity",     "fr"),
    TestCase("Qu'est-ce que la responsabilité civile ?",                     "obligations_contrats",{"82","83","84"},          "Civil liability",       "fr"),
    TestCase("Que dit l'article 13 ?",                                       None,                  {"13"},                   "Art 13 any domain",     "fr"),

    # Arabic
    TestCase("ما هي عقوبة السرقة؟",                                          "penal",               {"258","260","261","262"}, "Theft penalty",         "ar"),
    TestCase("ما هي عقوبة الرشوة؟",                                          "penal",               {"84","85","86"},          "Corruption penalty",    "ar"),
    TestCase("ماذا ينص الفصل 24 من الدستور؟",                                "constitution",        {"24"},                   "Right to life",         "ar"),
    TestCase("ما هي حقوق الموقوف؟",                                          "procedure_penale",    {"13","70"},               "Detainee rights",       "ar"),
    TestCase("ما هي مدة العمل القانونية؟",                                    "travail",             {"79","85"},               "Working hours",         "ar"),
    TestCase("ما هي شروط الزواج؟",                                           "statut_personnel",    {"5","8","14"},            "Marriage conditions",   "ar"),

    # English
    TestCase("What is the penalty for theft?",                               "penal",               {"258","260","261","262"}, "Theft penalty",         "en"),
    TestCase("What are the conditions for marriage?",                        "statut_personnel",    {"5","8","14"},            "Marriage conditions",   "en"),
    TestCase("What are the fundamental rights?",                             "constitution",        {"24","25","26"},          "Fundamental rights",    "en"),
    TestCase("What are the rights of a detainee?",                           "procedure_penale",    {"13","70"},               "Detainee rights",       "en"),
    TestCase("What is the legal working hours limit?",                       "travail",             {"79","85"},               "Working hours",         "en"),
]


def evaluate(top_k: int = 6) -> None:
    vs = load_vectorstore()

    hits_fr = hits_ar = hits_en = 0
    total_fr = total_ar = total_en = 0
    results = []

    for tc in TEST_CASES:
        # ── Step 1: rewrite ────────────────────────────────────────────────────
        french_q = step_rewrite(tc.question)

        # ── Step 2: sub-queries (same logic as ask_question) ──────────────────
        sub_queries: list[str] = []
        if _is_complex(tc.question):
            sub_queries = step_subqueries(french_q)

        # ── Step 3: hybrid retrieval ───────────────────────────────────────────
        candidates = step_retrieve(vs, tc.question, french_q, sub_queries, tc.law_type)

        # ── Step 4: rerank (end-to-end quality) ───────────────────────────────
        docs = step_rerank(french_q, candidates) if candidates else []
        docs = docs[:top_k]

        retrieved = {doc.metadata.get("article") for doc in docs}
        matched   = retrieved & tc.expected_articles
        hit       = bool(matched)
        results.append((hit, tc, retrieved, matched, french_q, sub_queries))

        if tc.language == "fr":
            hits_fr += int(hit); total_fr += 1
        elif tc.language == "ar":
            hits_ar += int(hit); total_ar += 1
        else:
            hits_en += int(hit); total_en += 1

    # ── Report ─────────────────────────────────────────────────────────────────
    W = 78
    print(f"\n{'='*W}")
    print(f"{'Tunisian Legal RAG — End-to-End Retrieval Evaluation':^{W}}")
    print(f"{'='*W}\n")

    for hit, tc, retrieved, matched, french_q, sub_queries in results:
        icon   = "OK  " if hit else "FAIL"
        lang   = tc.language.upper()
        domain = tc.law_type or "all"
        print(f"  [{icon}] [{lang}] [{domain}]  {tc.description}")
        if not hit:
            print(f"         Q          : {tc.question}")
            print(f"         Rewritten  : {french_q}")
            if sub_queries:
                for i, sq in enumerate(sub_queries, 1):
                    print(f"         Sub-query {i} : {sq}")
            print(f"         Expected   : {tc.expected_articles}")
            print(f"         Got        : {retrieved - {None}}")
        print()

    total    = len(TEST_CASES)
    hits_all = hits_fr + hits_ar + hits_en
    print(f"{'─'*W}")
    print(f"  Overall : {hits_all}/{total}  = {hits_all/total*100:.1f}%")
    if total_fr: print(f"  French  : {hits_fr}/{total_fr} = {hits_fr/total_fr*100:.1f}%")
    if total_ar: print(f"  Arabic  : {hits_ar}/{total_ar} = {hits_ar/total_ar*100:.1f}%")
    if total_en: print(f"  English : {hits_en}/{total_en} = {hits_en/total_en*100:.1f}%")
    print(f"{'='*W}\n")


if __name__ == "__main__":
    evaluate()
