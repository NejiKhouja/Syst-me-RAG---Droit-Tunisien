import json
from pathlib import Path
from analyze import analyze

with open(Path(__file__).resolve().parent / "analyze_tests.json", encoding="utf-8") as f:
    tests = json.load(f)

correct = 0
for t in tests:
    result = analyze(t["question"])
    ok = result.intent == t["expected_intent"]
    correct += ok
    print(f'{"OK " if ok else "BAD"} | expected={t["expected_intent"]:<12} '
          f'got={result.intent:<12} | {t["question"]}')
    if not ok:
        print("     ", result.model_dump())

print(f"{correct}/{len(tests)} correct")