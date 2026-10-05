# results/

| File | What it is |
|---|---|
| `official_v1_temp0.json` / `.txt` | **Official v1**: code at tag `v1-baseline-runnable` (v1 + the two config id fixes), whole question set, LLM temperature forced to 0. `meta` records the exact LLM, reranker, embedding model, temperatures, calls, cache hits and degraded events (5 reranker fallbacks = the v1 `ranked[top_k-1]` bug). |
| `historical_out_json_preaudit.json` | The `out.json` from before the audit (Hit@6 48.3%, number-only matching, no run metadata, produced with `openai/gpt-oss-120b` + the `v2` reranker plus uncommitted edits; the config in the `v1-baseline` tag could not have produced it). Kept for reference only. |

The v1 temperature-0.3 spread runs are not here yet: the Groq daily token limit (200k tokens/day for `openai/gpt-oss-120b`) was exhausted. See the Phase 2 report.
