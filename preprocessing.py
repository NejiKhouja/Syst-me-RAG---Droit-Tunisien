import re
from config import HEADER_PATTERNS

_HEADER_RE = re.compile("|".join(HEADER_PATTERNS), re.IGNORECASE | re.MULTILINE)
_CONTROL_RE = re.compile(r"[\x00-\x08\x0b-\x1f\x7f]")
_PAGE_NUMBER_LINE_RE = re.compile(r"^[ \t]*\d{1,3}[ \t]*$", re.MULTILINE)


def strip_headers(text: str) -> str:
    return _HEADER_RE.sub("", text).strip()


def strip_control_chars(text: str) -> str:
    """Control characters (e.g. runs of STX characters some PDFs use as separators) carry no meaning."""
    return _CONTROL_RE.sub("", text)


def strip_page_numbers(text: str) -> str:
    """Drop lines that are only a 1-3 digit number: PDF page numbers that otherwise end up inside articles."""
    return _PAGE_NUMBER_LINE_RE.sub("", text)


def normalize_whitespace(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def clean_text(text: str) -> str:
    return normalize_whitespace(strip_page_numbers(strip_control_chars(strip_headers(text))))
