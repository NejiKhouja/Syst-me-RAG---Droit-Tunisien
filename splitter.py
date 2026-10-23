"""Article-level chunking with stable chunk IDs.

Rules (see docs/CHUNK_IDS.md):
  * a chunk starts only at a real heading: "Article N", "Art. N", "Article premier",
    with optional sub-number ("6- 2") and suffix ("bis", "ter", ...). Headings must be at
    the start of a line (a few title-cased mid-line headings are accepted); in-text
    references such as "...prévues à l'article 62 du présent code" never split;
  * PDFs that bundle several texts (a code plus decrees, orders, conventions) are cut into
    sections: a new section starts when the article numbering restarts at 1 or 2, and the
    preamble of the next text ("Décret n° ... Décrète :") is removed from the previous article;
  * chunk_id = "<pdf stem>/s<section>/<article label>", e.g. "PenalFr/s01/226-ter",
    "travailFr/s00/6-2", "Statutpersonnel/s03/13". A "~k" suffix is added only if the same
    label occurs twice in one section.
"""
import re
import logging
import unicodedata
from collections import Counter
from pathlib import Path

from langchain_core.documents import Document
from preprocessing import clean_text

logger = logging.getLogger(__name__)

# Latin ordinal suffixes as they occur in the corpus, including misspellings ("quinquiès", "sexties",
# "sexis", "Septies", "« quinter »") and doubled ones ("ter bis")
_ONE_SUFFIX = (r"bis|ter|quater|quarter|quinter|quinqui[eèé]s|sext?[iy]?[eè]?s|sexies|sexis|sexties|sept[iy]?[eè]?s|septies|"
               r"oct[iy]?[eè]?s|octies|non[iy]?[eè]?s|nonies|dec[iy]?[eè]?s|decies|undecies|duodecies")
_SUFFIXES = rf"(?:{_ONE_SUFFIX})(?:[ 	]+(?:{_ONE_SUFFIX}))?"

_HEADING_RE = re.compile(
    rf"""(?P<kw>Article|ARTICLE|Art\.?|ART\.?)[ 	]*\.?[ 	]*
         (?P<num>\d+|[Pp]remier|PREMIER|1er)
         (?:[ 	]*[-–][ 	]*(?P<sub>\d+))?
         (?:[ 	]*[-–.]?[ 	]*[«"(]?[ 	]*(?P<suf>(?i:{_SUFFIXES}))[ 	]*[»")]?)?
         (?![\w])""",
    re.X,
)
# at line start, a heading that is really a reference ("Article 5 du code ...") is not a heading
_REFERENCE_AFTER = re.compile(r"[ \t]+(?:du|de|des|dudit|ci|et|à|au|aux|précit|susvis|ainsi|sus)\b")
# mid-line headings are only accepted when followed by a dash separator
_SEPARATOR_AFTER = re.compile(r"[ \t]*\.?[ \t]*[-–—]")

# first line of the preamble of a new bundled text (searched backwards from a numbering reset)
_PREAMBLE_RE = re.compile(
    r"^[ \t(]*\d{0,2}[ \t)]*(?:Loi|LOI|Décret|DECRET|Décret-loi|Arrêté|ARRETE|Arrêté|Code|CODE|Convention|CONVENTION|"
    r"Accord|ACCORD|Au nom du peuple|Nous|Le Président de la République|La Chambre|La chambre|"
    r"Vu|Texte|TEXTE|Projet|Annexe|ANNEXE)\b",
    re.M,
)
_PREAMBLE_WINDOW = 2500


def _label(m: re.Match) -> tuple[str, str]:
    """-> (base number, label) e.g. ("226", "226-ter"), ("6", "6-2"), ("1", "1")."""
    num = m.group("num")
    base = "1" if not num.isdigit() else str(int(num))
    label = base
    if m.group("sub"):
        label += "-" + m.group("sub")
    if m.group("suf"):
        suf = unicodedata.normalize("NFKD", m.group("suf").lower())
        suf = "".join(ch for ch in suf if not unicodedata.combining(ch))
        label += "-" + re.sub(r"\s+", "-", suf.strip())
    return base, label


def _find_headings(text: str) -> list[dict]:
    found = []
    for m in _HEADING_RE.finditer(text):
        line_start = text.rfind("\n", 0, m.start()) + 1
        at_line_start = not text[line_start:m.start()].strip()
        after = text[m.end():m.end() + 40]
        if at_line_start:
            if _REFERENCE_AFTER.match(after):
                continue
        else:
            prev_word = re.search(r"(\S+)\s*$", text[line_start:m.start()])
            ok_prev = bool(prev_word) and (prev_word.group(1)[0].isupper() or prev_word.group(1)[-1] in ".:;)")
            if not (ok_prev and _SEPARATOR_AFTER.match(after)):
                continue
        base, label = _label(m)
        found.append({"start": m.start(), "end": m.end(), "base": int(base), "base_s": base, "label": label})
    return found


def _split_sections(headings: list[dict]) -> None:
    """Annotate headings with a section number. A new text starts when the numbering restarts:
    a plain "Article 1/2" after a higher number, or any plain label already used in this section."""
    section, prev, seen = 0, None, set()
    for h in headings:
        plain = "-" not in h["label"]
        if prev is not None and plain:
            restart = (h["label"] in seen) or (h["base"] <= 2 and (
                prev["base"] >= 3 or (h["base"] == 1 and prev["base"] >= 2)))
            if restart:
                section += 1
                seen = set()
        seen.add(h["label"])
        h["section"] = section
        prev = h


_TITLE_RE = re.compile(
    r"(?:Loi|LOI|Décret-loi|Décret|DECRET|Arrêté|ARRETE|Convention|CONVENTION|Accord|CODE|Code)\b[^\n]{0,25}?"
    r"(?:n°|du\b|des\b|de\b|DE\b|ENTRE\b)[^\n]{0,150}"
)


def _clip_preamble(body: str) -> tuple[str, str]:
    """Remove the preamble of the next bundled text from the end of an article body.
    -> (clean body, title of the next text)."""
    window_start = max(0, len(body) - _PREAMBLE_WINDOW)
    m = _PREAMBLE_RE.search(body, window_start)
    if not m:
        return body, ""
    cut = m.start()
    preamble = body[cut:cut + 900]
    t = _TITLE_RE.search(preamble)
    title = re.sub(r"\s+", " ", t.group(0) if t else preamble[:300]).strip()
    return body[:cut].rstrip(), title[:200]


def split_by_article(docs: list[Document]) -> list[Document]:
    chunks: list[Document] = []

    for doc in docs:
        text = clean_text(doc.page_content)
        source = doc.metadata.get("source", "unknown")
        stem = Path(source).stem
        headings = _find_headings(text)
        _split_sections(headings)

        section_titles: dict[int, str] = {0: ""}
        seen: Counter = Counter()
        for i, h in enumerate(headings):
            body_end = headings[i + 1]["start"] if i + 1 < len(headings) else len(text)
            body = text[h["end"]:body_end]
            if i + 1 < len(headings) and headings[i + 1]["section"] != h["section"]:
                body, title = _clip_preamble(body)
                section_titles[headings[i + 1]["section"]] = title
            content = (text[h["start"]:h["end"]] + body).strip()
            if len(content) < 30:  # skip stubs
                continue

            base_id = f"{stem}/s{h['section']:02d}/{h['label']}"
            seen[base_id] += 1
            chunk_id = base_id if seen[base_id] == 1 else f"{base_id}~{seen[base_id]}"
            chunks.append(Document(
                page_content=content,
                metadata={
                    **doc.metadata,
                    "chunk_id": chunk_id,
                    "section": h["section"],
                    "article": h["base_s"],
                    "article_label": h["label"],
                },
            ))
        # section titles are known only after the pass (they come from the preceding text)
        for c in chunks:
            if c.metadata.get("source") == source and "section_title" not in c.metadata:
                c.metadata["section_title"] = section_titles.get(c.metadata["section"], "")

    logger.info("Article splitter: %d chunks from %d documents", len(chunks), len(docs))
    return chunks


def context_prefix(meta: dict) -> str:
    """Short context line for embedding: which text the chunk belongs to and which article it is.
    e.g. "Code Pénal - Article 226 ter" or "Loi n° 93-65 ... fonds de garantie ... - Article 2"."""
    from config import LAW_DISPLAY_NAMES
    where = LAW_DISPLAY_NAMES.get(meta.get("law_type"), meta.get("law_type", ""))
    if meta.get("section") and meta.get("section_title"):
        where = meta["section_title"]
    label = str(meta.get("article_label", meta.get("article", ""))).replace("-", " ")
    return f"{where} - Article {label}"
