import requests
import csv
from time import sleep

from utils.escape_csv_field import escape_csv_field

ORIGIN = "https://www.ebi.ac.uk"
BASE_URL = f"{ORIGIN}/chembl/api/data"
HEADERS = {"User-Agent": "chembl-neo4j-script", "Accept": "application/json"}
OUTPUT_FILE = "chembl_drugs.csv"


# Step 1: Get approved small molecule drug ChEMBL IDs
def get_approved_drug_chembl_ids():
    url = f"{BASE_URL}/molecule?max_phase=4&molecule_type=Small%20molecule&limit=1000"
    chembl_ids = []
    while url:
        print(f"Fetching data from: {url}")
        r = requests.get(url, headers=HEADERS)
        if r.status_code != 200:
            break
        print("Response data:")
        print(r.text)
        data = r.json()
        chembl_ids.extend([mol["molecule_chembl_id"] for mol in data["molecules"]])
        url = data["page_meta"].get("next")
        if url and url.startswith("/"):
            url = ORIGIN + url
        sleep(0.2)
    return chembl_ids


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


# Step 6: Synonyms
def get_synonyms(chembl_id):
    url = f"{BASE_URL}/molecule_synonyms?molecule_chembl_id={chembl_id}"
    r = requests.get(url, headers=HEADERS)
    if r.status_code != 200:
        return []
    return [
        s["synonyms"]
        for s in r.json().get("molecule_synonyms", [])
        if s.get("synonyms")
    ]


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


# Step 9: Driver function
def collect_data():
    chembl_ids = get_approved_drug_chembl_ids()
    print(f"Discovered {len(chembl_ids)} approved small molecules")

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
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
    collect_data()
