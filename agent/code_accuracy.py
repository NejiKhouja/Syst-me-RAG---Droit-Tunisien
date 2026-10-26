import sys, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from evaluate import load_questions

cache = json.loads((ROOT / "agent" / "plan_cache.json").read_text(encoding="utf-8"))

total = analyze_ok = plan_ok = 0
for q in load_questions("dev"):
    if not q["law_type"] or q["question"] not in cache:
        continue
    info = cache[q["question"]]
    plan_codes = [s["code"] for s in info["queries"]]
    total += 1
    a = q["law_type"] in info["codes"]       # did Analyze list the right code?
    p = q["law_type"] in plan_codes          # did Plan use the right code?
    analyze_ok += a
    plan_ok += p
    if not (a and p):
        print(f"expected {q['law_type']:<18} analyze={info['codes']} plan={plan_codes}\n    {q['question']}")

print(f"\nAnalyze listed the right code: {analyze_ok}/{total}")
print(f"Plan used the right code:      {plan_ok}/{total}")