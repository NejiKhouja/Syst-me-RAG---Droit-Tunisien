"""Apply approved label changes from eval/review_suggestions.json to eval/questions.json.

    python eval/apply_labels.py --approve penal_theft penal_homicide ...
    python eval/apply_labels.py --approve-all-except penal_self_defence coc_seller_duties

Only the listed concepts change: gold is replaced by the reviewed `proposed_gold`
(entries may carry an `anchor`), `label_status` becomes "verified" and the
rationale is stored in `label_note`. Everything else is left untouched.
Concepts you did not approve keep label_status "unverified".
"""
import argparse
import json
from pathlib import Path

HERE = Path(__file__).parent


def main() -> None:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--approve", nargs="+", metavar="CONCEPT")
    g.add_argument("--approve-all-except", nargs="*", metavar="CONCEPT")
    args = ap.parse_args()

    questions = json.loads((HERE / "questions.json").read_text(encoding="utf-8"))
    suggestions = json.loads((HERE / "review_suggestions.json").read_text(encoding="utf-8"))
    approved = set(args.approve) if args.approve else set(suggestions) - set(args.approve_all_except)
    unknown = approved - set(suggestions)
    if unknown:
        raise SystemExit(f"unknown concept ids: {sorted(unknown)}")

    changed = 0
    for q in questions:
        s = suggestions.get(q["concept_id"])
        if q["concept_id"] in approved and s:
            q["gold"] = [{k: v for k, v in e.items() if k != "multi"} for e in s["proposed_gold"]]
            q["label_status"] = "verified"
            q["label_note"] = s["rationale"]
            changed += 1
    (HERE / "questions.json").write_text(json.dumps(questions, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(approved)} concepts approved, {changed} questions updated")


if __name__ == "__main__":
    main()
