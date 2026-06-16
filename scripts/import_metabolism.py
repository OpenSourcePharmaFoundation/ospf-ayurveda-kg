#!/usr/bin/env python3
"""
Import ChemBL drug metabolism data into Neo4j.

Creates Enzyme, Metabolite nodes and their relationships to existing Drug nodes.
The metabolism CSV has complex quoting that LOAD CSV handles poorly, so this
script uses pandas + the neo4j Python driver instead.

Usage:
    python scripts/import_metabolism.py --password YOUR_PASSWORD
    python scripts/import_metabolism.py  # uses NEO4J_PASSWORD env var
"""

import argparse
import os
import sys

import pandas as pd
from neo4j import GraphDatabase


def import_metabolism(uri, user, password):
    driver = GraphDatabase.driver(uri, auth=(user, password))
    df = pd.read_csv("data/processed/chembl_drug_metabolism.csv")
    print(f"Loaded {len(df)} metabolism records")
    print(f"  Unique drugs: {df['drug_chembl_id'].nunique()}")
    print(f"  Unique enzymes: {df['enzyme_name'].dropna().nunique()}")
    print(f"  Unique metabolites: {df['metabolite_name'].dropna().nunique()}")

    with driver.session() as session:
        # Enzyme nodes
        enzyme_rows = df[df["enzyme_name"].notna() & (df["enzyme_name"] != "")]
        batch = [
            {
                "drug_chembl_id": row["drug_chembl_id"],
                "enzyme_name": str(row["enzyme_name"]).strip().strip('"'),
                "organism": str(row["organism"]) if pd.notna(row["organism"]) else None,
            }
            for _, row in enzyme_rows.iterrows()
        ]
        session.run(
            """
            UNWIND $batch AS row
            MATCH (d:Drug {chembl_id: row.drug_chembl_id})
            MERGE (e:Enzyme {name: row.enzyme_name})
            ON CREATE SET e.organism = row.organism
            MERGE (d)-[:METABOLIZED_BY]->(e)
            """,
            batch=batch,
        )
        result = session.run("MATCH (e:Enzyme) RETURN count(e) AS count")
        print(f"  Created {result.single()['count']} Enzyme nodes")

        # Metabolite nodes
        met_rows = df[df["metabolite_name"].notna() & (df["metabolite_name"] != "")]
        batch = [
            {
                "drug_chembl_id": row["drug_chembl_id"],
                "metabolite_name": str(row["metabolite_name"]).strip().strip('"'),
                "metabolite_chembl_id": (
                    str(row["metabolite_chembl_id"])
                    if pd.notna(row["metabolite_chembl_id"])
                    else None
                ),
                "met_conversion": (
                    str(row["met_conversion"])
                    if pd.notna(row["met_conversion"])
                    else None
                ),
                "enzyme_name": (
                    str(row["enzyme_name"]).strip().strip('"')
                    if pd.notna(row["enzyme_name"])
                    else None
                ),
            }
            for _, row in met_rows.iterrows()
        ]
        session.run(
            """
            UNWIND $batch AS row
            MATCH (d:Drug {chembl_id: row.drug_chembl_id})
            MERGE (m:Metabolite {name: row.metabolite_name})
            ON CREATE SET m.chembl_id = row.metabolite_chembl_id
            MERGE (d)-[r:PRODUCES_METABOLITE]->(m)
            ON CREATE SET r.conversion = row.met_conversion,
                          r.enzyme = row.enzyme_name
            """,
            batch=batch,
        )
        result = session.run("MATCH (m:Metabolite) RETURN count(m) AS count")
        print(f"  Created {result.single()['count']} Metabolite nodes")

        # Enzyme-Metabolite links
        em_rows = df[(df["enzyme_name"].notna()) & (df["metabolite_name"].notna())]
        batch = [
            {
                "enzyme_name": str(row["enzyme_name"]).strip().strip('"'),
                "metabolite_name": str(row["metabolite_name"]).strip().strip('"'),
            }
            for _, row in em_rows.iterrows()
        ]
        session.run(
            """
            UNWIND $batch AS row
            MATCH (e:Enzyme {name: row.enzyme_name})
            MATCH (m:Metabolite {name: row.metabolite_name})
            MERGE (e)-[:CATALYZES]->(m)
            """,
            batch=batch,
        )
        result = session.run("MATCH ()-[r:CATALYZES]->() RETURN count(r) AS count")
        print(f"  Created {result.single()['count']} CATALYZES relationships")

    driver.close()
    print("Done!")


def main():
    parser = argparse.ArgumentParser(description="Import metabolism data into Neo4j")
    parser.add_argument(
        "--uri",
        default=os.environ.get("NEO4J_URI", "bolt://localhost:7687"),
    )
    parser.add_argument(
        "--user",
        default=os.environ.get("NEO4J_USER", "neo4j"),
    )
    parser.add_argument(
        "--password",
        default=os.environ.get("NEO4J_PASSWORD"),
    )
    args = parser.parse_args()

    if not args.password:
        print("Provide --password or set NEO4J_PASSWORD env var")
        sys.exit(1)

    import_metabolism(args.uri, args.user, args.password)


if __name__ == "__main__":
    main()
