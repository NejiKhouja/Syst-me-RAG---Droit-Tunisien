"""Checks for loop_core.run_loop with stub functions: no Groq, no models.

    python agent/test_loop_core.py
"""
import sys
from pathlib import Path
from types import SimpleNamespace as NS

sys.path.insert(0, str(Path(__file__).resolve().parent))
from loop_core import run_loop

# documents are plain chunk-id strings here; fuse = keep order, drop duplicates
fuse = lambda lists: list(dict.fromkeys(d for l in lists for d in l))
to_evidence = lambda docs: {d: {"text": d} for d in docs}


def make(verdicts, new_docs=None):
    """Stubs that record every call. verdicts: list of True/False returned by successive grade calls."""
    calls = {"grade": 0, "reformulate": 0, "retrieve": 0, "tried_seen": [], "evidence_seen": []}
    new_docs = new_docs or [["n1", "n2"], ["n3", "n4"], ["n5"]]

    def grade(q, ev):
        calls["evidence_seen"].append(list(ev))
        v = verdicts[calls["grade"]]
        calls["grade"] += 1
        return NS(enough=v, missing="" if v else f"règle manquante {calls['grade']}")

    def reformulate(q, lang, tried, ev, missing):
        calls["tried_seen"].append(list(tried))
        calls["reformulate"] += 1
        k = calls["reformulate"]
        return NS(sub_queries=[NS(text=f"requête {k}", code=None)])

    def retrieve(sqs):
        calls["retrieve"] += 1
        return new_docs[calls["retrieve"] - 1]

    return calls, grade, reformulate, retrieve


ok = total = 0
def check(name, cond, detail=""):
    global ok, total
    total += 1
    ok += bool(cond)
    print(f"{'OK ' if cond else 'BAD'} {name}" + (f"   ({detail})" if detail and not cond else ""))
    return cond


ROUND0 = ["a", "b", "c", "d", "e", "f"]

# 1. grade says enough at once: 0 retries, exactly 1 grade call, docs unchanged
calls, g, r, ret = make([True])
out = run_loop("q", "fr", ROUND0, g, r, ret, fuse, to_evidence)
check("enough at once -> 0 retries", out["retries"] == 0, out["retries"])
check("enough at once -> 1 grade call, 0 reformulate", (calls["grade"], calls["reformulate"]) == (1, 0), calls)
check("enough at once -> docs unchanged", out["docs"] == ROUND0, out["docs"])
check("enough at once -> llm_calls == 1", out["llm_calls"] == 1, out["llm_calls"])
check("first_verdict recorded as enough", out["first_verdict"] == "enough", out["first_verdict"])

# 2. always weak: never more than max_retries, and no grade after the last reformulation
calls, g, r, ret = make([False, False, False, False])
out = run_loop("q", "fr", ROUND0, g, r, ret, fuse, to_evidence, max_retries=2)
check("always weak -> retries == max_retries (2)", out["retries"] == 2, out["retries"])
check("always weak -> 2 grades, 2 reformulations (no grade after the last one)",
      (calls["grade"], calls["reformulate"]) == (2, 2), calls)
check("always weak -> llm_calls == 4", out["llm_calls"] == 4, out["llm_calls"])
check("first_verdict recorded as weak", out["first_verdict"] == "weak", out["first_verdict"])
check("tried accumulates the new query texts", out["tried"] == ["requête 1", "requête 2"], out["tried"])
check("reformulate sees the queries tried before", calls["tried_seen"] == [[], ["requête 1"]], calls["tried_seen"])
check("missing_history has one entry per weak grade", out["missing_history"] == ["règle manquante 1", "règle manquante 2"],
      out["missing_history"])

# 3. merging and truncation to top_k; the second grade sees the merged evidence
calls, g, r, ret = make([False, True])
out = run_loop("q", "fr", ROUND0, g, r, ret, fuse, to_evidence, max_retries=2, top_k=6)
check("weak then enough -> 1 retry", out["retries"] == 1, out["retries"])
check("weak then enough -> 2 grades, 1 reformulation, llm_calls == 3",
      (calls["grade"], calls["reformulate"], out["llm_calls"]) == (2, 1, 3), (calls, out["llm_calls"]))
check("merged docs truncated to top_k", out["docs"] == ["a", "b", "c", "d", "e", "f"] and len(out["docs"]) == 6, out["docs"])
calls, g, r, ret = make([False, True])
out = run_loop("q", "fr", ["a", "b"], g, r, ret, fuse, to_evidence, top_k=3)
check("new documents are merged in (fuse) and cut at top_k=3", out["docs"] == ["a", "b", "n1"], out["docs"])
check("second grade sees the updated evidence", calls["evidence_seen"] == [["a", "b"], ["a", "b", "n1"]],
      calls["evidence_seen"])

# 4. max_retries respected for other values
for mr in (0, 1, 3):
    calls, g, r, ret = make([False] * 5, new_docs=[["x"]] * 5)
    out = run_loop("q", "fr", ROUND0, g, r, ret, fuse, to_evidence, max_retries=mr)
    check(f"max_retries={mr} -> retries == {mr}, grades == {mr}, llm_calls == {2 * mr}",
          (out["retries"], calls["grade"], out["llm_calls"]) == (mr, mr, 2 * mr), (out["retries"], calls))
check("max_retries=0 -> no grade at all, first_verdict None", out is not None and run_loop(
    "q", "fr", ROUND0, *make([True])[1:], fuse, to_evidence, max_retries=0)["first_verdict"] is None)

print(f"\n{ok}/{total} checks passed")
sys.exit(0 if ok == total else 1)
