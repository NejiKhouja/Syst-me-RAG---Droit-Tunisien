import logging
import streamlit as st

from config import DB_DIR, LAW_DISPLAY_NAMES
from pipeline import build_vectorstore, load_vectorstore, ask_question

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

st.set_page_config(
    page_title="Tunisian Legal AI",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
/* Source card */
.source-card {
    background: #f4f6f9;
    border-left: 3px solid #1a3c6e;
    padding: 0.75rem 1rem;
    border-radius: 4px;
    margin-bottom: 0.6rem;
}
.source-card .badge {
    display: inline-block;
    background: #1a3c6e;
    color: #fff;
    padding: 2px 10px;
    border-radius: 10px;
    font-size: 0.78rem;
    font-weight: 600;
    margin-right: 8px;
    letter-spacing: 0.02em;
}
.source-card .meta {
    font-size: 0.82rem;
    color: #555;
    margin-bottom: 0.35rem;
}
.source-card .snippet {
    font-size: 0.83rem;
    color: #222;
    line-height: 1.5;
    white-space: pre-wrap;
}
</style>
""", unsafe_allow_html=True)


@st.cache_resource(show_spinner=False)
def get_vectorstore():
    return load_vectorstore()


def render_sources(docs) -> None:
    if not docs:
        return
    with st.expander(f"Sources — {len(docs)} article(s) retrieved", expanded=False):
        for doc in docs:
            article  = doc.metadata.get("article", "?")
            source   = doc.metadata.get("source", "unknown")
            law_type = doc.metadata.get("law_type", "")
            snippet  = doc.page_content[:350].replace("\n", " ").strip()

            st.markdown(
                f'<div class="source-card">'
                f'<span class="badge">Article {article}</span>'
                f'<span class="meta">{source} &nbsp;·&nbsp; {law_type}</span><br>'
                f'<span class="snippet">{snippet}…</span>'
                f'</div>',
                unsafe_allow_html=True,
            )


with st.sidebar:
    st.title("Tunisian Legal AI")
    st.caption("Ask questions about Tunisian law in Arabic, French, or English.")
    st.divider()

    st.subheader("Search Filter")
    selected_law = st.selectbox(
        "Law Domain",
        options=list(LAW_DISPLAY_NAMES.keys()),
        format_func=lambda k: LAW_DISPLAY_NAMES[k],
        help="Narrow the search to a specific code for more accurate results.",
    )

    st.divider()
    st.subheader("Database")

    db_exists = DB_DIR.exists() and any(DB_DIR.iterdir())
    if db_exists:
        st.success("Database ready")
    else:
        st.warning("No database found — click Rebuild.")

    if st.button("Rebuild Database", use_container_width=True):
        st.cache_resource.clear()
        with st.spinner("Indexing legal documents — this takes several minutes..."):
            build_vectorstore()
        st.success("Rebuild complete.")
        st.rerun()

    if st.button("Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()
    st.caption("Indexed codes:")
    for label in list(LAW_DISPLAY_NAMES.values())[1:]:
        st.caption(f"  {label}")


st.title("Tunisian Legal AI Assistant")
st.caption(
    f"Domain: **{LAW_DISPLAY_NAMES[selected_law]}**  |  "
    "LaBSE + Cross-Encoder + Llama 3.3 70B"
)

if not db_exists:
    st.info("Rebuild the database using the sidebar before asking questions.")
    st.stop()

vectorstore = get_vectorstore()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg["role"] == "assistant" and msg.get("sources"):
            render_sources(msg["sources"])

question = st.chat_input("Ask a legal question in Arabic, French, or English...")

if question:
    st.chat_message("user").markdown(question)
    st.session_state.messages.append({"role": "user", "content": question})

    with st.chat_message("assistant"):
        with st.spinner("Searching and reasoning..."):
            answer, sources = ask_question(vectorstore, question, law_type=selected_law)
        st.markdown(answer)
        render_sources(sources)

    st.session_state.messages.append({
        "role":    "assistant",
        "content": answer,
        "sources": sources,
    })
