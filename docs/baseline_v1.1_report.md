# Baseline v1.1 report: retrieval-quality pass

Scope: retrieval only (question → top-6 chunks). No agentic features. Metrics are on `(source, article)` / chunk-id gold
labels; a hit in the wrong code is a miss. Hit@6 = a gold chunk is in the top 6; Hit@1 = the top chunk is a gold chunk;
Recall = share of gold entries found in the top 6; MRR = mean of 1/rank of the first gold chunk.

## 1. Result: v1 vs v1.1

Same questions, same final labels, same dev/test split, LLM temperature 0.
v1 = tag `v1-baseline-runnable` (v1 code plus the two config-id fixes, old index `db/`).
v1.1 = branch `baseline-v1.1` at the commit tagged `v1.1-baseline` (new index `db_v1_1/`).

| Split | n | | Hit@6 | Hit@1 | Recall | MRR |
|---|---|---|---|---|---|---|
| **Dev** (used for tuning) | 35 | v1 | 57.1 | 34.3 | 25.4 | 0.403 |
| | | **v1.1** | **88.6** | **57.1** | **54.1** | **0.659** |
| **Test** (run once, after tuning stopped) | 52 | v1 | 57.7 | 32.7 | 34.4 | 0.405 |
| | | **v1.1** | **80.8** | **59.6** | **50.4** | **0.687** |
| All | 87 | v1 | 57.5 | 33.3 | 30.8 | 0.404 |
| | | **v1.1** | **83.9** | **58.6** | **51.9** | **0.675** |

Reading it honestly:
* Test Hit@6 is 7.8 points below dev (80.8 vs 88.6) while Hit@1 and MRR are slightly higher on test. That is the normal
  small optimism of tuning on 35 questions; the test result is the number to quote. With 52 questions a 95% interval on
  Hit@6 is roughly ±11 points, so the v1 → v1.1 gain (+23 on test) is well outside noise, but differences between
  individual variants in the ablation below (often one question = 2.9 points) are not.
* 81 of 87 labels were reviewed against the corpus text; 6 questions (3 concepts) remain `unverified` (see §6).

By language, scope and category (all 87 questions):

| Group | n | v1 Hit@6 / MRR | v1.1 Hit@6 / MRR |
|---|---|---|---|
| French | 46 | 60.9 / 0.425 | 84.8 / 0.708 |
| Arabic | 21 | 52.4 / 0.348 | 76.2 / 0.560 |
| English | 20 | 55.0 / 0.414 | 90.0 / 0.722 |
| Filtered by law | 78 | 55.1 / 0.370 | 82.1 / 0.647 |
| Unfiltered (9 questions) | 9 | 77.8 / 0.704 | 100 / 0.926 |
| Concept questions | 69 | 52.2 / 0.335 | 82.6 / 0.637 |
| Article lookup | 5 | 100 / 1.000 | 100 / 1.000 |
| Colloquial | 4 | 50.0 / 0.175 | 50.0 / 0.375 |

Test split by domain (v1.1): penal 17 q → 70.6 Hit@6 / 0.515 MRR; labour 8 q → 100 / 0.875; personal status 7 q → 85.7 / 0.857;
contracts 6 q → 83.3 / 0.700; nationality 3 q → 0 / 0 (label issue, §5); other domains ≤ 5 questions each.

## 2. What changed, and what each change did (dev, 35 questions, each step cumulative)

| Step | Hit@6 | Hit@1 | Recall | MRR | Kept? |
|---|---|---|---|---|---|
| v1 (final labels) | 57.1 | 34.3 | 25.4 | 0.403 | |
| 1. Chunk fix + stable ids (`db_v1_1/`) | 71.4 | 25.7 | 32.0 | 0.403 | yes (correctness) |
| 2. Raw-first (French as written, faithful translation for AR/EN, no sub-queries) | 88.6 | 54.3 | 53.5 | 0.657 | yes |
| 3. Remove the leaked synonym table | 85.7 | 45.7 | 51.3 | 0.593 | yes (leak; must go) |
| 4. Reranker: fix crash, pool 20, int8, max length 256 | 85.7 | 57.1 | 52.7 | 0.651 | yes (and 4.5x faster) |
| 5. Reciprocal rank fusion before the reranker | 88.6 | 57.1 | 54.1 | 0.659 | yes |
| 6. Contextual text for embedding | 82.9 | 62.9 | 52.3 | 0.689 | **no** (Hit@6 −5.7) |
| 7. bge-m3 instead of Solon embeddings | 82.9 | 54.3 | 51.1 | 0.643 | **no** |

Notes per step (details and the other variants tried, with their numbers, are in `docs/LEARNING_v1.1.md`):
1. 16% of v1's chunk boundaries were in-text references ("…à l'article 62 du présent code…"); wrong fragments in the dev top 6
   went from 18 to 0. Bundled laws are separated into sections, and every chunk has a stable id (`docs/CHUNK_IDS.md`).
2. The biggest gain. v1's LLM rewrite and sub-queries injected invented article numbers (26% of 243 queries), filler words
   (64%) and "jurisprudence" (7%). French now needs no LLM call at all.
3. The hand-written synonym table had keys identical to the eval topics. Removing it cost 2.9 points of Hit@6 and 6.4 points
   of MRR: that much of step 2's gain was leakage. 85.7 / 0.593 is the honest figure at that point.
4. Reranker on or off: off loses 11 points of Hit@6 (74.3). Pool 20 beat 30 and 60; a 6-layer reranker was faster but worse.
   The v1 reranker also skipped reranking silently on 5% of questions (an `IndexError` hidden by `try/except`).
5. Fusing the final order with the cross-encoder was also tried and rejected (Hit@6 80.0).

The tuning pass stopped after steps 6 and 7 were both rejected.

## 3. Latency per query (CPU only, 8 threads, no GPU; retrieval + rerank, not answer generation)

| | LLM before retrieval | Retrieval | Rerank | Total |
|---|---|---|---|---|
| v1 | rewrite + 2 sub-queries (3 Groq calls per question) | 1.95 s | 15.96 s (mean) | ≈ 18 s + 3 LLM calls |
| **v1.1** (test run, mean over all 52 questions) | 0.34 s (1 call only for AR/EN; none for FR) | 0.39 s | 2.25 s | **≈ 3.0 s** |

The v1 LLM time is not measured: those calls were served from the on-disk cache in the official run (cache waits made the
recorded 21 s meaningless). Median rerank per query on dev: 9.6 s (v1 setting) → 2.1 s.
LLM calls over the 87 questions: v1 = 165 (87 rewrites + 78 sub-query calls); v1.1 = 38 translations (distinct Arabic and English questions only), all at low reasoning effort.

## 4. Remaining failures (14 of 87 questions miss the top 6)

| Category | Questions | What is going on |
|---|---|---|
| Label doubtful or incomplete | 8: self-defence ×3 (unverified gold = Art. 39, which is *necessity*; the self-defence article is 40), nationality ×3 (gold covers attribution at birth; the system returns acquisition by marriage / naturalisation), contract validity ×2 (gold = Art. 2-3 only) | Probably the system is not wrong here. These labels were left `unverified` or flagged incomplete in the review. |
| Arabic → French legal term mismatch | 2 (+1 self-defence): "الاحتفاظ" translated "conservation" instead of *garde à vue*; "الاحتيال" translated "fraude", the code says *escroquerie* | A faithful translation cannot know the code's vocabulary. A generic Arabic–French legal glossary (not built from the eval) is the natural next step. |
| Indirect / colloquial question | 2: "Que risque-t-on si on frappe quelqu'un ?", "Mon mari peut-il se remarier ?" | No lexical overlap with the target article. Hard for pure retrieval. |
| Neighbouring or exception article outranks the target | 2: abus de confiance (Art. 296 above 297), responsabilité civile (Arts. 102-104, the exceptions, above 82-84) | Better ranking, not coverage. |

## 5. Labels I suspect are wrong or incomplete (left untouched)

* `penal_self_defence` (3 questions): gold Art. 39 = état de nécessité; Art. 40 is the self-defence article (proposed in the review, not approved because I was least sure).
* `nat_acquisition` (3): "acquérir" also covers marriage (Arts. 13-14) and naturalisation, not only attribution at birth (Arts. 6-9).
* `coc_contract_validity` (3): consent, object and cause articles were not surfaced by lexical search and are not in the gold.
* `coc_seller_duties` (1) and `const_fundamental_rights` (2): proposals not approved; the current gold is a weak fit (564/611/612 are the sale definition, Art. 591 states the seller's duties).
* Labels were produced by me from the corpus text and reviewed once by delegation (not by a domain expert). A legal expert's pass would be worth more than any further tuning.

## 6. How it was kept honest

* No eval leakage in code: the synonym table is gone; no article numbers or per-question terms in prompts or code. Gold labels were
  derived from corpus text, never from system output; test retrievals were hidden during the label review.
* Tuning on dev only (35 questions, fixed before tuning: seed 20261022, stratified by domain/language/scope/category).
  Test run once at the end (`results/final_v1_1_test.json`); no change was made after seeing it.
* Temperature 0 everywhere; LLM outputs cached on disk (`eval/cache/`, git-ignored); every run file records model ids,
  temperatures, overrides, LLM calls, cache hits and degraded events (0 in the final test run; v1 had 5 reranker fallbacks).
* Rules for keeping a change: dev Hit@6 or MRR up by about 2 points or more with no clear regression. Two changes were rejected under it.

## 7. Reproduce

```
git checkout v1.1-baseline
python eval/make_split.py                                   # frozen split (seed 20261022)
python -c "from pipeline import build_vectorstore; build_vectorstore()"   # ~1 h CPU -> db_v1_1/
python evaluate.py --split dev  --temperature 0 --out results/dev.json
python evaluate.py --split test --temperature 0 --out results/test.json  # final reporting only
python evaluate.py --rescore results/official_v1_temp0.json              # v1 on the final labels
```
Files: `results/official_v1_temp0.json` (v1), `results/item*_dev.json` (every ablation run), `results/final_v1_1_test.json`
(test), `docs/LEARNING_v1.1.md` (plain-language notes per change), `docs/CHUNK_IDS.md`, `docs/label_review.md`.

## 8. Limits

* 87 questions, 37 concepts, 9 unfiltered questions: small. Differences of a few points between variants are noise.
* Retrieval only; answer generation (grounding, citations) was not evaluated.
* The LLM is `openai/gpt-oss-120b` on a free Groq tier (200k tokens/day), which shaped how many LLM variants could be tried.
* Not tried: a glossary for Arabic legal terms, chunk-level sub-splitting of the 40 articles longer than 2,500 characters
  (the embedder truncates them), a larger or fine-tuned reranker (CPU latency), hybrid weights tuned on more data.

## 9. Reproduction check (branch `agent-v2`, 2026-10-23)

`python evaluate.py --split dev --temperature 0` with no `--override`, at commit `19a58b6`, gives Hit@6 88.6, Hit@1 57.1,
Recall 54.1, MRR 0.659, and the top 6 of all 35 dev questions are identical to `results/item5_rrf_dev.json`
(0 LLM calls, all 13 translations from the cache). Run files: `results/repro_agent_v2_dev.{txt,json}`.
The step-5 dev run and the final test run both recorded `overrides: {}`, so the committed `config.py` defaults are exactly
the settings behind 88.6 and behind the test numbers (Solon, `db_v1_1/`, MMR_K 20, BM25_K 15, FUSION rrf, RRF_K 60,
RERANK_POOL 20, RERANK_MAX_LENGTH 256, RERANK_QUANTIZE True, RAW_FIRST True, USE_SUBQUERIES False, CONTEXTUAL_CHUNKS False).
No default was corrected, so the tag `v1.1-baseline` needs no follow-up tag.
One caveat: `DB_DIR` and `DATA_DIR` were relative paths, so a script started outside the repo root opened an empty index
(it created `agent/db_v1_1/` with 0 chunks). They are made absolute in the next commit, which does not change results
for runs started from the repo root.
