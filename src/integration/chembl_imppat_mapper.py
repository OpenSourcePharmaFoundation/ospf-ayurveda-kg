#!/usr/bin/env python3
"""
ChemBL-IMPPAT Compound Mapper
Maps compounds between ChemBL and IMPPAT databases using InChI Keys
"""

import pandas as pd
import requests
from time import sleep
from pathlib import Path
from typing import Dict, List, Tuple, Optional

# Configuration
DATA_DIR = Path(__file__).parent.parent.parent / "data" / "processed"
PUBCHEM_API = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
RATE_LIMIT = 0.2  # PubChem allows 5 requests/second


class CompoundMapper:
    """Maps compounds between ChemBL and IMPPAT databases"""

    def __init__(self):
        self.chembl_compounds = {}  # inchi_key -> chembl_data
        self.imppat_compounds = {}  # pubchem_id -> imppat_data
        self.pubchem_to_inchikey = {}  # pubchem_id -> inchi_key
        self.mappings = []  # List of mapping dicts

    def load_chembl_data(self):
        """Load ChemBL approved drugs and natural products"""
        print("📂 Loading ChemBL data...")

        # Load approved drugs
        drugs_file = DATA_DIR / "chembl_approved_drugs_sample.csv"
        if drugs_file.exists():
            df = pd.read_csv(drugs_file)
            for _, row in df.iterrows():
                inchi_key = row.get("inchi_key")
                if pd.notna(inchi_key) and inchi_key:
                    self.chembl_compounds[inchi_key] = {
                        "chembl_id": row["chembl_id"],
                        "name": row.get("pref_name", ""),
                        "source": "approved_drugs",
                        "molecular_weight": row.get("molecular_weight", ""),
                        "natural_product": row.get("natural_product", "")
                    }

        # Load natural products
        np_file = DATA_DIR / "chembl_natural_products_sample.csv"
        if np_file.exists():
            df = pd.read_csv(np_file)
            for _, row in df.iterrows():
                inchi_key = row.get("inchi_key")
                if pd.notna(inchi_key) and inchi_key:
                    # Add or update (prefer natural products source)
                    if inchi_key not in self.chembl_compounds:
                        self.chembl_compounds[inchi_key] = {
                            "chembl_id": row["chembl_id"],
                            "name": row.get("pref_name", ""),
                            "source": "natural_products",
                            "molecular_weight": row.get("molecular_weight", ""),
                            "natural_product": "1"
                        }

        print(f"✅ Loaded {len(self.chembl_compounds)} ChemBL compounds with InChI Keys")

    def load_imppat_data(self):
        """Load IMPPAT phytochemical data"""
        print("📂 Loading IMPPAT data...")

        phyto_file = DATA_DIR / "phytochem_imppatid_pubchem_id_url.csv"
        if phyto_file.exists():
            df = pd.read_csv(phyto_file)
            for _, row in df.iterrows():
                pubchem_id = row.get("PubChem ID")
                if pd.notna(pubchem_id):
                    # Only process numeric PubChem IDs
                    try:
                        pubchem_id_str = str(int(float(pubchem_id)))
                        self.imppat_compounds[pubchem_id_str] = {
                            "imppat_id": row.get("IMPPAT ID", ""),
                            "name": row.get("Name", ""),
                            "pubchem_id": pubchem_id_str
                        }
                    except (ValueError, TypeError):
                        # Skip non-numeric PubChem IDs
                        continue

        print(f"✅ Loaded {len(self.imppat_compounds)} IMPPAT compounds")

    def fetch_inchikey_from_pubchem(self, pubchem_id: str) -> Optional[str]:
        """Fetch InChI Key for a PubChem compound"""
        try:
            url = f"{PUBCHEM_API}/compound/cid/{pubchem_id}/property/InChIKey/JSON"
            response = requests.get(url, timeout=10)
            sleep(RATE_LIMIT)

            if response.status_code == 200:
                data = response.json()
                props = data.get("PropertyTable", {}).get("Properties", [])
                if props and len(props) > 0:
                    return props[0].get("InChIKey")
        except Exception as e:
            print(f"  ⚠️  Error fetching InChI Key for PubChem {pubchem_id}: {e}")

        return None

    def map_compounds(self, max_requests: int = 100):
        """
        Map IMPPAT compounds to ChemBL using InChI Keys

        Args:
            max_requests: Maximum number of PubChem API requests (rate limit protection)
        """
        print(f"\n🔗 Mapping compounds (max {max_requests} PubChem API requests)...")

        count = 0
        for pubchem_id, imppat_data in self.imppat_compounds.items():
            if count >= max_requests:
                print(f"\n⏸️  Reached request limit ({max_requests}). Stopping to respect rate limits.")
                break

            # Check cache first
            if pubchem_id in self.pubchem_to_inchikey:
                inchi_key = self.pubchem_to_inchikey[pubchem_id]
            else:
                # Fetch from PubChem
                print(f"  [{count+1}/{max_requests}] Fetching InChI Key for PubChem {pubchem_id}...", end="")
                inchi_key = self.fetch_inchikey_from_pubchem(pubchem_id)
                if inchi_key:
                    self.pubchem_to_inchikey[pubchem_id] = inchi_key
                    print(f" ✅")
                else:
                    print(f" ❌ Not found")
                count += 1

            # Check if this InChI Key exists in ChemBL
            if inchi_key and inchi_key in self.chembl_compounds:
                chembl_data = self.chembl_compounds[inchi_key]
                mapping = {
                    "chembl_id": chembl_data["chembl_id"],
                    "chembl_name": chembl_data["name"],
                    "imppat_id": imppat_data["imppat_id"],
                    "imppat_name": imppat_data["name"],
                    "pubchem_id": pubchem_id,
                    "inchi_key": inchi_key,
                    "chembl_source": chembl_data["source"],
                    "molecular_weight": chembl_data.get("molecular_weight", ""),
                    "is_natural_product": chembl_data.get("natural_product", "")
                }
                self.mappings.append(mapping)
                print(f"    🎯 MATCH! {imppat_data['name'][:30]} → {chembl_data['name'][:30]}")

        print(f"\n✅ Found {len(self.mappings)} compound matches")

    def save_mapping_table(self):
        """Save mapping table to CSV"""
        output_file = DATA_DIR / "chembl_imppat_compound_mapping.csv"

        if self.mappings:
            df = pd.DataFrame(self.mappings)
            df.to_csv(output_file, index=False)
            print(f"💾 Saved mapping table to {output_file}")
            print(f"   Total mappings: {len(self.mappings)}")
        else:
            print("⚠️  No mappings found. No file created.")

    def generate_statistics(self):
        """Generate mapping statistics"""
        if not self.mappings:
            print("\n📊 No mappings to analyze")
            return

        print("\n" + "="*80)
        print("📊 MAPPING STATISTICS")
        print("="*80)

        df = pd.DataFrame(self.mappings)

        print(f"\nTotal matches: {len(df)}")
        print(f"ChemBL compounds matched: {df['chembl_id'].nunique()}")
        print(f"IMPPAT compounds matched: {df['imppat_id'].nunique()}")

        # Breakdown by source
        print("\nMatches by ChemBL source:")
        for source, count in df['chembl_source'].value_counts().items():
            print(f"  {source}: {count}")

        # Natural products
        natural_count = df[df['is_natural_product'] == '1'].shape[0]
        print(f"\nNatural products: {natural_count} ({natural_count/len(df)*100:.1f}%)")

        print("="*80)


def main():
    """Main execution"""
    print("\n" + "="*80)
    print("🔗 ChemBL-IMPPAT Compound Mapper")
    print("="*80)

    mapper = CompoundMapper()

    # Load data
    mapper.load_chembl_data()
    mapper.load_imppat_data()

    # Map compounds (limited to 100 requests for testing)
    mapper.map_compounds(max_requests=100)

    # Save results
    mapper.save_mapping_table()

    # Show statistics
    mapper.generate_statistics()

    print("\n✅ Mapping complete!")


if __name__ == "__main__":
    main()
