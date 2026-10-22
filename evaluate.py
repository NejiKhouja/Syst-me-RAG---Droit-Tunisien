"""End-to-end retrieval evaluation for the Tunisian Legal RAG.

Questions live in eval/questions.json (gold = (source, article) pairs, grouped by
concept_id); eval/split.json assigns whole concepts to dev or test. A hit in the
wrong code is a miss. Results are saved with enough detail to be re-scored
offline (--rescore) after label changes, without re-running the pipeline.

    python evaluate.py --split dev  --out results/dev_run.json
    python evaluate.py --split all  --temperature 0 --out results/official_v1.json
    python evaluate.py --rescore results/official_v1.json
"""
import sys
import io
import json
import time
import logging
import argparse
import subprocess
from collections import defaultdict
from pathlib import Path

# Force UTF-8 output so Arabic text prints correctly on Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

HERE = Path(__file__).parent
QUESTIONS_PATH = HERE / "eval" / "questions.json"
SPLIT_PATH     = HERE / "eval" / "split.json"
CACHE_PATH     = HERE / "eval" / "cache" / "llm_cache.json"

logging.basicConfig(level=logging.WARNING)


# ── Scoring ────────────────────────────────────────────────────────────────────

def _norm(text: str) -> str:
    """Whitespace-free form, so anchors survive differences like 'Article 6- 2' vs 'Article 6-2'."""
    return "".join(text.split())


def _match(g: dict, r: dict) -> bool:
    """Gold entry g matches retrieved chunk r on (source, article); if g has an
    `anchor`, the chunk text must also start with it (whitespace-normalised).
    Anchors pick the intended chunk where a PDF bundles several laws or where
    in-text references created fragment chunks carrying the same number."""
    if g.get("chunk_ids") and r.get("chunk_id"):  # reviewed labels: exact chunk ids (any_of); v1 results have none
        return r.get("chunk_id") in g["chunk_ids"]
    if g["article"] != r["article"] or g["source"] not in ("*", r["source"]):
        return False
    anchor = g.get("anchor")
    return not anchor or _norm(r.get("snippet", "")).startswith(_norm(anchor))


def score_case(gold: list[dict], retrieved: list[dict]) -> dict:
    """retrieved: ordered [{source, article, snippet}]. Without anchors, duplicates by
    (source, article) are collapsed; with anchors, distinct chunks are distinct ranks."""
    chunk_level = any(g.get("anchor") or g.get("chunk_ids") for g in gold)
    seen, ordered = set(), []
    for r in retrieved:
        key = r.get("chunk_id") or ((r["source"], r["article"]) + ((_norm(r.get("snippet", ""))[:80],) if chunk_level else ()))
        if r["article"] is not None and key not in seen:
            seen.add(key); ordered.append(r)
    first = next((i for i, r in enumerate(ordered, 1) if any(_match(g, r) for g in gold)), None)
    found = sum(any(_match(g, r) for r in ordered) for g in gold)
    return {
        "hit":        first is not None,
        "hit_at_1":   first == 1,
        "first_rank": first,
        "recall":     found / len(gold),
        "rr":         1 / first if first else 0.0,
    }


def _agg(rows: list[dict]) -> dict:
    n = len(rows)
    if not n:
        return {"n": 0, "hit": 0.0, "hit_at_1": 0.0, "recall": 0.0, "mrr": 0.0}
    return {
        "n":        n,
        "hit":      sum(r["score"]["hit"] for r in rows) / n,
        "hit_at_1": sum(r["score"]["hit_at_1"] for r in rows) / n,
        "recall":   sum(r["score"]["recall"] for r in rows) / n,
        "mrr":      sum(r["score"]["rr"] for r in rows) / n,
    }


def _fmt(m: dict) -> str:
    return (f"{m['n']:>4}  {m['hit']*100:>6.1f}%  {m['hit_at_1']*100:>6.1f}%  "
            f"{m['recall']*100:>6.1f}%  {m['mrr']:>6.3f}")


def _table(title: str, groups: dict[str, list[dict]], top_k: int) -> None:
    print(f"  {title}")
    print(f"  {'':<24}{'n':>4}  {'Hit@'+str(top_k):>7}  {'Hit@1':>7}  {'Recall':>7}  {'MRR':>6}")
    for name, rs in sorted(groups.items()):
        print(f"  {name:<24}{_fmt(_agg(rs))}")
    print()


def _groups(rows: list[dict]) -> dict[str, dict[str, list[dict]]]:
    out: dict[str, dict[str, list[dict]]] = {k: defaultdict(list) for k in
        ("filtered vs unfiltered", "language", "category", "domain")}
    for r in rows:
        out["filtered vs unfiltered"]["filtered (law given)" if r["law_type"] else "unfiltered (no law)"].append(r)
        out["language"][r["language"]].append(r)
        out["category"][r["category"]].append(r)
        out["domain"][r["law_type"] or "all"].append(r)
    return out


def report(rows: list[dict], meta: dict, split: str, top_k: int) -> None:
    W = 80
    print(f"\n{'='*W}")
    print(f"{'Tunisian Legal RAG — End-to-End Retrieval Evaluation':^{W}}")
    print(f"{('split=' + split + '  n=' + str(len(rows)) + '  top_k=' + str(top_k)):^{W}}")
    print(f"{'='*W}")
    if meta:
        print(f"  LLM        : {meta.get('llm_model')}  temps={meta.get('llm_temperatures')}")
        print(f"  Reranker   : {meta.get('reranker_model')}  ran on {meta.get('rerank_ran')}/{meta.get('n_cases')} cases")
        print(f"  Code       : {meta.get('git_describe')}")
        print(f"  Degraded   : {len(meta.get('degraded_events', []))} events")
    print()

    # Test-split breakdowns are only shown when the test split was asked for explicitly.
    if split == "all":
        shown = [r for r in rows if r["split"] == "dev"]
        print("  Overall (dev + test)       " + _fmt(_agg(rows)))
        print("  Breakdowns below: DEV split only (test is shown only with --split test)\n")
    else:
        shown = rows
    print(f"  Overall ({split if split != 'all' else 'dev'})".ljust(29) + _fmt(_agg(shown)) + "\n")
    for title, groups in _groups(shown).items():
        _table("By " + title, groups, top_k)

    failed = [r for r in shown if not r["score"]["hit"]]
    print(f"  Misses ({len(failed)}):")
    for r in failed:
        exp = ", ".join(f"{g['article']}" for g in r["gold"])
        got = ", ".join(f"{x['article']}@{x['source'][:6]}" for x in r["retrieved"])
        print(f"    - [{r['language']}] {r['question']}\n        gold: {exp}   got: {got}")
    print(f"{'='*W}\n")


# ── Run ────────────────────────────────────────────────────────────────────────

def _git_describe() -> str:
    try:
        return subprocess.check_output(["git", "describe", "--always", "--dirty", "--tags"],
                                       cwd=HERE, text=True, stderr=subprocess.DEVNULL).strip()
    except Exception:
        return "unknown"


def load_questions(split: str) -> list[dict]:
    qs = json.loads(QUESTIONS_PATH.read_text(encoding="utf-8"))
    sp = json.loads(SPLIT_PATH.read_text(encoding="utf-8"))
    dev = set(sp["dev"])
    for q in qs:
        q["split"] = "dev" if q["concept_id"] in dev else "test"
    return qs if split == "all" else [q for q in qs if q["split"] == split]


def apply_overrides(pairs: list[str]) -> dict:
    """--override KEY=VALUE: set config knobs for this run (before pipeline modules import them)."""
    import ast
    import config
    applied = {}
    for p in pairs or []:
        key, _, val = p.partition("=")
        if not hasattr(config, key):
            raise SystemExit(f"unknown config key {key!r}")
        try:
            parsed = ast.literal_eval(val)
        except Exception:
            parsed = val
        setattr(config, key, parsed)
        applied[key] = parsed
    return applied


def run(args) -> tuple[list[dict], dict]:
    overrides = apply_overrides(args.override)
    import translate
    import retriever
    from config import LLM_MODEL, RERANKER_MODEL, EMBEDDING_MODEL
    from eval_harness import install_llm_cache, DegradationCounter
    from pipeline import (load_vectorstore, step_query, step_subqueries_if_enabled,
                          step_retrieve, step_rerank)

    cache = None if args.no_cache else CACHE_PATH
    stats = install_llm_cache(translate, args.temperature, cache, args.cache_salt)
    degraded = DegradationCounter().attach()

    cases = load_questions(args.split)
    vs = load_vectorstore()
    bm25_ok = retriever._get_bm25(vs) is not None
    rows: list[dict] = []
    rerank_ran = 0

    for i, q in enumerate(cases, 1):
        print(f"\r  running {i}/{len(cases)}...", end="", file=sys.stderr, flush=True)
        n_events = len(degraded.events)

        t0 = time.time()
        french_q    = step_query(q["question"])
        sub_queries = step_subqueries_if_enabled(q["question"], french_q)
        t1 = time.time()
        candidates  = step_retrieve(vs, q["question"], french_q, sub_queries, q["law_type"])
        t2 = time.time()
        docs        = (step_rerank(french_q, candidates) if candidates else [])[:args.top_k]
        t3 = time.time()

        new_events = degraded.events[n_events:]
        llm_failed = [e for e in new_events if e.startswith("translate")]
        # An LLM failure (rewrite/sub-queries) always aborts: the case would silently run on the raw question.
        # Reranker fallbacks abort too unless --allow-degraded (v1 has a known one, see the Phase 2 report).
        if llm_failed or (new_events and not args.allow_degraded):
            print(file=sys.stderr)
            raise SystemExit("ABORT: a pipeline component silently fell back:\n  " + "\n  ".join(new_events)
                             + ("" if llm_failed else "\nFix it, or pass --allow-degraded to record the run anyway."))
        if candidates and not any(e.startswith("reranker") for e in degraded.events[n_events:]):
            rerank_ran += 1

        retrieved = [{"source": d.metadata.get("source"), "article": d.metadata.get("article"),
                      "chunk_id": d.metadata.get("chunk_id"), "article_label": d.metadata.get("article_label"),
                      "snippet": d.page_content[:300]} for d in docs]
        rows.append({
            "id": q["id"], "concept_id": q["concept_id"], "split": q["split"],
            "question": q["question"], "language": q["language"], "law_type": q["law_type"],
            "category": q["category"], "gold": q["gold"], "rewrite": french_q, "sub_queries": sub_queries,
            "retrieved": retrieved, "n_candidates": len(candidates), "score": score_case(q["gold"], retrieved),
            "t_llm": round(t1 - t0, 2), "t_retrieve": round(t2 - t1, 2), "t_rerank": round(t3 - t2, 2),
        })
    print(file=sys.stderr)

    meta = {
        "git_describe": _git_describe(), "split": args.split, "n_cases": len(rows), "top_k": args.top_k,
        "llm_model": LLM_MODEL, "reranker_model": RERANKER_MODEL, "embedding_model": EMBEDDING_MODEL,
        "llm_temperatures": sorted(stats.temps), "temperature_override": args.temperature,
        "llm_calls": stats.calls, "llm_cache_hits": stats.cache_hits, "cache_salt": args.cache_salt,
        "bm25_built": bm25_ok, "rerank_ran": rerank_ran, "degraded_events": degraded.events,
        "overrides": overrides,
        "avg_seconds": {k: round(sum(r[k] for r in rows) / len(rows), 2)
                        for k in ("t_llm", "t_retrieve", "t_rerank")},
    }
    return rows, meta


def rescore(path: Path) -> tuple[list[dict], dict]:
    """Re-score a saved run against the current questions.json (labels may have changed)."""
    saved = json.loads(path.read_text(encoding="utf-8"))
    current = {q["id"]: q for q in load_questions("all")}
    rows = []
    for r in saved["cases"]:
        q = current.get(r["id"])
        if not q:
            continue
        r["gold"], r["split"] = q["gold"], q["split"]
        r["score"] = score_case(q["gold"], r["retrieved"])
        rows.append(r)
    return rows, saved["meta"]


def main() -> None:
    ap = argparse.ArgumentParser(description="Evaluate the Tunisian Legal RAG retrieval pipeline.")
    ap.add_argument("--split", choices=["dev", "test", "all"], default="dev",
                    help="default dev; test/all are for final reporting only")
    ap.add_argument("--top-k", type=int, default=6)
    ap.add_argument("--temperature", type=float, default=None,
                    help="force this LLM temperature (use 0 for reproducible runs); "
                         "omit to keep the pipeline's own 0.0 / 0.3")
    ap.add_argument("--no-cache", action="store_true", help="disable the on-disk LLM cache")
    ap.add_argument("--cache-salt", default="", help="changes the cache key (separate sampling runs)")
    ap.add_argument("--allow-degraded", action="store_true",
                    help="do not abort when the rewrite/rerank component silently falls back")
    ap.add_argument("--override", action="append", metavar="KEY=VALUE",
                    help="override a config knob for this run, e.g. --override RAW_FIRST=False")
    ap.add_argument("--out", help="write the full run (meta + per-case results) to this JSON")
    ap.add_argument("--rescore", help="re-score a saved run JSON against the current labels")
    args = ap.parse_args()

    if args.rescore:
        rows, meta = rescore(Path(args.rescore))
        split = "all"
    else:
        rows, meta = run(args)
        split = args.split
    report(rows, meta, split, args.top_k)

    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        payload = {"meta": meta, "cases": rows}
        Path(args.out).write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"  Saved {args.out}\n")


if __name__ == "__main__":
    main()
