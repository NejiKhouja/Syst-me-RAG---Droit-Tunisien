import re
from config import HEADER_PATTERNS

_HEADER_RE = re.compile("|".join(HEADER_PATTERNS), re.IGNORECASE | re.MULTILINE)


def strip_headers(text: str) -> str:
    return _HEADER_RE.sub("", text).strip()


def normalize_whitespace(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def clean_text(text: str) -> str:
    return normalize_whitespace(strip_headers(text))


