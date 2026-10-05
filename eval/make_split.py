"""Deterministic dev/test split of eval/questions.json by concept_id (~25% dev).

All languages/variants of a concept land on the same side, so a topic never
straddles the split. Concepts are stratified by domain (the prefix of the
concept_id): within each domain they are ordered by sha1(concept_id) and the
first round(0.25 * n) go to dev (at least 1 when the domain has 3+ concepts).
Re-running gives the identical result; labels do not influence the split.
"""
import hashlib
import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent
DEV_FRACTION = 0.25


def main() -> None:
    questions = json.loads((HERE / "questions.json").read_text(encoding="utf-8"))
    by_domain: dict[str, set[str]] = defaultdict(set)
    for q in questions:
        by_domain[q["concept_id"].split("_")[0]].add(q["concept_id"])

    dev: list[str] = []
    for domain, concepts in sorted(by_domain.items()):
        ordered = sorted(concepts, key=lambda c: hashlib.sha1(c.encode()).hexdigest())
        n_dev = int(DEV_FRACTION * len(ordered) + 0.5)
        if len(ordered) >= 3:
            n_dev = max(n_dev, 1)
        dev += ordered[:n_dev]

    all_concepts = sorted({q["concept_id"] for q in questions})
    split = {
        "method": "stratified by domain prefix, sha1(concept_id) order, ~25% dev",
        "dev":  sorted(dev),
        "test": sorted(set(all_concepts) - set(dev)),
    }
    (HERE / "split.json").write_text(json.dumps(split, indent=1), encoding="utf-8")
    n_dev_q = sum(q["concept_id"] in set(dev) for q in questions)
    print(f"{len(split['dev'])} dev concepts ({n_dev_q} questions), "
          f"{len(split['test'])} test concepts ({len(questions) - n_dev_q} questions)")


if __name__ == "__main__":
    main()
