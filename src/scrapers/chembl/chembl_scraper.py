#!/usr/bin/env python3
"""
ChemBL Data Scraper for Drug Repurposing
Comprehensive scraper following the chembl-scraping-plan.md specifications
"""

import requests
import csv
import json
import os
import pandas as pd
from time import sleep, time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any

# Import CSV utility function directly
def util_escape_csv_field(field):
    """Properly escape a field for CSV format following RFC 4180 standard."""
    if field is None:
        return ""

    field_str = str(field)

    # Check if field needs quoting
    needs_quoting = any(char in field_str for char in [',', '"', '\n', '\r'])

    if needs_quoting or field_str.strip() != field_str:  # Also quote if has leading/trailing spaces
        # Escape any existing double quotes by doubling them
        field_str = field_str.replace('"', '""')
        # Enclose in double quotes
        return f'"{field_str}"'

    return field_str

# Configuration
ORIGIN = "https://www.ebi.ac.uk"
BASE_URL = f"{ORIGIN}/chembl/api/data"
HEADERS = {"User-Agent": "chembl-neo4j-script", "Accept": "application/json"}
RATE_LIMIT_DELAY = 0.5  # seconds between API calls

# Get absolute path to data directory
DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../data/processed"))

# Ensure output directory exists
os.makedirs(DATA_DIR, exist_ok=True)

class ChemBLScraper:
    """Main scraper class for ChemBL data collection"""

    def __init__(self, test_mode=False, time_limit_minutes=None, record_limit=None):
        """
        Initialize the scraper
        Args:
            test_mode: If True, only fetch a small subset of data for testing
            time_limit_minutes: If set, stop scraping after this many minutes
            record_limit: If set, stop after processing this many records
        """
        self.test_mode = test_mode
        self.test_limit = record_limit if record_limit else (10 if test_mode else None)
        self.time_limit_minutes = time_limit_minutes
        self.start_time = None
        self.session = requests.Session()
        self.session.headers.update(HEADERS)

    def escape_csv_field(self, field: Any) -> str:
        """
        Properly escape a field for CSV format using utility function
        """
        return util_escape_csv_field(field)

    def is_time_limit_exceeded(self) -> bool:
        """
        Check if the time limit has been exceeded
        """
        if not self.time_limit_minutes or not self.start_time:
            return False

        elapsed = time() - self.start_time
        return elapsed >= (self.time_limit_minutes * 60)

    def make_request(self, url: str) -> Optional[Dict]:
        """
        Make an API request with error handling and rate limiting
        """
        try:
            response = self.session.get(url, timeout=30)
            sleep(RATE_LIMIT_DELAY)

            if response.status_code == 200:
                return response.json()
            else:
                print(f"❌ Error {response.status_code} for URL: {url}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"❌ Request failed: {e}")
            return None

    def get_paginated_results(self, initial_url: str, data_key: str) -> List[Dict]:
        """
        Handle paginated API responses
        """
        results = []
        url = initial_url
        page_count = 0

        while url:
            if self.test_mode and page_count >= 1:  # Only fetch first page in test mode
                break

            print(f"  Fetching page {page_count + 1}...")
            data = self.make_request(url)

            if not data:
                break

            results.extend(data.get(data_key, []))

            # Get next page URL
            page_meta = data.get("page_meta", {})
            url = page_meta.get("next")
            if url and url.startswith("/"):
                url = ORIGIN + url

            page_count += 1

            if self.test_mode and len(results) >= self.test_limit:
                results = results[:self.test_limit]
                break

        return results

    def get_approved_drugs(self) -> List[Dict]:
        """
        Fetch all approved small molecule drugs (Phase 4)
        """
        print("\n📊 Fetching approved drugs...")
        url = f"{BASE_URL}/molecule?max_phase=4&molecule_type=Small%20molecule&limit=1000"

        molecules = self.get_paginated_results(url, "molecules")
        print(f"✅ Found {len(molecules)} approved drugs")
        return molecules

    def load_approved_drugs_from_csv(self) -> List[Dict]:
        """
        Load approved drugs from existing CSV file (for development/testing)
        Returns a list of drug dictionaries with minimal info needed for further processing
        """
        csv_file = os.path.join(DATA_DIR, "chembl_approved_drugs.csv")

        if not os.path.exists(csv_file):
            print(f"❌ CSV file not found: {csv_file}")
            print("   Please run --approved-drugs-only first to generate the base dataset")
            return []

        print(f"\n📂 Loading existing drugs from CSV...")
        df = pd.read_csv(csv_file)

        # Convert to list of dicts with minimal required fields
        drugs = []
        for _, row in df.iterrows():
            drugs.append({
                "molecule_chembl_id": row["chembl_id"],
                "pref_name": row.get("pref_name", "")
            })

        print(f"✅ Loaded {len(drugs)} drugs from CSV")
        return drugs

    def get_natural_products(self) -> List[Dict]:
        """
        Fetch natural products and plant-derived compounds
        """
        print("\n🌿 Fetching natural products...")
        url = f"{BASE_URL}/molecule?natural_product=1&limit=1000"

        molecules = self.get_paginated_results(url, "molecules")
        print(f"✅ Found {len(molecules)} natural products")
        return molecules

    def get_molecule_details(self, chembl_id: str) -> Optional[Dict]:
        """
        Get detailed information for a specific molecule
        """
        url = f"{BASE_URL}/molecule/{chembl_id}"
        return self.make_request(url)

    def get_mechanisms(self, chembl_id: str) -> List[Dict]:
        """
        Get mechanism of action data for a molecule
        """
        url = f"{BASE_URL}/mechanism?molecule_chembl_id={chembl_id}&limit=1000"
        data = self.make_request(url)
        return data.get("mechanisms", []) if data else []

    def get_indications(self, chembl_id: str) -> List[Dict]:
        """
        Get drug indication data
        """
        url = f"{BASE_URL}/drug_indication?molecule_chembl_id={chembl_id}&limit=1000"
        return self.get_paginated_results(url, "drug_indications")

    def get_drug_warnings(self, chembl_id: str) -> List[Dict]:
        """
        Get drug safety warnings
        """
        url = f"{BASE_URL}/drug_warning?molecule_chembl_id={chembl_id}&limit=1000"
        data = self.make_request(url)
        return data.get("drug_warnings", []) if data else []

    def get_targets(self, chembl_id: str) -> List[Dict]:
        """
        Get target information for a molecule
        """
        url = f"{BASE_URL}/activity?molecule_chembl_id={chembl_id}&limit=1000"
        activities = self.get_paginated_results(url, "activities")

        # Extract unique targets
        targets = {}
        for activity in activities:
            target_id = activity.get("target_chembl_id")
            if target_id and target_id not in targets:
                target_data = self.get_target_details(target_id)
                if target_data:
                    targets[target_id] = target_data

        return list(targets.values())

    def get_target_details(self, target_chembl_id: str) -> Optional[Dict]:
        """
        Get detailed information for a specific target
        """
        url = f"{BASE_URL}/target/{target_chembl_id}"
        return self.make_request(url)

    def get_bioactivities(self, chembl_id: str) -> List[Dict]:
        """
        Get bioactivity data for a molecule
        """
        url = f"{BASE_URL}/activity?molecule_chembl_id={chembl_id}&limit=1000"
        activities = self.get_paginated_results(url, "activities")

        # Filter for high-confidence standard activities
        filtered = []
        for activity in activities:
            if (activity.get("standard_type") in ["IC50", "EC50", "Ki", "Kd"] and
                activity.get("data_validity_comment") is None and
                activity.get("standard_value") is not None):
                filtered.append(activity)

        return filtered

    def get_metabolism(self, chembl_id: str) -> List[Dict]:
        """
        Get drug metabolism data for a molecule
        """
        url = f"{BASE_URL}/metabolism?molecule_chembl_id={chembl_id}&limit=1000"
        data = self.make_request(url)
        return data.get("metabolisms", []) if data else []

    def get_toxicity_assays(self, chembl_id: str) -> List[Dict]:
        """
        Get toxicity and ADME assay data for a molecule
        Filters activities for toxicity (T) and ADME (A) assay types
        """
        url = f"{BASE_URL}/activity?molecule_chembl_id={chembl_id}&limit=1000"
        activities = self.get_paginated_results(url, "activities")

        # Filter for toxicity and ADME assays
        tox_activities = []
        for activity in activities:
            assay_type = activity.get("assay_type", "")
            assay_desc = str(activity.get("assay_description", "")).lower()

            # Include if: assay type is T (Toxicity) or A (ADME), OR description mentions toxicity/herg
            if (assay_type in ["T", "A"] or
                any(keyword in assay_desc for keyword in ["toxicity", "toxic", "herg", "cytotox", "genotox"])):
                tox_activities.append(activity)

        return tox_activities

    def process_approved_drugs(self):
        """
        Process and save approved drug data
        """
        print("\n🔄 Processing approved drugs...")

        # Set start time if using time limit
        if self.time_limit_minutes:
            self.start_time = time()
            print(f"⏱️  Time limit set to {self.time_limit_minutes} minutes")

        drugs = self.get_approved_drugs()

        output_file = os.path.join(DATA_DIR, "chembl_approved_drugs.csv")

        with open(output_file, "w", newline="", encoding="utf-8") as f:
            fieldnames = [
                "chembl_id", "pref_name", "synonyms", "smiles", "inchi", "inchi_key",
                "molecular_formula", "molecular_weight", "alogp", "logd", "hba", "hbd",
                "psa", "rtb", "ro5_violations", "aromatic_rings", "heavy_atoms",
                "qed_weighted", "cx_logp", "cx_logd", "molecular_species",
                "first_approval", "oral_bioavailability", "bioavailability_score",
                "permeability", "indication_class",
                "therapeutic_areas", "natural_product", "polymer_flag",
                "molecule_type", "max_phase", "withdrawn_flag", "withdrawn_reason",
                "withdrawn_year", "withdrawn_country"
            ]

            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for i, drug in enumerate(drugs):
                if self.test_limit and i >= self.test_limit:
                    break

                # Check time limit
                if self.is_time_limit_exceeded():
                    print(f"⏱️  Time limit reached. Processed {i} drugs.")
                    break

                chembl_id = drug["molecule_chembl_id"]

                # Show time remaining if using time limit
                if self.time_limit_minutes:
                    elapsed = time() - self.start_time
                    remaining = (self.time_limit_minutes * 60) - elapsed
                    print(f"  [{i+1}/{len(drugs)}] Processing {chembl_id}... ({remaining:.0f}s remaining)")
                else:
                    print(f"  [{i+1}/{len(drugs)}] Processing {chembl_id}...")

                # Get additional details
                details = self.get_molecule_details(chembl_id)
                if not details:
                    continue

                # Get molecule properties
                props = details.get("molecule_properties", {})

                # Get molecule structures (handle None case)
                structures = details.get("molecule_structures") or {}

                # Get molecule synonyms
                synonyms = details.get("molecule_synonyms", [])
                synonym_list = [s.get("molecule_synonym") for s in synonyms if s.get("molecule_synonym")]

                # Get indication data
                indications = self.get_indications(chembl_id)
                therapeutic_areas = set()
                indication_classes = set()

                for ind in indications:
                    if ind.get("mesh_heading"):
                        therapeutic_areas.add(ind["mesh_heading"])
                    if ind.get("efo_term"):
                        indication_classes.add(ind["efo_term"])

                # Prepare row data
                row = {
                    "chembl_id": chembl_id,
                    "pref_name": details.get("pref_name", ""),
                    "synonyms": self.escape_csv_field("; ".join(synonym_list[:10])),  # Limit synonyms
                    "smiles": structures.get("canonical_smiles", ""),
                    "inchi": structures.get("standard_inchi", ""),
                    "inchi_key": structures.get("standard_inchi_key", ""),
                    "molecular_formula": props.get("full_molformula", ""),
                    "molecular_weight": props.get("mw_freebase", ""),
                    "alogp": props.get("alogp", ""),
                    "logd": props.get("acd_logd", props.get("logd", "")),  # Try multiple field names
                    "hba": props.get("hba", ""),
                    "hbd": props.get("hbd", ""),
                    "psa": props.get("psa", ""),
                    "rtb": props.get("rtb", ""),
                    "ro5_violations": props.get("num_ro5_violations", ""),
                    "aromatic_rings": props.get("aromatic_rings", ""),
                    "heavy_atoms": props.get("heavy_atoms", ""),
                    "qed_weighted": props.get("qed_weighted", ""),
                    "cx_logp": props.get("cx_logp", ""),
                    "cx_logd": props.get("cx_logd", ""),
                    "molecular_species": props.get("molecular_species", ""),
                    "first_approval": details.get("first_approval", ""),
                    "oral_bioavailability": "True" if details.get("oral") else "False",  # Convert to boolean string
                    "bioavailability_score": props.get("bioavailability", ""),  # May not be available
                    "permeability": "",  # Not directly available in ChemBL API
                    "indication_class": self.escape_csv_field("; ".join(indication_classes)),
                    "therapeutic_areas": self.escape_csv_field("; ".join(therapeutic_areas)),
                    "natural_product": details.get("natural_product", ""),
                    "polymer_flag": details.get("polymer_flag", ""),
                    "molecule_type": details.get("molecule_type", ""),
                    "max_phase": details.get("max_phase", ""),
                    "withdrawn_flag": details.get("withdrawn_flag", ""),
                    "withdrawn_reason": details.get("withdrawn_reason", ""),
                    "withdrawn_year": details.get("withdrawn_year", ""),
                    "withdrawn_country": details.get("withdrawn_country", "")
                }

                writer.writerow(row)

        print(f"✅ Saved approved drugs to {output_file}")

    def process_natural_products(self):
        """
        Process and save natural product data
        Following Phase 3 of the scraping plan
        """
        print("\n🔄 Processing natural products...")

        # Set start time if using time limit
        if self.time_limit_minutes:
            self.start_time = time()
            print(f"⏱️  Time limit set to {self.time_limit_minutes} minutes")

        natural_products = self.get_natural_products()

        output_file = os.path.join(DATA_DIR, "chembl_natural_products.csv")

        with open(output_file, "w", newline="", encoding="utf-8") as f:
            fieldnames = [
                "chembl_id", "pref_name", "synonyms", "smiles", "inchi", "inchi_key",
                "molecular_formula", "molecular_weight", "alogp", "logd", "hba", "hbd",
                "psa", "rtb", "ro5_violations", "aromatic_rings", "heavy_atoms",
                "qed_weighted", "cx_logp", "cx_logd", "molecular_species",
                "natural_product", "prodrug", "polymer_flag", "molecule_type",
                "max_phase", "first_approval", "oral_bioavailability",
                "indication_class", "therapeutic_areas", "parent_molecule_chembl_id",
                "structure_type", "chirality", "black_box_warning"
            ]

            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for i, compound in enumerate(natural_products):
                if self.test_limit and i >= self.test_limit:
                    break

                # Check time limit
                if self.is_time_limit_exceeded():
                    print(f"⏱️  Time limit reached. Processed {i} natural products.")
                    break

                chembl_id = compound["molecule_chembl_id"]

                # Show time remaining if using time limit
                if self.time_limit_minutes:
                    elapsed = time() - self.start_time
                    remaining = (self.time_limit_minutes * 60) - elapsed
                    print(f"  [{i+1}/{len(natural_products)}] Processing {chembl_id}... ({remaining:.0f}s remaining)")
                else:
                    print(f"  [{i+1}/{len(natural_products)}] Processing {chembl_id}...")

                # Get additional details
                details = self.get_molecule_details(chembl_id)
                if not details:
                    continue

                # Get molecule properties
                props = details.get("molecule_properties", {})

                # Get molecule structures (handle None case)
                structures = details.get("molecule_structures") or {}

                # Get molecule synonyms
                synonyms = details.get("molecule_synonyms", [])
                synonym_list = [s.get("molecule_synonym") for s in synonyms if s.get("molecule_synonym")]

                # Get indication data
                indications = self.get_indications(chembl_id)
                therapeutic_areas = set()
                indication_classes = set()

                for ind in indications:
                    if ind.get("mesh_heading"):
                        therapeutic_areas.add(ind["mesh_heading"])
                    if ind.get("efo_term"):
                        indication_classes.add(ind["efo_term"])

                # Check for black box warnings
                warnings = self.get_drug_warnings(chembl_id)
                has_black_box = any(w.get("warning_type") == "Black Box Warning" for w in warnings)

                # Get hierarchy information for semi-synthetic derivatives
                hierarchy = details.get("molecule_hierarchy", {})
                parent_chembl_id = hierarchy.get("parent_chembl_id", "")

                # Prepare row data
                row = {
                    "chembl_id": chembl_id,
                    "pref_name": details.get("pref_name", ""),
                    "synonyms": self.escape_csv_field("; ".join(synonym_list[:10])),  # Limit synonyms
                    "smiles": structures.get("canonical_smiles", ""),
                    "inchi": structures.get("standard_inchi", ""),
                    "inchi_key": structures.get("standard_inchi_key", ""),
                    "molecular_formula": props.get("full_molformula", ""),
                    "molecular_weight": props.get("mw_freebase", ""),
                    "alogp": props.get("alogp", ""),
                    "logd": props.get("acd_logd", props.get("logd", "")),
                    "hba": props.get("hba", ""),
                    "hbd": props.get("hbd", ""),
                    "psa": props.get("psa", ""),
                    "rtb": props.get("rtb", ""),
                    "ro5_violations": props.get("num_ro5_violations", ""),
                    "aromatic_rings": props.get("aromatic_rings", ""),
                    "heavy_atoms": props.get("heavy_atoms", ""),
                    "qed_weighted": props.get("qed_weighted", ""),
                    "cx_logp": props.get("cx_logp", ""),
                    "cx_logd": props.get("cx_logd", ""),
                    "molecular_species": props.get("molecular_species", ""),
                    "natural_product": details.get("natural_product", ""),
                    "prodrug": details.get("prodrug", ""),
                    "polymer_flag": details.get("polymer_flag", ""),
                    "molecule_type": details.get("molecule_type", ""),
                    "max_phase": details.get("max_phase", ""),
                    "first_approval": details.get("first_approval", ""),
                    "oral_bioavailability": "True" if details.get("oral") else "False",
                    "indication_class": self.escape_csv_field("; ".join(indication_classes)),
                    "therapeutic_areas": self.escape_csv_field("; ".join(therapeutic_areas)),
                    "parent_molecule_chembl_id": parent_chembl_id,
                    "structure_type": details.get("structure_type", ""),
                    "chirality": props.get("chirality", ""),
                    "black_box_warning": "True" if has_black_box else "False"
                }

                writer.writerow(row)

        print(f"✅ Saved natural products to {output_file}")

    def process_mechanisms(self, use_cached_drugs=True):
        """
        Process and save drug mechanism data
        Args:
            use_cached_drugs: If True, load drugs from CSV instead of fetching from API
        """
        print("\n🔄 Processing drug mechanisms...")

        # Load drugs from CSV or fetch from API
        if use_cached_drugs:
            drugs = self.load_approved_drugs_from_csv()
            if not drugs:
                print("❌ No cached drugs available. Run --approved-drugs-only first.")
                return
        else:
            drugs = self.get_approved_drugs()

        output_file = os.path.join(DATA_DIR, "chembl_drug_mechanisms.csv")

        with open(output_file, "w", newline="", encoding="utf-8") as f:
            fieldnames = [
                "chembl_id", "drug_name", "mechanism_of_action", "action_type",
                "target_chembl_id", "target_name", "target_type", "binding_site",
                "direct_interaction", "molecular_mechanism", "disease_efficacy",
                "mechanism_comment", "selectivity_comment", "references"
            ]

            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for i, drug in enumerate(drugs):
                if self.test_limit and i >= self.test_limit:
                    break

                chembl_id = drug["molecule_chembl_id"]
                drug_name = drug.get("pref_name", "")
                print(f"  [{i+1}/{len(drugs)}] Processing mechanisms for {chembl_id}...")

                mechanisms = self.get_mechanisms(chembl_id)

                for mech in mechanisms:
                    # Get target details
                    target_id = mech.get("target_chembl_id")
                    target_name = ""
                    target_type = ""

                    if target_id:
                        target_data = self.get_target_details(target_id)
                        if target_data:
                            target_name = target_data.get("pref_name", "")
                            target_type = target_data.get("target_type", "")

                    # Prepare row data
                    # Handle references which might be dict objects
                    refs = mech.get("mechanism_refs", [])
                    ref_strings = []
                    for ref in refs:
                        if isinstance(ref, dict):
                            ref_strings.append(ref.get("ref_id", str(ref)))
                        else:
                            ref_strings.append(str(ref))

                    row = {
                        "chembl_id": chembl_id,
                        "drug_name": drug_name,
                        "mechanism_of_action": self.escape_csv_field(mech.get("mechanism_of_action", "")),
                        "action_type": mech.get("action_type", ""),
                        "target_chembl_id": target_id or "",
                        "target_name": target_name,
                        "target_type": target_type,
                        "binding_site": self.escape_csv_field(mech.get("binding_site_comment", "")),
                        "direct_interaction": mech.get("direct_interaction", ""),
                        "molecular_mechanism": mech.get("molecular_mechanism", ""),
                        "disease_efficacy": mech.get("disease_efficacy", ""),
                        "mechanism_comment": self.escape_csv_field(mech.get("mechanism_comment", "")),
                        "selectivity_comment": self.escape_csv_field(mech.get("selectivity_comment", "")),
                        "references": self.escape_csv_field("; ".join(ref_strings))
                    }

                    writer.writerow(row)

        print(f"✅ Saved drug mechanisms to {output_file}")

    def process_targets(self, use_cached_drugs=True):
        """
        Process and save drug target data
        Args:
            use_cached_drugs: If True, load drugs from CSV instead of fetching from API
        """
        print("\n🔄 Processing drug targets...")

        # Load drugs from CSV or fetch from API
        if use_cached_drugs:
            drugs = self.load_approved_drugs_from_csv()
            if not drugs:
                print("❌ No cached drugs available. Run --approved-drugs-only first.")
                return
        else:
            drugs = self.get_approved_drugs()

        output_file = os.path.join(DATA_DIR, "chembl_drug_targets.csv")

        # Collect unique targets
        all_targets = {}

        for i, drug in enumerate(drugs):
            if self.test_limit and i >= self.test_limit:
                break

            chembl_id = drug["molecule_chembl_id"]
            print(f"  [{i+1}/{len(drugs)}] Getting targets for {chembl_id}...")

            targets = self.get_targets(chembl_id)
            for target in targets:
                target_id = target.get("target_chembl_id")
                if target_id and target_id not in all_targets:
                    all_targets[target_id] = target

        # Write target data
        with open(output_file, "w", newline="", encoding="utf-8") as f:
            fieldnames = [
                "target_chembl_id", "pref_name", "target_type", "organism",
                "tax_id", "gene_names", "uniprot_accessions", "target_components",
                "target_family", "target_class", "protein_class"
            ]

            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for target_id, target in all_targets.items():
                # Extract component information
                components = target.get("target_components", [])
                gene_names = []
                uniprot_ids = []

                for comp in components:
                    if comp.get("gene_name"):
                        gene_names.append(comp["gene_name"])
                    if comp.get("accession"):
                        uniprot_ids.append(comp["accession"])

                row = {
                    "target_chembl_id": target_id,
                    "pref_name": target.get("pref_name", ""),
                    "target_type": target.get("target_type", ""),
                    "organism": target.get("organism", ""),
                    "tax_id": target.get("tax_id", ""),
                    "gene_names": self.escape_csv_field("; ".join(gene_names)),
                    "uniprot_accessions": self.escape_csv_field("; ".join(uniprot_ids)),
                    "target_components": len(components),
                    "target_family": target.get("target_family", ""),
                    "target_class": target.get("target_class", ""),
                    "protein_class": self.escape_csv_field("; ".join(target.get("protein_class", [])))
                }

                writer.writerow(row)

        print(f"✅ Saved drug targets to {output_file}")

    def process_indications(self, use_cached_drugs=True):
        """
        Process and save drug indication data
        Args:
            use_cached_drugs: If True, load drugs from CSV instead of fetching from API
        """
        print("\n🔄 Processing drug indications...")

        # Load drugs from CSV or fetch from API
        if use_cached_drugs:
            drugs = self.load_approved_drugs_from_csv()
            if not drugs:
                print("❌ No cached drugs available. Run --approved-drugs-only first.")
                return
        else:
            drugs = self.get_approved_drugs()

        output_file = os.path.join(DATA_DIR, "chembl_drug_indications.csv")

        with open(output_file, "w", newline="", encoding="utf-8") as f:
            fieldnames = [
                "chembl_id", "drug_name", "mesh_id", "mesh_heading",
                "efo_id", "efo_term", "max_phase_for_ind", "indication_refs"
            ]

            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for i, drug in enumerate(drugs):
                if self.test_limit and i >= self.test_limit:
                    break

                chembl_id = drug["molecule_chembl_id"]
                drug_name = drug.get("pref_name", "")
                print(f"  [{i+1}/{len(drugs)}] Processing indications for {chembl_id}...")

                indications = self.get_indications(chembl_id)

                for ind in indications:
                    # Handle references which might be dict objects
                    refs = ind.get("indication_refs", [])
                    ref_strings = []
                    for ref in refs:
                        if isinstance(ref, dict):
                            ref_strings.append(ref.get("ref_id", str(ref)))
                        else:
                            ref_strings.append(str(ref))

                    row = {
                        "chembl_id": chembl_id,
                        "drug_name": drug_name,
                        "mesh_id": ind.get("mesh_id", ""),
                        "mesh_heading": self.escape_csv_field(ind.get("mesh_heading", "")),
                        "efo_id": ind.get("efo_id", ""),
                        "efo_term": self.escape_csv_field(ind.get("efo_term", "")),
                        "max_phase_for_ind": ind.get("max_phase_for_ind", ""),
                        "indication_refs": self.escape_csv_field("; ".join(ref_strings))
                    }

                    writer.writerow(row)

        print(f"✅ Saved drug indications to {output_file}")

    def process_warnings(self, use_cached_drugs=True):
        """
        Process and save drug safety warning data
        Args:
            use_cached_drugs: If True, load drugs from CSV instead of fetching from API
        """
        print("\n🔄 Processing drug warnings...")

        # Load drugs from CSV or fetch from API
        if use_cached_drugs:
            drugs = self.load_approved_drugs_from_csv()
            if not drugs:
                print("❌ No cached drugs available. Run --approved-drugs-only first.")
                return
        else:
            drugs = self.get_approved_drugs()

        output_file = os.path.join(DATA_DIR, "chembl_drug_warnings.csv")

        with open(output_file, "w", newline="", encoding="utf-8") as f:
            fieldnames = [
                "chembl_id", "drug_name", "warning_type", "warning_class",
                "warning_description", "warning_text", "warning_country",
                "warning_year", "warning_refs"
            ]

            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for i, drug in enumerate(drugs):
                if self.test_limit and i >= self.test_limit:
                    break

                chembl_id = drug["molecule_chembl_id"]
                drug_name = drug.get("pref_name", "")
                print(f"  [{i+1}/{len(drugs)}] Processing warnings for {chembl_id}...")

                warnings = self.get_drug_warnings(chembl_id)

                for warning in warnings:
                    # Handle references which might be dict objects
                    refs = warning.get("warning_refs", [])
                    ref_strings = []
                    for ref in refs:
                        if isinstance(ref, dict):
                            ref_strings.append(ref.get("ref_id", str(ref)))
                        else:
                            ref_strings.append(str(ref))

                    row = {
                        "chembl_id": chembl_id,
                        "drug_name": drug_name,
                        "warning_type": warning.get("warning_type", ""),
                        "warning_class": warning.get("warning_class", ""),
                        "warning_description": self.escape_csv_field(warning.get("warning_description", "")),
                        "warning_text": self.escape_csv_field(warning.get("warning_text", "")),
                        "warning_country": warning.get("warning_country", ""),
                        "warning_year": warning.get("warning_year", ""),
                        "warning_refs": self.escape_csv_field("; ".join(ref_strings))
                    }

                    writer.writerow(row)

        print(f"✅ Saved drug warnings to {output_file}")

    def process_metabolism(self, use_cached_drugs=True):
        """
        Process and save drug metabolism data
        Args:
            use_cached_drugs: If True, load drugs from CSV instead of fetching from API
        """
        print("\n🔄 Processing drug metabolism...")

        # Load drugs from CSV or fetch from API
        if use_cached_drugs:
            drugs = self.load_approved_drugs_from_csv()
            if not drugs:
                print("❌ No cached drugs available. Run --approved-drugs-only first.")
                return
        else:
            drugs = self.get_approved_drugs()

        output_file = os.path.join(DATA_DIR, "chembl_drug_metabolism.csv")

        with open(output_file, "w", newline="", encoding="utf-8") as f:
            fieldnames = [
                "drug_chembl_id", "drug_name", "substrate_chembl_id", "substrate_name",
                "metabolite_chembl_id", "metabolite_name", "enzyme_name", "enzyme_tid",
                "organism", "pathway_id", "pathway_key", "met_conversion",
                "met_comment", "references"
            ]

            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for i, drug in enumerate(drugs):
                if self.test_limit and i >= self.test_limit:
                    break

                chembl_id = drug["molecule_chembl_id"]
                drug_name = drug.get("pref_name", "")
                print(f"  [{i+1}/{len(drugs)}] Processing metabolism for {chembl_id}...")

                metabolisms = self.get_metabolism(chembl_id)

                for metab in metabolisms:
                    # Handle references which might be dict objects
                    refs = metab.get("metabolism_refs", [])
                    ref_strings = []
                    for ref in refs:
                        if isinstance(ref, dict):
                            ref_strings.append(ref.get("ref_id", str(ref)))
                        else:
                            ref_strings.append(str(ref))

                    row = {
                        "drug_chembl_id": metab.get("drug_chembl_id", chembl_id),
                        "drug_name": drug_name,
                        "substrate_chembl_id": metab.get("substrate_chembl_id", ""),
                        "substrate_name": self.escape_csv_field(metab.get("substrate_name", "")),
                        "metabolite_chembl_id": metab.get("metabolite_chembl_id", ""),
                        "metabolite_name": self.escape_csv_field(metab.get("metabolite_name", "")),
                        "enzyme_name": self.escape_csv_field(metab.get("enzyme_name", "")),
                        "enzyme_tid": metab.get("target_chembl_id", ""),
                        "organism": metab.get("organism", ""),
                        "pathway_id": metab.get("pathway_id", ""),
                        "pathway_key": metab.get("pathway_key", ""),
                        "met_conversion": self.escape_csv_field(metab.get("met_conversion", "")),
                        "met_comment": self.escape_csv_field(metab.get("met_comment", "")),
                        "references": self.escape_csv_field("; ".join(ref_strings))
                    }

                    writer.writerow(row)

        print(f"✅ Saved drug metabolism to {output_file}")

    def process_bioactivities(self, use_cached_drugs=True):
        """
        Process and save bioactivity data
        Args:
            use_cached_drugs: If True, load drugs from CSV instead of fetching from API
        """
        print("\n🔄 Processing bioactivities...")

        # Load drugs from CSV or fetch from API
        if use_cached_drugs:
            drugs = self.load_approved_drugs_from_csv()
            if not drugs:
                print("❌ No cached drugs available. Run --approved-drugs-only first.")
                return
        else:
            drugs = self.get_approved_drugs()

        output_file = os.path.join(DATA_DIR, "chembl_bioactivities.csv")

        with open(output_file, "w", newline="", encoding="utf-8") as f:
            fieldnames = [
                "chembl_id", "drug_name", "activity_id", "assay_chembl_id",
                "assay_description", "assay_type", "target_chembl_id", "target_name",
                "target_organism", "standard_type", "standard_relation", "standard_value",
                "standard_units", "pchembl_value", "activity_comment", "data_validity_comment"
            ]

            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for i, drug in enumerate(drugs):
                if self.test_limit and i >= self.test_limit:
                    break

                chembl_id = drug["molecule_chembl_id"]
                drug_name = drug.get("pref_name", "")
                print(f"  [{i+1}/{len(drugs)}] Processing bioactivities for {chembl_id}...")

                activities = self.get_bioactivities(chembl_id)

                for act in activities:
                    row = {
                        "chembl_id": chembl_id,
                        "drug_name": drug_name,
                        "activity_id": act.get("activity_id", ""),
                        "assay_chembl_id": act.get("assay_chembl_id", ""),
                        "assay_description": self.escape_csv_field(act.get("assay_description", "")),
                        "assay_type": act.get("assay_type", ""),
                        "target_chembl_id": act.get("target_chembl_id", ""),
                        "target_name": self.escape_csv_field(act.get("target_pref_name", "")),
                        "target_organism": act.get("target_organism", ""),
                        "standard_type": act.get("standard_type", ""),
                        "standard_relation": act.get("standard_relation", ""),
                        "standard_value": act.get("standard_value", ""),
                        "standard_units": act.get("standard_units", ""),
                        "pchembl_value": act.get("pchembl_value", ""),
                        "activity_comment": self.escape_csv_field(act.get("activity_comment", "")),
                        "data_validity_comment": act.get("data_validity_comment", "")
                    }

                    writer.writerow(row)

        print(f"✅ Saved bioactivities to {output_file}")

    def process_toxicity(self, use_cached_drugs=True):
        """
        Process and save toxicity and ADME assay data
        Args:
            use_cached_drugs: If True, load drugs from CSV instead of fetching from API
        """
        print("\n🔄 Processing toxicity assays...")

        # Load drugs from CSV or fetch from API
        if use_cached_drugs:
            drugs = self.load_approved_drugs_from_csv()
            if not drugs:
                print("❌ No cached drugs available. Run --approved-drugs-only first.")
                return
        else:
            drugs = self.get_approved_drugs()

        output_file = os.path.join(DATA_DIR, "chembl_toxicity.csv")

        with open(output_file, "w", newline="", encoding="utf-8") as f:
            fieldnames = [
                "chembl_id", "drug_name", "activity_id", "assay_chembl_id",
                "assay_type", "assay_description", "target_chembl_id", "target_name",
                "target_organism", "standard_type", "standard_relation", "standard_value",
                "standard_units", "pchembl_value", "activity_comment", "toxicity_category"
            ]

            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for i, drug in enumerate(drugs):
                if self.test_limit and i >= self.test_limit:
                    break

                chembl_id = drug["molecule_chembl_id"]
                drug_name = drug.get("pref_name", "")
                print(f"  [{i+1}/{len(drugs)}] Processing toxicity for {chembl_id}...")

                tox_assays = self.get_toxicity_assays(chembl_id)

                for assay in tox_assays:
                    # Categorize toxicity type based on description
                    assay_desc = str(assay.get("assay_description", "")).lower()
                    tox_category = "ADME" if assay.get("assay_type") == "A" else "Toxicity"

                    if "herg" in assay_desc:
                        tox_category = "Cardiotoxicity (hERG)"
                    elif "cytotox" in assay_desc:
                        tox_category = "Cytotoxicity"
                    elif "genotox" in assay_desc:
                        tox_category = "Genotoxicity"
                    elif "hepatotox" in assay_desc or "liver" in assay_desc:
                        tox_category = "Hepatotoxicity"
                    elif "neurotox" in assay_desc:
                        tox_category = "Neurotoxicity"

                    row = {
                        "chembl_id": chembl_id,
                        "drug_name": drug_name,
                        "activity_id": assay.get("activity_id", ""),
                        "assay_chembl_id": assay.get("assay_chembl_id", ""),
                        "assay_type": assay.get("assay_type", ""),
                        "assay_description": self.escape_csv_field(assay.get("assay_description", "")),
                        "target_chembl_id": assay.get("target_chembl_id", ""),
                        "target_name": self.escape_csv_field(assay.get("target_pref_name", "")),
                        "target_organism": assay.get("target_organism", ""),
                        "standard_type": assay.get("standard_type", ""),
                        "standard_relation": assay.get("standard_relation", ""),
                        "standard_value": assay.get("standard_value", ""),
                        "standard_units": assay.get("standard_units", ""),
                        "pchembl_value": assay.get("pchembl_value", ""),
                        "activity_comment": self.escape_csv_field(assay.get("activity_comment", "")),
                        "toxicity_category": tox_category
                    }

                    writer.writerow(row)

        print(f"✅ Saved toxicity data to {output_file}")

    def run_full_scrape(self, use_cached_drugs=True):
        """
        Run the complete scraping pipeline
        Args:
            use_cached_drugs: If True, use existing drug CSV for secondary data collections
        """
        start_time = datetime.now()
        print(f"\n{'='*60}")
        print(f"ChemBL Data Scraper - {'TEST MODE' if self.test_mode else 'FULL MODE'}")
        print(f"Started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*60}")

        # Process each data type
        if not use_cached_drugs:
            # Only fetch approved drugs if not using cache
            self.process_approved_drugs()

        # Process secondary data (will use cached drugs if available)
        self.process_mechanisms(use_cached_drugs=use_cached_drugs)
        self.process_targets(use_cached_drugs=use_cached_drugs)
        self.process_indications(use_cached_drugs=use_cached_drugs)
        self.process_warnings(use_cached_drugs=use_cached_drugs)

        # Calculate runtime
        end_time = datetime.now()
        duration = end_time - start_time

        print(f"\n{'='*60}")
        print(f"✅ Scraping completed!")
        print(f"End time: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Total duration: {duration}")
        print(f"Output directory: {os.path.abspath(DATA_DIR)}")
        print(f"{'='*60}\n")


def main():
    """
    Main entry point for the scraper
    """
    import argparse

    parser = argparse.ArgumentParser(description="ChemBL Data Scraper")
    parser.add_argument(
        "--test",
        action="store_true",
        help="Run in test mode (fetch only 10 records)"
    )
    parser.add_argument(
        "--approved-drugs-only",
        action="store_true",
        help="Only fetch approved drugs data"
    )
    parser.add_argument(
        "--mechanisms-only",
        action="store_true",
        help="Only fetch mechanism data"
    )
    parser.add_argument(
        "--natural-products-only",
        action="store_true",
        help="Only fetch natural products data"
    )
    parser.add_argument(
        "--metabolism-only",
        action="store_true",
        help="Only fetch metabolism data"
    )
    parser.add_argument(
        "--targets-only",
        action="store_true",
        help="Only fetch target data"
    )
    parser.add_argument(
        "--bioactivities-only",
        action="store_true",
        help="Only fetch bioactivity data"
    )
    parser.add_argument(
        "--indications-only",
        action="store_true",
        help="Only fetch indication data"
    )
    parser.add_argument(
        "--warnings-only",
        action="store_true",
        help="Only fetch warning data"
    )
    parser.add_argument(
        "--toxicity-only",
        action="store_true",
        help="Only fetch toxicity and ADME assay data"
    )
    parser.add_argument(
        "--time-limit",
        type=float,
        help="Time limit in minutes for scraping (e.g., 5 for 5 minutes)"
    )
    parser.add_argument(
        "--use-cache",
        action="store_true",
        help="Use cached drug list from CSV instead of re-downloading (faster for development)"
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Maximum number of records to process (e.g., 200 for 200 records)"
    )

    args = parser.parse_args()

    # Initialize scraper
    scraper = ChemBLScraper(test_mode=args.test, time_limit_minutes=args.time_limit, record_limit=args.limit)

    # Run appropriate scraping mode
    if args.approved_drugs_only:
        scraper.process_approved_drugs()
    elif args.natural_products_only:
        scraper.process_natural_products()
    elif args.mechanisms_only:
        scraper.process_mechanisms(use_cached_drugs=args.use_cache)
    elif args.indications_only:
        scraper.process_indications(use_cached_drugs=args.use_cache)
    elif args.metabolism_only:
        scraper.process_metabolism(use_cached_drugs=args.use_cache)
    elif args.targets_only:
        scraper.process_targets(use_cached_drugs=args.use_cache)
    elif args.bioactivities_only:
        scraper.process_bioactivities(use_cached_drugs=args.use_cache)
    elif args.warnings_only:
        scraper.process_warnings(use_cached_drugs=args.use_cache)
    elif args.toxicity_only:
        scraper.process_toxicity(use_cached_drugs=args.use_cache)
    else:
        scraper.run_full_scrape(use_cached_drugs=args.use_cache)


if __name__ == "__main__":
    main()
