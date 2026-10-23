import json, re
from plan import make_plan


BANNED = ["jurisprudence", "alinéa", "alinea"]

def check(plan, t):
    errors = []
    n = len(plan.sub_queries)
    if not (t["min_q"] <= n <= t["max_q"]):
        errors.append(f"{n} queries, expected {t['min_q']}-{t['max_q']}")
    for sq in plan.sub_queries:
        if not t["allow_digits"] and re.search(r"\d", sq.text):
            errors.append("digit: " + sq.text)
        if re.search(r"[\u0600-\u06FF]", sq.text):
            errors.append("arabic text: " + sq.text)
        if any(w in sq.text.lower() for w in BANNED):
            errors.append("filler word: " + sq.text)
        if sq.code and sq.code not in t["target_codes"]:
            errors.append("bad code: " + sq.code)
        if len(sq.text.split()) > 12:
            errors.append("too long: " + sq.text)
    return errors


with open("plan_tests.json", encoding="utf-8") as f:
    tests = json.load(f)

ok = 0
for t in tests:
    plan = make_plan(t["question"], t["language"], t["target_codes"])
    errs = check(plan, t)
    ok += not errs
    print("OK " if not errs else "BAD", t["question"])
    for sq in plan.sub_queries:
        print("     -", sq.code, "|", sq.text)
    for e in errs:
        print("     !!", e)
print(f"\n{ok}/{len(tests)} passed")