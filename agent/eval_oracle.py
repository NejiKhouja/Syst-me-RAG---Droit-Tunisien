import sys, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "agent"))

from evaluate import load_questions, score_case, _agg, _fmt
from retrieve import retrieve_for_plan

cache = json.loads((ROOT / "agent" / "plan_cache.json").read_text(encoding="utf-8"))

rows = []
for i, q in enumerate(load_questions("dev"), 1):
    print(f"\r  {i}", end="", file=sys.stderr, flush=True)
    info = cache[q["question"]]
    sqs = [(s["text"], q["law_type"]) for s in info["queries"]]   # correct code from the dataset
    docs = retrieve_for_plan(sqs, 6, use_code_filter=True)
    retrieved = [{"source": d.metadata.get("source"), "article": d.metadata.get("article"),
                  "chunk_id": d.metadata.get("chunk_id"), "article_label": d.metadata.get("article_label"),
                  "snippet": d.page_content[:300]} for d in docs]
    rows.append({"score": score_case(q["gold"], retrieved)})

print()
print(f"  {'variant':<28}{'n':>4}  {'Hit@6':>7}  {'Hit@1':>7}  {'Recall':>7}  {'MRR':>6}")
print(f"  {'F plan queries + true code':<28}{_fmt(_agg(rows))}")