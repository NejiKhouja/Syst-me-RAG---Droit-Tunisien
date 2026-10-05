"""Build docs/label_review.md: one section per concept, for human label review.

For each concept it shows the current gold chunks (full text start), corpus
candidates found by lexical (BM25) search of the concept's French question over
the headings of the gold source(s), and what the official v1 run retrieved.
Suggestions come from eval/review_suggestions.json (written after reading this
sheet's evidence); nothing here edits eval/questions.json.

    python eval/make_review_sheet.py --run results/official_v1_temp0.json
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import chromadb
from rank_bm25 import BM25Okapi

HERE = Path(__file__).parent
ROOT = HERE.parent
STOP = set("""le la les l un une des de du d et en à au aux ce cet cette ces que qui quoi quel quelle quels quelles
est sont être a ont pour par sur dans avec sans ou où il elle ils on se s qu quelles-sont comment que dit
article loi code selon peut peuvent y m n t c j""".split())
HEADING = re.compile(r"^(Article|Art\.?)\s*\d", re.I)


def tokens(text: str) -> list[str]:
    return [t for t in re.findall(r"\w+", text.lower()) if t not in STOP and len(t) > 2 and not t.isdigit()]


def is_heading_chunk(doc: str) -> bool:
    """True when the chunk starts like a real article heading (capital 'Article'/'Art.')."""
    return bool(re.match(r"^(Article|Art\.?)\s*\d", doc))


def flat(text: str, n: int) -> str:
    return re.sub(r"\s+", " ", text)[:n]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", help="results JSON of an official run (adds the retrieved top-6)")
    ap.add_argument("--out", default=str(ROOT / "docs" / "label_review.md"))
    args = ap.parse_args()

    questions = json.loads((HERE / "questions.json").read_text(encoding="utf-8"))
    sugg_path = HERE / "review_suggestions.json"
    suggestions = json.loads(sugg_path.read_text(encoding="utf-8")) if sugg_path.exists() else {}
    run = {c["id"]: c for c in json.loads(Path(args.run).read_text(encoding="utf-8"))["cases"]} if args.run else {}

    col = chromadb.PersistentClient(path=str(ROOT / "db")).get_collection("langchain")
    got = col.get(include=["documents", "metadatas"])
    by_key: dict[tuple, list[str]] = defaultdict(list)
    by_source: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for doc, m in zip(got["documents"], got["metadatas"]):
        by_key[(m["source"], m.get("article"))].append(doc)
        if is_heading_chunk(doc):
            by_source[m["source"]].append((m.get("article"), doc))
    bm25 = {s: BM25Okapi([tokens(d) for _, d in items]) for s, items in by_source.items()}

    concepts: dict[str, list[dict]] = defaultdict(list)
    for q in questions:
        concepts[q["concept_id"]].append(q)

    out = ["# Gold-label review sheet", "",
           "One section per concept. For each: mark **Decision** (approve / reject / edit) for the suggested change.",
           "`H` = chunk starts with a real article heading, `F` = fragment created by an in-text reference "
           "(\"…de l'article 62 du présent code…\"). Candidates are lexical hits for the French question over "
           "heading chunks of the gold source; they are evidence, not truth.", ""]
    for cid, qs in concepts.items():
        fr = next((q for q in qs if q["language"] == "fr"), qs[0])
        gold = fr["gold"]
        out += [f"---", f"## {cid}", ""]
        for q in qs:
            tag = "unfiltered" if q["law_type"] is None else q["law_type"]
            out.append(f"- `{q['id']}` [{q['language']}, {tag}, {q['category']}] {q['question']}")
        out += ["", "**Current gold** (" + ("source-ambiguous: any code accepted" if fr["source_ambiguous"] else gold[0]["source"]) + ")", ""]
        gold_keys = {(g["source"], g["article"]) for g in gold}
        for g in gold:
            if g["source"] == "*":
                out.append(f"- article {g['article']} (any code)")
                continue
            chunks = by_key.get((g["source"], g["article"]), [])
            if not chunks:
                out.append(f"- **{g['article']}** — NO CHUNK with this number in {g['source']}")
            for c in chunks:
                out.append(f"- **{g['article']}** `{'H' if is_heading_chunk(c) else 'F'}` {flat(c, 300)}")
        # candidates
        src = gold[0]["source"]
        if src != "*" and src in bm25:
            query = tokens(fr["question"])
            scores = bm25[src].get_scores(query)
            ranked = sorted(zip(scores, by_source[src]), key=lambda x: -x[0])
            out += ["", f"**Corpus candidates** (BM25 over {src} headings; query terms: {' '.join(query)})", ""]
            n = 0
            for sc, (art, doc) in ranked:
                if sc <= 0 or n >= 8:
                    break
                mark = "gold" if (src, art) in gold_keys else "    "
                abro = " ABROGATED" if re.search(r"abrog", doc[:140], re.I) else ""
                out.append(f"- {mark} **{art}** ({sc:.1f}){abro} {flat(doc, 200)}")
                n += 1
        # retrieved
        if run:
            out += ["", "**Retrieved by official v1** (top-6, one block per language variant)", ""]
            for q in qs:
                r = run.get(q["id"])
                if not r:
                    continue
                out.append(f"- `{q['id']}` [{q['language']}] hit={r['score']['hit']}")
                for x in r["retrieved"]:
                    ok = "✓" if any(g["article"] == x["article"] and g["source"] in ("*", x["source"]) for g in gold) else " "
                    out.append(f"    - {ok} {x['source'][:10]} art {x['article']}: {flat(x['snippet'], 150)}")
        s = suggestions.get(cid)
        if s:
            cur = {(g["source"], g["article"]) for g in gold}
            new_pairs = {(g["source"], g["article"]) for g in s["proposed_gold"]}
            added = sorted(new_pairs - cur, key=lambda x: int(x[1]))
            removed = sorted(cur - new_pairs, key=lambda x: int(x[1]))
            out += ["", "**Suggested change:** " + s["rationale"], ""]
            out.append(f"- add: {', '.join(a for _, a in added) or 'none'}   |   remove: {', '.join(a for _, a in removed) or 'none'}")
            out.append("- proposed gold (anchor = the text the intended chunk must start with):")
            for pg in s["proposed_gold"]:
                if pg["source"] == "*":
                    out.append(f"    - any code, article {pg['article']}")
                    continue
                hits = [d for d in by_key.get((pg["source"], pg["article"]), [])
                        if re.sub(r"\s+", " ", d).startswith(re.sub(r"\s+", " ", pg["anchor"]))]
                flag = "" if (len(hits) == 1 or (pg.get("multi") and hits)) else f"  **CHECK: {len(hits)} chunks match this anchor**"
                multi_tag = f" ({len(hits)} chunks: sub-numbered series, all intended)" if pg.get("multi") else ""
                new_tag = "NEW " if (pg["source"], pg["article"]) in added else ""
                out.append(f"    - {new_tag}**{pg['article']}** `{pg['anchor']}`{multi_tag}{flag}")
                if hits:
                    out.append(f"        > {flat(hits[0], 150)}")
        else:
            out += ["", "**Suggested change:** _none_"]
        out += ["", "**Decision:** [ ] approve  [ ] reject  [ ] edit: ______", ""]
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text("\n".join(out), encoding="utf-8")
    print(f"wrote {args.out} ({len(concepts)} concepts, {sum(len(v) for v in concepts.values())} questions)")


if __name__ == "__main__":
    main()
