#!/usr/bin/env python3
"""Build a blinded copy of data/processed/ with disease-specific indication
signal redacted, for held-out benchmark evaluation of the discovery pipeline.

The pipeline is run against the blinded tree; the answer key (what was removed)
is written separately so a later scoring step can measure whether the pipeline
rediscovered the known therapies without having been shown them.

Usage:
    python src/holdout/blind_dataset.py --disease diabetic-retinopathy
"""

import argparse
import csv
import json
import re
import shutil
import sys
from datetime import date
from pathlib import Path

csv.field_size_limit(sys.maxsize)

# Terms whose presence in an indication field reveals that a drug is already
# used for the held-out disease (or a close ocular analogue whose drug classes
# would give the answer away).
HOLDOUT_PATTERNS = {
    "diabetic-retinopathy": [
        r"retinopath",
        r"macular\s+(o)?edema",
        r"macular\s+retinal\s+edema",
        r"macular\s+degeneration",
        r"vitreoretinopath",
        r"choroidal\s+neovascular",
        r"retinal\s+neovascular",
        r"diabetic\s+macular",
        r"retinal\s+vein\s+occlusion",
        r"wet\s+mac",
    ],
}

# (filename, [columns to scrub]). Columns hold ';'-joined or ','-joined terms.
SCRUB_TARGETS = [
    ("chembl_approved_drugs.csv", ["indication_class", "therapeutic_areas"]),
    ("chembl_drug_indications.csv", ["mesh_heading", "efo_term"]),
    ("chembl_drug_warnings.csv", ["warning_description"]),
    ("chembl_bioactivities.csv", ["assay_description"]),
]


def compile_patterns(disease):
    if disease not in HOLDOUT_PATTERNS:
        raise SystemExit(f"No holdout pattern set defined for '{disease}'")
    return re.compile("|".join(HOLDOUT_PATTERNS[disease]), re.I)


def split_terms(value):
    """ChEMBL joins indication terms with ';'. Preserve other content as one term."""
    return [t for t in value.split(";")]


def scrub_cell(value, rx):
    """Drop semicolon-delimited terms matching the holdout patterns.

    Returns (new_value, removed_terms).
    """
    if not value:
        return value, []
    terms = split_terms(value)
    kept, removed = [], []
    for t in terms:
        (removed if rx.search(t) else kept).append(t)
    if not removed:
        return value, []
    # Rejoin cleanly. A visible redaction marker, a stray leading separator, or
    # odd whitespace would each fingerprint a scrubbed row and let a reader
    # reconstruct the answer key by elimination. A scrubbed field must be
    # indistinguishable from an ordinarily-empty one.
    kept = [t.strip() for t in kept if t.strip()]
    new = "; ".join(kept)
    return new, [t.strip().strip('"') for t in removed]


def build(disease, src_dir, out_dir, key_dir):
    rx = compile_patterns(disease)

    if out_dir.exists():
        shutil.rmtree(out_dir)
    shutil.copytree(src_dir, out_dir, ignore=shutil.ignore_patterns(".DS_Store", ".claude"))

    answer_key = {
        "disease": disease,
        "generated": date.today().isoformat(),
        "source_dir": str(src_dir),
        "blinded_dir": str(out_dir),
        "patterns": HOLDOUT_PATTERNS[disease],
        "redacted_drugs": [],
        "files_scrubbed": {},
    }

    for fname, columns in SCRUB_TARGETS:
        path = out_dir / fname
        if not path.exists():
            continue
        with open(path, newline="", encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            fieldnames = reader.fieldnames
            rows = list(reader)
        cols = [c for c in columns if c in (fieldnames or [])]
        if not cols:
            continue

        n_cells = 0
        for r in rows:
            removed_here = []
            for c in cols:
                new, removed = scrub_cell(r.get(c) or "", rx)
                if removed:
                    r[c] = new
                    removed_here.extend(removed)
                    n_cells += 1
            if removed_here:
                answer_key["redacted_drugs"].append(
                    {
                        "file": fname,
                        "chembl_id": r.get("chembl_id") or r.get("molecule_chembl_id", ""),
                        "name": r.get("pref_name") or r.get("drug_name", ""),
                        "removed_terms": sorted(set(removed_here)),
                    }
                )
        if n_cells:
            with open(path, "w", newline="", encoding="utf-8") as fh:
                w = csv.DictWriter(fh, fieldnames=fieldnames)
                w.writeheader()
                w.writerows(rows)
        answer_key["files_scrubbed"][fname] = {"columns": cols, "cells_redacted": n_cells}

    key_dir.mkdir(parents=True, exist_ok=True)
    (key_dir / "answer-key.json").write_text(json.dumps(answer_key, indent=2))
    return answer_key


def verify(disease, out_dir):
    """Confirm no holdout term survives anywhere in the blinded tree."""
    rx = compile_patterns(disease)
    leaks = []
    for p in sorted(out_dir.rglob("*")):
        if not p.is_file():
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            m = rx.search(line)
            if m:
                leaks.append((str(p.relative_to(out_dir)), i, m.group(0)))
    return leaks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--disease", required=True)
    ap.add_argument("--src", default="data/processed")
    ap.add_argument("--out", default=None)
    ap.add_argument("--key", default=None)
    args = ap.parse_args()

    src = Path(args.src)
    out = Path(args.out or f"data/processed-blinded-{args.disease}")
    key = Path(args.key or f"data/holdout/{args.disease}")

    k = build(args.disease, src, out, key)
    print(f"Blinded tree: {out}")
    for f, meta in k["files_scrubbed"].items():
        print(f"  {f}: {meta['cells_redacted']} cells redacted in {meta['columns']}")
    print(f"Drugs with redacted indications: {len(k['redacted_drugs'])}")
    print(f"Answer key: {key/'answer-key.json'}")

    leaks = verify(args.disease, out)
    print(f"\nVerification: {len(leaks)} residual matches in blinded tree")
    for l in leaks[:20]:
        print("  LEAK", l)
    return 1 if leaks else 0


if __name__ == "__main__":
    raise SystemExit(main())
