#!/usr/bin/env python3
"""
ChemBL Data Display and Generation CLI Tool

This script provides a command-line interface to:
1. Generate ChemBL approved drugs data using the scraper
2. Display the data in various formats (table, vertical, CSV)
3. Export data with customizable empty value placeholders

Usage:
    python scripts/chembl_display.py --generate        # Generate new data
    python scripts/chembl_display.py --display table   # Display as table
    python scripts/chembl_display.py --display vertical # Display vertically
    python scripts/chembl_display.py --export output.csv --empty-value "-"
"""

import argparse
import csv
import os
import sys
import subprocess
from pathlib import Path
from typing import List, Dict, Optional

# Add project root to path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Configuration
DATA_DIR = project_root / "data" / "processed"
CHEMBL_APPROVED_DRUGS_FILE = DATA_DIR / "chembl_approved_drugs.csv"
SCRAPER_PATH = project_root / "src" / "scrapers" / "chembl" / "chembl_scraper.py"


class ChemBLDataManager:
    """Manages ChemBL data generation and display"""

    def __init__(self, empty_value: str = "-"):
        """
        Initialize the data manager.

        Args:
            empty_value: String to use for empty/missing values
        """
        self.empty_value = empty_value
        self.drugs_data: List[Dict] = []

    def generate_data(self, test_mode: bool = True) -> bool:
        """
        Generate new ChemBL data using the scraper.

        Args:
            test_mode: If True, only fetch 10 drugs; if False, fetch all

        Returns:
            True if successful, False otherwise
        """
        print("🔄 Generating ChemBL approved drugs data...")

        # Check if virtual environment exists
        venv_path = project_root / "venv"
        if not venv_path.exists():
            print("❌ Virtual environment not found. Please run:")
            print("   python3 -m venv ./venv")
            print("   source ./venv/bin/activate")
            print("   pip install -r requirements.txt")
            return False

        # Build command
        cmd = [
            str(venv_path / "bin" / "python"),
            str(SCRAPER_PATH),
            "--approved-drugs-only"
        ]

        if test_mode:
            cmd.append("--test")

        # Run scraper
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ Data generation completed successfully!")
                print(f"   Output saved to: {CHEMBL_APPROVED_DRUGS_FILE}")
                return True
            else:
                print(f"❌ Error running scraper: {result.stderr}")
                return False
        except Exception as e:
            print(f"❌ Failed to run scraper: {e}")
            return False

    def load_data(self) -> bool:
        """
        Load ChemBL data from CSV file.

        Returns:
            True if successful, False otherwise
        """
        if not CHEMBL_APPROVED_DRUGS_FILE.exists():
            print(f"❌ Data file not found: {CHEMBL_APPROVED_DRUGS_FILE}")
            print("   Run with --generate flag to create the data first.")
            return False

        try:
            with open(CHEMBL_APPROVED_DRUGS_FILE, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.drugs_data = list(reader)

            # Replace empty values
            for drug in self.drugs_data:
                for key in drug:
                    if drug[key] == '' or drug[key] is None:
                        drug[key] = self.empty_value

            print(f"✅ Loaded {len(self.drugs_data)} drugs from {CHEMBL_APPROVED_DRUGS_FILE}")
            return True
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            return False

    def display_table(self, max_rows: Optional[int] = None):
        """
        Display data in a formatted table.

        Args:
            max_rows: Maximum number of rows to display
        """
        if not self.drugs_data:
            print("❌ No data loaded. Run with --generate or check data file exists.")
            return

        drugs_to_show = self.drugs_data[:max_rows] if max_rows else self.drugs_data

        print("\n" + "="*120)
        print("📊 ChemBL APPROVED DRUGS DATA")
        print("="*120)

        # Key columns for table display
        print(f"{'ChEMBL ID':<12} {'Drug Name':<20} {'Year':<6} {'Formula':<15} {'MW':<8} {'LogP':<7} {'Natural':<8} {'Oral':<6}")
        print("-"*120)

        for drug in drugs_to_show:
            chembl_id = drug['chembl_id'][:12]
            name = drug['pref_name'][:19] if drug['pref_name'] != self.empty_value else self.empty_value
            year = drug['first_approval'][:6] if drug['first_approval'] != self.empty_value else self.empty_value
            formula = drug['molecular_formula'][:14] if drug['molecular_formula'] != self.empty_value else self.empty_value
            mw = f"{float(drug['molecular_weight']):.1f}" if drug['molecular_weight'] != self.empty_value else self.empty_value
            logp = f"{float(drug['alogp']):.2f}" if drug['alogp'] != self.empty_value else self.empty_value
            natural = '✓' if drug['natural_product'] == '1' else '✗' if drug['natural_product'] == '0' else self.empty_value
            oral = '✓' if drug['oral_bioavailability'] == 'True' else '✗' if drug['oral_bioavailability'] == 'False' else self.empty_value

            print(f"{chembl_id:<12} {name:<20} {year:<6} {formula:<15} {mw:<8} {logp:<7} {natural:<8} {oral:<6}")

        print("-"*120)
        print(f"Total drugs: {len(self.drugs_data)} | Columns: {len(self.drugs_data[0].keys()) if self.drugs_data else 0}")

    def display_vertical(self, max_drugs: Optional[int] = None):
        """
        Display data vertically (all fields for each drug).

        Args:
            max_drugs: Maximum number of drugs to display
        """
        if not self.drugs_data:
            print("❌ No data loaded. Run with --generate or check data file exists.")
            return

        drugs_to_show = self.drugs_data[:max_drugs] if max_drugs else self.drugs_data

        for i, drug in enumerate(drugs_to_show, 1):
            print(f"\n{'='*80}")
            print(f"DRUG {i}: {drug.get('pref_name', self.empty_value)} ({drug.get('chembl_id', self.empty_value)})")
            print('='*80)

            for key, value in drug.items():
                # Truncate very long values for display
                display_value = value
                if len(str(value)) > 100:
                    display_value = str(value)[:97] + '...'
                print(f"{key:<28}: {display_value}")

        print(f"\n{'='*80}")
        print(f"Total drugs displayed: {len(drugs_to_show)} of {len(self.drugs_data)}")
        print(f"Total columns: {len(self.drugs_data[0].keys()) if self.drugs_data else 0}")

    def display_raw(self):
        """Display raw CSV content"""
        if not self.drugs_data:
            print("❌ No data loaded. Run with --generate or check data file exists.")
            return

        # Get column headers
        if self.drugs_data:
            headers = list(self.drugs_data[0].keys())

            # Print header
            print(','.join(headers))

            # Print data rows
            for drug in self.drugs_data:
                row = [str(drug.get(h, self.empty_value)) for h in headers]
                print(','.join(row))

    def export_data(self, output_path: str):
        """
        Export data to a new CSV file.

        Args:
            output_path: Path for the output CSV file
        """
        if not self.drugs_data:
            print("❌ No data loaded. Run with --generate or check data file exists.")
            return

        try:
            with open(output_path, 'w', newline='', encoding='utf-8') as f:
                if self.drugs_data:
                    writer = csv.DictWriter(f, fieldnames=self.drugs_data[0].keys())
                    writer.writeheader()
                    writer.writerows(self.drugs_data)

            print(f"✅ Data exported to: {output_path}")
            print(f"   Total drugs: {len(self.drugs_data)}")
            print(f"   Total columns: {len(self.drugs_data[0].keys()) if self.drugs_data else 0}")
        except Exception as e:
            print(f"❌ Error exporting data: {e}")

    def show_statistics(self):
        """Display statistics about the data"""
        if not self.drugs_data:
            print("❌ No data loaded. Run with --generate or check data file exists.")
            return

        print("\n" + "="*80)
        print("📊 ChemBL DATA STATISTICS")
        print("="*80)

        total_drugs = len(self.drugs_data)
        total_columns = len(self.drugs_data[0].keys()) if self.drugs_data else 0

        # Count various properties
        natural_products = sum(1 for d in self.drugs_data if d.get('natural_product') == '1')
        oral_drugs = sum(1 for d in self.drugs_data if d.get('oral_bioavailability') == 'True')
        withdrawn_drugs = sum(1 for d in self.drugs_data if d.get('withdrawn_flag') == 'True')

        # Year statistics
        years = [int(d['first_approval']) for d in self.drugs_data
                if d.get('first_approval') and d['first_approval'] != self.empty_value]

        print(f"Total drugs:          {total_drugs}")
        print(f"Total data fields:    {total_columns}")
        print(f"Natural products:     {natural_products} ({natural_products*100/total_drugs:.1f}%)")
        print(f"Oral bioavailability: {oral_drugs} ({oral_drugs*100/total_drugs:.1f}%)")
        print(f"Withdrawn drugs:      {withdrawn_drugs}")

        if years:
            print(f"Approval year range:  {min(years)} - {max(years)}")

        # Column completeness
        print("\nData completeness by field:")
        for key in list(self.drugs_data[0].keys())[:10]:  # Show first 10 fields
            non_empty = sum(1 for d in self.drugs_data
                          if d.get(key) and d[key] != self.empty_value)
            print(f"  {key:<25}: {non_empty}/{total_drugs} ({non_empty*100/total_drugs:.1f}%)")

        print("="*80)


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="ChemBL Data Display and Generation Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Generate test data (10 drugs):
    ./scripts/chembl_display.py --generate

  Generate full data (all drugs):
    ./scripts/chembl_display.py --generate --full

  Display as table (default):
    ./scripts/chembl_display.py

  Display all fields vertically:
    ./scripts/chembl_display.py --vertical --max 5

  Show statistics:
    ./scripts/chembl_display.py --stats

  Export with custom empty value:
    ./scripts/chembl_display.py --export output.csv --empty "N/A"
        """
    )

    # Generation options
    parser.add_argument(
        '--generate', '-g',
        action='store_true',
        help='Generate new ChemBL data (default: test mode with 10 drugs)'
    )

    parser.add_argument(
        '--full',
        action='store_true',
        help='When generating, fetch ALL drugs (may take hours)'
    )

    # Display options (shortcuts for common operations)
    parser.add_argument(
        '--table', '-t',
        action='store_true',
        help='Display as table (this is the default)'
    )

    parser.add_argument(
        '--vertical', '-v',
        action='store_true',
        help='Display all fields vertically'
    )

    parser.add_argument(
        '--raw', '-r',
        action='store_true',
        help='Display raw CSV format'
    )

    parser.add_argument(
        '--stats', '-s',
        action='store_true',
        help='Show statistics about the data'
    )

    # Modifiers
    parser.add_argument(
        '--max', '-m',
        type=int,
        dest='max_drugs',
        help='Maximum number of drugs to display'
    )

    parser.add_argument(
        '--export', '-e',
        type=str,
        metavar='PATH',
        help='Export data to a new CSV file'
    )

    parser.add_argument(
        '--empty',
        type=str,
        default='-',
        dest='empty_value',
        help='Value for empty fields (default: "-")'
    )

    args = parser.parse_args()

    # Create data manager
    manager = ChemBLDataManager(empty_value=args.empty_value)

    # Handle generation
    if args.generate:
        # Default to test mode unless --full is specified
        test_mode = not args.full
        success = manager.generate_data(test_mode=test_mode)
        if not success:
            sys.exit(1)
        # After generation, also display the table by default
        if manager.load_data():
            manager.display_table(max_rows=args.max_drugs)
        return

    # Load data for all other operations
    if not manager.load_data():
        print("\n💡 Tip: Run with --generate flag to create the data first.")
        sys.exit(1)

    # Determine what to display
    displayed = False

    # Handle display options
    if args.vertical:
        manager.display_vertical(max_drugs=args.max_drugs)
        displayed = True
    elif args.raw:
        manager.display_raw()
        displayed = True
    elif args.table or not (args.stats or args.export):
        # Default to table display if nothing else specified
        manager.display_table(max_rows=args.max_drugs)
        displayed = True

    # Handle statistics
    if args.stats:
        if displayed:
            print()  # Add spacing
        manager.show_statistics()
        displayed = True

    # Handle export
    if args.export:
        if displayed:
            print()  # Add spacing
        manager.export_data(args.export)


if __name__ == "__main__":
    main()