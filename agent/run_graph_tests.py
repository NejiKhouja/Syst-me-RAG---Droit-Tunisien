"""Manual check of the agent graph (calls Groq and loads the models). Run it yourself:

    python agent/run_graph_tests.py
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from agent_graph import app

TESTS = [
    ("hit",      "Que risque-t-on si on frappe quelqu'un ?"),     # expect retries >= 1, tried mentions coups/blessures
    ("contract", "What makes a contract valid?"),                 # expect 1-2 retries
    ("leave",    "Quelle est la durée du congé annuel payé ?"),   # expect 0 retries if Grade says enough
    ("cake",     "How do I bake a chocolate cake?"),              # out of scope: refusal before retrieve, no evidence
]

for thread, q in TESTS:
    print(f"\n=== [{thread}] {q}")
    try:
        state = app.invoke({"question": q}, {"configurable": {"thread_id": thread}})
        print("   intent: ", state.get("intent"))
        print("   status: ", state.get("status"))
        if state.get("status") == "clarify":
            print("   asked for clarification:", state.get("text"))
            continue
        print("   retries:", state.get("retries"))
        print("   tried:  ", state.get("tried"))
        evidence = state.get("evidence")
        print("   evidence (first 3):", list(evidence)[:3] if evidence else None)
    except Exception as e:
        print(f"   ERROR: {e.__class__.__name__}: {e}")
