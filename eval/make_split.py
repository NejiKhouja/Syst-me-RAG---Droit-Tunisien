"""Deterministic dev/test split of eval/questions.json by concept_id (~40% dev).

All languages/variants of a concept land on the same side, so a topic never
straddles the split. Among SEEDED random candidate splits (whole concepts, about
40% of questions in dev) we keep the one whose dev share is closest to 40% in
every stratum at once: law domain, language, filtered/unfiltered, and question
category. Labels do not influence the split. Same seed + same questions ->
same split; the seed and the achieved balance are stored in eval/split.json.

    python eval/make_split.py
"""
import json
import random
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent
SEED = 20261022
N_CANDIDATES = 50_000
DEV_FRACTION = 0.40


def strata(q: dict) -> list[str]:
    return [
        "domain:" + q["concept_id"].split("_")[0],
        "lang:" + q["language"],
        "scope:" + ("unfiltered" if q["law_type"] is None else "filtered"),
        "category:" + q["category"],
    ]


def main() -> None:
    questions = json.loads((HERE / "questions.json").read_text(encoding="utf-8"))
    by_concept: dict[str, list[dict]] = defaultdict(list)
    for q in questions:
        by_concept[q["concept_id"]].append(q)
    concepts = sorted(by_concept)

    total: dict[str, int] = defaultdict(int)
    per_concept: dict[str, dict[str, int]] = {}
    for c, qs in by_concept.items():
        counts: dict[str, int] = defaultdict(int)
        for q in qs:
            for s in strata(q):
                counts[s] += 1
                total[s] += 1
        per_concept[c] = counts
    n_q = len(questions)
    n_concepts_dev = round(DEV_FRACTION * len(concepts))

    def cost(dev: list[str]) -> float:
        got: dict[str, int] = defaultdict(int)
        dev_q = 0
        for c in dev:
            dev_q += len(by_concept[c])
            for s, n in per_concept[c].items():
                got[s] += n
        # global size term + every stratum's deviation from the target share (weighted by sqrt of its size)
        c_total = 3.0 * abs(dev_q / n_q - DEV_FRACTION)
        c_strata = sum(abs(got[s] / t - DEV_FRACTION) * (t ** 0.5) for s, t in total.items()) / sum(t ** 0.5 for t in total.values())
        return c_total + c_strata

    rng = random.Random(SEED)
    best, best_cost = None, float("inf")
    for _ in range(N_CANDIDATES):
        cand = rng.sample(concepts, n_concepts_dev)
        k = cost(cand)
        if k < best_cost:
            best, best_cost = sorted(cand), k

    dev = set(best)
    report = {}
    for s, t in sorted(total.items()):
        d = sum(per_concept[c].get(s, 0) for c in dev)
        report[s] = f"{d}/{t} dev ({d / t * 100:.0f}%)"
    split = {
        "method": f"seeded random search over {N_CANDIDATES} whole-concept splits "
                  f"({n_concepts_dev} of {len(concepts)} concepts in dev); kept the split whose dev share is closest to "
                  f"{DEV_FRACTION:.0%} in every stratum (domain, language, filtered/unfiltered, category)",
        "seed": SEED,
        "n_candidates": N_CANDIDATES,
        "cost": round(best_cost, 4),
        "dev_questions": sum(len(by_concept[c]) for c in dev),
        "total_questions": n_q,
        "balance": report,
        "dev": sorted(dev),
        "test": sorted(set(concepts) - dev),
    }
    (HERE / "split.json").write_text(json.dumps(split, indent=1), encoding="utf-8")
    print(f"dev: {len(dev)} concepts, {split['dev_questions']}/{n_q} questions (cost {best_cost:.4f})")
    for s, v in report.items():
        print(f"  {s:<28}{v}")


if __name__ == "__main__":
    main()
