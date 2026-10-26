import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))   # lets us import pipeline, retriever, config

from pipeline import load_vectorstore, step_retrieve, step_rerank
from retriever import _fuse

_vs = None
def get_vs():
    global _vs
    if _vs is None:
        _vs = load_vectorstore()
    return _vs

def retrieve_for_plan(sub_queries, top_k=6, use_code_filter=True, soft=False):
    """sub_queries: list of (text, code).
    use_code_filter=False: ignore the codes.
    soft=True: search with the code filter AND without it, and fuse both
    (the code is a hint, not a rule)."""
    vs = get_vs()
    ranked_lists = []
    for text, code in sub_queries:
        if not use_code_filter or not code:
            filters = [None]
        else:
            filters = [code, None] if soft else [code]
        for law_type in filters:
            candidates = step_retrieve(vs, text, text, [], law_type)
            if candidates:
                ranked_lists.append(step_rerank(text, candidates))
    return _fuse(ranked_lists)[:top_k]

if __name__ == "__main__":
    for soft in (False, True):
        print("soft =", soft)
        docs = retrieve_for_plan([("peine du vol", "penal")], soft=soft)
        for d in docs:
            print("  ", d.metadata["chunk_id"], "|", d.page_content[:70].replace("\n", " "))