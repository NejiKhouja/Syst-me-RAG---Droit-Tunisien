"""Central configuration for the Tunisian Legal RAG system."""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

DATA_DIR = Path("data")
DB_DIR   = Path("db_v1_1")   # v1 index stays untouched in ./db (rebuilt chunks go here)

GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")

EMBEDDING_MODEL = "OrdalieTech/Solon-embeddings-large-0.1"
LLM_MODEL       = "openai/gpt-oss-120b"
RERANKER_MODEL  = "cross-encoder/mmarco-mMiniLMv2-L12-H384-v1"

# Retrieval knobs
MMR_K        = 20   # semantic candidates per query
BM25_K       = 15   # BM25 candidates (primary query only)
RERANK_TOP_K = 6    # docs returned to the user after reranking
RERANK_ENABLED    = True   # False: keep the retrieval order (ablation)
RERANK_POOL       = 20     # max candidates sent to the reranker (None = all retrieved)
RERANK_MAX_LENGTH = 256    # tokens per (query, passage) pair
RERANK_QUANTIZE   = True   # int8 dynamic quantization of the cross-encoder (CPU speed-up)
RERANK_BATCH      = 16
SUBQUERY_N   = 2    # sub-queries generated for complex (non-article) questions

# Query preparation. RAW_FIRST: French questions are searched as written (no LLM call); Arabic/English are
# translated to French faithfully (no enrichment). USE_SUBQUERIES: LLM sub-queries (v1 behaviour, off).
RAW_FIRST                   = True
USE_SUBQUERIES              = False
TRANSLATE_REASONING_EFFORT  = "low"   # translation needs no deliberation; keeps Groq token use small

# Maps law_type substrings to match against the lowercased PDF filename
LAW_TYPE_MAP: dict[str, list[str]] = {
    "procedure_penale":       ["procedurepenal"],
    "procedure_civile":       ["procedurecivile"],
    "penal":                  ["penal", "crim"],
    "constitution":           ["constitution", "recac", "freeli"],
    "travail":                ["travail"],
    "commerce":               ["commerce"],
    "societes":               ["societe"],
    "obligations_contrats":   ["coc"],
    "statut_personnel":       ["statut", "personnel"],
    "protection_enfant":      ["enfant"],
    "nationalite":            ["nationalite"],
    "arbitrage":              ["arbitrage"],
    "droit_international_prive": ["dip"],
    "droits_reels":           ["dtree", "dreel"],
}

LAW_DISPLAY_NAMES: dict[str | None, str] = {
    None:                        "All Documents",
    "constitution":              "Constitution",
    "penal":                     "Code Pénal",
    "procedure_penale":          "Code de Procédure Pénale",
    "procedure_civile":          "Code de Procédure Civile et Commerciale",
    "obligations_contrats":      "Code des Obligations et Contrats (COC)",
    "commerce":                  "Code de Commerce",
    "societes":                  "Code des Sociétés Commerciales",
    "travail":                   "Code du Travail",
    "statut_personnel":          "Code du Statut Personnel",
    "protection_enfant":         "Code de Protection de l'Enfant",
    "droit_international_prive": "Droit International Privé",
    "droits_reels":              "Droits Réels",
    "arbitrage":                 "Code de l'Arbitrage",
    "nationalite":               "Code de la Nationalité",
}

# PDF cleaning patterns
HEADER_PATTERNS: list[str] = [
    r"Page\s+\d+\s+sur\s+\d+",
    r"Imp[re]+imerie\s+Officielle\s+de\s+la\s+R[eé]publique\s+Tunisienne",
    r"Accès aux lois[^\n]*",
    r"WWW\.LEGISLATION-SECURITE\.TN",
    r"www\.legislation-securite\.tn",
    r"Base de donn[eé]es\s*\n?\s*LA LEGISLATION[^\n]*",
    r"LA LEGISLATION DU SECTEUR[^\n]*",
    r"J\.?O\.?R\.?T\.?\s+n°[^\n]{0,80}",
]

# Used for documentation / potential future augmentation. Not injected into
# queries use rewrite_query() from translate.py for proper translation.
LEGAL_TRANSLATIONS: dict[str, str] = {
    "سرقة":   "vol soustraction frauduleuse",
    "قتل":    "meurtre homicide",
    "اغتصاب": "viol agression sexuelle",
    "احتيال": "escroquerie fraude",
    "رشوة":   "corruption soudoiement",
    "اعتداء": "agression voies de fait",
    "حبس":    "emprisonnement prison",
    "غرامة":  "amende pénalité",
    "إعدام":  "peine de mort",
    "طلاق":   "divorce répudiation",
    "زواج":   "mariage union conditions consentement capacité",
    "ميراث":  "succession héritage",
    "عقد":    "contrat obligation",
    "فسخ":    "résiliation annulation",
    "تعويض":  "indemnisation réparation",
    "موقوف":  "détenu arrestation garde à vue droits",
    "حقوق":   "droits garanties libertés fondamentaux",
    "شروط":   "conditions exigences capacité",
    "اعتقال": "arrestation garde à vue",
    "توقيف":  "détention provisoire garde à vue",
    "محكمة":  "tribunal juridiction",
    "دفاع":   "défense avocat",
    "حرية":   "liberté droit fondamental",
    "عمل":    "travail emploi",
    "عامل":   "travailleur salarié",
    "طفل":    "enfant mineur",
    "جنسية":  "nationalité citoyenneté",
    "شركة":   "société entreprise",
    "عقوبة":  "peine sanction",
    "جريمة":  "crime délit infraction",
    "تحقيق":  "enquête instruction",
    "شاهد":   "témoin témoignage",
    "ضحية":   "victime plaignant",
}
