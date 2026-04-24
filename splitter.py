import re
import logging
from langchain_core.documents import Document
from preprocessing import clean_text

logger = logging.getLogger(__name__)


_ARTICLE_RE = re.compile(
    r"((?:Article|Art\.?)\s*\d+\s*(?:bis|ter|quater|quinquies)?\s*[\.\-–]*"
    r"|الفصل\s*\d+\s*[\.\-–]*)",
    re.IGNORECASE,
)

_NUMBER_RE = re.compile(r"\d+")


def _extract_number(title: str) -> str | None:
    m = _NUMBER_RE.search(title)
    return m.group() if m else None


def split_by_article(docs: list[Document]) -> list[Document]:
    chunks: list[Document] = []

    for doc in docs:
        text  = clean_text(doc.page_content)
        parts = _ARTICLE_RE.split(text)

        for i in range(1, len(parts), 2):
            title   = parts[i].strip()
            body    = parts[i + 1].strip() if i + 1 < len(parts) else ""
            content = f"{title} {body}".strip()

            if len(content) < 30:  # skip stubs 
                continue

            chunks.append(Document(
                page_content=content,
                metadata={**doc.metadata, "article": _extract_number(title)},
            ))

    logger.info("Article splitter: %d chunks produced from %d pages", len(chunks), len(docs))
    return chunks
