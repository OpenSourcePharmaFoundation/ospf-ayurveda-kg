"""Run the FGF21 bridge literature queries and dump abstracts for manual extraction.

Usage:  python -m src.analysis.fgf21_bridge.harvest <query-set>
Writes one text file per query set into the directory given by $FGF21_OUT
(default: the current directory).
"""

import os
import pathlib
import sys

from src.analysis.fgf21_bridge.pubmed import efetch_abstracts, esearch

QUERY_SETS: dict[str, list[str]] = {
    # ---- limb 1: human plasma FGF21 concentrations -------------------------
    "plasma_fibrate": [
        "fenofibrate AND FGF21 AND (serum OR plasma)",
        "(fibrate OR bezafibrate OR gemfibrozil OR pemafibrate) AND FGF21 AND human",
        "PPAR alpha agonist AND circulating FGF21 AND man",
    ],
    "plasma_baseline": [
        "FGF21 AND type 2 diabetes AND serum concentration AND adults",
        "serum FGF21 AND healthy adults AND reference range",
        "FGF21 AND diabetic retinopathy AND serum",
    ],
    "assay": [
        "FGF21 immunoassay AND (comparison OR discrepancy OR ELISA) AND plasma",
        "FGF21 ELISA AND intact AND C-terminal AND FAP cleavage",
    ],
    # ---- limb 2: retinal concentration-response ----------------------------
    "retina_response": [
        "FGF21 AND retina AND (endothelial OR Muller OR retinal pigment epithelium)",
        "FGF21 AND retinopathy AND mice",
        "LY2405319 OR PF-05231023 AND retina",
        "FGF21 analog AND neovascularization AND eye",
    ],
    # ---- limb 4: receptor / pharmacokinetics -------------------------------
    "klotho_pk": [
        "beta-Klotho AND FGF21 AND EC50 AND FGFR1c",
        "FGF21 AND pharmacokinetics AND half-life AND human",
        "FGF21 AND binding protein OR free fraction AND plasma",
    ],
}


def main() -> int:
    which = sys.argv[1] if len(sys.argv) > 1 else None
    out = pathlib.Path(os.environ.get("FGF21_OUT", "."))
    out.mkdir(parents=True, exist_ok=True)
    sets = {which: QUERY_SETS[which]} if which else QUERY_SETS
    for name, queries in sets.items():
        chunks = []
        for q in queries:
            pmids = esearch(q, retmax=25)
            chunks.append(
                f"\n\n{'='*78}\nQUERY: {q}\nPMIDS: {','.join(pmids)}\n{'='*78}\n"
            )
            chunks.append(efetch_abstracts(pmids))
        (out / f"{name}.txt").write_text("".join(chunks))
        print(f"wrote {out / f'{name}.txt'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
