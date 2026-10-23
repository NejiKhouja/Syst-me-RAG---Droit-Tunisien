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


def retrieve_for_plan(sub_queries, top_k=6, use_code_filter=True):
    """sub_queries: list of (text, code). Returns a list of Documents, best first."""
    vs = get_vs()
    ranked_lists = []
    for text, code in sub_queries:
        law_type = code if use_code_filter else None
        candidates = step_retrieve(vs, text, text, [], law_type)
        if not candidates:
            continue
        ranked_lists.append(step_rerank(text, candidates))
    return _fuse(ranked_lists)[:top_k]



if __name__ == "__main__":
    docs = retrieve_for_plan([("peine du vol", "penal")])
    for d in docs:
        print(d.metadata["chunk_id"], "|", d.page_content[:80].replace("\n", " "))