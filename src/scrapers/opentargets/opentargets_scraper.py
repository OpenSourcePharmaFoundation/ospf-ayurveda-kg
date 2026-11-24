#!/usr/bin/env python3
"""
Open Targets gene-disease association scraper for Diabetic Retinopathy (DR)
and related diabetic complications.

Open Targets (https://platform.opentargets.org/) is a free, key-less GraphQL
API. It is used here as a substitute for DisGeNET, whose API now requires a
registered key we do not have for the DR disease set.

NOTE on disease coverage: Open Targets has no ontology term for "diabetic
microvascular complications" as a single entity (only
EFO_0010977 "macrovascular complications of diabetes" exists on the
macrovascular side). The microvascular complication set is therefore
operationalised here as its three standard clinical endpoints - retina
(diabetic retinopathy / diabetic macular edema), kidney (diabetic kidney
disease), and nerve (diabetic neuropathy).

IMPORTANT - LEAKAGE WARNING: the "known_drug" and "clinical" datatype score
columns encode approved-indication / clinical-trial evidence for the
disease, which means they leak DR indication status. Any future blinded
rediscovery run must drop these two columns before use.
"""

import argparse
import csv
import os
import time

import requests

GRAPHQL_URL = "https://api.platform.opentargets.org/api/v4/graphql"
PAGE_SIZE = 500
RATE_LIMIT_DELAY = 0.3

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
DATA_DIR = os.path.join(PROJECT_ROOT, "data", "processed")

QUERY = """
query($id:String!,$i:Int!,$s:Int!){
  disease(efoId:$id){ id name
    associatedTargets(page:{index:$i,size:$s}){
      count
      rows{ score datatypeScores{id score} target{ id approvedSymbol biotype } } } } }
"""

DEFAULT_DISEASES = [
    # Note: slug "DR_only" (not "DR") to avoid colliding with the combined
    # six-disease output file opentargets__DR_gene_disease.csv
    ("MONDO_0005266", "DR_only"),
    ("MONDO_0001660", "PDR"),
    ("EFO_0009760", "NPDR"),
    ("MONDO_0004728", "DME"),
    ("MONDO_0005016", "DKD"),
    ("MONDO_0006626", "DN"),
]

KNOWN_DATATYPES = [
    "genetic_association",
    "literature",
    "known_drug",
    "clinical",
    "animal_model",
    "somatic_mutation",
    "rna_expression",
    "affected_pathway",
    "genetic_literature",
]

LEAKAGE_WARNING = (
    "LEAKAGE WARNING: known_drug and clinical datatype scores encode "
    "approved-indication / clinical-trial evidence for the disease and "
    "therefore leak DR indication status. Drop these two columns before "
    "any blinded rediscovery run."
)


def fetch_disease_targets(disease_id):
    """Fetch all scored target associations for a disease, paginating by PAGE_SIZE."""
    rows = []
    index = 0
    disease_name = None
    expected_count = None

    while True:
        payload = {
            "query": QUERY,
            "variables": {"id": disease_id, "i": index, "s": PAGE_SIZE},
        }
        response = requests.post(
            GRAPHQL_URL,
            json=payload,
            headers={"content-type": "application/json"},
            timeout=60,
        )

        if response.status_code != 200:
            raise RuntimeError(
                f"Open Targets API error for {disease_id}: HTTP {response.status_code} - {response.text}"
            )

        data = response.json()
        if data.get("errors"):
            raise RuntimeError(
                f"Open Targets API GraphQL errors for {disease_id}: {data['errors']}"
            )

        disease = data["data"]["disease"]
        disease_name = disease["name"]
        associated = disease["associatedTargets"]
        expected_count = associated["count"]
        page_rows = associated["rows"]

        rows.extend(page_rows)

        if not page_rows or len(rows) >= expected_count:
            break

        index += 1
        time.sleep(RATE_LIMIT_DELAY)

    if len(rows) != expected_count:
        raise RuntimeError(
            f"Row count mismatch for {disease_id}: collected {len(rows)}, "
            f"API reported count={expected_count}."
        )

    return disease_name, expected_count, rows


def build_rows(disease_id, disease_name, raw_rows, extra_datatypes):
    """Flatten raw API rows into tidy CSV row dicts, discovering unknown datatype ids."""
    out_rows = []
    for r in raw_rows:
        datatype_scores = {ds["id"]: ds["score"] for ds in r.get("datatypeScores", [])}
        for dt_id in datatype_scores:
            if dt_id not in KNOWN_DATATYPES and dt_id not in extra_datatypes:
                extra_datatypes.append(dt_id)

        row = {
            "disease_id": disease_id,
            "disease_name": disease_name,
            "ensembl_id": r["target"]["id"],
            "gene_symbol": r["target"]["approvedSymbol"],
            "biotype": r["target"]["biotype"],
            "overall_score": r["score"],
        }
        for dt_id in KNOWN_DATATYPES + extra_datatypes:
            row[f"score_{dt_id}"] = datatype_scores.get(dt_id, "")
        out_rows.append(row)
    return out_rows


def write_csv(path, rows, fieldnames):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def main():
    parser = argparse.ArgumentParser(
        description="Open Targets gene-disease association scraper"
    )
    parser.add_argument(
        "--disease",
        action="append",
        dest="diseases",
        default=None,
        help="Disease as ID:slug (repeatable). Defaults to the 6-disease DR set.",
    )
    args = parser.parse_args()

    if args.diseases:
        diseases = []
        for entry in args.diseases:
            disease_id, slug = entry.split(":", 1)
            diseases.append((disease_id, slug))
    else:
        diseases = DEFAULT_DISEASES

    extra_datatypes = []
    all_disease_results = {}

    for disease_id, slug in diseases:
        print(f"Fetching Open Targets associations for {disease_id} ({slug})...")
        disease_name, expected_count, raw_rows = fetch_disease_targets(disease_id)
        print(
            f"  {disease_name}: collected {len(raw_rows)} rows (API count={expected_count})"
        )
        all_disease_results[(disease_id, slug)] = (disease_name, raw_rows)

    # Build flattened rows for every disease once all datatype ids are known
    fieldnames = [
        "disease_id",
        "disease_name",
        "ensembl_id",
        "gene_symbol",
        "biotype",
        "overall_score",
    ]
    fieldnames += [f"score_{dt}" for dt in KNOWN_DATATYPES]

    combined_rows = []
    for (disease_id, slug), (disease_name, raw_rows) in all_disease_results.items():
        flat_rows = build_rows(disease_id, disease_name, raw_rows, extra_datatypes)
        if extra_datatypes:
            fieldnames += [
                f"score_{dt}"
                for dt in extra_datatypes
                if f"score_{dt}" not in fieldnames
            ]

        out_path = os.path.join(DATA_DIR, f"opentargets__{slug}_gene_disease.csv")
        write_csv(out_path, flat_rows, fieldnames)
        print(f"  wrote {len(flat_rows)} rows to {out_path}")

        combined_rows.extend(flat_rows)

    if extra_datatypes:
        print(
            f"Discovered datatype ids not in the expected list, columns added: {extra_datatypes}"
        )

    combined_path = os.path.join(DATA_DIR, "opentargets__DR_gene_disease.csv")
    write_csv(combined_path, combined_rows, fieldnames)
    print(f"wrote combined {len(combined_rows)} rows to {combined_path}")

    print(LEAKAGE_WARNING)

    # Report: top 15 genes for MONDO_0005266 by overall_score
    dr_rows = [r for r in combined_rows if r["disease_id"] == "MONDO_0005266"]
    dr_rows_sorted = sorted(dr_rows, key=lambda r: r["overall_score"], reverse=True)[
        :15
    ]
    print("\nTop 15 genes for MONDO_0005266 (diabetic retinopathy) by overall_score:")
    for r in dr_rows_sorted:
        print(f"  {r['gene_symbol']:10s} {r['overall_score']:.4f}")


if __name__ == "__main__":
    main()
