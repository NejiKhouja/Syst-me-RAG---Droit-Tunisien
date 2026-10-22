# L3 Data: Agentic Legal Researcher

This file describes the data that travels between the boxes of the L2 flow diagram.
Every arrow label in L2 maps to a field in `AgentState` below.

Status of this document: **draft v1**. Items marked `PROPOSED` are design decisions to confirm.

---

## 1. Conventions

- **Article ID**: `<source>_<article>`, for example `PenalFr_258`, `COC_242`.
  Built from the chunk metadata (`source`, `article`). Article numbers repeat across codes,
  so the source prefix is required.
- **law_type values** (from the baseline config): `arbitrage`, `obligations_contrats`, `commerce`,
  `droit_international_prive`, `droits_reels`, `protection_enfant`, `nationalite`, `penal`,
  `procedure_civile`, `procedure_penale`, `societes`, `statut_personnel`, `travail`, `constitution`.
- **Limits** (constants, defined once in config):
  - `MAX_RETRIEVE_RETRIES = 2`
  - `MAX_REPAIR_RETRIES = 1`
- **Languages**: `fr`, `ar`, `en`. Retrieval runs in French. The final answer is in the user's language.

---

## 2. Input and output contracts

### Input (UI to agent)

| Field | Type | Notes |
|---|---|---|
| `question` | str | raw user text |
| `thread_id` | str | same id across a clarification exchange |
| `law_type_hint` | str or null | optional filter chosen in the Streamlit sidebar |

### Output (agent to UI), always exactly one of three statuses

| Field | Type | Notes |
|---|---|---|
| `status` | `"answer"` / `"clarify"` / `"refuse"` | drives UI behaviour |
| `text` | str | answer, follow-up question, or refusal reason |
| `citations` | list[Citation] | empty unless `status = "answer"` |
| `trace` | list[TraceEntry] | shown in the UI reasoning panel |

---

## 3. AgentState

| Field | Type | Written by | Read by |
|---|---|---|---|
| `question` | str | UI | Analyze, Plan, Answer |
| `thread_id` | str | UI | Thread memory |
| `law_type_hint` | str or null | UI | Analyze |
| `language` | `"fr"` / `"ar"` / `"en"` | Analyze | Plan, Answer |
| `intent` | `"clear"` / `"ambiguous"` / `"out_of_scope"` | Analyze | router after Analyze |
| `clarification_question` | str or null | Analyze | UI |
| `target_codes` | list[str] (law_type values) | Analyze | Plan, Retrieve |
| `sub_queries` | list[SubQuery] | Plan, Reformulate | Retrieve |
| `evidence` | dict[article_id, Article] | Retrieve, Grade (filters it) | Grade, Answer, Support check |
| `evidence_ok` | bool | Grade | router after Grade |
| `retrieve_retries` | int, 0 to 2 | Reformulate | router after Grade |
| `claims` | list[Claim] | Answer, Repair | Existence check, Support check |
| `verification` | list[VerificationResult] | Existence check, Support check | router after verification, Repair |
| `repair_retries` | int, 0 to 1 | Repair | router after verification |
| `draft_answer` | str | Answer | Final answer |
| `status` | `"answer"` / `"clarify"` / `"refuse"` | Clarify, Refuse, Final answer | UI |
| `citations` | list[Citation] | Final answer | UI |
| `trace` | list[TraceEntry] | Trace wrapper | UI, trace log |

---

## 4. Sub-types

### SubQuery
| Field | Type | Notes |
|---|---|---|
| `text` | str | French search query |
| `code` | str or null | likely `law_type`, used as a metadata filter; null means search all codes |

### Article
| Field | Type | Notes |
|---|---|---|
| `article_id` | str | `source_article` |
| `source` | str | PDF name, for example `PenalFr` |
| `article` | str | article number |
| `law_type` | str | code category |
| `text` | str | full article text |
| `score` | float | best reranker score across sub-queries |
| `found_by` | list[int] | indexes of the sub-queries that retrieved it |

### Claim
| Field | Type | Notes |
|---|---|---|
| `text` | str | one factual statement in the answer |
| `article_ids` | list[str] | the articles the model says support it |

### VerificationResult
| Field | Type | Notes |
|---|---|---|
| `claim_idx` | int | index into `claims` |
| `id_exists` | bool | set by Existence check (code, not LLM) |
| `supported` | bool or null | set by Support check (LLM); null if `id_exists` is false |

A claim **passes** only if `id_exists` is true and `supported` is true.

### Citation
| Field | Type | Notes |
|---|---|---|
| `article_id` | str | |
| `verified` | bool | true only if the claim citing it passed both checks |

### TraceEntry (one per node execution)
| Field | Type | Notes |
|---|---|---|
| `run_id` | str | one per question |
| `question_id` | str or null | links to the eval set |
| `step` | int | order of execution |
| `node` | str | node name |
| `input` | dict | summary of what the node received |
| `output` | dict | summary of what it produced |
| `decision` | str or null | route taken, for example `clarify`, `retry`, `repair` |
| `latency_ms` | int | |
| `llm_calls` | int | |
| `tokens` | int | |
| `error` | str or null | |

---

## 5. Node cards

### Analyze (LLM)
- **Reads:** `question`, `law_type_hint`, thread history (from Thread memory)
- **Calls:** Groq, Thread memory
- **Writes:** `language`, `intent`, `target_codes`, `clarification_question`
- **Decides:** `clear` / `ambiguous` / `out_of_scope`
- **Ambiguous means:** several legal domains could apply and the answer would differ
  (for example "Can I break my contract?" could be employment, lease, or sale).
- **Out of scope means:** not Tunisian law, or not covered by the 14 codes.
- **Fails when:** the LLM returns output that cannot be parsed. Fallback: treat as `clear`.

### Plan (LLM)
- **Reads:** `question`, `language`, `target_codes`
- **Calls:** Groq
- **Writes:** `sub_queries`
- **Decides:** nothing
- **Behaviour:** one sub-query for a simple question, up to 4 for a cross-code question.
  Each sub-query is in French and tagged with a code when one is clear.
- **Fails when:** zero sub-queries returned. Fallback: use the question itself as the only sub-query.

### Retrieve (reuses baseline code)
- **Reads:** `sub_queries`, `target_codes`
- **Calls:** ChromaDB, BM25, reranker (`step_retrieve` and `step_rerank` from the baseline)
- **Writes:** `evidence`
- **Decides:** nothing
- **Behaviour:** runs once per sub-query, keeps each sub-query's own top results, then merges by `article_id`.
- **Fails when:** a sub-query returns nothing. That is recorded, not fatal.

### Grade (LLM)
- **Reads:** `evidence`, `question`
- **Calls:** Groq
- **Writes:** `evidence` (irrelevant articles removed), `evidence_ok`
- **Decides:** enough / not enough
- **Fails when:** all evidence is judged irrelevant (then `evidence_ok = false`).

### Reformulate (LLM)
- **Reads:** `question`, `sub_queries`, `evidence`
- **Calls:** Groq
- **Writes:** `sub_queries` (new ones), `retrieve_retries` (+1)

### Answer (LLM)
- **Reads:** `question`, `evidence`, `language`
- **Calls:** Groq
- **Writes:** `claims`, `draft_answer`
- **Rule:** may only cite `article_id`s present in `evidence`. Output is structured (claims with article ids), not free text.

### Existence check (plain code)
- **Reads:** `claims`
- **Calls:** Article Index (SQLite lookup)
- **Writes:** `verification[].id_exists`
- **Rule:** deterministic. A cited id not in the index means a fabricated citation.

### Support check (LLM)
- **Reads:** `claims`, `evidence`
- **Calls:** Groq
- **Writes:** `verification[].supported`
- **Rule:** only runs for claims whose ids exist. Question asked: "Does this article text support this claim? yes/no."

### Repair (LLM)
- **Reads:** `claims`, `verification`, `evidence`
- **Calls:** Groq
- **Writes:** `claims` (failed ones rewritten or removed), `repair_retries` (+1)

### Drop failed claims (plain code)
- **Reads:** `claims`, `verification`
- **Writes:** `claims` (only passing claims kept), `draft_answer`

### Final answer (plain code)
- **Reads:** `draft_answer`, `claims`, `verification`
- **Writes:** `status = "answer"`, `citations`

### Clarify and Refuse (plain code)
- **Clarify writes:** `status = "clarify"`, `text = clarification_question`
- **Refuse writes:** `status = "refuse"`, `text = reason`

---

## 6. Routing rules

| After | Condition | Goes to |
|---|---|---|
| Analyze | `intent = clear` | Plan |
| Analyze | `intent = ambiguous` | Clarify (then waits for the user's reply on the same `thread_id`, back to Analyze) |
| Analyze | `intent = out_of_scope` | Refuse |
| Grade | `evidence_ok = true` | Answer |
| Grade | `evidence_ok = false` and `retrieve_retries < 2` | Reformulate, then Retrieve |
| Grade | `evidence_ok = false` and `retrieve_retries = 2` | DECIDE (see section 7) |
| Support check | every claim passes | Final answer |
| Support check | some fail and `repair_retries < 1` | Repair, then Answer |
| Support check | some fail and `repair_retries = 1` | Drop failed claims, then Final answer |

---

## 7. Open decisions (PROPOSED defaults, confirm or change)

1. **DECIDE: weak evidence and no retries left.**
   Proposed: **Refuse** with the reason "not enough evidence in the codes to answer reliably".
   Rationale: for legal answers, a refusal is safer than a guess, and the evaluation
   counts a correct refusal on unanswerable questions as a success.
2. **Same article returned by two sub-queries.**
   Proposed: **merge by `article_id`**, keep the highest `score`, and record both sub-query indexes in `found_by`.
   Rationale: one entry per article avoids duplicate context and shows which sub-queries were useful.
3. **"What does Article 9999 say?"** (a trap question).
   Proposed: caught at **Retrieve** (the direct article lookup finds nothing), so `evidence` is empty,
   Grade sets `evidence_ok = false`, and the run ends in Refuse after the retry limit.
   The Existence check is the second line of defence if the model ever cites a non-existent id.
   Open point: skip the retries when an explicitly named article is not found, to save calls.

---

## 8. Worked example (paper trace)

Question: "What is the penalty for theft?"

| Step | Node | State after the step |
|---|---|---|
| 0 | UI | `question` = "What is the penalty for theft?", `thread_id` = "t1" |
| 1 | Analyze | `language` = "en", `intent` = "clear", `target_codes` = ["penal"] |
| 2 | Plan | `sub_queries` = [{"sanction du vol simple", "penal"}, {"circonstances aggravantes du vol", "penal"}] |
| 3 | Retrieve | `evidence` = {PenalFr_258, PenalFr_260, PenalFr_261, ...} |
| 4 | Grade | `evidence_ok` = true, irrelevant articles removed |
| 5 | Answer | `claims` = [{"Simple theft is punishable by ...", ["PenalFr_258"]}, ...] |
| 6 | Existence check | `verification[].id_exists` = true for all |
| 7 | Support check | `verification[].supported` = true for all |
| 8 | Final answer | `status` = "answer", `citations` = [{PenalFr_258, verified: true}, ...] |

Exercise: write the same table for an ambiguous question ("Can I break my contract?")
and for the trap question ("What does Article 9999 say?").
