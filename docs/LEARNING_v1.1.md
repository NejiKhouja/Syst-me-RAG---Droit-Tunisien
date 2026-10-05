# Learning notes for baseline v1.1

Plain-language notes, one entry per change. Numbers come from `results/*.json`.

## Phase 2.0 — Making "v1" something you can actually run

**What was wrong.** The code tagged `v1-baseline` named an LLM your Groq key no longer has
(`llama-3.3-70b-versatile`) and a reranker that does not exist on Hugging Face
(`...mMiniLM-L12-H384-v1`; the real one has `v2` in the name). Both failures were caught inside
the code and logged as warnings, so v1 "ran" while skipping query rewriting and reranking.
**What I changed.** On a branch from the tag I committed only those two ids and tagged it
`v1-baseline-runnable`. That tag is the official v1.
**Why it helps.** A baseline that silently skips two of its own components is not a baseline.
**Numbers.** See the Phase 2 report: the official v1 numbers come from this tag.

## Phase 2.1 — Scoring on (source, article) instead of the article number alone

**What was wrong.** The evaluator said "hit" whenever any retrieved chunk had an expected
article *number*, whichever code it came from. "Article 258" exists in the penal code (theft) and
also in the COC and arbitration code, so a hit in the wrong code counted as correct.
**What I changed.** Gold labels are now `(source file, article)` pairs and a hit must match both.
For the one question that names no code at all ("Que dit l'article 13 ?") the source is a
wildcard on purpose.
**Why it helps.** Unfiltered questions can no longer be "answered" by an unrelated code.
**Numbers.** Unfiltered cases are reported separately from filtered ones.

## Phase 2.2 — Concepts and a dev/test split

**What was wrong.** The same question appeared in French, Arabic and English, plus an unfiltered
twin. If those were split at random, a topic could be in both the set you tune on and the set you
report on, which makes tuning look better than it is.
**What I changed.** Every question got a `concept_id`; all variants of a concept go to the same
side. 9 concepts (19 questions) are dev, 28 (68 questions) are test, chosen deterministically by
hashing the id and stratified by law domain.
**Why it helps.** Test numbers stay honest. Caveat: 19 dev questions is small, so one question
moves a percentage by about 5 points.

## Phase 2.3 — A harness that cannot silently degrade

**What was wrong.** When the LLM or the reranker failed, the pipeline logged a warning and went on
with a weaker path, so a broken run still produced a score.
**What I changed.** The evaluator watches for those warnings and aborts on an LLM failure (the
reranker one is allowed only with an explicit flag, see below), records which model ids and
temperatures actually ran, caches LLM answers on disk, and waits out Groq's rate limits instead
of giving up.
**Why it helps.** Every saved run says exactly what ran, and reruns cost almost nothing.
**What it found at once.** v1 has a real bug: with fewer than 6 candidates the reranker's debug
log line indexes past the end of a list, the error is swallowed, and the original order is
returned, i.e. no reranking for those questions. It is fixed in Phase 3.
