"""Audit LLM-generated search queries (rewrites + sub-queries) in one or more run files.

    python eval/audit_queries.py results/official_v1_temp0.json [more.json ...]

Flags, per query: invented article numbers, "article X"/"alinéa X/Y" placeholders,
jurisprudence/doctrine (the corpus is codes only), invented figures (penalty
durations / amounts, including spelled-out numbers, spaced thousands and 'dinars'),
filler legal words injected by the prompt, and length over 30 words.
A figure/number counts as invented only if it does not already appear in the question.
"""
import json
import re
import sys
from collections import Counter, defaultdict

SPACES = "   "
NUM_WORDS = (r"un|une|deux|trois|quatre|cinq|six|sept|huit|neuf|dix|onze|douze|treize|quinze|seize|"
             r"vingt|trente|quarante|cinquante|soixante|cent|mille|million")
UNITS = r"ans?|années?|mois|jours?|semaines?|heures?|dinars?|dt|tnd|euros?|%|pour\s*cent"
DIGITS = rf"\d[\d{SPACES}.,]*"

# "30 000 dinars", "5 ans", "de 2 à 10 ans", "deux à dix ans", "vingt mille dinars", "emprisonnement à vie" is NOT a figure
FIGURE = re.compile(
    rf"(?:{DIGITS}|\b(?:{NUM_WORDS})\b)(?:[{SPACES}]*(?:à|a|et|-|–|jusqu'à)[{SPACES}]*(?:{DIGITS}|\b(?:{NUM_WORDS})\b))?"
    rf"[{SPACES}]*(?:{NUM_WORDS}[{SPACES}]+)?(?:{UNITS})\b",
    re.IGNORECASE,
)
ARTICLE_NUM = re.compile(r"\b(?:art(?:icles?|\.)?)\s*(\d+)", re.IGNORECASE)
PLACEHOLDER = re.compile(r"\b(?:article|art\.)\s+[XYZNn]\b|alin[ée]a\s+[XYxy](?:\s*/\s*[XYxy])?\b|\balin[ée]as?\s+Y\b", re.IGNORECASE)
JURIS = re.compile(r"jurisprudence|doctrine", re.IGNORECASE)
FILLER = re.compile(r"alin[ée]a|capacit[ée]|consentement", re.IGNORECASE)


def norm_digits(s: str) -> set[str]:
    return {re.sub(rf"[{SPACES}.,]", "", d) for d in re.findall(DIGITS, s) if re.search(r"\d", d)}


def figures(s: str) -> set[str]:
    return {re.sub(rf"[{SPACES}]+", " ", m.group(0)).strip().lower() for m in FIGURE.finditer(s)}


def audit(rows: list[dict]) -> tuple[int, Counter, dict]:
    cnt, ex, total = Counter(), defaultdict(list), 0
    for r in rows:
        q0 = r["question"]
        queries = [("rewrite", r["rewrite"])] + [("sub", s) for s in (r.get("sub_queries") or r.get("subs") or [])]
        for kind, q in queries:
            total += 1
            flags = []
            new_art = {a for a in ARTICLE_NUM.findall(q)} - norm_digits(q0)
            if new_art or (norm_digits(q) - norm_digits(q0) - {""} and ARTICLE_NUM.search(q)):
                flags.append("invented article number")
            if PLACEHOLDER.search(q):
                flags.append('placeholder "article X"/"alinéa X/Y"')
            if JURIS.search(q):
                flags.append("jurisprudence/doctrine")
            if figures(q) - figures(q0):
                flags.append("invented figure (duration/amount)")
            if FILLER.search(q):
                flags.append("filler alinéa/capacité/consentement")
            if len(q.split()) > 30:
                flags.append(">30 words")
            for f in flags:
                cnt[f] += 1
                if len(ex[f]) < 4:
                    ex[f].append((q0, kind, q))
    return total, cnt, ex


def main() -> None:
    for path in sys.argv[1:]:
        data = json.load(open(path, encoding="utf-8"))
        rows = data["cases"] if isinstance(data, dict) else data
        total, cnt, ex = audit(rows)
        print(f"\n== {path}: {total} queries ({len(rows)} rewrites)")
        for flag, n in cnt.most_common():
            print(f"  {n:>4}  {flag}  ({n / total * 100:.0f}%)")
            for q0, kind, q in ex[flag]:
                print(f"        [{kind}] {q0[:40]!r} -> {q[:170]}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
