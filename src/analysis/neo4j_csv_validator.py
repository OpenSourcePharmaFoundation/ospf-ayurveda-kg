#!/usr/bin/env python3
"""
Neo4j CSV Compatibility Validator

Validates ChemBL CSV files for compatibility with Neo4j's LOAD CSV command.
Checks for common issues that cause import failures.

Neo4j LOAD CSV Requirements:
- UTF-8 encoding (no BOM)
- Consistent delimiters (comma by default)
- Proper quoting for fields containing delimiters
- Escaped quotes within quoted fields (doubled quotes)
- Consistent number of columns per row
- No null bytes or other problematic characters
"""

import csv
import os
import re
from pathlib import Path
from typing import List, Dict, Tuple, Any
from datetime import datetime


class Neo4jCSVValidator:
    """Validates CSV files for Neo4j LOAD CSV compatibility."""

    # Characters that can cause Neo4j import issues
    PROBLEMATIC_CHARS = {
        '\x00': 'null byte',
        '\r': 'carriage return (without newline)',
        '\ufeff': 'BOM marker',
    }

    # Characters that need proper quoting
    NEEDS_QUOTING = [',', '"', '\n', '\r\n']

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.filename = os.path.basename(filepath)
        self.issues: List[Dict[str, Any]] = []
        self.warnings: List[Dict[str, Any]] = []
        self.stats: Dict[str, Any] = {}

    def validate(self) -> Dict[str, Any]:
        """Run all validation checks and return results."""
        self.issues = []
        self.warnings = []
        self.stats = {
            'filename': self.filename,
            'filepath': self.filepath,
            'file_size_bytes': os.path.getsize(self.filepath),
        }

        # Run all checks
        self._check_encoding()
        self._check_bom()
        self._check_line_endings()
        self._check_csv_structure()
        self._check_problematic_characters()
        self._check_neo4j_data_types()

        # Determine overall status
        if self.issues:
            self.stats['status'] = '❌ FAILED'
        elif self.warnings:
            self.stats['status'] = '⚠️ WARNINGS'
        else:
            self.stats['status'] = '✅ PASSED'

        self.stats['issues'] = self.issues
        self.stats['warnings'] = self.warnings
        self.stats['issue_count'] = len(self.issues)
        self.stats['warning_count'] = len(self.warnings)

        return self.stats

    def _check_encoding(self):
        """Verify file is valid UTF-8."""
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                f.read()
            self.stats['encoding'] = 'UTF-8 ✓'
        except UnicodeDecodeError as e:
            self.issues.append({
                'type': 'encoding',
                'message': f'File is not valid UTF-8: {e}',
                'severity': 'ERROR'
            })
            self.stats['encoding'] = 'Invalid UTF-8 ✗'

    def _check_bom(self):
        """Check for UTF-8 BOM (Byte Order Mark)."""
        with open(self.filepath, 'rb') as f:
            first_bytes = f.read(3)

        if first_bytes == b'\xef\xbb\xbf':
            self.issues.append({
                'type': 'bom',
                'message': 'File has UTF-8 BOM - Neo4j may misinterpret first column header',
                'severity': 'ERROR',
                'fix': 'Re-save file without BOM or use encoding="utf-8-sig" when reading'
            })
            self.stats['bom'] = 'Present ✗'
        else:
            self.stats['bom'] = 'None ✓'

    def _check_line_endings(self):
        """Check for consistent line endings."""
        with open(self.filepath, 'rb') as f:
            content = f.read()

        crlf_count = content.count(b'\r\n')
        lf_count = content.count(b'\n') - crlf_count
        cr_only = content.count(b'\r') - crlf_count

        self.stats['line_endings'] = {
            'CRLF (Windows)': crlf_count,
            'LF (Unix)': lf_count,
            'CR (old Mac)': cr_only
        }

        if cr_only > 0:
            self.issues.append({
                'type': 'line_endings',
                'message': f'Found {cr_only} standalone CR characters - may cause parsing issues',
                'severity': 'ERROR'
            })

        # Check for mixed line endings
        endings_used = sum([1 for x in [crlf_count, lf_count, cr_only] if x > 0])
        if endings_used > 1:
            self.warnings.append({
                'type': 'line_endings',
                'message': 'Mixed line endings detected - may cause inconsistent behavior',
                'severity': 'WARNING'
            })

    def _check_csv_structure(self):
        """Validate CSV structure - consistent columns, proper quoting."""
        try:
            with open(self.filepath, 'r', encoding='utf-8', newline='') as f:
                # First pass: count columns in header
                reader = csv.reader(f)
                header = next(reader)
                expected_cols = len(header)
                self.stats['columns'] = expected_cols
                self.stats['header'] = header

                # Check for empty column names
                empty_headers = [i for i, h in enumerate(header) if not h.strip()]
                if empty_headers:
                    self.issues.append({
                        'type': 'header',
                        'message': f'Empty column names at positions: {empty_headers}',
                        'severity': 'ERROR'
                    })

                # Check for duplicate column names
                seen = {}
                for i, h in enumerate(header):
                    if h in seen:
                        self.warnings.append({
                            'type': 'header',
                            'message': f'Duplicate column name "{h}" at positions {seen[h]} and {i}',
                            'severity': 'WARNING'
                        })
                    seen[h] = i

                # Second pass: check all rows
                row_count = 1
                inconsistent_rows = []
                for row_num, row in enumerate(reader, start=2):
                    row_count += 1
                    if len(row) != expected_cols:
                        inconsistent_rows.append({
                            'row': row_num,
                            'expected': expected_cols,
                            'actual': len(row)
                        })

                self.stats['row_count'] = row_count

                if inconsistent_rows:
                    # Limit to first 10 examples
                    examples = inconsistent_rows[:10]
                    self.issues.append({
                        'type': 'structure',
                        'message': f'Found {len(inconsistent_rows)} rows with inconsistent column count',
                        'severity': 'ERROR',
                        'examples': examples
                    })
                else:
                    self.stats['structure'] = 'Consistent ✓'

        except csv.Error as e:
            self.issues.append({
                'type': 'csv_parse',
                'message': f'CSV parsing error: {e}',
                'severity': 'ERROR'
            })

    def _check_problematic_characters(self):
        """Check for characters that cause Neo4j import issues."""
        with open(self.filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()

        found_problems = []
        for char, name in self.PROBLEMATIC_CHARS.items():
            if char in content:
                count = content.count(char)
                found_problems.append(f'{name} ({count} occurrences)')

        if found_problems:
            self.issues.append({
                'type': 'characters',
                'message': f'Problematic characters found: {", ".join(found_problems)}',
                'severity': 'ERROR'
            })

        # Check for unescaped quotes within fields
        # This is tricky - we need to parse properly
        try:
            with open(self.filepath, 'r', encoding='utf-8', newline='') as f:
                reader = csv.reader(f)
                for row_num, row in enumerate(reader, start=1):
                    for col_num, field in enumerate(row):
                        # Check for potential issues that slipped through
                        if '"' in field and field.count('"') % 2 != 0:
                            self.warnings.append({
                                'type': 'quoting',
                                'message': f'Odd number of quotes in field at row {row_num}, col {col_num}',
                                'severity': 'WARNING'
                            })
        except Exception:
            pass  # Already reported in structure check

    def _check_neo4j_data_types(self):
        """Check for data type compatibility with Neo4j."""
        try:
            with open(self.filepath, 'r', encoding='utf-8', newline='') as f:
                reader = csv.DictReader(f)

                # Sample first 100 rows for type inference
                sample_size = 100
                type_samples: Dict[str, List[str]] = {col: [] for col in reader.fieldnames or []}

                for i, row in enumerate(reader):
                    if i >= sample_size:
                        break
                    for col, value in row.items():
                        if value and col:
                            type_samples[col].append(value)

                # Infer types
                type_info = {}
                for col, samples in type_samples.items():
                    if not samples:
                        type_info[col] = 'empty'
                        continue

                    # Check if numeric
                    numeric = all(self._is_numeric(s) for s in samples[:20])
                    # Check if boolean
                    boolean = all(s.lower() in ('true', 'false', '0', '1', 'yes', 'no', '') for s in samples[:20])
                    # Check if contains lists (comma or pipe separated)
                    has_lists = any('|' in s or (s.count(',') > 2 and not self._is_numeric(s)) for s in samples[:20])

                    if boolean:
                        type_info[col] = 'boolean'
                    elif numeric:
                        type_info[col] = 'numeric'
                    elif has_lists:
                        type_info[col] = 'list/array'
                        self.warnings.append({
                            'type': 'data_type',
                            'message': f'Column "{col}" appears to contain list data - may need split() in Cypher',
                            'severity': 'INFO'
                        })
                    else:
                        type_info[col] = 'string'

                self.stats['inferred_types'] = type_info

        except Exception as e:
            self.warnings.append({
                'type': 'type_inference',
                'message': f'Could not infer data types: {e}',
                'severity': 'WARNING'
            })

    def _is_numeric(self, value: str) -> bool:
        """Check if a value is numeric."""
        if not value:
            return True
        try:
            float(value)
            return True
        except ValueError:
            return False


def validate_all_chembl_files(data_dir: str) -> Dict[str, Any]:
    """Validate all ChemBL CSV files in the data directory."""
    results = {
        'timestamp': datetime.now().isoformat(),
        'data_dir': data_dir,
        'files': {},
        'summary': {
            'total': 0,
            'passed': 0,
            'warnings': 0,
            'failed': 0
        }
    }

    # Find all ChemBL CSV files
    chembl_files = sorted(Path(data_dir).glob('chembl_*.csv'))

    # Exclude sample files
    chembl_files = [f for f in chembl_files if '_sample' not in f.name]

    print(f"\n{'='*60}")
    print("Neo4j CSV Compatibility Validator")
    print(f"{'='*60}")
    print(f"Validating {len(chembl_files)} ChemBL CSV files...\n")

    for filepath in chembl_files:
        print(f"📄 Validating {filepath.name}...")
        validator = Neo4jCSVValidator(str(filepath))
        file_results = validator.validate()
        results['files'][filepath.name] = file_results

        results['summary']['total'] += 1
        if '✅' in file_results['status']:
            results['summary']['passed'] += 1
            print(f"   {file_results['status']} ({file_results['row_count']:,} rows)")
        elif '⚠️' in file_results['status']:
            results['summary']['warnings'] += 1
            print(f"   {file_results['status']} ({file_results['warning_count']} warnings)")
        else:
            results['summary']['failed'] += 1
            print(f"   {file_results['status']} ({file_results['issue_count']} issues)")

    return results


def generate_validation_report(results: Dict[str, Any]) -> str:
    """Generate a markdown validation report."""
    report = []
    report.append("# Neo4j CSV Compatibility Report")
    report.append(f"\n**Generated:** {results['timestamp']}")
    report.append(f"**Data Directory:** `{results['data_dir']}`")
    report.append("\n---\n")

    # Summary
    s = results['summary']
    report.append("## 📊 Summary\n")
    report.append(f"| Status | Count |")
    report.append(f"|--------|-------|")
    report.append(f"| ✅ Passed | {s['passed']} |")
    report.append(f"| ⚠️ Warnings | {s['warnings']} |")
    report.append(f"| ❌ Failed | {s['failed']} |")
    report.append(f"| **Total** | **{s['total']}** |")
    report.append("\n")

    # Overall status
    if s['failed'] > 0:
        report.append("### ❌ Overall: NOT READY FOR IMPORT\n")
        report.append("Critical issues must be resolved before Neo4j import.\n")
    elif s['warnings'] > 0:
        report.append("### ⚠️ Overall: READY WITH CAUTIONS\n")
        report.append("Files can be imported but review warnings below.\n")
    else:
        report.append("### ✅ Overall: READY FOR IMPORT\n")
        report.append("All files passed validation checks.\n")

    # File Details
    report.append("## 📁 File Details\n")

    for filename, file_data in results['files'].items():
        report.append(f"### {file_data['status']} `{filename}`\n")
        report.append(f"- **Size:** {file_data['file_size_bytes']:,} bytes")
        report.append(f"- **Rows:** {file_data.get('row_count', 'N/A'):,}")
        report.append(f"- **Columns:** {file_data.get('columns', 'N/A')}")
        report.append(f"- **Encoding:** {file_data.get('encoding', 'Unknown')}")
        report.append(f"- **BOM:** {file_data.get('bom', 'Unknown')}")

        # Issues
        if file_data.get('issues'):
            report.append("\n**❌ Issues:**")
            for issue in file_data['issues']:
                report.append(f"- [{issue['severity']}] {issue['message']}")
                if 'fix' in issue:
                    report.append(f"  - Fix: {issue['fix']}")

        # Warnings
        if file_data.get('warnings'):
            report.append("\n**⚠️ Warnings:**")
            for warning in file_data['warnings']:
                report.append(f"- [{warning['severity']}] {warning['message']}")

        # Inferred types (abbreviated)
        if 'inferred_types' in file_data:
            types = file_data['inferred_types']
            list_cols = [k for k, v in types.items() if v == 'list/array']
            if list_cols:
                report.append(f"\n**List columns (need split()):** {', '.join(list_cols[:5])}")

        report.append("\n")

    # Neo4j Import Tips
    report.append("## 💡 Neo4j Import Tips\n")
    report.append("### Basic LOAD CSV Pattern")
    report.append("```cypher")
    report.append("LOAD CSV WITH HEADERS FROM 'file:///chembl_approved_drugs.csv' AS row")
    report.append("CREATE (d:Drug {")
    report.append("  chembl_id: row.chembl_id,")
    report.append("  name: row.pref_name,")
    report.append("  molecular_weight: toFloat(row.molecular_weight)")
    report.append("})")
    report.append("```\n")

    report.append("### Handling List Fields")
    report.append("```cypher")
    report.append("// For comma-separated values in synonyms field:")
    report.append("WITH row, split(row.synonyms, ',') AS synonym_list")
    report.append("UNWIND synonym_list AS synonym")
    report.append("// ... create relationships")
    report.append("```\n")

    report.append("### Handling Null Values")
    report.append("```cypher")
    report.append("// Check for empty strings before conversion:")
    report.append("molecular_weight: CASE WHEN row.molecular_weight = '' THEN null")
    report.append("                       ELSE toFloat(row.molecular_weight) END")
    report.append("```\n")

    return "\n".join(report)


def main():
    """Main function to run validation."""
    data_dir = "data/processed"

    # Run validation
    results = validate_all_chembl_files(data_dir)

    # Generate report
    report = generate_validation_report(results)

    # Save report
    report_path = Path("docs/databases/chembl/neo4j-csv-validation.md")
    report_path.parent.mkdir(parents=True, exist_ok=True)

    with open(report_path, 'w') as f:
        f.write(report)

    # Print summary
    print(f"\n{'='*60}")
    s = results['summary']
    print(f"VALIDATION COMPLETE")
    print(f"{'='*60}")
    print(f"  ✅ Passed:   {s['passed']}")
    print(f"  ⚠️  Warnings: {s['warnings']}")
    print(f"  ❌ Failed:   {s['failed']}")
    print(f"{'='*60}")
    print(f"\n📄 Full report: {report_path}")

    # Return exit code based on results
    return 1 if s['failed'] > 0 else 0


if __name__ == "__main__":
    exit(main())
