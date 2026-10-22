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

## Phase 3.1 — Chunk fix with stable IDs

**What was wrong.** The old splitter cut the text at *every* "article N" it found, including sentences like
"…prévues à l'article 62 du présent code…". 16% of all cuts were these references, each producing a
fragment labelled with the referenced number (penal article 62 had 6 chunks, 5 of them fragments). It also
missed "Article premier", glued the preamble of the next decree onto the last article of the previous text,
left control characters and page numbers inside articles, and gave no way to tell the code's "Article 13"
from a decree's "Article 13" in the same PDF.
**What I changed.** A chunk now starts only at a real heading at the start of a line. Bundled texts are
separated into sections (numbering restarts), each chunk gets a stable id such as `PenalFr/s02/226-ter`
(scheme in `docs/CHUNK_IDS.md`), and retrieval de-duplicates by id instead of by article number. The new
index lives in `db_v1_1/`; the v1 index in `db/` is untouched.
**Why it helps.** Fragments no longer compete with real articles, `13` and `13 bis` are different chunks,
and a citation can point at exactly one chunk.
**Numbers (dev, 35 questions, same cached LLM output, 0 new tokens).** With today's unverified labels,
Hit@6 40.0% → 51.4%, MRR 0.182 → 0.253. Fragment chunks in the top-6: 18 → 0. With the proposed (not yet
approved) labels: Hit@6 60.0% → 74.3%, MRR 0.418 → 0.417.

| Dev, labels = current (unverified) | Hit@6 | Hit@1 | Recall | MRR |
|---|---|---|---|---|
| v1 chunks (`db/`) | 40.0 | 8.6 | 26.9 | 0.182 |
| + chunk fix (`db_v1_1/`) | 51.4 | 17.1 | 32.9 | 0.253 |

| Dev, labels = proposed (hypothetical) | Hit@6 | Hit@1 | Recall | MRR |
|---|---|---|---|---|
| v1 chunks | 60.0 | 34.3 | 27.8 | 0.418 |
| + chunk fix | 74.3 | 25.7 | 34.4 | 0.417 |

## Phase 3.2 — Raw-first retrieval (no LLM for French, faithful translation for Arabic/English)

**What was wrong.** v1 sent every question through an LLM "rewrite" and two LLM "sub-queries". The audit of
243 generated queries showed what that did: 26% contained an article number the user never wrote (e.g.
"article 226" for breach of trust), 64% contained filler words such as "alinéa", "capacité", "consentement",
7% mentioned "jurisprudence" (the corpus is only codes), and a few contained the literal placeholder
"article X, alinéa Y". Those extra words pulled retrieval towards unrelated articles.
**What I changed.** French questions are searched exactly as written (no LLM call). Arabic and English
questions get a literal French translation with a strict prompt: no added terms, no article numbers, keep
ambiguous words in parentheses. No sub-queries. (The original Arabic/English question is still searched in
addition, as before.) Switches in `config.py`: `RAW_FIRST`, `USE_SUBQUERIES`.
**Why it helps.** The search text now says only what the user said. It also removes ~2/3 of the LLM calls
(and all of them for French).
**Numbers (dev, 35 questions, temperature 0).** Hit@6 71.4% → 88.6%, Hit@1 25.7% → 54.3%, MRR 0.403 → 0.657.
13 new LLM calls in total (one per distinct non-French question), all at low reasoning effort.

| Dev, final labels | Hit@6 | Hit@1 | Recall | MRR |
|---|---|---|---|---|
| v1 (old chunks, rewrite + sub-queries) | 57.1 | 34.3 | 25.4 | 0.403 |
| + chunk fix | 71.4 | 25.7 | 32.0 | 0.403 |
| + raw-first (no sub-queries) | 88.6 | 54.3 | 53.5 | 0.657 |

## Phase 3.3 — Remove the hand-written synonym table (`_expand_synonyms`)

**What was wrong.** Every query had " article loi code tunisien" appended, plus extra words from a table whose
keys (`vol`, `meurtre`, `viol`, `corruption`, `licenciement`, `mariage`, `divorce`, `garde à vue`,
`droits fondamentaux`, ...) are exactly the topics of the evaluation questions. That is tuning to the test
questions: it inflates scores and would not help on a question about any other topic.
**What I changed.** Deleted the table, the function and the appended phrase; queries are searched as they are.
**Why it helps.** It does not help the score, and that is the point: it makes the score honest. It must be
removed whatever the numbers say.
**Numbers (dev, 35 questions).** Hit@6 88.6% → 85.7%, Hit@1 54.3% → 45.7%, MRR 0.657 → 0.593. So roughly 3 points
of Hit@6 and 6 points of MRR in the previous step came from the leak. Both numbers are logged below; the
85.7% / 0.593 line is the real baseline for the next steps.

| Dev, final labels | Hit@6 | Hit@1 | Recall | MRR |
|---|---|---|---|---|
| + raw-first, synonym table still in | 88.6 | 54.3 | 53.5 | 0.657 |
| − synonym table (leak removed) | 85.7 | 45.7 | 51.3 | 0.593 |
