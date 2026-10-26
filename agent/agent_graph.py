from typing import TypedDict, Optional
from langgraph.graph import StateGraph, START, END
from analyze import analyze
from langgraph.checkpoint.memory import MemorySaver
from plan import make_plan
from retrieve import retrieve_for_plan

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
    sub_queries: list
    evidence: dict
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

def plan_node(state: AgentState)->dict:
    try:
        plan = make_plan(state["question"], state["language"], state["target_codes"])
        return {"sub_queries": [sq.model_dump() for sq in plan.sub_queries]}
    except Exception as e:
        print("Plan failed:", e)
        return {"sub_queries": [{"text": state["question"], "code": None}]}   # fallback from L3
def retrieve_node(state: AgentState) -> dict:
    sqs = [(sq["text"], sq["code"]) for sq in state["sub_queries"]]
    docs = retrieve_for_plan(sqs, soft=True)
    evidence = {
        d.metadata["chunk_id"]: {
            "source": d.metadata.get("source"),
            "article": d.metadata.get("article"),
            "law_type": d.metadata.get("law_type"),
            "text": d.page_content,
        }
        for d in docs
    }
    return {"evidence": evidence, "status": "answer",
            "text": "[stub] evidence: " + ", ".join(evidence),
            "clarify_count": 0, "original_question": None}

def route_after_analyze(state: AgentState) -> str:
    if state["intent"] == "out_of_scope":
        return "refuse"
    if state["intent"] == "ambiguous" and state.get("clarify_count", 0) < 2:
        return "clarify"
    return "plan"

def refuse(state):
    return {"status": "refuse", "text": "This is outside the Tunisian legal codes I cover.", "clarify_count": 0, "original_question": None}

builder = StateGraph(AgentState)

builder.add_node("analyze", analyze_node)
builder.add_node("clarify", clarify)
builder.add_node("refuse", refuse)
builder.add_node("plan", plan_node)
builder.add_node("retrieve", retrieve_node)

builder.add_edge(START, "analyze")
builder.add_conditional_edges("analyze", route_after_analyze) 
builder.add_edge("clarify", END)
builder.add_edge("refuse", END)
builder.add_edge("plan", "retrieve")
builder.add_edge("retrieve", END)

app = builder.compile(checkpointer=MemorySaver())
def run(thread, turns):
    cfg = {"configurable": {"thread_id": thread}}
    for q in turns:
        r = app.invoke({"question": q}, cfg)
        print(f"[{thread}] {q!r} -> {r['status']}")
        print("   text:", r["text"])
        if r.get("sub_queries"):
            print("   queries:", r["sub_queries"])

if __name__ == "__main__":
    run("clear", ["What is the penalty for theft?"])
    run("ambig", ["Can I break my contract?", "It is my employment contract, I want to resign"])
    run("off",   ["What is the capital of France?"])