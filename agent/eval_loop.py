"""Does a grade -> reformulate -> retrieve loop improve the baseline? DEV split by default.

    python agent/eval_loop.py                     # round 0 = A2 (baseline on the raw question, no hint)
    python agent/eval_loop.py --start g           # round 0 = G  (A2 + Analyze's single code as a soft hint)
    python agent/eval_loop.py --split test --i-know-this-uses-the-test-set    # reporting only, never tuning

Round 0 needs no LLM call except the cached AR/EN translation of the baseline. Then loop_core.run_loop:
Grade the top 6; if weak, Reformulate, retrieve the new queries (code as a soft filter), merge, at most
MAX_RETRIES times. Every Grade / Reformulate answer is cached in agent/loop_cache.json, so a re-run after
an interruption repeats no call.
"""
import sys
import json
import hashlib
import argparse
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))                 # baseline modules: pipeline, evaluate, ...
sys.path.insert(0, str(ROOT / "agent"))       # agent modules

from evaluate import load_questions, score_case, _agg, _fmt, CACHE_PATH
import translate
from eval_harness import install_llm_cache, DegradationCounter
from pipeline import step_query, step_subqueries_if_enabled, step_retrieve, step_rerank
from retriever import _fuse
from retrieve import retrieve_for_plan, get_vs
from loop_core import run_loop
from grade import grade, Grade, GRADE_PROMPT
from reformulate import reformulate, Reformulation, REFORMULATE_PROMPT
from eval_plan_vs_raw import provenance as plan_provenance, to_row, cache_key, load_cache, _sha

TOP_K = 6
MAX_RETRIES = 2
LOOP_CACHE = ROOT / "agent" / "loop_cache.json"
CODES_PY = ROOT / "agent" / "codes.py"

A2_ROW = "A2 baseline, no hint"
G_ROW = "G  round 0 (A2 + hint)"
LOOP_ROW = "LOOP final"


def out_path(split: str, start: str) -> Path:
    return ROOT / "results" / f"eval_loop_{split}_{start}.json"


def parse_args():
    ap = argparse.ArgumentParser(description="Grade -> reformulate -> retrieve loop vs the baseline.")
    ap.add_argument("--split", choices=["dev", "test"], default="dev")
    ap.add_argument("--i-know-this-uses-the-test-set", dest="test_ok", action="store_true",
                    help="required with --split test")
    ap.add_argument("--start", choices=["a2", "g"], default="a2",
                    help="round 0: a2 = baseline, no hint; g = baseline + Analyze's single code as a soft hint")
    args = ap.parse_args()
    if args.split == "test":
        if not args.test_ok:
            raise SystemExit("Refusing to run on the test split without --i-know-this-uses-the-test-set.")
        print("WARNING: test split. These results must not be used for tuning.", file=sys.stderr)
    return args


def provenance(split: str, start: str) -> dict:
    p = plan_provenance()                       # branch, describe, analyze/plan/codes.py hashes, prompt_hash
    p["grade_prompt_sha1"] = _sha(GRADE_PROMPT)
    p["reformulate_prompt_sha1"] = _sha(REFORMULATE_PROMPT)
    p["split"], p["start"] = split, start
    return p


class LoopCache:
    """Grade / Reformulate answers on disk, keyed by the prompts, codes.py, the question, the evidence chunk ids
    and the queries tried so far. Written after every new answer, so an interrupted run loses nothing."""

    def __init__(self, path: Path):
        self.path = path
        self.data = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
        self.codes = CODES_PY.read_text(encoding="utf-8")
        self.calls = self.hits = 0

    def key(self, kind: str, question: str, evidence: dict, tried: list) -> str:
        raw = json.dumps([kind, GRADE_PROMPT, REFORMULATE_PROMPT, self.codes, question, list(evidence), list(tried)],
                         ensure_ascii=False)
        return hashlib.sha1(raw.encode("utf-8")).hexdigest()

    def get_or_call(self, kind, question, evidence, tried, call, model):
        k = self.key(kind, question, evidence, tried)
        if k in self.data:
            self.hits += 1
            return model(**self.data[k])
        out = call()
        self.calls += 1
        self.data[k] = out.model_dump()
        self.path.write_text(json.dumps(self.data, ensure_ascii=False, indent=1), encoding="utf-8")
        return out


def to_evidence(docs) -> dict:
    """Same shape as retrieve_node in agent_graph.py."""
    return {d.metadata["chunk_id"]: {"source": d.metadata.get("source"), "article": d.metadata.get("article"),
                                     "law_type": d.metadata.get("law_type"), "text": d.page_content}
            for d in docs}


def analyze_hint(question: str, split: str, plan_cache: dict, prompt_hash: str, counts: Counter):
    """Analyze's single code from the plan cache (no new Analyze call). Same reuse rule as eval_plan_vs_raw:
    matching prompt hash, or a legacy entry (no hash) on dev only. Otherwise no hint."""
    entry = plan_cache.get(cache_key(question, split))
    if entry is None:
        counts["missing"] += 1
        return None
    if entry.get("prompt_hash") != prompt_hash:
        if "prompt_hash" in entry or split != "dev":
            counts["stale"] += 1
            return None
        counts["legacy"] += 1
    codes = entry["codes"]
    return codes[0] if len(codes) == 1 else None


def outcome(r0: dict, lp: dict) -> str:
    """better / worse / same on Hit@6, then on the rank of the first gold chunk."""
    if r0["hit"] != lp["hit"]:
        return "better" if lp["hit"] else "worse"
    if r0["hit"] and r0["first_rank"] != lp["first_rank"]:
        return "better" if lp["first_rank"] < r0["first_rank"] else "worse"
    return "same"


def main():
    args = parse_args()
    split, start = args.split, args.start
    prov = provenance(split, start)
    print(f"  provenance: branch={prov['branch']}  describe={prov['describe']}  split={split}  start={start}")
    print(f"              analyze={prov['analyze_prompt_sha1']}  plan={prov['plan_prompt_sha1']}  codes.py={prov['codes_py_sha1']}"
          f"  grade={prov['grade_prompt_sha1']}  reformulate={prov['reformulate_prompt_sha1']}")

    cases = load_questions(split)
    tstats = install_llm_cache(translate, 0.0, CACHE_PATH, "")     # baseline translations, cached at temperature 0
    degraded = DegradationCounter().attach()
    vs = get_vs()
    plan_cache = load_cache() if start == "g" else {}
    lc = LoopCache(LOOP_CACHE)
    hint_counts = Counter()

    row_names = [A2_ROW] + ([G_ROW] if start == "g" else []) + [LOOP_ROW]
    r0_name = G_ROW if start == "g" else A2_ROW
    rows = {n: [] for n in row_names}
    details = []

    for i, q in enumerate(cases, 1):
        print(f"\r  running {i}/{len(cases)}...", end="", file=sys.stderr, flush=True)

        # --- round 0 (same calls as evaluate.py) ---
        french_q = step_query(q["question"])
        subs = step_subqueries_if_enabled(q["question"], french_q)

        def baseline(law_type):
            cands = step_retrieve(vs, q["question"], french_q, subs, law_type)
            return (step_rerank(french_q, cands) if cands else [])[:TOP_K]

        a2 = baseline(None)
        outs = {A2_ROW: a2}
        if start == "g":
            hint = analyze_hint(q["question"], split, plan_cache, prov["prompt_hash"], hint_counts)
            outs[G_ROW] = _fuse([baseline(hint), a2])[:TOP_K] if hint else a2
        round0 = outs[r0_name]

        # --- loop ---
        state = {"tried": []}
        calls_before = lc.calls + lc.hits

        def grade_fn(question, evidence):
            return lc.get_or_call("grade", question, evidence, state["tried"],
                                  lambda: grade(question, evidence), Grade)

        def reformulate_fn(question, language, tried, evidence, missing):
            r = lc.get_or_call("reformulate", question, evidence, tried,
                               lambda: reformulate(question, language, tried, evidence, missing), Reformulation)
            state["tried"] = list(tried) + [sq.text for sq in r.sub_queries]
            return r

        def retrieve_fn(sub_queries):
            return retrieve_for_plan([(sq.text, sq.code) for sq in sub_queries], TOP_K, True, soft=True)

        try:
            res = run_loop(q["question"], q["language"], round0, grade_fn, reformulate_fn, retrieve_fn, _fuse,
                           to_evidence, max_retries=MAX_RETRIES, top_k=TOP_K)
        except Exception as e:
            print(f"\n  ABORT on {q['id']} ({q['question']!r}): {e}", file=sys.stderr)
            print(f"  Answers obtained so far are cached in {LOOP_CACHE}; re-run the same command.", file=sys.stderr)
            sys.exit(2)
        outs[LOOP_ROW] = res["docs"]

        for name in row_names:
            retrieved = to_row(outs[name])
            rows[name].append({
                "id": q["id"], "concept_id": q["concept_id"], "language": q["language"], "question": q["question"],
                "gold": q["gold"], "retrieved": retrieved, "score": score_case(q["gold"], retrieved),
            })
        details.append({"id": q["id"], "question": q["question"], "language": q["language"],
                        "retries": res["retries"], "first_verdict": res["first_verdict"], "tried": res["tried"],
                        "missing_history": res["missing_history"], "llm_requests": res["llm_calls"],
                        "llm_requests_check": lc.calls + lc.hits - calls_before})
    print(file=sys.stderr)

    if hint_counts["legacy"]:
        print(f"  WARNING: {hint_counts['legacy']} Analyze hints came from cached plans without a prompt hash; "
              f"reused on dev, UNVERIFIED against the current prompts.")
    if hint_counts["missing"] or hint_counts["stale"]:
        print(f"  NOTE: no hint for {hint_counts['missing']} questions without a cached Analyze output and "
              f"{hint_counts['stale']} with an outdated one (round 0 = A2 for those).")

    # ---------------- report ----------------
    W = 78
    print("=" * W)
    print(f"{'Grade -> reformulate loop vs baseline, ' + split.upper() + ' split, start=' + start:^{W}}")
    print(f"{'n=' + str(len(cases)) + '   top_k=' + str(TOP_K) + '   max_retries=' + str(MAX_RETRIES):^{W}}")
    print("=" * W)
    print(f"  {'variant':<28}{'n':>4}  {'Hit@6':>7}  {'Hit@1':>7}  {'Recall':>7}  {'MRR':>6}")
    for name in row_names:
        print(f"  {name:<28}{_fmt(_agg(rows[name]))}")

    print("\n  By language")
    for lang in sorted({q["language"] for q in cases}):
        print(f"   [{lang}]")
        for name in row_names:
            print(f"    {name:<28}{_fmt(_agg([r for r in rows[name] if r['language'] == lang]))}")

    def concept_hits(name):
        hits = defaultdict(list)
        for r in rows[name]:
            hits[r["concept_id"]].append(r["score"]["hit"])
        return {cid: (sum(h), len(h)) for cid, h in hits.items()}

    ref = concept_hits(A2_ROW)
    print(f"\n  By concept ({len(ref)} concepts; full = every language version hits)")
    print(f"  {'variant':<28}{'full':>5}{'part':>6}{'miss':>6}     vs A2: {'better':>6}{'same':>6}{'worse':>6}")
    for name in row_names:
        ch = concept_hits(name)
        full = sum(h == n for h, n in ch.values())
        miss = sum(h == 0 for h, n in ch.values())
        if name == A2_ROW:
            paired = f"{'-':>6}{'-':>6}{'-':>6}"
        else:
            better = sum(ch[c][0] > ref[c][0] for c in ch)
            worse = sum(ch[c][0] < ref[c][0] for c in ch)
            paired = f"{better:>6}{len(ch) - better - worse:>6}{worse:>6}"
        print(f"  {name:<28}{full:>5}{len(ch) - full - miss:>6}{miss:>6}            {paired}")

    r0_scores = [r["score"] for r in rows[r0_name]]
    lp_scores = [r["score"] for r in rows[LOOP_ROW]]
    grid = Counter((d["first_verdict"], s["hit"]) for d, s in zip(details, r0_scores))
    print(f"\n  Grade check: first verdict vs round-0 Hit@6 ({r0_name.strip()})")
    print(f"  {'':<16}{'round0 hit':>12}{'round0 miss':>13}")
    for v in ("enough", "weak"):
        print(f"  {v:<16}{grid[(v, True)]:>12}{grid[(v, False)]:>13}")

    outcomes = [outcome(a, b) for a, b in zip(r0_scores, lp_scores)]
    retried = [k for k, d in enumerate(details) if d["retries"] > 0]
    n_retries = Counter(d["retries"] for d in details)
    oc = Counter(outcomes[k] for k in retried)
    print(f"\n  Retries: {len(retried)}/{len(details)} questions retried "
          f"(1 retry: {n_retries[1]}, 2 retries: {n_retries[2]})")
    print(f"  Among retried questions (Hit@6, then first gold rank): better {oc['better']}, same {oc['same']}, "
          f"worse {oc['worse']}")

    reqs = [d["llm_requests"] for d in details]
    print(f"\n  LLM requests (Grade + Reformulate): {sum(reqs)} total, {sum(reqs) / len(reqs):.2f} per question,"
          f" max {max(reqs)}; Groq calls {lc.calls}, cache hits {lc.hits}")
    print(f"  Translation (baseline AR/EN): Groq calls {tstats.calls}, cache hits {tstats.cache_hits}")

    print("\n  Questions whose outcome changed (round 0 -> loop):")
    for k, d in enumerate(details):
        if outcomes[k] == "same":
            continue
        a, b = r0_scores[k], lp_scores[k]
        print(f"    {outcomes[k].upper():<7} [{d['language']}] {d['question']}\n"
              f"        round 0: hit={a['hit']} rank={a['first_rank']}  ->  loop: hit={b['hit']} rank={b['first_rank']}"
              f"   retries={d['retries']}\n"
              f"        tried: {' | '.join(d['tried']) or '-'}\n"
              f"        missing: {' | '.join(d['missing_history']) or '-'}")

    ev = degraded.events
    print(f"\n  Degraded events (silent fallbacks): {len(ev)}")
    for e in ev[:5]:
        print("    ", e)
    print("=" * W)

    stats = {"grid": {f"{v}|{h}": n for (v, h), n in grid.items()}, "retries": dict(n_retries),
             "retried_outcomes": dict(oc), "llm_requests": sum(reqs), "groq_calls": lc.calls, "cache_hits": lc.hits,
             "translation_calls": tstats.calls, "translation_cache_hits": tstats.cache_hits,
             "hint_counts": dict(hint_counts)}
    out = out_path(split, start)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"provenance": prov, "split": split, "start": start, "rows": rows, "loop": details,
                               "outcomes": outcomes, "stats": stats}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"  Saved {out}")


if __name__ == "__main__":
    main()
