from typing import TypedDict, Optional
from langgraph.graph import StateGraph, START, END
from analyze import analyze
from langgraph.checkpoint.memory import MemorySaver
from retrieve import retrieve_for_plan
from retriever import _fuse
from retrieve_g import retrieve_g
from grade import grade
from reformulate import reformulate

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
    docs: list
    retries: int
    tried: list[str]
    missing: str
    enough: bool
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

def to_evidence(docs) -> dict:
    return {
        d.metadata["chunk_id"]: {
            "source": d.metadata.get("source"),
            "article": d.metadata.get("article"),
            "law_type": d.metadata.get("law_type"),
            "text": d.page_content,
        }
        for d in docs
    }

def retrieve_node(state: AgentState) -> dict:
    docs = retrieve_g(state["question"], state["target_codes"])
    evidence = to_evidence(docs)
    return {"docs": docs, "evidence": evidence, "retries": 0, "tried": [], "missing": "",
            "status": "answer", "text": "[stub] evidence: " + ", ".join(evidence),
            "clarify_count": 0, "original_question": None}

def grade_node(state: AgentState) -> dict:
    g = grade(state["question"], state["evidence"])
    return {"enough": g.enough, "missing": g.missing}

def reformulate_node(state: AgentState) -> dict:
    r = reformulate(state["question"], state["language"], state["tried"], state["evidence"], state["missing"])
    return {"sub_queries": [(s.text, s.code) for s in r.sub_queries],
            "tried": state["tried"] + [s.text for s in r.sub_queries]}

def retrieve_more_node(state: AgentState) -> dict:
    extra = retrieve_for_plan(state["sub_queries"], 6, True, soft=True)
    docs = _fuse([state["docs"], extra])[:6]
    return {"docs": docs, "evidence": to_evidence(docs), "retries": state["retries"] + 1}

def answer_stub(state: AgentState) -> dict:
    return {"status": "done"}   # placeholder until the Answer node exists

def route_after_analyze(state: AgentState) -> str:
    if state["intent"] == "out_of_scope":
        return "refuse"
    if state["intent"] == "ambiguous" and state.get("clarify_count", 0) < 2:
        return "clarify"
    return "retrieve"

def route_after_grade(state: AgentState) -> str:
    return "answer" if state["enough"] or state["retries"] >= 2 else "reformulate"

def route_after_more(state: AgentState) -> str:
    return "answer" if state["retries"] >= 2 else "grade"   # no grade after the last reformulation (as loop_core)

def refuse(state):
    return {"status": "refuse", "text": "This is outside the Tunisian legal codes I cover.", "clarify_count": 0, "original_question": None}

builder = StateGraph(AgentState)

builder.add_node("analyze", analyze_node)
builder.add_node("clarify", clarify)
builder.add_node("refuse", refuse)
builder.add_node("retrieve", retrieve_node)
builder.add_node("grade", grade_node)
builder.add_node("reformulate", reformulate_node)
builder.add_node("retrieve_more", retrieve_more_node)
builder.add_node("answer", answer_stub)

builder.add_edge(START, "analyze")
builder.add_conditional_edges("analyze", route_after_analyze,
                              {"refuse": "refuse", "clarify": "clarify", "retrieve": "retrieve"})
builder.add_edge("clarify", END)
builder.add_edge("refuse", END)
builder.add_edge("retrieve", "grade")
builder.add_conditional_edges("grade", route_after_grade, {"answer": "answer", "reformulate": "reformulate"})
builder.add_edge("reformulate", "retrieve_more")
builder.add_conditional_edges("retrieve_more", route_after_more, {"answer": "answer", "grade": "grade"})
builder.add_edge("answer", END)

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