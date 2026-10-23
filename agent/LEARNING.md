# Learning log: Agentic Legal Researcher

My own notes. Plain words, so I can explain every step in an interview.
Last updated: 23 Oct 2026.

---

## 0. Where I am right now

| Part | Status |
|---|---|
| Baseline RAG v1.1 (retrieval fixes) | Done, tagged `v1.1-baseline`, pushed |
| Agent branch `agent-v2` | Created from the v1.1 tag, pushed |
| Analyze node (understands the question) | Works on my dev set, held-out set still to do |
| Agent graph (Analyze, Clarify, Refuse, stub) | Works, with the follow-up question loop |
| Plan node (writes French search queries) | 20/20 format checks, retrieval test still to do |
| Retrieve, Grade, Answer, Verify | Not started |
| 100-question answer-level evaluation | Not started |

---

## 1. The project in one paragraph

I have a Tunisian legal RAG: 14 legal codes, questions in Arabic, French or English.
I am turning it into an **agentic legal researcher**. The agent should:
split a question into smaller searches, search across the codes, check that every article
it cites really exists and really supports the claim, ask a follow-up when the question is
unclear, and refuse questions that are not about Tunisian law.

The story I will show has three columns: **v1 (original) → v1.1 (better retrieval) → v2 (agent)**,
with accuracy and hallucination numbers for each.

---

## 2. The plan in four phases

1. **Design** the agent on paper (diagrams, data).
2. **Fix the baseline** first, so I measure the agent against the best version of the old system.
3. **Learn LangGraph** with a tiny toy, then build the agent nodes one by one.
4. **Evaluate** on about 100 questions: accuracy, fake citations, unsupported claims.

I write the agent code myself to learn. Claude explains, gives syntax, and reviews.

---

## 3. Phase 1: Design (done)

**What I did:** drew three diagrams in draw.io and wrote one data file.
- L1: who talks to the system (user, app, models, database).
- L2: the flow of the agent from question to answer.
- L3: the data that moves between the boxes (`docs/L3_data.md`).

**The agent flow:**
Analyze → (Clarify | Refuse | Plan) → Retrieve → Grade (retry max 2) → Answer →
Existence check → Support check (repair max 1) → Final answer.

**Why design first:** I did not understand the old code, and starting to code the agent
without a map would have made me lost. The diagrams are the map.

**Limits I decided:** at most 2 retrieval retries, at most 1 repair.
Every loop needs a limit, or the agent can run forever.

**Still to update:** the article ID format in `L3_data.md` (see section 4, chunk IDs).

---

## 4. Phase 2: Fix the baseline

### Why fix it before building the agent

If I build the agent on a weak baseline, I cannot tell if the agent helped or if I just
fixed bugs. So I improved the baseline as far as I reasonably could, then froze it.

### What I found wrong in v1 (the diagnosis)

- The v1 tag did not even run: two model names no longer worked. The reranker also failed
  silently, so the system ran without reranking and nobody noticed.
- The old query rewrite **hurt**: using the raw question got 57.5% Hit@6, rewrite plus
  sub-queries only 46.0%.
- Of 243 generated queries, 63 had an invented article number, 155 had filler words,
  17 contained "jurisprudence".
- 16% of chunk boundaries were wrong: a mention like "see article 5" was treated as the
  start of a new article, cutting real articles into fragments.
- Several PDFs contain more than one law, so "article 12" alone is ambiguous.
- A synonym table in the code used the same topics as my evaluation questions
  (theft, divorce, dismissal...). That is **leakage**: the system was partly given the answers.
- My gold labels were written from memory and had errors (for example an abrogated article).
- The reranker took about 13 s per query on CPU.

### How I measure (so the numbers mean something)

- A question counts as found only if **both the code (source) and the article number** match.
  Matching the number alone is wrong, because article 12 exists in many codes.
- Temperature 0 everywhere, so a rerun gives the same answer.
- The questions are split into **dev** (35, for tuning) and **test** (52, used once at the end).
  Seed 20261022.
- Labels were reviewed by me, not only by the AI.

**Metrics in plain words:**
- **Hit@6:** the right article is somewhere in the top 6 results.
- **Hit@1:** the right article is the very first result.
- **Recall:** how many of the right articles were found.
- **MRR:** how high the first right article ranks (1.0 is perfect).

### The seven improvement steps (dev set, 35 questions)

| Step | What I changed | Hit@6 | Hit@1 | Recall | MRR | Kept? |
|---|---|---|---|---|---|---|
| Start | v1 with corrected labels | 57.1 | 34.3 | 25.4 | 0.403 | |
| 1 | Chunks start only at real article headings, stable IDs | 71.4 | 25.7 | 32.0 | 0.403 | Yes |
| 2 | Search with the raw question first (translate only Arabic/English) | 88.6 | 54.3 | 53.5 | 0.657 | Yes |
| 3 | Remove the leaked synonym table | 85.7 | 45.7 | 51.3 | 0.593 | Yes |
| 4 | Reranker fix, pool of 20, int8, shorter max length | 85.7 | 57.1 | 52.7 | 0.651 | Yes |
| 5 | Reciprocal rank fusion before the reranker | 88.6 | 57.1 | 54.1 | 0.659 | Yes |
| 6 | Add context text to each chunk before embedding | 82.9 | 62.9 | 52.3 | 0.689 | **No** |
| 7 | Try bge-m3 instead of Solon embeddings | 82.9 | 54.3 | 51.1 | 0.643 | **No** |

**What each step means:**
1. **Chunk fix.** Articles now start only at real headings. Wrong fragments in the top 6
   went from 18 to 0. Chunk IDs look like `PenalFr/s02/226-ter` (source, section, article),
   so an ID never collides. See `docs/CHUNK_IDS.md`.
2. **Raw first.** The biggest jump (+17 points of Hit@6). The old LLM rewrite was adding
   noise; the plain question is usually the best query.
3. **Synonym table removed.** The score dropped on purpose. The table was cheating,
   so 85.7% is the honest number. A drop caused by removing leakage is progress.
4. **Reranker.** Same quality, about 4.5 times faster.
5. **Fusion.** Combines the semantic and keyword rankings in a fairer way than before.
6 and 7. **Rejected.** They helped one metric and hurt another. I tried them, measured,
   and kept the simpler setup. Showing what did not work makes the result more credible.

### Final result: run once on the test set (52 questions)

| | Hit@6 | Hit@1 | Recall | MRR | Time per question |
|---|---|---|---|---|---|
| v1 | 57.7 | 32.7 | 34.4 | 0.405 | about 18 s plus 3 LLM calls |
| **v1.1** | **80.8** | **59.6** | **50.4** | **0.687** | **about 3 s** |

Retrieval is far better, much faster, and it needs no LLM call before searching.
Full write-up: `docs/baseline_v1.1_report.md`. Tag: `v1.1-baseline`.

**Caveat to remember:** these are retrieval numbers (is the right article in the results).
They do not yet say whether the final answer is correct or whether citations are real.
That is what the agent evaluation will measure.

---

## 5. Phase 3a: Learning LangGraph with a toy

**Why a toy:** I wanted to understand graphs, routing and loops on something tiny, before
mixing them with a legal system.

**What I built (`toy_graph/`):**
- `toy.py`: classify a text as question, statement or empty, then route to the right reply.
- `toy_loop.py`: a node that runs twice, then the router sends it to the end.

**What I learned (and the errors that taught me):**
- A node returns **only the fields it changes**. Other fields keep their value.
- `invoke` returns the final state.
- `add_conditional_edges` needs a real **node name** as its source. A router function
  is not a node. I got this wrong first.
- A router must return the `END` constant, not the string `"END"`.
- A node with no edge going in is unreachable.
- Every path must end at END.
- A loop limit belongs in my own state (a counter). Do not rely on LangGraph's safety limit.
- "Ends with a question mark" is a bad rule for detecting a question
  ("Tell me the penalty for theft" has none). That is why Analyze uses an LLM.

---

## 6. Phase 3b: Analyze node

**Job:** read the question and return: language, intent, which codes apply, and a follow-up
question if needed.

**Intent has three values:**
- **clear:** one area of law applies. The answer can list the rules and their variants.
  "Simple theft is punished by X, aggravated theft by Y" is a clear question.
- **ambiguous:** several different areas of law could apply, so a search would be a guess
  ("Can I break my contract?" could be employment, rent or sale).
  Or a missing fact decides **which rule** applies.
- **out_of_scope:** not about Tunisian law, or not covered by the 14 codes.

**How it works:** Groq `openai/gpt-oss-120b` with a Pydantic schema and
`with_structured_output(Analysis, method="json_schema")`. Temperature 0.

**Problems and fixes:**
| Problem | Fix |
|---|---|
| 400 error "Tool choice is required" | Use `method="json_schema"` |
| The model asked "which country?" | Tell it that all questions are about Tunisia |
| The prompt examples were my test questions | Replaced them (**prompt leakage**). Use a separate held-out set |
| "Tell me the penalty for theft" came back ambiguous | The model reasoned "it depends on the type of theft". Almost every legal answer depends on facts, so I narrowed the definition of ambiguous to the **area of law**, not the details |
| A garbled line in my prompt (I pasted a note instead of a rule) | Rewrite it as a clear rule |
| Output showed `target_code` | Field name must be `target_codes` everywhere |

**Scores:**
| Date | Change | Dev score |
|---|---|---|
| Oct 2026 | First prompt with Tunisian context | 9/10 |
| | Narrower "ambiguous" + "if unsure choose clear" | (fill in) |
| | Dev set with 3-language groups and consistency check | (fill in) |
| | Held-out set, run once | (fill in) |

**Is English better than other languages?** It might be. French questions match the French
codes directly, English and Arabic go through a translation step, the Solon embedding model
is French-oriented, and LLMs are usually weakest in Arabic. I must **measure** it: the same
30 questions in FR, EN and AR, and report Hit@6 and answer accuracy per language.

---

## 7. Phase 3c: The agent graph and the follow-up loop

**Graph:** START → analyze → (clarify | refuse | plan_stub) → END.
The three branches are chosen by `route_after_analyze`. The plan node is still a stub.

**Safety:** if Analyze crashes, the question continues as "clear" (fallback from the L3 file).

**Follow-up question loop:**
- A **checkpointer** (`MemorySaver`) remembers the state between calls that share a `thread_id`.
  Without it, every call starts from zero and "it is my job contract" means nothing.
- The Clarify node saves a running **transcript** of the conversation and a counter.
- The user's reply goes back through Analyze, which sees the whole transcript.
- The agent asks at most **2** follow-up questions. After that it does its best with what
  it knows. This is a design choice: asking forever is annoying.
- The language of the first question is passed on, so the follow-up stays in the same language.
- After an answer or a refusal, the counter and transcript are reset.

**Bugs I hit:**
- I had **two functions named `clarify`**. Python silently keeps the last one, so the good version
  never ran: no memory, no counter, and a confusing answer in the wrong language.
  Lesson: Python does not warn about redefined functions. Search for `def name` when behaviour is strange.
- My test inputs were poor ("what do not understand?"). A test is only as good as its inputs.

**Test scenarios to keep:**
1. Vague question, then a real answer → ends in `answer` with the right code.
2. Vague question, then "I don't know" twice → the limit stops the follow-ups.
3. Vague question, then something off-topic → `refuse`.

---

## 8. Phase 3d: Plan node

**Job:** turn one question into 1 to 4 short **French** search queries, each tagged with a code.

**Rules in the prompt:** French only; one query for a simple question, up to four for a
mixed one; never invent an article number (the baseline had 63 of 243 with one);
no filler words; code must be one of the codes found by Analyze.

**Tested with plain code, no LLM judge** (`plan_tests.json`, `run_plan_tests.py`):
number of queries in range, no digits (unless the user named an article), no Arabic script,
no banned filler words, code allowed, max 12 words, **no English words**.

**Results:**
| Date | Change | Score |
|---|---|---|
| Oct 2026 | First prompt, 8 tests | 8/8 |
| | 12 harder tests added (typos, Tunisian dialect, one-word question, long story, empty codes, named article in Arabic, three-code question) | 20/20 |
| | Added the English-word check | 19/20: it caught "award" in an arbitration query |
| | Added "French legal vocabulary only" to the prompt | (fill in) |

**Lessons:**
- The checks said 20/20 but one query contained an English word. Passing means "well-formed",
  not "good". I also read the queries by hand.
- A new check should fail first, then pass after the fix. That proves the check works.
- Some queries are very short ("vol"). Whether they retrieve well is an open question.

**The experiment that decides if Plan is useful:** on the 35 dev questions, compare
(A) the raw question, (B) the Plan queries only, (C) raw question plus Plan queries.
Report Hit@6 for each. The old rewrite hurt, so Plan must prove it does not.

---

## 9. Git state

- `v1-baseline`: unrunnable original. `v1-baseline-runnable`: only two model IDs fixed.
- `baseline-v1.1` and tag `v1.1-baseline`: the fixed baseline (final commit `bef876f`).
- `agent-v2`: branch for the agent, created from `v1.1-baseline`. Agent files live in `agent/`.
- `toy_graph/` is git-ignored, it is my scratch space.
- `.env` is git-ignored. Never commit API keys.

---

## 10. Check-yourself questions (rewrite in my own words)

1. What does a node return, and what happens to the fields it does not return?
   It returns a dict with only the fields to change; the others keep their value.
2. What does `invoke` return? The final state.
3. What happens if a router returns a name that is not a node? LangGraph raises an error.
   (I tried it on purpose and wrote down the message.)
4. What does `thread_id` do? It identifies one conversation, so the checkpointer can
   restore its state on the next call.
5. Why does `MemorySaver` lose everything when the program stops? It keeps state in RAM only.
   In production I would use a database-backed saver.
6. Why is "the answer depends on the facts" not enough to call a question ambiguous?
   Because almost every legal answer does. The question is whether one area of law applies.
7. Why did removing the synonym table lower my score, and why is that good news?
   The table copied the topics of my test questions, so part of the score was cheating.

---

## 11. What is next

1. Finish the Plan fix: add the French-only rule, rerun, record the score.
2. Finish Analyze: language-group consistency check, then the held-out set once.
3. Build the Retrieve node on top of the v1.1 retrieval (`hybrid_retrieve` in `retriever.py`).
4. Run the experiment: raw vs Plan vs raw plus Plan on the 35 dev questions.
5. Grade node: drop irrelevant articles, retry max 2.
6. Answer node: structured claims, each with the article IDs that support it.
7. Verifier: existence check in plain code, support check with an LLM, repair max 1.
8. Trace wrapper (one JSONL line per node) and a Streamlit panel showing the reasoning.
9. Build the ~100-question answer-level test set: normal, ambiguous, unanswerable, trap
   questions (such as "What does Article 9999 say?"), in three languages.
10. Measure v1, v1.1 and v2: accuracy, fake-citation rate, unsupported-claim rate, refusal quality,
    and compare languages.

**Open questions:**
- Groq free tier is 200k tokens per day on this model. The evaluation will need more:
  a paid tier, a cheaper model for simple nodes, or Ollama for Analyze and Grade.
  Put every LLM call behind one function with the model name in config.
- What to do when evidence is weak and retries are used up. Proposed: refuse.
- Update the article ID format in `L3_data.md` to the new chunk IDs.
