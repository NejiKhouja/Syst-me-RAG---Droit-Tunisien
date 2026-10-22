# Chunk IDs

Every chunk in the index has a stable, human-readable `chunk_id`, stored in its metadata and used as
the Chroma id. The citation verifier and the reviewed gold labels refer to chunks by this id.

```
<pdf stem>/s<NN>/<article label>[~k]
```

| Part | Meaning | Example |
|---|---|---|
| `pdf stem` | PDF file name without `.pdf` | `PenalFr`, `Statutpersonnel` |
| `s<NN>` | Section: one text inside the PDF, numbered from `s00` in reading order | `s01` |
| `article label` | Article number, plus `-<sub>` for numbered sub-articles and `-<suffix>` for bis/ter/... | `13`, `13-bis`, `226-ter`, `6-2`, `21-13` |
| `~k` | Only if the same label occurs twice in one section (k = 2, 3, ...). Currently never happens. | `PenalFr/s01/12~2` |

Examples: `PenalFr/s02/258` (theft, Code pénal), `ProcedurepenaleFr/s01/13-bis` (garde à vue),
`Statutpersonnel/s01/18` (polygamy, CSP) vs `Statutpersonnel/s01/...` for other CSP articles and
`Statutpersonnel/s02/29` (an état-civil article that also happens to be number 29).

## Sections

Several PDFs bundle texts: a code followed by decrees, orders, conventions or amending laws
(`Statutpersonnel.pdf` has 16 sections: the personal status code, the état-civil law, the community of
property law, the alimony fund...). A new section starts when the article numbering restarts
(a plain `Article 1/2` after a higher number, or an article label already used in the current section).
`s00` is normally the promulgation text that precedes the code. The text of the next section's
preamble (`Décret n° ... Décrète :`) is removed from the last article of the previous section and
kept as `section_title`.

## Metadata per chunk

`chunk_id`, `source`, `law_type`, `section` (int), `section_title`, `article` (base number as a string,
`"13"` for `13-bis`; kept for filters and backwards compatibility), `article_label` (`"13-bis"`).

## What changed from v1 chunks

* A chunk starts only at a real heading at the start of a line (`Article N`, `Art. N`, `Art . N`,
  `Article premier`, with `bis/ter/quater/...` and numbered sub-articles). In-text references such as
  "prévues à l'article 62 du présent code" no longer split text (v1: 16% of boundaries were such references,
  producing wrong fragments labelled with the referenced number).
* `Article premier` is now recognised (v1 dropped article 1 of every text).
* Spelling variants of the suffixes (`quinquiès`, `sexties`, `Septies`, `sexis`, `« quinter »`) are recognised.
* Control characters (e.g. runs of `\x02`) and bare page-number lines are removed.
* Retrieval de-duplicates by `chunk_id` (v1 used `(source, article)`, which merged `13` and `13 bis`).
* Not changed: very long articles are still one chunk (the longest is about 12,000 characters; 40 chunks exceed
  2,500 characters, which the embedding model truncates).
