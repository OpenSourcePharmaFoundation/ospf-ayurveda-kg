#!/usr/bin/env python3
"""
Enrich drug candidates with route-of-administration data.

Combines two ChemBL API sources:
  1. drug_indication endpoint — per-indication ATC codes (high precision, ~7% coverage)
  2. molecule endpoint — drug-level ATC classifications (broad coverage, used as fallback)

ATC codes encode route information in their first 3 characters (anatomical/therapeutic group).
"""

import csv
import json
import os
import sys
import time

import requests

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))
CANDIDATES_CSV = os.path.join(
    PROJECT_ROOT,
    "frontend-demo",
    "public",
    "data",
    "analysis",
    "oral_mucositis_candidates.csv",
)
OUTPUT_JSON = os.path.join(
    PROJECT_ROOT,
    "frontend-demo",
    "public",
    "data",
    "analysis",
    "drug_indication_routes.json",
)

CHEMBL_API = "https://www.ebi.ac.uk/chembl/api/data"
RATE_LIMIT = 0.25

# ATC 3-character prefix → typical route of administration
ATC_ROUTE = {
    "A01": "Topical (oral cavity)",
    "A02": "Oral",
    "A03": "Oral",
    "A04": "Oral",
    "A05": "Oral",
    "A06": "Oral",
    "A07": "Oral",
    "A08": "Oral",
    "A09": "Oral",
    "A10": "Oral/Injection",
    "A11": "Oral",
    "A12": "Oral",
    "A14": "Oral",
    "A16": "Oral",
    "B01": "Oral",
    "B02": "Oral/IV",
    "B03": "Oral",
    "B05": "IV",
    "C01": "Oral",
    "C02": "Oral",
    "C03": "Oral",
    "C04": "Oral",
    "C05": "Topical",
    "C07": "Oral",
    "C08": "Oral",
    "C09": "Oral",
    "C10": "Oral",
    "D01": "Topical",
    "D02": "Topical",
    "D03": "Topical",
    "D04": "Topical",
    "D05": "Topical",
    "D06": "Topical",
    "D07": "Topical",
    "D08": "Topical",
    "D10": "Topical",
    "D11": "Topical",
    "G01": "Topical",
    "G02": "Oral",
    "G03": "Oral",
    "G04": "Oral",
    "H01": "Injection",
    "H02": "Oral",
    "H03": "Oral",
    "H04": "Injection",
    "H05": "Injection",
    "J01": "Oral/IV",
    "J02": "Oral/IV",
    "J04": "Oral",
    "J05": "Oral",
    "J06": "Injection",
    "J07": "Injection",
    "L01": "Oral/IV",
    "L02": "Oral",
    "L03": "Injection",
    "L04": "Oral",
    "M01": "Oral",
    "M02": "Topical",
    "M03": "Oral",
    "M04": "Oral",
    "M05": "Oral",
    "M09": "Oral",
    "N01": "Injection/Inhaled",
    "N02": "Oral",
    "N03": "Oral",
    "N04": "Oral",
    "N05": "Oral",
    "N06": "Oral",
    "N07": "Oral",
    "P01": "Oral",
    "P02": "Oral",
    "P03": "Topical",
    "R01": "Nasal",
    "R02": "Topical (oropharyngeal)",
    "R03": "Inhaled",
    "R05": "Oral",
    "R06": "Oral",
    "R07": "Oral",
    "S01": "Ophthalmic",
    "S02": "Otic",
    "S03": "Ophthalmic/Otic",
    "V01": "Injection",
    "V03": "Oral/IV",
    "V04": "Various",
    "V08": "IV",
    "V09": "IV",
    "V10": "IV",
}

# Keywords in indication names → ATC anatomical group prefix for route inference
INDICATION_BODY_SYSTEM = {
    "eye": "S01",
    "ophthalm": "S01",
    "glauc": "S01",
    "conjunctiv": "S01",
    "cataract": "S01",
    "retina": "S01",
    "macula": "S01",
    "uveitis": "S01",
    "keratitis": "S01",
    "ear ": "S02",
    "otitis": "S02",
    "nasal": "R01",
    "rhinitis": "R01",
    "asthma": "R03",
    "bronch": "R03",
    "copd": "R03",
    "dermatitis": "D07",
    "eczema": "D07",
    "psoriasis": "D05",
    "acne": "D10",
    "skin": "D01",
    "stomatitis": "A01",
    "oral ulcer": "A01",
    "oral mucositis": "A01",
    "gingivitis": "A01",
    "periodontal": "A01",
}


def atc_to_route(atc_code: str) -> str | None:
    prefix = atc_code[:3]
    return ATC_ROUTE.get(prefix)


def get_json(url: str, params: dict | None = None) -> dict:
    time.sleep(RATE_LIMIT)
    r = requests.get(url, params=params, timeout=30)
    r.raise_for_status()
    return r.json()


def fetch_molecule(chembl_id: str) -> dict:
    data = get_json(f"{CHEMBL_API}/molecule/{chembl_id}.json")
    return {
        "atc_classifications": data.get("atc_classifications", []),
        "oral": data.get("oral", False),
    }


def fetch_drug_indications(chembl_id: str) -> list[dict]:
    results = []
    offset = 0
    while True:
        data = get_json(
            f"{CHEMBL_API}/drug_indication.json",
            params={"molecule_chembl_id": chembl_id, "limit": 100, "offset": offset},
        )
        inds = data.get("drug_indications", [])
        results.extend(inds)
        total = data.get("page_meta", {}).get("total_count", 0)
        if offset + 100 >= total:
            break
        offset += 100
    return results


def derive_drug_routes(atc_codes: list[str]) -> list[str]:
    """Derive unique routes from a drug's ATC classifications."""
    routes = set()
    for code in atc_codes:
        route = atc_to_route(code)
        if route:
            for r in route.split("/"):
                routes.add(r.strip())
    return sorted(routes)


def infer_route_from_indication(
    indication_name: str, drug_atc_codes: list[str]
) -> str | None:
    """Try to match indication keywords to a body system, then find matching drug ATC code."""
    name_lower = indication_name.lower()
    for keyword, atc_prefix in INDICATION_BODY_SYSTEM.items():
        if keyword in name_lower:
            # First try exact 3-char prefix match (e.g., S01 for ophthalmic)
            for code in drug_atc_codes:
                if code[:3] == atc_prefix:
                    route = atc_to_route(code)
                    if route:
                        return route
            # Fall back to the canonical route for this prefix
            return atc_to_route(atc_prefix)
    return None


def build_route_data(chembl_ids: list[str]) -> dict:
    """Build route data for all candidates."""
    result = {}
    total = len(chembl_ids)

    for i, cid in enumerate(chembl_ids):
        print(f"  [{i + 1}/{total}] {cid}...", end=" ", flush=True)

        try:
            mol = fetch_molecule(cid)
        except Exception as e:
            print(f"molecule fetch failed: {e}")
            result[cid] = {"routes_by_indication": {}, "available_routes": []}
            continue

        drug_atc = mol["atc_classifications"]
        available_routes = derive_drug_routes(drug_atc)

        try:
            indications = fetch_drug_indications(cid)
        except Exception as e:
            print(f"indication fetch failed: {e}")
            result[cid] = {
                "routes_by_indication": {},
                "available_routes": available_routes,
            }
            continue

        routes_by_indication = {}
        for ind in indications:
            # Use both efo_term and mesh_heading as keys for matching
            names = set()
            if ind.get("efo_term"):
                names.add(ind["efo_term"].lower())
            if ind.get("mesh_heading"):
                names.add(ind["mesh_heading"].lower())

            # Strategy 1: per-indication ATC code (highest precision)
            route = None
            refs = ind.get("indication_refs", [])
            atc_refs = [r for r in refs if r.get("ref_type") == "ATC"]
            if atc_refs:
                route = atc_to_route(atc_refs[0]["ref_id"])

            # Strategy 2: keyword inference from indication name
            if not route:
                for name in names:
                    route = infer_route_from_indication(name, drug_atc)
                    if route:
                        break

            # Strategy 3: drug-level fallback (single route drugs)
            if not route and len(available_routes) == 1:
                route = available_routes[0]

            if route:
                for name in names:
                    routes_by_indication[name] = route

        result[cid] = {
            "routes_by_indication": routes_by_indication,
            "available_routes": available_routes,
        }

        matched = sum(1 for v in routes_by_indication.values() if v)
        print(f"{len(indications)} indications, {matched} routes resolved")

    return result


def load_candidate_ids() -> list[str]:
    ids = []
    with open(CANDIDATES_CSV) as f:
        reader = csv.DictReader(f)
        for row in reader:
            cid = (
                row.get(" chembl_id", row.get("chembl_id", "")).strip().strip('"')
            )
            if cid:
                ids.append(cid)
    return ids


def main():
    print("Loading candidate IDs...")
    chembl_ids = load_candidate_ids()
    print(f"Found {len(chembl_ids)} candidates")

    print("Fetching route data from ChemBL API...")
    route_data = build_route_data(chembl_ids)

    os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
    with open(OUTPUT_JSON, "w") as f:
        json.dump(route_data, f, indent=2, sort_keys=True)

    total_inds = sum(
        len(d["routes_by_indication"]) for d in route_data.values()
    )
    with_routes = sum(
        sum(1 for v in d["routes_by_indication"].values() if v)
        for d in route_data.values()
    )
    print(f"\nDone. {total_inds} indication-route pairs, {with_routes} resolved.")
    print(f"Output: {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
