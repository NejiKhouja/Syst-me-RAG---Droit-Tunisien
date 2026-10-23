from typing import TypedDict, Optional
from langgraph.graph import StateGraph, START, END
from analyze import analyze
from langgraph.checkpoint.memory import MemorySaver

class AgentState(TypedDict):
    question: str
    language: str
    intent: str
    target_codes: list
    clarification_question: Optional[str]
    status: str
    text: str
    original_question: Optional[str]
    clarify_count: int
def analyze_node(state: AgentState) -> dict:
 
    if state.get("status") == "clarify" and state.get("original_question"):
        full_question = state["original_question"] + f"\nUser's answer: {state['question']}"
    else:
        full_question = state["question"]
    try:
        hint = state.get("language") if state.get("clarify_count", 0) > 0 else None
        r = analyze(full_question, hint)
        return {
            "language": r.language,
            "intent": r.intent,
            "target_codes": r.target_codes,
            "clarification_question": r.clarification_question,
        }
    except Exception as e:
        print("Analyze failed:", e)
        return {
            "language": "en",
            "intent": "clear",
            "target_codes": [],
            "clarification_question": None,
        }

def clarify(state: AgentState) -> dict:
    prev = state.get("original_question") or ""
    transcript = prev + f"\nUser: {state['question']}\nAgent asked: {state['clarification_question']}"
    count = state.get("clarify_count", 0)
    return {
        "status": "clarify",
        "text": state["clarification_question"] or "Could you give more details?",
        "original_question": transcript.strip(),
        "clarify_count": count + 1,
    }

def route_after_analyze(state: AgentState) -> str:
    if state["intent"] == "out_of_scope":
        return "refuse"
    if state["intent"] == "ambiguous" and state.get("clarify_count", 0) < 2:
        return "clarify"
    return "plan_stub"

def refuse(state):
    return {"status": "refuse", "text": "...", "clarify_count": 0, "original_question": None}
def plan_stub(state):
    return {"status": "answer", "text": f"[stub] would search in: {state['target_codes']}", "clarify_count": 0, "original_question": None}
builder = StateGraph(AgentState)

builder.add_node("analyze", analyze_node)
builder.add_node("clarify", clarify)
builder.add_node("refuse", refuse)
builder.add_node("plan_stub", plan_stub)

builder.add_edge(START, "analyze")
builder.add_conditional_edges("analyze", route_after_analyze)

builder.add_edge("clarify", END)
builder.add_edge("refuse", END)
builder.add_edge("plan_stub", END)

app = builder.compile(checkpointer=MemorySaver())

if __name__ == "__main__":
    cfg = {"configurable": {"thread_id": "t1"}}

    r1 = app.invoke({"question": "Can I break my contract?"}, cfg)
    print("TURN 1:", r1["status"], "|", r1["text"])

    r2 = app.invoke({"question": "It is a contract, what do not understand?"}, cfg)
    print("TURN 2:", r2["status"], "|", r2["text"])

    
    r3 = app.invoke({"question": "i think my question is clear!"}, cfg)
    print("TURN 3:", r3["status"], "|", r3["text"])
    print("intent:", r3["intent"], "| codes:", r3["target_codes"])