"""Apply approved label changes from eval/review_suggestions.json to eval/questions.json.

    python eval/apply_labels.py --approve penal_theft penal_homicide ...
    python eval/apply_labels.py --approve-all-except penal_self_defence coc_seller_duties

Only the listed concepts change. Each proposed gold entry is resolved against the clean index
(db_v1_1) to exact `chunk_ids` (any-of: a sub-numbered series such as 14 / 14 bis / 14 ter is one
entry). The entry keeps `source`, `article` and `anchor` so results from the v1 index (which has no
chunk ids) can still be scored. `label_status` becomes "verified" and the rationale is stored in
`label_note`; concepts you did not approve keep their gold and stay "unverified".
"""
import argparse
import json
from pathlib import Path

from make_review_sheet import Corpus

HERE = Path(__file__).parent
ROOT = HERE.parent


def main() -> None:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--approve", nargs="+", metavar="CONCEPT")
    g.add_argument("--approve-all-except", nargs="*", metavar="CONCEPT")
    ap.add_argument("--db", default=str(ROOT / "db_v1_1"))
    args = ap.parse_args()

    questions = json.loads((HERE / "questions.json").read_text(encoding="utf-8"))
    suggestions = json.loads((HERE / "review_suggestions.json").read_text(encoding="utf-8"))
    approved = set(args.approve) if args.approve else set(suggestions) - set(args.approve_all_except)
    unknown = approved - set(suggestions)
    if unknown:
        raise SystemExit(f"unknown concept ids: {sorted(unknown)}")
    corpus = Corpus(Path(args.db))

    resolved: dict[str, list[dict]] = {}
    for cid in approved:
        entries = []
        for e in suggestions[cid]["proposed_gold"]:
            entry = {k: v for k, v in e.items() if k != "multi"}
            if e["source"] != "*":
                ids = corpus.resolve(e)
                if not ids or (len(ids) > 1 and not e.get("multi")):
                    raise SystemExit(f"{cid}: entry {e['source']} art {e['article']} resolves to {len(ids)} chunks: {ids}")
                entry["chunk_ids"] = ids
            entries.append(entry)
        resolved[cid] = entries

    changed = 0
    for q in questions:
        if q["concept_id"] in approved:
            q["gold"] = resolved[q["concept_id"]]
            q["label_status"] = "verified"
            q["label_note"] = suggestions[q["concept_id"]]["rationale"]
            changed += 1
    (HERE / "questions.json").write_text(json.dumps(questions, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(approved)} concepts approved, {changed} questions updated")


if __name__ == "__main__":
    main()
