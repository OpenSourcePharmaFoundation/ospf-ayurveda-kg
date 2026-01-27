#!/usr/bin/env python3
"""
ChemBL Data Statistics Generator

Generates comprehensive statistics for all collected ChemBL datasets,
including record counts, column completeness, and key field distributions.
"""

import pandas as pd
import os
from pathlib import Path
from datetime import datetime


def load_csv_safely(filepath: str) -> pd.DataFrame:
    """Load CSV with proper handling of quoted fields containing commas."""
    try:
        return pd.read_csv(filepath, encoding='utf-8', on_bad_lines='warn')
    except Exception as e:
        print(f"  ⚠️  Error loading {filepath}: {e}")
        return pd.DataFrame()


def calculate_completeness(df: pd.DataFrame) -> dict:
    """Calculate percentage of non-null values for each column."""
    total_rows = len(df)
    if total_rows == 0:
        return {}

    completeness = {}
    for col in df.columns:
        non_null = df[col].notna().sum()
        # Also check for empty strings
        if df[col].dtype == 'object':
            non_empty = (df[col].notna() & (df[col].str.strip() != '')).sum()
            completeness[col] = round(non_empty / total_rows * 100, 1)
        else:
            completeness[col] = round(non_null / total_rows * 100, 1)

    return completeness


def get_unique_counts(df: pd.DataFrame, columns: list) -> dict:
    """Get unique value counts for specified columns."""
    unique_counts = {}
    for col in columns:
        if col in df.columns:
            unique_counts[col] = df[col].nunique()
    return unique_counts


def analyze_approved_drugs(filepath: str) -> dict:
    """Analyze the approved drugs dataset (main production data)."""
    print("\n📊 Analyzing Approved Drugs Dataset...")
    df = load_csv_safely(filepath)

    if df.empty:
        return {"error": "Could not load file"}

    stats = {
        "file": os.path.basename(filepath),
        "file_size_mb": round(os.path.getsize(filepath) / (1024 * 1024), 2),
        "total_records": len(df),
        "total_columns": len(df.columns),
        "columns": list(df.columns),
    }

    # Key metrics
    stats["unique_chembl_ids"] = df['chembl_id'].nunique() if 'chembl_id' in df.columns else 0
    stats["unique_drug_names"] = df['pref_name'].nunique() if 'pref_name' in df.columns else 0

    # Completeness analysis
    stats["completeness"] = calculate_completeness(df)

    # Identify well-populated fields (>80% complete)
    stats["well_populated_fields"] = [k for k, v in stats["completeness"].items() if v >= 80]
    stats["sparse_fields"] = [k for k, v in stats["completeness"].items() if v < 50]

    # Approval year distribution
    if 'first_approval' in df.columns:
        approval_years = df['first_approval'].dropna().astype(int)
        if len(approval_years) > 0:
            stats["approval_year_range"] = f"{int(approval_years.min())} - {int(approval_years.max())}"
            stats["drugs_with_approval_year"] = len(approval_years)
            # Decade distribution
            decades = (approval_years // 10 * 10).value_counts().sort_index()
            stats["approval_by_decade"] = decades.to_dict()

    # Molecule type distribution
    if 'molecule_type' in df.columns:
        stats["molecule_types"] = df['molecule_type'].value_counts().to_dict()

    # Natural product flag
    if 'natural_product' in df.columns:
        np_counts = df['natural_product'].value_counts()
        stats["natural_products"] = np_counts.to_dict()

    # Withdrawn drugs
    if 'withdrawn_flag' in df.columns:
        withdrawn = df['withdrawn_flag'].sum() if df['withdrawn_flag'].dtype in ['int64', 'float64'] else (df['withdrawn_flag'] == True).sum()
        stats["withdrawn_drugs"] = int(withdrawn)

    # Rule of 5 violations
    if 'ro5_violations' in df.columns:
        ro5 = df['ro5_violations'].value_counts().sort_index()
        stats["ro5_violations_distribution"] = ro5.to_dict()

    # Molecular weight statistics
    if 'molecular_weight' in df.columns:
        mw = df['molecular_weight'].dropna()
        if len(mw) > 0:
            stats["molecular_weight"] = {
                "min": round(mw.min(), 2),
                "max": round(mw.max(), 2),
                "mean": round(mw.mean(), 2),
                "median": round(mw.median(), 2)
            }

    return stats


def analyze_natural_products(filepath: str) -> dict:
    """Analyze natural products dataset."""
    print("\n🌿 Analyzing Natural Products Dataset...")
    df = load_csv_safely(filepath)

    if df.empty:
        return {"error": "Could not load file"}

    stats = {
        "file": os.path.basename(filepath),
        "file_size_kb": round(os.path.getsize(filepath) / 1024, 2),
        "total_records": len(df),
        "unique_compounds": df['chembl_id'].nunique() if 'chembl_id' in df.columns else 0,
        "completeness": calculate_completeness(df),
    }

    if 'max_phase' in df.columns:
        stats["max_phase_distribution"] = df['max_phase'].value_counts().to_dict()

    return stats


def analyze_mechanisms(filepath: str) -> dict:
    """Analyze drug mechanisms dataset."""
    print("\n⚙️  Analyzing Drug Mechanisms Dataset...")
    df = load_csv_safely(filepath)

    if df.empty:
        return {"error": "Could not load file"}

    stats = {
        "file": os.path.basename(filepath),
        "file_size_kb": round(os.path.getsize(filepath) / 1024, 2),
        "total_records": len(df),
        "unique_drugs": df['chembl_id'].nunique() if 'chembl_id' in df.columns else 0,
        "unique_targets": df['target_chembl_id'].nunique() if 'target_chembl_id' in df.columns else 0,
        "completeness": calculate_completeness(df),
    }

    if 'action_type' in df.columns:
        stats["action_types"] = df['action_type'].value_counts().to_dict()

    if 'target_type' in df.columns:
        stats["target_types"] = df['target_type'].value_counts().to_dict()

    return stats


def analyze_indications(filepath: str) -> dict:
    """Analyze drug indications dataset."""
    print("\n💊 Analyzing Drug Indications Dataset...")
    df = load_csv_safely(filepath)

    if df.empty:
        return {"error": "Could not load file"}

    stats = {
        "file": os.path.basename(filepath),
        "file_size_kb": round(os.path.getsize(filepath) / 1024, 2),
        "total_records": len(df),
        "unique_drugs": df['chembl_id'].nunique() if 'chembl_id' in df.columns else 0,
        "unique_mesh_terms": df['mesh_heading'].nunique() if 'mesh_heading' in df.columns else 0,
        "unique_efo_terms": df['efo_term'].nunique() if 'efo_term' in df.columns else 0,
        "completeness": calculate_completeness(df),
    }

    if 'max_phase_for_ind' in df.columns:
        stats["phase_distribution"] = df['max_phase_for_ind'].value_counts().to_dict()

    return stats


def analyze_targets(filepath: str) -> dict:
    """Analyze drug targets dataset."""
    print("\n🎯 Analyzing Drug Targets Dataset...")
    df = load_csv_safely(filepath)

    if df.empty:
        return {"error": "Could not load file"}

    stats = {
        "file": os.path.basename(filepath),
        "file_size_kb": round(os.path.getsize(filepath) / 1024, 2),
        "total_records": len(df),
        "unique_targets": df['target_chembl_id'].nunique() if 'target_chembl_id' in df.columns else 0,
        "completeness": calculate_completeness(df),
    }

    if 'target_type' in df.columns:
        stats["target_types"] = df['target_type'].value_counts().to_dict()

    if 'organism' in df.columns:
        stats["organisms"] = df['organism'].value_counts().head(10).to_dict()

    return stats


def analyze_warnings(filepath: str) -> dict:
    """Analyze drug warnings dataset."""
    print("\n⚠️  Analyzing Drug Warnings Dataset...")
    df = load_csv_safely(filepath)

    if df.empty:
        return {"error": "Could not load file"}

    stats = {
        "file": os.path.basename(filepath),
        "file_size_kb": round(os.path.getsize(filepath) / 1024, 2),
        "total_records": len(df),
        "unique_drugs": df['chembl_id'].nunique() if 'chembl_id' in df.columns else 0,
        "completeness": calculate_completeness(df),
    }

    if 'warning_class' in df.columns:
        stats["warning_classes"] = df['warning_class'].value_counts().to_dict()

    if 'warning_type' in df.columns:
        stats["warning_types"] = df['warning_type'].value_counts().to_dict()

    return stats


def analyze_bioactivities(filepath: str) -> dict:
    """Analyze bioactivities dataset."""
    print("\n🧪 Analyzing Bioactivities Dataset...")
    df = load_csv_safely(filepath)

    if df.empty:
        return {"error": "Could not load file"}

    stats = {
        "file": os.path.basename(filepath),
        "file_size_kb": round(os.path.getsize(filepath) / 1024, 2),
        "total_records": len(df),
        "unique_drugs": df['chembl_id'].nunique() if 'chembl_id' in df.columns else 0,
        "unique_assays": df['assay_chembl_id'].nunique() if 'assay_chembl_id' in df.columns else 0,
        "completeness": calculate_completeness(df),
    }

    if 'standard_type' in df.columns:
        stats["activity_types"] = df['standard_type'].value_counts().to_dict()

    if 'pchembl_value' in df.columns:
        pchembl = df['pchembl_value'].dropna()
        if len(pchembl) > 0:
            stats["pchembl_stats"] = {
                "min": round(pchembl.min(), 2),
                "max": round(pchembl.max(), 2),
                "mean": round(pchembl.mean(), 2),
                "records_with_pchembl": len(pchembl)
            }

    return stats


def analyze_metabolism(filepath: str) -> dict:
    """Analyze drug metabolism dataset."""
    print("\n🔄 Analyzing Drug Metabolism Dataset...")
    df = load_csv_safely(filepath)

    if df.empty:
        return {"error": "Could not load file"}

    stats = {
        "file": os.path.basename(filepath),
        "file_size_mb": round(os.path.getsize(filepath) / (1024 * 1024), 2),
        "total_records": len(df),
        "unique_drugs": df['drug_chembl_id'].nunique() if 'drug_chembl_id' in df.columns else 0,
        "unique_metabolites": df['metabolite_chembl_id'].nunique() if 'metabolite_chembl_id' in df.columns else 0,
        "unique_enzymes": df['enzyme_name'].nunique() if 'enzyme_name' in df.columns else 0,
        "completeness": calculate_completeness(df),
    }

    if 'enzyme_name' in df.columns:
        stats["top_enzymes"] = df['enzyme_name'].value_counts().head(10).to_dict()

    return stats


def analyze_toxicity(filepath: str) -> dict:
    """Analyze toxicity dataset."""
    print("\n☠️  Analyzing Toxicity Dataset...")
    df = load_csv_safely(filepath)

    if df.empty:
        return {"error": "Could not load file"}

    stats = {
        "file": os.path.basename(filepath),
        "file_size_bytes": os.path.getsize(filepath),
        "total_records": len(df),
        "unique_drugs": df['chembl_id'].nunique() if 'chembl_id' in df.columns else 0,
        "completeness": calculate_completeness(df),
        "note": "ChemBL has limited toxicity data - this is expected"
    }

    if 'toxicity_category' in df.columns:
        stats["toxicity_categories"] = df['toxicity_category'].value_counts().to_dict()

    return stats


def generate_summary_report(all_stats: dict) -> str:
    """Generate a markdown summary report."""
    report = []
    report.append("# ChemBL Data Collection Statistics Report")
    report.append(f"\n**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append(f"**Project:** OSPF Ayurveda Knowledge Graph")
    report.append("\n---\n")

    # Executive Summary
    report.append("## 📊 Executive Summary\n")

    total_records = sum(s.get('total_records', 0) for s in all_stats.values())
    total_size_mb = sum(s.get('file_size_mb', s.get('file_size_kb', 0) / 1024) for s in all_stats.values())

    report.append(f"| Metric | Value |")
    report.append(f"|--------|-------|")
    report.append(f"| Total Datasets | {len(all_stats)} |")
    report.append(f"| Total Records | {total_records:,} |")
    report.append(f"| Total Storage | {total_size_mb:.2f} MB |")

    if 'approved_drugs' in all_stats:
        ad = all_stats['approved_drugs']
        report.append(f"| Unique Approved Drugs | {ad.get('unique_chembl_ids', 'N/A'):,} |")

    report.append("\n")

    # Dataset Overview Table
    report.append("## 📁 Dataset Overview\n")
    report.append("| Dataset | Records | Size | Status |")
    report.append("|---------|---------|------|--------|")

    dataset_info = [
        ('approved_drugs', 'Approved Drugs', '✅ Production'),
        ('natural_products', 'Natural Products', '⚠️ Test Data'),
        ('mechanisms', 'Drug Mechanisms', '⚠️ Test Data'),
        ('indications', 'Drug Indications', '⚠️ Test Data'),
        ('targets', 'Drug Targets', '⚠️ Test Data'),
        ('bioactivities', 'Bioactivities', '⚠️ Test Data'),
        ('metabolism', 'Drug Metabolism', '⚠️ Test Data'),
        ('warnings', 'Drug Warnings', '⚠️ Test Data'),
        ('toxicity', 'Toxicity', '⚠️ Test Data'),
    ]

    for key, name, status in dataset_info:
        if key in all_stats:
            s = all_stats[key]
            records = s.get('total_records', 0)
            size = s.get('file_size_mb', s.get('file_size_kb', s.get('file_size_bytes', 0) / 1024) / 1024)
            if size >= 1:
                size_str = f"{size:.2f} MB"
            elif size * 1024 >= 1:
                size_str = f"{size * 1024:.1f} KB"
            else:
                size_str = f"{int(size * 1024 * 1024)} B"
            report.append(f"| {name} | {records:,} | {size_str} | {status} |")

    report.append("\n")

    # Approved Drugs Deep Dive
    if 'approved_drugs' in all_stats:
        ad = all_stats['approved_drugs']
        report.append("## 💊 Approved Drugs Analysis (Production Data)\n")

        report.append(f"### Key Metrics\n")
        report.append(f"- **Total Records:** {ad.get('total_records', 0):,}")
        report.append(f"- **Unique ChemBL IDs:** {ad.get('unique_chembl_ids', 0):,}")
        report.append(f"- **Unique Drug Names:** {ad.get('unique_drug_names', 0):,}")
        report.append(f"- **File Size:** {ad.get('file_size_mb', 0):.2f} MB")
        report.append(f"- **Columns:** {ad.get('total_columns', 0)}")

        if 'approval_year_range' in ad:
            report.append(f"- **Approval Year Range:** {ad['approval_year_range']}")
            report.append(f"- **Drugs with Approval Year:** {ad.get('drugs_with_approval_year', 0):,}")

        if 'withdrawn_drugs' in ad:
            report.append(f"- **Withdrawn Drugs:** {ad['withdrawn_drugs']}")

        report.append("\n")

        # Molecule Type Distribution
        if 'molecule_types' in ad:
            report.append("### Molecule Type Distribution\n")
            report.append("| Type | Count |")
            report.append("|------|-------|")
            for mtype, count in sorted(ad['molecule_types'].items(), key=lambda x: -x[1]):
                report.append(f"| {mtype} | {count:,} |")
            report.append("\n")

        # Approval by Decade
        if 'approval_by_decade' in ad:
            report.append("### Approvals by Decade\n")
            report.append("| Decade | Count |")
            report.append("|--------|-------|")
            for decade, count in sorted(ad['approval_by_decade'].items()):
                report.append(f"| {int(decade)}s | {count:,} |")
            report.append("\n")

        # Molecular Weight Stats
        if 'molecular_weight' in ad:
            mw = ad['molecular_weight']
            report.append("### Molecular Weight Statistics\n")
            report.append(f"- **Min:** {mw['min']} Da")
            report.append(f"- **Max:** {mw['max']} Da")
            report.append(f"- **Mean:** {mw['mean']} Da")
            report.append(f"- **Median:** {mw['median']} Da")
            report.append("\n")

        # Data Completeness
        report.append("### Column Completeness\n")
        report.append("| Column | Completeness |")
        report.append("|--------|--------------|")
        if 'completeness' in ad:
            for col, pct in sorted(ad['completeness'].items(), key=lambda x: -x[1]):
                status = "✅" if pct >= 80 else "⚠️" if pct >= 50 else "❌"
                report.append(f"| {col} | {status} {pct}% |")
        report.append("\n")

    # Secondary Datasets Summary
    report.append("## 📋 Secondary Datasets (Test Data)\n")
    report.append("*Note: These datasets contain test data only (10-25 records each, except metabolism).*\n")
    report.append("*Full production runs needed for: natural products, mechanisms, indications, targets, bioactivities, warnings, toxicity.*\n\n")

    secondary_datasets = ['mechanisms', 'indications', 'targets', 'warnings', 'bioactivities']
    for key in secondary_datasets:
        if key in all_stats:
            s = all_stats[key]
            report.append(f"### {key.replace('_', ' ').title()}\n")
            report.append(f"- Records: {s.get('total_records', 0):,}")
            if 'unique_drugs' in s:
                report.append(f"- Unique Drugs: {s.get('unique_drugs', 0)}")
            if 'unique_targets' in s:
                report.append(f"- Unique Targets: {s.get('unique_targets', 0)}")

            # Show key distributions
            for dist_key in ['action_types', 'target_types', 'warning_classes', 'activity_types']:
                if dist_key in s:
                    report.append(f"- {dist_key.replace('_', ' ').title()}: {dict(list(s[dist_key].items())[:5])}")
            report.append("\n")

    # Metabolism Special Section
    if 'metabolism' in all_stats:
        m = all_stats['metabolism']
        report.append("### Drug Metabolism (Rich Dataset)\n")
        report.append(f"- **Records:** {m.get('total_records', 0):,}")
        report.append(f"- **File Size:** {m.get('file_size_mb', 0):.2f} MB")
        report.append(f"- **Unique Drugs:** {m.get('unique_drugs', 0)}")
        report.append(f"- **Unique Metabolites:** {m.get('unique_metabolites', 0)}")
        report.append(f"- **Unique Enzymes:** {m.get('unique_enzymes', 0)}")
        if 'top_enzymes' in m:
            report.append(f"- **Top Enzymes:** {list(m['top_enzymes'].keys())[:5]}")
        report.append("\n")

    # Neo4j Readiness Assessment
    report.append("## 🔗 Neo4j Import Readiness\n")
    report.append("### Required Node Types\n")
    report.append("| Node Type | Source Dataset | Status |")
    report.append("|-----------|---------------|--------|")
    report.append("| Drug | approved_drugs | ✅ Ready (Production) |")
    report.append("| NaturalProduct | natural_products | ⚠️ Needs Full Run |")
    report.append("| Target | targets | ⚠️ Needs Full Run |")
    report.append("| Mechanism | mechanisms | ⚠️ Needs Full Run |")
    report.append("| Indication | indications | ⚠️ Needs Full Run |")
    report.append("| Warning | warnings | ⚠️ Needs Full Run |")
    report.append("\n")

    report.append("### Key Relationships to Create\n")
    report.append("- `Drug -[HAS_MECHANISM]-> Mechanism`")
    report.append("- `Mechanism -[TARGETS]-> Target`")
    report.append("- `Drug -[TREATS]-> Indication`")
    report.append("- `Drug -[HAS_WARNING]-> Warning`")
    report.append("- `Drug -[METABOLIZED_BY]-> Enzyme`")
    report.append("\n")

    # Recommendations
    report.append("## 📌 Recommendations\n")
    report.append("1. **Run full collection** for secondary datasets (natural products, mechanisms, etc.)")
    report.append("2. **Validate CSV compatibility** with Neo4j LOAD CSV")
    report.append("3. **Create IMPPAT-ChemBL mapping** after natural products full run")
    report.append("4. **Update Cypher scripts** for new node types and relationships")
    report.append("\n")

    return "\n".join(report)


def main():
    """Main function to generate all statistics."""
    data_dir = Path("data/processed")

    # Files to analyze
    files = {
        'approved_drugs': data_dir / 'chembl_approved_drugs.csv',
        'natural_products': data_dir / 'chembl_natural_products.csv',
        'mechanisms': data_dir / 'chembl_drug_mechanisms.csv',
        'indications': data_dir / 'chembl_drug_indications.csv',
        'targets': data_dir / 'chembl_drug_targets.csv',
        'warnings': data_dir / 'chembl_drug_warnings.csv',
        'bioactivities': data_dir / 'chembl_bioactivities.csv',
        'metabolism': data_dir / 'chembl_drug_metabolism.csv',
        'toxicity': data_dir / 'chembl_toxicity.csv',
    }

    # Analysis functions
    analyzers = {
        'approved_drugs': analyze_approved_drugs,
        'natural_products': analyze_natural_products,
        'mechanisms': analyze_mechanisms,
        'indications': analyze_indications,
        'targets': analyze_targets,
        'warnings': analyze_warnings,
        'bioactivities': analyze_bioactivities,
        'metabolism': analyze_metabolism,
        'toxicity': analyze_toxicity,
    }

    print("=" * 60)
    print("ChemBL Data Statistics Generator")
    print("=" * 60)

    all_stats = {}

    for key, filepath in files.items():
        if filepath.exists():
            all_stats[key] = analyzers[key](str(filepath))
        else:
            print(f"\n⚠️  File not found: {filepath}")

    # Generate markdown report
    report = generate_summary_report(all_stats)

    # Save report to docs/databases/chembl/ (not data/docs/)
    project_root = Path(__file__).parent.parent.parent
    report_path = project_root / 'docs' / 'databases' / 'chembl' / 'chembl-data-statistics.md'
    report_path.parent.mkdir(parents=True, exist_ok=True)

    with open(report_path, 'w') as f:
        f.write(report)

    print("\n" + "=" * 60)
    print(f"✅ Report saved to: {report_path}")
    print("=" * 60)

    # Also print summary to console
    print("\n📊 QUICK SUMMARY:")
    print("-" * 40)
    for key, stats in all_stats.items():
        records = stats.get('total_records', 0)
        size = stats.get('file_size_mb', stats.get('file_size_kb', 0) / 1024)
        print(f"  {key:20s}: {records:>8,} records ({size:.2f} MB)")

    total = sum(s.get('total_records', 0) for s in all_stats.values())
    print("-" * 40)
    print(f"  {'TOTAL':20s}: {total:>8,} records")

    return all_stats


if __name__ == "__main__":
    main()
