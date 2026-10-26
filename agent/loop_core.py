"""Grade -> reformulate -> retrieve loop, as plain Python.

No imports of pipeline, retriever, langchain or torch: every heavy step is passed in as a function,
so the loop can be tested with stubs (agent/test_loop_core.py) and reused by the graph or the eval.
"""


def run_loop(question, language, round0_docs, grade_fn, reformulate_fn, retrieve_fn, fuse_fn,
             to_evidence_fn, max_retries=2, top_k=6) -> dict:
    """Start from the round-0 documents; while the evidence is graded weak, reformulate and retrieve again
    (at most max_retries times), merging the new documents into the current list.

    grade_fn(question, evidence) -> object with .enough (bool) and .missing (str)
    reformulate_fn(question, language, tried, evidence, missing) -> object with .sub_queries (items with .text)
    retrieve_fn(sub_queries) -> list of documents
    fuse_fn(list of document lists) -> one merged list
    to_evidence_fn(documents) -> evidence dict (what grade_fn and reformulate_fn see)

    After a retry that uses the last allowed reformulation, the new evidence is NOT graded again
    (that grade could not change anything and would cost one more LLM call).
    """
    docs = list(round0_docs)[:top_k]
    evidence = to_evidence_fn(docs)
    tried: list[str] = []
    missing_history: list[str] = []
    retries = 0
    first_verdict = None
    llm_calls = 0

    while retries < max_retries:
        g = grade_fn(question, evidence)
        llm_calls += 1
        if first_verdict is None:
            first_verdict = "enough" if g.enough else "weak"
        if g.enough:
            break
        missing_history.append(g.missing)
        new = reformulate_fn(question, language, list(tried), evidence, g.missing)
        llm_calls += 1
        tried.extend(sq.text for sq in new.sub_queries)
        extra = retrieve_fn(new.sub_queries)
        docs = fuse_fn([docs, extra])[:top_k]
        evidence = to_evidence_fn(docs)
        retries += 1

    return {
        "docs": docs,
        "retries": retries,
        "first_verdict": first_verdict,
        "tried": tried,
        "missing_history": missing_history,
        "llm_calls": llm_calls,
    }
