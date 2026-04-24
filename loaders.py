import logging
from pathlib import Path

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_core.documents import Document

from config import DATA_DIR, LAW_TYPE_MAP

logger = logging.getLogger(__name__)


def detect_law_type(filename: str) -> str:
    fl = filename.lower()
    for law_type, keywords in LAW_TYPE_MAP.items():
        if any(kw in fl for kw in keywords):
            return law_type
    return "other"


def load_pdf(path: Path, source: str, law_type: str) -> list[Document]:
    pages = PyMuPDFLoader(str(path)).load()
    full_text = "\n\n".join(p.page_content for p in pages)
    return [Document(
        page_content=full_text,
        metadata={"source": source, "law_type": law_type},
    )]


def load_all_documents(folder: Path = DATA_DIR) -> list[Document]:
    all_docs: list[Document] = []
    for pdf_path in sorted(folder.glob("*.pdf")):
        name     = pdf_path.name
        law_type = detect_law_type(name)
        docs     = load_pdf(pdf_path, name, law_type)
        logger.info("Loaded %-25s | %s", law_type, name)
        all_docs.extend(docs)

    logger.info("Total documents loaded: %d", len(all_docs))
    return all_docs
