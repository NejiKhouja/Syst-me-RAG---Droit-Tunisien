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

## Phase 3.4 — Reranker: fix the crash, rerank fewer candidates, make it 4x faster

**What was wrong.** (1) The reranker's debug log line indexed `ranked[top_k-1]` even when logging was off, so with
fewer than 6 candidates it crashed; the surrounding `try/except` swallowed the error and returned the unranked
list. 5% of v1 questions silently skipped reranking, and any other failure (model not found, as happened with the
wrong model id) was equally silent. (2) It scored every retrieved candidate with 512-token inputs: ~9.6 s per query
on this CPU.
**What I changed.** The reranker now fails loudly (no catch-all). New knobs in `config.py`: `RERANK_ENABLED`,
`RERANK_POOL` (candidates sent to the reranker; retrieval lists are merged round-robin so truncation keeps the
best of semantic, BM25 and original-language search), `RERANK_MAX_LENGTH`, `RERANK_QUANTIZE` (int8). Defaults:
pool 20, max length 256, int8.
**Why it helps.** Fewer, better candidates give the cross-encoder less noise to be fooled by, and shorter int8
inputs cut the CPU time. Reranking is still worth it: switching it off loses 11 points of Hit@6.
**Numbers (dev, 35 questions, temperature 0, 0 tokens). Seconds = median rerank time per query, first query excluded
(model load); CPU only (8 threads).**

| Variant | Hit@6 | Hit@1 | Recall | MRR | rerank s/q |
|---|---|---|---|---|---|
| crash fixed, all candidates, fp32, len 512 | 85.7 | 48.6 | 51.3 | 0.612 | 9.6 |
| reranker OFF (retrieval order) | 74.3 | 57.1 | 47.7 | 0.639 | 0 |
| pool 20 | 88.6 | 57.1 | 54.5 | 0.663 | 7.1 |
| pool 30 | 85.7 | 48.6 | 51.3 | 0.612 | 8.9 |
| pool 60 (+ deeper retrieval k=40/30) | 82.9 | 48.6 | 50.4 | 0.599 | 11.7 |
| smaller multilingual reranker (mMiniLM L6) | 88.6 | 40.0 | 50.4 | 0.562 | 3.8 |
| int8 + length 256 (same L12 model) | 88.6 | 51.4 | 51.9 | 0.620 | 2.9 |
| **pool 20 + int8 + length 256 (chosen)** | 85.7 | 57.1 | 52.7 | 0.651 | **2.1** |

Notes: dev has 35 questions, so one question is 2.9 points of Hit@6; pool 20 fp32 vs the chosen row differ by one
question. The chosen row is kept for speed (4.5x faster, MRR within 0.012). Interesting: with the reranker off,
the top-1 is *better* than with it, which says the cross-encoder's ordering is weak; fusing it with the retrieval
rank is the next thing to try.

## Phase 3.5 — Reciprocal rank fusion before the reranker

**What was wrong.** The semantic, BM25 and original-language result lists were merged round-robin ("first of each,
then second of each..."), which ignores the fact that a chunk found by several sources is more likely to be
right than a chunk one source ranks first.
**What I changed.** Reciprocal rank fusion: each chunk scores the sum of 1/(60+rank) over the lists it appears
in, and the best 20 go to the reranker (`FUSION="rrf"`; `"roundrobin"` still available).
**Why it helps.** Agreement between independent retrievers is good evidence; fusion also needs no score
calibration between BM25 and cosine similarity.
**Numbers (dev, 35 questions).** Hit@6 85.7% → 88.6% (one question), MRR 0.651 → 0.659. Kept: no regression, and
it is the standard, tuning-free choice.
**Tried and rejected.** Also fusing the cross-encoder order with the retrieval order for the final top-6
(`FINAL_FUSE`, since the reranker-off run had better top-1): Hit@1 57.1 → 60.0 and MRR → 0.667, but Hit@6
88.6 → 80.0. A clear regression in coverage, so removed.

| Dev | Hit@6 | Hit@1 | Recall | MRR |
|---|---|---|---|---|
| round-robin merge (previous step) | 85.7 | 57.1 | 52.7 | 0.651 |
| **RRF merge** | 88.6 | 57.1 | 54.1 | 0.659 |
| RRF + final fusion with rerank order (rejected) | 80.0 | 60.0 | 50.3 | 0.667 |

## Phase 3.6 — Contextual chunk text for embedding (tried, rejected)

**What I tried.** Prepend "<code or text name> - Article <label>" (e.g. "Code Pénal - Article 226 ter") to the text that is
*embedded* only; the stored text, BM25 and the reranker still see the original chunk. Needs a full re-embed
(`db_v1_1_ctx/`, 98 min CPU, no LLM tokens). `CONTEXTUAL_CHUNKS` in `config.py`, build-time, default off.
**Why it might help.** The embedding would know which code a short article belongs to.
**Numbers (dev, 35 questions).** Hit@6 88.6% → 82.9% (two questions), Hit@1 57.1% → 62.9%, MRR 0.659 → 0.689,
recall 54.1% → 52.3%. Better first place, worse coverage of the top-6.
**Decision.** Rejected: a 5.7-point drop in Hit@6 is a regression and the MRR gain comes from two questions moving
to rank 1. Code kept (off) so it can be re-tested on more data.

| Dev | Hit@6 | Hit@1 | Recall | MRR |
|---|---|---|---|---|
| RRF, plain embeddings (kept) | 88.6 | 57.1 | 54.1 | 0.659 |
| + contextual embedding text (rejected) | 82.9 | 62.9 | 52.3 | 0.689 |

## Phase 3.7 — A different multilingual embedding model (tried, rejected)

**What I tried.** Same 6,031 chunks, same pipeline, only the embedding model changed: `BAAI/bge-m3` (multilingual,
568M parameters, input capped at 512 tokens like Solon) instead of `OrdalieTech/Solon-embeddings-large-0.1`.
New index `db_v1_1_bge/` (105 min CPU, no LLM tokens).
**Numbers (dev, 35 questions).** Hit@6 88.6% → 82.9%, Hit@1 57.1% → 54.3%, MRR 0.659 → 0.643. By language: French
89.5 → 84.2, Arabic 75.0 → 75.0, English 100 → 87.5 (Hit@6).
**Decision.** Rejected; Solon stays. Retrieval time per query is the same (0.3 s).

| Dev | Hit@6 | Hit@1 | Recall | MRR |
|---|---|---|---|---|
| Solon-embeddings-large (kept) | 88.6 | 57.1 | 54.1 | 0.659 |
| BAAI/bge-m3 | 82.9 | 54.3 | 51.1 | 0.643 |

**Stopping.** Items 6 and 7 were both rejected, so the tuning pass ends here. The final configuration is the one after
Phase 3.5 (chunk fix, raw-first, no synonym table, pool 20 + int8 + length 256, RRF, Solon).

## Phase 4 — Final test run (once) and report

Run once after the tuning pass ended, with no change made afterwards: Hit@6 80.8%, Hit@1 59.6%, recall 50.4%,
MRR 0.687 on the 52 test questions (v1 on the same questions: 57.7 / 32.7 / 34.4 / 0.405). Full write-up, latency per
query, remaining failure categories and suspected label problems: `docs/baseline_v1.1_report.md`.
