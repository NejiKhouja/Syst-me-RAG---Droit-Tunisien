# Tunisian Legal AI Assistant

A production-grade, multilingual Retrieval-Augmented Generation (RAG) system for querying Tunisian legal codes in **French, Arabic, and English**. Built to explore the real-world challenges of multilingual legal NLP and progressively refined through systematic evaluation.

---

## What It Does

Ask a question about Tunisian law in any of the three supported languages and receive a **structured, grounded answer** that cites the exact article numbers and source documents it relied on — with no hallucinated content.

**Example questions:**
- `Quelle est la peine pour le vol ?` (French)
- `ما هي شروط الزواج؟` (Arabic)
- `What are the rights of a detainee?` (English)

**Supported legal codes:** Constitution (2022), Code Pénal, Code de Procédure Pénale, Code de Procédure Civile, Code du Travail, Code des Obligations et Contrats, Code du Statut Personnel, Code de Commerce, and more.

---

## Architecture

```
User Question  (French / Arabic / English)
       │
       ▼  translate.py
rewrite_query()
  • Translates to French if needed (Arabic → FR, English → FR)
  • Rewrites into precise Tunisian legal terminology
  • Deterministic LLM call, cached in-process
       │
       ▼  translate.py  [skipped for direct article lookups]
generate_subqueries()
  • For complex questions: generates 2 focused sub-queries
  • Each sub-query targets a different legal angle
  • (definition / conditions / penalty / procedure / exceptions)
       │
       ▼  retriever.py
hybrid_retrieve()
  ├── Semantic search (embeddings)  ×  (primary + sub-queries)
  │     ↳ synonym-expanded French query → ChromaDB → top-20 per query
  ├── BM25 keyword search (primary query)
  │     ↳ exact-match on legal terms, code names, proper nouns
  └── Multilingual semantic fallback
        ↳ original Arabic/English query searched too (catches Arabic passages)
  └── Deduplicate by (source, article)
       │
       ▼  reranker.py
cross_encoder_rerank()
  • (French query, article text) pairs jointly re-scored
  • French-to-French comparison → higher cross-encoder precision
  • Returns top-6 documents
       │
       ▼  pipeline.py
generate_answer()
  • Strict grounding: answer ONLY from retrieved context
  • Responds in user's original language
  • Structured output: Direct Answer → Articles → Sources → Explanation
       │
       ▼
Grounded structured answer + cited articles + source documents
```

---

## Tech Stack

| Component | Model / Library | Reason |
|-----------|----------------|--------|
| Embeddings | `OrdalieTech/Solon-embeddings-large-0.1` | Trained on French legal corpora — far better domain alignment than general-purpose models |
| Vector store | ChromaDB | File-based, no server required, supports metadata filtering by `law_type` and `article` |
| BM25 | `rank_bm25` via LangChain | Exact keyword matching; complements semantic search for legal proper nouns and code names |
| Reranker | `cross-encoder/mmarco-mMiniLM-L12-H384-v1` | Multilingual cross-encoder; evaluates (query, passage) pairs jointly for much higher precision than cosine similarity |
| LLM | Llama 3.3 70B via Groq | Free API, fast inference, strong multilingual instruction-following |
| PDF parsing | PyMuPDF | Best text extraction quality for French/Arabic legal PDFs |
| UI | Streamlit | Chat interface with domain filter sidebar, source cards, and database rebuild button |
| Query rewriting | Llama 3.3 70B (temp=0.0) | Translates and rewrites questions into optimised French legal search queries |

---

## Project Structure

```
config.py          Constants — models, paths, law type maps, retrieval knobs
loaders.py         PDF ingestion; concatenates all pages per PDF before splitting
preprocessing.py   Header/watermark stripping, whitespace normalisation
splitter.py        Splits full-document text into one chunk per article
translate.py       rewrite_query(), generate_subqueries(), to_french()
retriever.py       Hybrid BM25 + semantic retrieval, deduplication
reranker.py        Cross-encoder reranking (lazy-loaded, cached)
pipeline.py        Modular pipeline: step_rewrite → step_subqueries → step_retrieve
                                   → step_rerank → step_generate
app.py             Streamlit UI — chat, domain filter, source cards
evaluate.py        End-to-end benchmark (24 test cases, FR + AR + EN)
```

---

## Improvements Made

The system was iteratively improved through systematic evaluation. Below is the full progression.

### v1 — Baseline
Article-level chunking, LaBSE embeddings, cross-encoder reranker, French/Arabic support.

**Accuracy: 84.2% overall (FR: 92.3%, AR: 66.7%)**

### v2 — Honest Retrieval + English Support

**Problems identified in v1:**
- Arabic retrieval was poor because LaBSE's Arabic-French alignment is weak for legal terminology.
- Query "expansion" was injecting hardcoded article numbers into queries — a form of cheating that inflated evaluation numbers without improving real retrieval.
- No English support.

**Changes:**
1. **LLM-based query translation** (`translate.py`) — replaced dictionary-based keyword injection with an LLM call that properly translates Arabic/English queries to French before embedding. Honest, robust, and generalises to any query.
2. **English language support** — `detect_english()` added; pipeline now handles FR/AR/EN with the same translation approach.
3. **Removed hardcoded article numbers** from all query expansions — evaluation now measures real semantic retrieval quality.
4. **`_FR_SYNONYMS` cleaned** — kept only genuine synonyms (no article number hints).

**Accuracy: 100% Arabic, 80% English on retrieval benchmark**

### v3 — High-Performance RAG Architecture

**Problems identified in v2:**
- Single query per question misses articles that are relevant but semantically distant from the query.
- Pure semantic search struggles with exact legal terms, proper nouns, and code names.
- Articles spanning two PDF pages were being silently truncated at the page boundary.
- The evaluation only tested raw retrieval, not the full end-to-end pipeline including reranking.

**Changes:**

#### 1. LLM Query Rewriting (`translate.py` — `rewrite_query()`)
Replaced the literal translation step with a full query rewriting step. The LLM now:
- Translates to French if needed
- Adds precise Tunisian legal terminology
- References the relevant code when obvious (Code Pénal, Constitution, etc.)
- Expands colloquial terms to their formal legal equivalents

This is more robust than translation alone: "what happens if I get arrested" becomes "droits du suspect lors de l'arrestation et garde à vue — Code de Procédure Pénale".

#### 2. Multi-Query Sub-Query Generation (`translate.py` — `generate_subqueries()`)
For complex questions (no article number, ≥4 words), the LLM generates 2 focused sub-queries targeting different legal angles. Example:

> **Question:** "What are the fundamental rights?"
> **Sub-query 1:** "Droit à la vie, à la dignité et à l'intégrité physique — Constitution tunisienne"
> **Sub-query 2:** "Libertés d'expression, de conscience et de réunion — Constitution"

Each sub-query is sent to the retrieval pipeline independently, and results are merged. This dramatically improves recall for broad legal questions.

#### 3. Hybrid Retrieval — BM25 + Semantic (`retriever.py` — `hybrid_retrieve()`)
Combined two complementary retrieval strategies:
- **Semantic search** (embeddings): captures conceptual similarity, works across paraphrases
- **BM25** (keyword): exact-match on legal terms, article numbers, code names — things embeddings sometimes miss

Results from both are deduplicated by `(source, article)` before reranking. The cross-encoder then selects the best 6 from the merged candidate pool.

This is the industry-standard approach for high-recall RAG: semantic retrieval for fuzzy matching, BM25 for precision on domain-specific vocabulary.

#### 4. Multilingual Semantic Fallback (`retriever.py`)
After translating to French for retrieval, the original Arabic/English query is also run through semantic search. This catches any Arabic-language passages in the corpus that the French translation would not reach.

#### 5. Cross-Page Article Fix (`loaders.py`)
Previously, articles that started on one page and ended on the next were silently split into two incomplete chunks. Fixed by concatenating all pages of each PDF into a single document before the article splitter runs. The splitter now sees the full text and captures every article completely.

**Before:** `Article 258` → truncated at page boundary → bad chunk  
**After:** `Article 258` → full text captured → complete chunk

> **Note:** Rebuilding the vectorstore is required after this change.

#### 6. Modular Pipeline Steps (`pipeline.py`)
The pipeline was refactored into named, importable steps:
```python
step_rewrite()      # query rewriting
step_subqueries()   # sub-query generation
step_retrieve()     # hybrid retrieval
step_rerank()       # cross-encoder reranking
step_generate()     # LLM answer generation
```
This makes each component independently testable and replaceable.

#### 7. Strict Grounding Prompt (`pipeline.py`)
The system prompt was hardened with explicit anti-hallucination rules:
- Answer EXCLUSIVELY from the provided context passages
- Never add information not present in the context
- Say explicitly if context is insufficient — do NOT guess
- Respond in the user's original language

#### 8. End-to-End Evaluation (`evaluate.py`)
The evaluation benchmark was updated to test the full pipeline including reranking, rather than just raw retrieval. A question now passes only if the expected article survives both retrieval AND reranking into the final top-6. This gives a true accuracy signal.

On failures, the evaluator now prints the rewritten query and sub-queries, making it easy to diagnose exactly where the pipeline is going wrong.

---

## Evaluation

Run the full end-to-end benchmark (24 test cases across French, Arabic, and English):

```bash
python evaluate.py
```

The benchmark tests whether the expected article numbers appear in the final top-6 results after reranking. Each test case covers a different legal domain and question type.

| Language | Test Cases | Topics Covered |
|----------|-----------|----------------|
| French | 13 | Theft, homicide, corruption, marriage, divorce, working hours, dismissal, contract, civil liability, custody, fundamental rights |
| Arabic | 6 | Theft, corruption, right to life, detainee rights, working hours, marriage |
| English | 5 | Theft, marriage, fundamental rights, detainee rights, working hours |

---

## Setup

### Prerequisites

```bash
conda create -n rag-app python=3.11
conda activate rag-app
pip install -r requirements.txt
pip install rank_bm25        # required for BM25 hybrid retrieval
```

Create a `.env` file:
```
GROQ_API_KEY=your_groq_api_key_here
```

Get a free Groq API key at [console.groq.com](https://console.groq.com).

Place all legal PDFs in the `data/` folder.

### First Run — Build the Vector Database

```bash
streamlit run app.py
# Click "Rebuild Database" in the sidebar
# This takes ~5–10 minutes for ~1400 pages
```

### Subsequent Runs

```bash
streamlit run app.py       # start the UI
python evaluate.py         # run the retrieval benchmark
```

> **Important:** If you update `loaders.py` or `splitter.py`, always rebuild the vectorstore to pick up the changes.

---

## Configuration

All tunable parameters are in `config.py`:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `EMBEDDING_MODEL` | `OrdalieTech/Solon-embeddings-large-0.1` | French legal embedding model |
| `LLM_MODEL` | `llama-3.3-70b-versatile` | Groq model for generation and rewriting |
| `RERANKER_MODEL` | `cross-encoder/mmarco-mMiniLM-L12-H384-v1` | Cross-encoder for reranking |
| `MMR_K` | `20` | Semantic candidates fetched per query |
| `BM25_K` | `15` | BM25 candidates (primary query only) |
| `RERANK_TOP_K` | `6` | Final documents returned after reranking |
| `SUBQUERY_N` | `2` | Sub-queries generated for complex questions |

---

## Key Technical Lessons

Building and improving this system surfaced several non-obvious lessons about production RAG:

**On embeddings:** Domain-specific embedding models are not interchangeable with general-purpose ones. `Solon-embeddings-large` (trained on French legal corpora) dramatically outperforms LaBSE on French legal retrieval despite LaBSE's superior multilingual MTEB scores. Benchmark scores predict benchmark performance, not production performance.

**On query design:** Translating a query to French before embedding is not the same as rewriting it into legal French. "What happens if I get arrested?" and "droits du mis en cause lors de la garde à vue — Code de Procédure Pénale" retrieve very different articles, and only one of them finds articles 13 and 70.

**On hybrid retrieval:** Semantic and BM25 retrieval are complementary, not competing. Embeddings capture paraphrases and conceptual similarity; BM25 captures exact legal terminology. Using both together consistently outperforms either alone, especially for domain-specific vocabulary.

**On evaluation:** Without a structured benchmark, it is impossible to know whether a change improved or degraded the system. Every change in this project was validated against the 24-case benchmark before being kept. The difference between "it seems to work" and "it works" is a test suite.

**On cross-encoders:** A cross-encoder must compare text in the same language as the documents to score well. Passing an Arabic query to a cross-encoder trained on French text will produce poor rankings. Translating the query to French before reranking (not just before retrieval) is essential.

---

## License

MIT
