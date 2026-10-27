import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))   # lets us import pipeline, retriever, config

from pipeline import step_query, step_subqueries_if_enabled, step_retrieve, step_rerank
from retriever import _fuse
from retrieve import get_vs

TOP_K = 6

def retrieve_g(question, target_codes):
    """Variant G as measured in eval_plan_vs_raw.py / eval_loop.py --start g: baseline retrieval on the raw
    question (A2), plus, when Analyze gave exactly one code, the same baseline filtered on that code, fused
    with A2 (soft hint). The French query and sub-queries are computed once and shared by both searches."""
    vs = get_vs()
    french_q = step_query(question)
    subs = step_subqueries_if_enabled(question, french_q)

    def baseline(law_type):
        cands = step_retrieve(vs, question, french_q, subs, law_type)
        return (step_rerank(french_q, cands) if cands else [])[:TOP_K]

    a2 = baseline(None)
    if len(target_codes) == 1:
        return _fuse([baseline(target_codes[0]), a2])[:TOP_K]
    return a2
