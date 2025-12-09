import requests
import csv
import sys
import os
from time import sleep

# Add project root to Python path to import utilities
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
sys.path.insert(0, project_root)

from src.utils.escape_csv_field import escape_csv_field

ORIGIN = "https://www.ebi.ac.uk"
BASE_URL = f"{ORIGIN}/chembl/api/data"
HEADERS = {"User-Agent": "chembl-neo4j-script", "Accept": "application/json"}

# Output file paths
APPROVED_DRUGS_FILE = "data/processed/chembl_approved_drugs.csv"
DRUG_MECHANISMS_FILE = "data/processed/chembl_drug_mechanisms.csv"
DRUG_INDICATIONS_FILE = "data/processed/chembl_drug_indications.csv"
DRUG_TARGETS_FILE = "data/processed/chembl_drug_targets.csv"
DRUG_WARNINGS_FILE = "data/processed/chembl_drug_warnings.csv"


# Step 1: Get approved small molecule drugs with comprehensive data
def get_approved_drugs_comprehensive(limit_for_testing=None):
    """
    Fetch approved drugs (max_phase=4) with comprehensive molecular data.

    Args:
        limit_for_testing: If provided, limits results to this many drugs for testing

    Returns:
        List of dict containing comprehensive drug data
    """
    url = f"{BASE_URL}/molecule?max_phase=4&molecule_type=Small%20molecule&limit=1000"
    all_drugs = []
    processed_count = 0

    while url:
        print(f"Fetching page from: {url}")
        r = requests.get(url, headers=HEADERS)
        if r.status_code != 200:
            print(f"❌ Failed to fetch page: HTTP {r.status_code}")
            break

        data = r.json()
        drugs = data.get("molecules", [])
        print(f"  Retrieved {len(drugs)} drugs from this page")

        for drug in drugs:
            # Extract core fields available in molecule endpoint
            drug_data = {
                "chembl_id": drug.get("molecule_chembl_id"),
                "pref_name": drug.get("pref_name"),
                "max_phase": drug.get("max_phase"),
                "molecule_type": drug.get("molecule_type"),
                "first_approval": drug.get("first_approval"),
                "oral": drug.get("oral"),
                "parenteral": drug.get("parenteral"),
                "topical": drug.get("topical"),
                "black_box_warning": drug.get("black_box_warning"),
                "natural_product": drug.get("natural_product"),
                "polymer_flag": drug.get("polymer_flag"),
                "therapeutic_flag": drug.get("therapeutic_flag"),
                "dosed_ingredient": drug.get("dosed_ingredient"),
                "structure_type": drug.get("structure_type"),
                "biotherapeutic": drug.get("biotherapeutic"),
                "withdrawn_flag": drug.get("withdrawn_flag"),
                "withdrawn_year": drug.get("withdrawn_year"),
                "withdrawn_country": drug.get("withdrawn_country"),
                "withdrawn_reason": drug.get("withdrawn_reason"),
                # Molecular structure data
                "molecular_formula": drug.get("molecule_properties", {}).get("molecular_formula") if drug.get("molecule_properties") else None,
                "smiles": drug.get("molecule_structures", {}).get("canonical_smiles") if drug.get("molecule_structures") else None,
                "inchi": drug.get("molecule_structures", {}).get("standard_inchi") if drug.get("molecule_structures") else None,
                "inchi_key": drug.get("molecule_structures", {}).get("standard_inchi_key") if drug.get("molecule_structures") else None,
                # Molecular properties
                "molecular_weight": drug.get("molecule_properties", {}).get("full_mwt") if drug.get("molecule_properties") else None,
                "alogp": drug.get("molecule_properties", {}).get("alogp") if drug.get("molecule_properties") else None,
                "psa": drug.get("molecule_properties", {}).get("psa") if drug.get("molecule_properties") else None,
                "hba": drug.get("molecule_properties", {}).get("hba") if drug.get("molecule_properties") else None,
                "hbd": drug.get("molecule_properties", {}).get("hbd") if drug.get("molecule_properties") else None,
                "ro5_violations": drug.get("molecule_properties", {}).get("num_ro5_violations") if drug.get("molecule_properties") else None,
                "rtb": drug.get("molecule_properties", {}).get("rtb") if drug.get("molecule_properties") else None,
                "aromatic_rings": drug.get("molecule_properties", {}).get("aromatic_rings") if drug.get("molecule_properties") else None,
            }
            all_drugs.append(drug_data)
            processed_count += 1

            # Break if we've reached testing limit
            if limit_for_testing and processed_count >= limit_for_testing:
                print(f"Reached testing limit of {limit_for_testing} drugs")
                return all_drugs

        # Get next page
        url = data["page_meta"].get("next")
        if url and url.startswith("/"):
            url = ORIGIN + url
        sleep(0.2)

    print(f"Total approved drugs collected: {len(all_drugs)}")
    return all_drugs


# Legacy function for backward compatibility
def get_approved_drug_chembl_ids():
    drugs = get_approved_drugs_comprehensive()
    return [drug["chembl_id"] for drug in drugs if drug["chembl_id"]]


# Step 2: Retrieve full molecule data
def get_drug_data(chembl_id):
    url = f"{BASE_URL}/molecule/{chembl_id}"
    r = requests.get(url, headers=HEADERS)
    return r.json() if r.status_code == 200 else None


# Step 3: Mechanism of action, binding site, and target
def get_mechanism_data(chembl_id):
    url = f"{BASE_URL}/mechanism?molecule_chembl_id={chembl_id}"
    r = requests.get(url, headers=HEADERS)
    return r.json().get("mechanisms", []) if r.status_code == 200 else []


def get_target_name_and_type(target_chembl_id):
    url = f"{BASE_URL}/target/{target_chembl_id}"
    r = requests.get(url, headers=HEADERS)
    if r.status_code != 200:
        return None, None
    data = r.json()
    return data.get("pref_name"), data.get("target_type")


# Step 4: Lipophilicity
def get_lipophilicity(chembl_id):
    url = f"{BASE_URL}/molecule/{chembl_id}/molecule_properties"
    r = requests.get(url, headers=HEADERS)
    return r.json().get("alogp") if r.status_code == 200 else None


# Step 5: Therapeutic uses (indications)
def get_indications(chembl_id):
    url = f"{BASE_URL}/drug_indication?molecule_chembl_id={chembl_id}"
    indications = []
    while url:
        r = requests.get(url, headers=HEADERS)
        if r.status_code != 200:
            break
        data = r.json()
        for i in data.get("drug_indications", []):
            term = i.get("efo_term") or i.get("indication") or i.get("mesh_heading")
            if term:
                indications.append(escape_csv_field(term))
        url = data["page_meta"].get("next")
        if url and url.startswith("/"):
            url = ORIGIN + url
        sleep(0.2)
    return indications


# Step 6: Enhanced synonyms collection
def get_synonyms(chembl_id):
    """Get all synonyms for a ChEMBL compound, properly escaped for CSV."""
    url = f"{BASE_URL}/molecule_synonyms?molecule_chembl_id={chembl_id}"
    r = requests.get(url, headers=HEADERS)
    if r.status_code != 200:
        return []

    synonyms = []
    for s in r.json().get("molecule_synonyms", []):
        if s.get("synonyms"):
            synonyms.append(escape_csv_field(s["synonyms"]))
    return synonyms


def enrich_drug_data(drug_data):
    """
    Enrich basic drug data with additional information requiring separate API calls.

    Args:
        drug_data: Dictionary containing basic drug info from molecule endpoint

    Returns:
        Dictionary with additional fields: synonyms
    """
    chembl_id = drug_data["chembl_id"]
    print(f"  Enriching data for {chembl_id}...")

    # Add synonyms
    synonyms = get_synonyms(chembl_id)
    drug_data["synonyms"] = "; ".join(synonyms) if synonyms else ""

    sleep(0.2)  # Rate limiting
    return drug_data


# Step 7: Drug class
def get_drug_class(chembl_id):
    url = f"{BASE_URL}/drug_class?molecule_chembl_id={chembl_id}"
    r = requests.get(url, headers=HEADERS)
    if r.status_code != 200:
        return []
    return [
        c["drug_class_name"]
        for c in r.json().get("drug_classes", [])
        if c.get("drug_class_name")
    ]


# Step 8: Adverse effects (via drug warnings)
def get_drug_warnings(chembl_id):
    url = f"{BASE_URL}/drug_warning?molecule_chembl_id={chembl_id}"
    result = requests.get(url, headers=HEADERS)
    if result.status_code != 200:
        return []
    result = []
    # Type: array<string>
    drug_warnings = result.json().get("drug_warnings", [])

    for drug_warning in drug_warnings:
        if drug_warning.get("warning_class"):
            warning_text = escape_csv_field(
                drug_warning.get("warning_text", "").strip()
            )
            formatted_warning = f"{drug_warning['warning_class']} ({warning_text})"
            result.append(formatted_warning)
    return result


# Step 9: New comprehensive approved drugs collection
def collect_approved_drugs_data(test_limit=None):
    """
    Collect comprehensive approved drug data following Phase 2 requirements.

    Args:
        test_limit: If provided, limits collection to this many drugs for testing
    """
    print("🔍 Collecting approved drugs data...")
    drugs = get_approved_drugs_comprehensive(limit_for_testing=test_limit)

    if not drugs:
        print("❌ No drugs collected, exiting")
        return

    print(f"📊 Collected {len(drugs)} approved drugs")
    print("💾 Enriching with additional data (synonyms, etc.)...")

    # Enrich each drug with additional data requiring separate API calls
    enriched_drugs = []
    for i, drug in enumerate(drugs):
        print(f"[{i+1}/{len(drugs)}] Processing {drug['chembl_id']}...")
        try:
            enriched_drug = enrich_drug_data(drug)
            enriched_drugs.append(enriched_drug)
        except Exception as e:
            print(f"❌ Error enriching {drug['chembl_id']}: {e}")
            # Still add the basic data even if enrichment fails
            enriched_drugs.append(drug)

    # Write to CSV
    print(f"💾 Writing {len(enriched_drugs)} drugs to {APPROVED_DRUGS_FILE}")
    with open(APPROVED_DRUGS_FILE, "w", newline="", encoding="utf-8") as f:
        if not enriched_drugs:
            print("⚠️ No enriched drugs to write")
            return

        writer = csv.DictWriter(f, fieldnames=enriched_drugs[0].keys())
        writer.writeheader()

        for drug in enriched_drugs:
            # Apply CSV escaping to string fields that may contain commas
            for key, value in drug.items():
                if isinstance(value, str) and ("," in value or '"' in value):
                    drug[key] = escape_csv_field(value)
            writer.writerow(drug)

    print(f"✅ Approved drugs data saved to {APPROVED_DRUGS_FILE}")


# Step 10: Legacy driver function (preserved for backward compatibility)
def collect_data():
    """Legacy function - use collect_approved_drugs_data() instead."""
    chembl_ids = get_approved_drug_chembl_ids()
    print(f"Discovered {len(chembl_ids)} approved small molecules")

    with open("chembl_drugs_legacy.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "chembl_id",
                "drug_name",
                "class",
                "therapeutic_uses",
                "adverse_effects",
                "binding_sites",
                "target_names",
                "target_types",
                "mechanism_of_action",
                "lipophilicity",
                "synonyms",
            ]
        )

        for i, chembl_id in enumerate(chembl_ids):
            print(f"[{i+1}/{len(chembl_ids)}] Processing {chembl_id}...")

            try:
                molecule = get_drug_data(chembl_id)
                if not molecule:
                    continue

                drug_name = molecule.get("pref_name", "Not available")

                drug_class_raw = get_drug_class(chembl_id)
                print(f"Drug class raw:", drug_class_raw)

                indications_raw = get_indications(chembl_id)
                print(f"Indications raw:", indications_raw)

                warnings_raw = get_drug_warnings(chembl_id)
                print(f"Warnings raw:", warnings_raw)

                synonyms_raw = get_synonyms(chembl_id)
                print(f"Synonyms raw:", synonyms_raw)

                # Turn returned lists into semicolon-separated strings
                drug_class = "; ".join(get_drug_class(chembl_id)) or "Not available"
                uses = "; ".join(get_indications(chembl_id)) or "Not available"
                warnings = "; ".join(get_drug_warnings(chembl_id)) or "Not available"
                synonyms = "; ".join(get_synonyms(chembl_id)) or "Not available"
                lipophilicity = get_lipophilicity(chembl_id) or "Not available"

                mechanisms = get_mechanism_data(chembl_id)
                moa = set()
                binding_sites = set()
                targets = set()
                target_types = set()

                for mech in mechanisms:
                    moa_text = mech.get("mechanism_of_action")
                    if moa_text:
                        moa.add(moa_text)
                    if mech.get("binding_site_comment"):
                        binding_sites.add(mech["binding_site_comment"])
                    target_id = mech.get("target_chembl_id")
                    if target_id:
                        target_name, target_type = get_target_name_and_type(target_id)
                        if target_name:
                            targets.add(target_name)
                        if target_type:
                            target_types.add(target_type)

                # Actual CSV writing occurs here
                writer.writerow(
                    [
                        chembl_id,
                        drug_name,
                        drug_class,
                        uses,
                        warnings,
                        # The below join calls turn returned Python lists into semicolon-separated strings
                        "; ".join(binding_sites) or "Not available",
                        "; ".join(targets) or "Not available",
                        "; ".join(target_types) or "Not available",
                        "; ".join(moa) or "Not available",
                        lipophilicity,
                        synonyms,
                    ]
                )

                sleep(0.2)

            except Exception as e:
                print(f"❌ Error with {chembl_id}: {e}")
                continue


if __name__ == "__main__":
    # Phase 2: Core Drug Data Collection
    # Test with 10 sample drugs first as per plan
    print("🧪 Testing with 10 sample drugs...")
    collect_approved_drugs_data(test_limit=10)

    # To run full collection (uncomment the line below):
    # print("🚀 Running full collection...")
    # collect_approved_drugs_data()
