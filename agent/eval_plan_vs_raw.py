"""Does the agent's Plan help retrieval? Compare it with the baseline on the DEV split.

Run from the repo root (paths in config.py are absolute, so agent/ works too):
    python agent/eval_plan_vs_raw.py
    python agent/eval_plan_vs_raw.py --split test --i-know-this-uses-the-test-set   # reporting only, never tuning

Variants (same scorer as evaluate.py, top 6, strict chunk/article matching):
  A1  baseline + the dataset's law_type hint      (what the official dev numbers use)
  A2  baseline, NO law_type hint                  (the fair baseline for the agent)
  B1  Analyze -> Plan -> retrieval, code filter from Plan
  B2  same, but no code filter (tests whether a wrong code from Plan hurts)
  C   A2 and B1 merged with the baseline fusion   (baseline query + Plan queries)
  D   Plan with a soft code filter                (only if retrieve_for_plan accepts `soft`)
  E   A2 and D merged

Sanity check: A1 must reproduce the baseline's dev numbers (Hit@6 88.6, Hit@1 57.1,
Recall 54.1, MRR 0.659). If it does not, do not trust the other rows.
"""
import sys
import json
import inspect
import argparse
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))                 # baseline modules: pipeline, evaluate, ...
sys.path.insert(0, str(ROOT / "agent"))       # agent modules: analyze, plan, retrieve

from evaluate import load_questions, score_case, _agg, _fmt, CACHE_PATH
import translate
from eval_harness import install_llm_cache, DegradationCounter
from pipeline import step_query, step_subqueries_if_enabled, step_retrieve, step_rerank
from retriever import _fuse
from analyze import analyze
from plan import make_plan
from retrieve import retrieve_for_plan, get_vs

TOP_K = 6
PLAN_CACHE = ROOT / "agent" / "plan_cache.json"     # Analyze + Plan answers, so Groq is called once per question

VARIANTS = [
    "A1 baseline + law hint",
    "A2 baseline, no hint",
    "B1 plan, code filter",
    "B2 plan, no filter",
    "C  A2 + B1 merged",
]
SOFT_VARIANTS = [
    "D  plan, soft filter",
    "E  A2 + D merged",
]
HAS_SOFT = "soft" in inspect.signature(retrieve_for_plan).parameters


def out_path(split: str) -> Path:
    return ROOT / "results" / f"plan_vs_raw_{split}.json"


def cache_key(question: str, split: str) -> str:
    """dev keeps the bare question (the existing cache); other splits get their own keys."""
    return question if split == "dev" else f"{split}::{question}"


def load_cache() -> dict:
    if PLAN_CACHE.exists():
        return json.loads(PLAN_CACHE.read_text(encoding="utf-8"))
    return {}


def get_plan(question: str, cache: dict, split: str = "dev") -> dict:
    """Run Analyze then Plan once per question; later runs read the cache."""
    key = cache_key(question, split)
    if key in cache:
        return cache[key]
    try:
        a = analyze(question)
        p = make_plan(question, a.language, a.target_codes)
        info = {
            "intent": a.intent,
            "codes": list(a.target_codes),
            "queries": [sq.model_dump() for sq in p.sub_queries],
        }
    except Exception as e:                       # not cached, so a rerun retries it
        print(f"\n  Analyze/Plan failed for {question!r}: {e}", file=sys.stderr)
        return {"intent": "error", "codes": [], "queries": [{"text": question, "code": None}]}
    cache[key] = info
    PLAN_CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=1), encoding="utf-8")
    return info


def to_row(docs) -> list[dict]:
    """Same shape evaluate.py gives to score_case."""
    return [{"source": d.metadata.get("source"), "article": d.metadata.get("article"),
             "chunk_id": d.metadata.get("chunk_id"), "article_label": d.metadata.get("article_label"),
             "snippet": d.page_content[:300]} for d in docs]


def parse_args():
    ap = argparse.ArgumentParser(description="Plan vs baseline retrieval.")
    ap.add_argument("--split", choices=["dev", "test"], default="dev")
    ap.add_argument("--i-know-this-uses-the-test-set", dest="test_ok", action="store_true",
                    help="required with --split test")
    args = ap.parse_args()
    if args.split == "test":
        if not args.test_ok:
            raise SystemExit("Refusing to run on the test split without --i-know-this-uses-the-test-set.")
        print("WARNING: test split. These results must not be used for tuning.", file=sys.stderr)
    return args


def main():
    args = parse_args()
    split = args.split
    variants = VARIANTS + (SOFT_VARIANTS if HAS_SOFT else [])
    if not HAS_SOFT:
        print("  retrieve_for_plan has no `soft` parameter: variants D and E skipped.", file=sys.stderr)

    cases = load_questions(split)
    install_llm_cache(translate, 0.0, CACHE_PATH, "")     # translations cached at temperature 0, like the official runs
    degraded = DegradationCounter().attach()
    vs = get_vs()
    cache = load_cache()

    rows = {v: [] for v in variants}
    notes = []
    intents = Counter()

    for i, q in enumerate(cases, 1):
        print(f"\r  running {i}/{len(cases)}...", end="", file=sys.stderr, flush=True)

        # --- baseline path (same calls as evaluate.py) ---
        french_q = step_query(q["question"])
        subs = step_subqueries_if_enabled(q["question"], french_q)

        def baseline(law_type):
            cands = step_retrieve(vs, q["question"], french_q, subs, law_type)
            return (step_rerank(french_q, cands) if cands else [])[:TOP_K]

        # --- agent path ---
        info = get_plan(q["question"], cache, split)
        sqs = [(s["text"], s["code"]) for s in info["queries"]]
        intents[info["intent"]] += 1

        a1 = baseline(q["law_type"])
        a2 = baseline(None)
        b1 = retrieve_for_plan(sqs, TOP_K, use_code_filter=True)
        b2 = retrieve_for_plan(sqs, TOP_K, use_code_filter=False)
        c = _fuse([a2, b1])[:TOP_K]
        outs = [a1, a2, b1, b2, c]
        if HAS_SOFT:
            d = retrieve_for_plan(sqs, TOP_K, use_code_filter=True, soft=True)
            e = _fuse([a2, d])[:TOP_K]
            outs += [d, e]

        for name, docs in zip(variants, outs):
            retrieved = to_row(docs)
            rows[name].append({
                "id": q["id"], "concept_id": q["concept_id"], "language": q["language"], "question": q["question"],
                "gold": q["gold"], "retrieved": retrieved,
                "score": score_case(q["gold"], retrieved),
            })
        notes.append({"id": q["id"], "question": q["question"], "intent": info["intent"],
                      "codes": info["codes"], "queries": info["queries"], "law_type": q["law_type"]})
    print(file=sys.stderr)

    # ---------------- report ----------------
    W = 78
    print("=" * W)
    print(f"{'Plan vs baseline retrieval, ' + split.upper() + ' split':^{W}}")
    print(f"{'n=' + str(len(cases)) + '   top_k=' + str(TOP_K):^{W}}")
    print("=" * W)
    print(f"  {'variant':<28}{'n':>4}  {'Hit@6':>7}  {'Hit@1':>7}  {'Recall':>7}  {'MRR':>6}")
    for name in variants:
        print(f"  {name:<28}{_fmt(_agg(rows[name]))}")

    print("\n  By language")
    for lang in sorted({q["language"] for q in cases}):
        print(f"   [{lang}]")
        for name in variants:
            subset = [r for r in rows[name] if r["language"] == lang]
            print(f"    {name:<28}{_fmt(_agg(subset))}")

    # One concept = the same question asked in FR/AR/EN; count how many of its questions hit (Hit@6).
    def concept_hits(name):
        hits = defaultdict(list)
        for r in rows[name]:
            hits[r["concept_id"]].append(r["score"]["hit"])
        return {cid: (sum(h), len(h)) for cid, h in hits.items()}

    ref = concept_hits("A2 baseline, no hint")
    print(f"\n  By concept ({len(ref)} concepts; full = every language version hits)")
    print(f"  {'variant':<28}{'full':>5}{'part':>6}{'miss':>6}     vs A2: {'better':>6}{'same':>6}{'worse':>6}")
    for name in variants:
        ch = concept_hits(name)
        full = sum(h == n for h, n in ch.values())
        miss = sum(h == 0 for h, n in ch.values())
        part = len(ch) - full - miss
        if name == "A2 baseline, no hint":
            paired = f"{'-':>6}{'-':>6}{'-':>6}"
        else:
            better = sum(ch[c][0] > ref[c][0] for c in ch)
            worse = sum(ch[c][0] < ref[c][0] for c in ch)
            paired = f"{better:>6}{len(ch) - better - worse:>6}{worse:>6}"
        print(f"  {name:<28}{full:>5}{part:>6}{miss:>6}            {paired}")

    print("\n  Analyze verdict on these (all answerable) questions:", dict(intents))
    wrong_gate = [n for n in notes if n["intent"] != "clear"]
    for n in wrong_gate:
        print(f"    gate: {n['intent']:<13} {n['question']}")

    print("\n  Questions where B1 (Plan) loses or wins against A2 (baseline, no hint):")
    for k, n in enumerate(notes):
        a_hit = rows["A2 baseline, no hint"][k]["score"]["hit"]
        b_hit = rows["B1 plan, code filter"][k]["score"]["hit"]
        if a_hit != b_hit:
            tag = "PLAN LOSES" if a_hit else "PLAN WINS "
            gold = ", ".join(g["article"] for g in cases[k]["gold"])
            qs = " | ".join(f"{s['code']}:{s['text']}" for s in n["queries"])
            plan_codes = sorted({str(s["code"]) for s in n["queries"]})
            wrong = "   <-- WRONG CODE" if n["law_type"] and n["law_type"] not in plan_codes else ""
            print(f"    {tag} {n['question']}\n        gold: {gold}\n        plan: {qs}"
                  f"\n        code: plan={', '.join(plan_codes)}  dataset law_type={n['law_type']}{wrong}")

    d = degraded.events
    print(f"\n  Degraded events (silent fallbacks): {len(d)}")
    for e in d[:5]:
        print("    ", e)
    print("=" * W)

    out = out_path(split)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"split": split, "variants": rows, "notes": notes}, ensure_ascii=False, indent=1),
                   encoding="utf-8")
    print(f"  Saved {out}")


if __name__ == "__main__":
    main()
