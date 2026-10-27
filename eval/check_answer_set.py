"""Validate eval/answer_set.json and print counts. Loads no model: the corpus (source, article) pairs are read
directly from the Chroma SQLite metadata of the index.

    python eval/check_answer_set.py

Entry format:
    {"id": "...", "question": "...", "language": "ar|fr|en", "expected": "answer|clarify|refuse",
     "gold": [{"source": "PenalFr.pdf", "article": "218"}, ...],   # non-empty for answer, empty otherwise
     "reference_points": ["...", ...],                                # answer only, non-empty
     "reason": "..."}                                                 # clarify / refuse only, non-empty
"""
import sys
import json
import sqlite3
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from config import DB_DIR

SET_PATH = ROOT / "eval" / "answer_set.json"
LANGS = {"ar", "fr", "en"}
EXPECTED = {"answer", "clarify", "refuse"}


def corpus_index():
    """-> ({(source, article or article_label)}, {source: law_type}), or (None, None) if the index is missing."""
    db = Path(DB_DIR) / "chroma.sqlite3"
    if not db.exists():
        return None, None
    con = sqlite3.connect(f"file:{db.as_posix()}?mode=ro", uri=True)
    meta = {}
    for cid, key, val in con.execute(
            "select id, key, string_value from embedding_metadata where key in ('source','article','article_label','law_type')"):
        meta.setdefault(cid, {})[key] = val
    con.close()
    pairs, law = set(), {}
    for m in meta.values():
        pairs.add((m.get("source"), m.get("article")))
        pairs.add((m.get("source"), m.get("article_label")))
        law[m.get("source")] = m.get("law_type")
    return pairs, law


def check(entries, pairs) -> list[str]:
    errors, seen = [], set()
    if not isinstance(entries, list):
        return ["the file must contain a JSON list"]
    for k, e in enumerate(entries):
        where = f"entry {k} (id={e.get('id') if isinstance(e, dict) else '?'})"
        if not isinstance(e, dict):
            errors.append(f"{where}: not an object"); continue
        for key in ("id", "question", "language", "expected"):
            if not e.get(key):
                errors.append(f"{where}: missing '{key}'")
        if e.get("id") in seen:
            errors.append(f"{where}: duplicate id")
        seen.add(e.get("id"))
        if e.get("language") not in LANGS:
            errors.append(f"{where}: language must be one of {sorted(LANGS)}")
        exp, gold = e.get("expected"), e.get("gold", [])
        if exp not in EXPECTED:
            errors.append(f"{where}: expected must be one of {sorted(EXPECTED)}")
        elif exp == "answer":
            if not isinstance(gold, list) or not gold:
                errors.append(f"{where}: answer needs a non-empty gold list")
            else:
                for g in gold:
                    if not (isinstance(g, dict) and g.get("source") and g.get("article")):
                        errors.append(f"{where}: gold item {g!r} needs 'source' and 'article'")
                    elif pairs is not None and (g["source"], str(g["article"])) not in pairs:
                        errors.append(f"{where}: gold ({g['source']}, {g['article']}) not found in the corpus index")
            rp = e.get("reference_points")
            if not (isinstance(rp, list) and rp and all(isinstance(x, str) and x.strip() for x in rp)):
                errors.append(f"{where}: answer needs a non-empty reference_points list of strings")
        else:
            if gold:
                errors.append(f"{where}: {exp} must have an empty gold list")
            if not (isinstance(e.get("reason"), str) and e["reason"].strip()):
                errors.append(f"{where}: {exp} needs a non-empty 'reason'")
    return errors


def main():
    entries = json.loads(SET_PATH.read_text(encoding="utf-8"))
    pairs, law = corpus_index()
    if pairs is None:
        print(f"WARNING: no index at {DB_DIR}; the gold-exists-in-corpus check is SKIPPED.")
    else:
        print(f"Corpus index: {len(law)} sources, {len(pairs)} (source, article) keys, read from {DB_DIR}")

    errors = check(entries, pairs)
    ok = entries if isinstance(entries, list) else []
    print(f"\nTotal entries: {len(ok)}")
    print("By expected:", dict(Counter(e.get("expected") for e in ok if isinstance(e, dict))) or "{}")
    print("By language:", dict(Counter(e.get("language") for e in ok if isinstance(e, dict))) or "{}")

    if law is not None:
        per_code = Counter()
        for e in ok:
            if isinstance(e, dict) and e.get("expected") == "answer":
                for code in {law.get(g.get("source")) for g in e.get("gold", []) if isinstance(g, dict)} - {None}:
                    per_code[code] += 1
        print("By source (answer questions per code):")
        for code in sorted(set(law.values())):
            n = per_code[code]
            print(f"  {code:<28}{n:>4}{'   WARNING: no question' if n == 0 else ''}")

    if errors:
        print(f"\nINVALID: {len(errors)} problem(s)")
        for msg in errors:
            print("  -", msg)
        sys.exit(1)
    print("\nAll entries valid.")


if __name__ == "__main__":
    main()
