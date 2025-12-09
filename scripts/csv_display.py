#!/usr/bin/env python3
"""
Generic CSV Display Tool

A flexible command-line tool for displaying CSV files in formatted tables.
Works with any CSV file and provides various display options.

Usage:
    ./scripts/csv_display.py <file.csv>                    # Display as table (first 20 rows)
    ./scripts/csv_display.py <file.csv> --max 50           # Show 50 rows
    ./scripts/csv_display.py <file.csv> --all              # Show all rows
    ./scripts/csv_display.py <file.csv> --vertical         # Show all fields vertically
    ./scripts/csv_display.py <file.csv> --stats            # Show statistics
    ./scripts/csv_display.py data/processed/*.csv          # Display multiple files
"""

import argparse
import csv
import sys
from pathlib import Path
from typing import List, Dict, Optional
import glob


class CSVDisplay:
    """Display CSV files in various formatted views"""

    def __init__(self, filepath: str, empty_value: str = ""):
        """
        Initialize CSV display.

        Args:
            filepath: Path to CSV file
            empty_value: String to display for empty values
        """
        self.filepath = Path(filepath)
        self.empty_value = empty_value
        self.data: List[Dict] = []
        self.headers: List[str] = []

    def load(self) -> bool:
        """
        Load CSV data from file.

        Returns:
            True if successful, False otherwise
        """
        if not self.filepath.exists():
            print(f"❌ File not found: {self.filepath}")
            return False

        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                self.data = list(reader)
                if self.data:
                    self.headers = list(self.data[0].keys())

            # Replace empty values
            for row in self.data:
                for key in row:
                    if row[key] == "" or row[key] is None:
                        row[key] = self.empty_value

            return True
        except Exception as e:
            print(f"❌ Error loading CSV: {e}")
            return False

    def display_table(
        self, max_rows: Optional[int] = 20, max_col_width: int = 30
    ) -> None:
        """
        Display data as a formatted table.

        Args:
            max_rows: Maximum number of rows to display (None = all)
            max_col_width: Maximum width for each column
        """
        if not self.data:
            print("❌ No data to display")
            return

        rows_to_show = self.data[:max_rows] if max_rows else self.data

        # Print filename header
        print(f"\n{'='*120}")
        print(f"📄 {self.filepath.name}")
        print(f"{'='*120}\n")

        # Calculate column widths
        col_widths = {}
        for header in self.headers:
            # Start with header length
            width = len(header)
            # Check data lengths
            for row in rows_to_show:
                width = max(width, len(str(row.get(header, ""))))
            # Cap at max_col_width
            col_widths[header] = min(width, max_col_width)

        # Build format string
        format_parts = []
        separator_parts = []
        for header in self.headers:
            width = col_widths[header]
            format_parts.append(f"{{:<{width}}}")
            separator_parts.append("-" * width)

        format_string = "  ".join(format_parts)
        separator = "  ".join(separator_parts)

        # Print header
        header_values = [h[:col_widths[h]] for h in self.headers]
        print(format_string.format(*header_values))
        print(separator)

        # Print data rows
        for row in rows_to_show:
            values = []
            for header in self.headers:
                value = str(row.get(header, self.empty_value))
                # Truncate if too long
                if len(value) > col_widths[header]:
                    value = value[: col_widths[header] - 3] + "..."
                values.append(value)
            print(format_string.format(*values))

        # Print summary
        print(separator)
        total_rows = len(self.data)
        displayed_rows = len(rows_to_show)
        print(
            f"\nShowing {displayed_rows} of {total_rows} rows | {len(self.headers)} columns"
        )

        if displayed_rows < total_rows:
            print(f"(Use --max {total_rows} or --all to see all rows)")

    def display_vertical(self, max_rows: Optional[int] = 5) -> None:
        """
        Display data vertically (all fields for each row).

        Args:
            max_rows: Maximum number of rows to display
        """
        if not self.data:
            print("❌ No data to display")
            return

        rows_to_show = self.data[:max_rows] if max_rows else self.data

        print(f"\n{'='*80}")
        print(f"📄 {self.filepath.name}")
        print(f"{'='*80}\n")

        # Find max key length for alignment
        max_key_len = max(len(h) for h in self.headers)

        for i, row in enumerate(rows_to_show, 1):
            print(f"{'─'*80}")
            print(f"Row {i} of {len(self.data)}")
            print(f"{'─'*80}")

            for header in self.headers:
                value = row.get(header, self.empty_value)
                # Truncate very long values
                if len(str(value)) > 150:
                    value = str(value)[:147] + "..."
                print(f"{header:<{max_key_len}} : {value}")

            print()

        if len(rows_to_show) < len(self.data):
            remaining = len(self.data) - len(rows_to_show)
            print(f"... and {remaining} more rows (use --max to see more)")

    def display_stats(self) -> None:
        """Display statistics about the CSV data"""
        if not self.data:
            print("❌ No data to display")
            return

        print(f"\n{'='*80}")
        print(f"📊 STATISTICS: {self.filepath.name}")
        print(f"{'='*80}\n")

        total_rows = len(self.data)
        total_cols = len(self.headers)

        print(f"Total rows:    {total_rows:,}")
        print(f"Total columns: {total_cols}")
        print(f"File size:     {self.filepath.stat().st_size:,} bytes")

        # Column statistics
        print(f"\n{'Column Name':<30} {'Filled':>10} {'Empty':>10} {'Fill %':>10}")
        print("-" * 62)

        for header in self.headers[:15]:  # Show first 15 columns
            filled = sum(
                1 for row in self.data if row.get(header) and row[header] != self.empty_value
            )
            empty = total_rows - filled
            fill_pct = (filled / total_rows * 100) if total_rows > 0 else 0

            print(f"{header[:29]:<30} {filled:>10} {empty:>10} {fill_pct:>9.1f}%")

        if len(self.headers) > 15:
            print(f"... and {len(self.headers) - 15} more columns")

        print(f"\n{'='*80}\n")


def display_multiple_files(filepaths: List[str], args) -> None:
    """
    Display multiple CSV files.

    Args:
        filepaths: List of file paths
        args: Parsed command line arguments
    """
    print(f"\n{'='*120}")
    print(f"📚 Displaying {len(filepaths)} CSV files")
    print(f"{'='*120}\n")

    for filepath in filepaths:
        displayer = CSVDisplay(filepath, empty_value=args.empty)

        if not displayer.load():
            continue

        if args.stats:
            displayer.display_stats()
        elif args.vertical:
            displayer.display_vertical(max_rows=args.max)
        else:
            # Default: table view
            max_rows = None if args.all else args.max
            displayer.display_table(max_rows=max_rows, max_col_width=args.width)

        # Add spacing between files
        if len(filepaths) > 1:
            print("\n")


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Generic CSV Display Tool - View CSV files in formatted tables",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Display CSV file (first 20 rows):
    ./scripts/csv_display.py data/processed/chembl_drug_targets.csv

  Show 50 rows:
    ./scripts/csv_display.py data/file.csv --max 50

  Show all rows:
    ./scripts/csv_display.py data/file.csv --all

  Vertical display (all fields):
    ./scripts/csv_display.py data/file.csv --vertical --max 3

  Show statistics:
    ./scripts/csv_display.py data/file.csv --stats

  Display multiple files:
    ./scripts/csv_display.py data/processed/chembl*.csv

  Custom column width and empty value:
    ./scripts/csv_display.py data/file.csv --width 40 --empty "N/A"
        """,
    )

    parser.add_argument(
        "files", nargs="+", help="CSV file(s) to display (supports wildcards)"
    )

    parser.add_argument(
        "--max",
        "-m",
        type=int,
        default=20,
        help="Maximum number of rows to display (default: 20)",
    )

    parser.add_argument(
        "--all", "-a", action="store_true", help="Display all rows (no limit)"
    )

    parser.add_argument(
        "--vertical",
        "-v",
        action="store_true",
        help="Display all fields vertically (default max: 5 rows)",
    )

    parser.add_argument(
        "--stats", "-s", action="store_true", help="Show statistics about the CSV"
    )

    parser.add_argument(
        "--width",
        "-w",
        type=int,
        default=30,
        help="Maximum column width in table view (default: 30)",
    )

    parser.add_argument(
        "--empty",
        "-e",
        type=str,
        default="",
        help='Value to display for empty cells (default: "")',
    )

    args = parser.parse_args()

    # Expand wildcards in file arguments
    all_files = []
    for pattern in args.files:
        matches = glob.glob(pattern)
        if matches:
            all_files.extend(matches)
        else:
            # If no matches, treat as literal filename
            all_files.append(pattern)

    if not all_files:
        print("❌ No files found")
        sys.exit(1)

    # Adjust max for vertical mode default
    if args.vertical and args.max == 20:
        args.max = 5

    # Display files
    display_multiple_files(all_files, args)


if __name__ == "__main__":
    main()
