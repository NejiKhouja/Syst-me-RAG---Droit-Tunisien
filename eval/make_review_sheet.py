"""Build docs/label_review.md: one section per concept, for human label review, on the clean chunks.

For each concept it shows
  * the questions,
  * the current gold resolved to chunk ids (with the chunk text start),
  * corpus candidates found by lexical (BM25) search of the French question over the chunks of the gold source,
  * what the system retrieved (DEV concepts only; test concepts are hidden so that label decisions are
    not influenced by test-set behaviour),
  * the proposed gold (eval/review_suggestions.json) resolved to chunk ids, with a CHECK flag when an
    anchor matches no chunk or an unexpected number of chunks.

Nothing here edits eval/questions.json (see eval/apply_labels.py).

    python eval/make_review_sheet.py --run results/dev_run.json
"""
import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

import chromadb
from rank_bm25 import BM25Okapi

HERE = Path(__file__).parent
ROOT = HERE.parent
STOP = set("""le la les l un une des de du d et en à au aux ce cet cette ces que qui quoi quel quelle quels quelles
est sont être a ont pour par sur dans avec sans ou où il elle ils on se s qu quelles-sont comment que dit
article loi code selon peut peuvent y m n t c j""".split())


def tokens(text: str) -> list[str]:
    return [t for t in re.findall(r"\w+", text.lower()) if t not in STOP and len(t) > 2 and not t.isdigit()]


def flat(text: str, n: int) -> str:
    return re.sub(r"\s+", " ", text)[:n]


def norm(text: str) -> str:
    return "".join(text.split())


class Corpus:
    def __init__(self, db_dir: Path) -> None:
        col = chromadb.PersistentClient(path=str(db_dir)).get_collection("langchain")
        got = col.get(include=["documents", "metadatas"])
        self.chunks: dict[str, dict] = {}
        self.by_source: dict[str, list[str]] = defaultdict(list)
        self.by_key: dict[tuple, list[str]] = defaultdict(list)
        for doc, m in zip(got["documents"], got["metadatas"]):
            cid = m["chunk_id"]
            self.chunks[cid] = {"text": doc, **m}
            self.by_source[m["source"]].append(cid)
            self.by_key[(m["source"], m["article"])].append(cid)
        self._bm25: dict[str, BM25Okapi] = {}

    def resolve(self, entry: dict) -> list[str]:
        """Gold entry {source, article[, anchor]} -> matching chunk ids."""
        if entry["source"] == "*":
            return [c for (s, a), ids in self.by_key.items() if a == entry["article"] for c in ids]
        ids = self.by_key.get((entry["source"], entry["article"]), [])
        anchor = entry.get("anchor")
        if anchor:
            ids = [c for c in ids if norm(self.chunks[c]["text"]).startswith(norm(anchor))]
        return ids

    def bm25(self, source: str) -> BM25Okapi:
        if source not in self._bm25:
            self._bm25[source] = BM25Okapi([tokens(self.chunks[c]["text"]) for c in self.by_source[source]])
        return self._bm25[source]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", help="results JSON of a dev run on the new index (adds retrieved top-6 for dev concepts)")
    ap.add_argument("--db", default=str(ROOT / "db_v1_1"))
    ap.add_argument("--out", default=str(ROOT / "docs" / "label_review.md"))
    args = ap.parse_args()

    questions = json.loads((HERE / "questions.json").read_text(encoding="utf-8"))
    split = json.loads((HERE / "split.json").read_text(encoding="utf-8"))
    dev = set(split["dev"])
    suggestions = json.loads((HERE / "review_suggestions.json").read_text(encoding="utf-8"))
    run = {c["id"]: c for c in json.loads(Path(args.run).read_text(encoding="utf-8"))["cases"]} if args.run else {}
    corpus = Corpus(Path(args.db))

    concepts: dict[str, list[dict]] = defaultdict(list)
    for q in questions:
        concepts[q["concept_id"]].append(q)

    def chunk_line(cid: str, mark: str = "", n: int = 300) -> str:
        c = corpus.chunks[cid]
        title = f" [{c['section_title'][:50]}]" if c["section"] and c.get("section_title") else ""
        return f"- {mark}`{cid}`{title} {flat(c['text'], n)}"

    out = ["# Gold-label review sheet (clean chunks)", "",
           "One section per concept. Mark **Decision** (approve / reject / edit). Chunk ids are described in "
           "`docs/CHUNK_IDS.md`: `<pdf>/s<section>/<article>`; `[title]` is the text inside the PDF the chunk "
           "belongs to (code vs. decree/convention). Candidates are lexical hits for the French question over "
           "the chunks of the gold source: evidence, not truth. Retrieved results are shown for **dev** "
           "concepts only.", ""]
    n_check = 0
    for cid_, qs in concepts.items():
        fr = next((q for q in qs if q["language"] == "fr"), qs[0])
        gold = fr["gold"]
        is_dev = cid_ in dev
        out += ["---", f"## {cid_}  ({'dev' if is_dev else 'test'})", ""]
        for q in qs:
            tag = "unfiltered" if q["law_type"] is None else q["law_type"]
            out.append(f"- `{q['id']}` [{q['language']}, {tag}, {q['category']}] {q['question']}")

        out += ["", "**Current gold** → chunks", ""]
        gold_ids: set[str] = set()
        for g in gold:
            ids = corpus.resolve(g)
            if g["source"] == "*":
                out.append(f"- article {g['article']} in any code ({len(ids)} chunks)")
                continue
            if not ids:
                out.append(f"- **{g['article']}** — NO CHUNK for this article in {g['source']}")
            for cid in ids:
                out.append(chunk_line(cid))
            gold_ids.update(ids)

        src = gold[0]["source"]
        if src != "*" and src in corpus.by_source:
            query = tokens(fr["question"])
            scores = corpus.bm25(src).get_scores(query)
            ranked = sorted(zip(scores, corpus.by_source[src]), key=lambda x: -x[0])
            out += ["", f"**Corpus candidates** (BM25 over {src}; query terms: {' '.join(query)})", ""]
            n = 0
            for sc, cid in ranked:
                if sc <= 0 or n >= 8:
                    break
                abro = " ABROGATED" if re.search(r"abrog", corpus.chunks[cid]["text"][:140], re.I) else ""
                out.append(chunk_line(cid, mark=("gold " if cid in gold_ids else "     "), n=200) + f" ({sc:.1f}){abro}")
                n += 1

        if is_dev and run:
            out += ["", "**Retrieved** (top-6, dev only)", ""]
            for q in qs:
                r = run.get(q["id"])
                if not r:
                    continue
                out.append(f"- `{q['id']}` [{q['language']}]")
                for x in r["retrieved"]:
                    ok = "✓" if x.get("chunk_id") in gold_ids else " "
                    out.append(f"    - {ok} `{x.get('chunk_id')}` {flat(x['snippet'], 150)}")
        elif not is_dev:
            out += ["", "**Retrieved:** _hidden (test concept)_"]

        s = suggestions.get(cid_)
        out += [""]
        if s:
            cur_ids = gold_ids
            new_ids: set[str] = set()
            lines = []
            for pg in s["proposed_gold"]:
                if pg["source"] == "*":
                    lines.append(f"    - any code, article {pg['article']}")
                    continue
                ids = corpus.resolve(pg)
                new_ids.update(ids)
                bad = (len(ids) == 0) or (len(ids) > 1 and not pg.get("multi"))
                n_check += bad
                flag = f"  **CHECK: {len(ids)} chunks match this anchor**" if bad else ""
                new_tag = "NEW " if not (set(ids) & cur_ids) else ""
                lines.append(f"    - {new_tag}article {pg['article']} `{pg['anchor']}` → {', '.join('`'+i+'`' for i in ids) or 'none'}{flag}")
                if ids:
                    lines.append(f"        > {flat(corpus.chunks[ids[0]]['text'], 150)}")
            added = sorted(new_ids - cur_ids)
            removed = sorted(cur_ids - new_ids)
            out += ["**Suggested change:** " + s["rationale"], "",
                    f"- add chunks: {', '.join(added) or 'none'}",
                    f"- drop chunks: {', '.join(removed) or 'none'}",
                    "- proposed gold:"] + lines
        else:
            out += ["**Suggested change:** _none_"]
        out += ["", "**Decision:** [ ] approve  [ ] reject  [ ] edit: ______", ""]

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text("\n".join(out), encoding="utf-8")
    print(f"wrote {args.out} ({len(concepts)} concepts, {n_check} CHECK flags)")


if __name__ == "__main__":
    main()
