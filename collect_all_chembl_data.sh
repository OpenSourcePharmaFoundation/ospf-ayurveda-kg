#!/bin/bash
# ChemBL Full Data Collection Script
# Run this to collect all ChemBL data without needing Claude Code
#
# Estimated total time: 8-12 hours
# Estimated total storage: ~190MB

set -e  # Exit on error

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "════════════════════════════════════════════════════════════════"
echo "🔬 ChemBL Full Data Collection"
echo "════════════════════════════════════════════════════════════════"
echo ""
echo "Project: $SCRIPT_DIR"
echo "Start time: $(date)"
echo ""

# Activate virtual environment
echo "📦 Activating virtual environment..."
source venv/bin/activate

echo ""
echo "════════════════════════════════════════════════════════════════"
echo "Phase 1: Foundation Datasets (6-9 hours)"
echo "════════════════════════════════════════════════════════════════"

# 1. Approved Drugs (Foundation - REQUIRED for all other collections)
echo ""
echo "📊 [1/9] Collecting Approved Drugs (~3,280 drugs, 4-6 hours)..."
python src/scrapers/chembl/chembl_scraper.py --approved-drugs-only
echo "✅ Approved drugs complete!"

# 2. Natural Products
echo ""
echo "🌿 [2/9] Collecting Natural Products (~5,000 compounds, 2-3 hours)..."
python src/scrapers/chembl/chembl_scraper.py --natural-products-only
echo "✅ Natural products complete!"

echo ""
echo "════════════════════════════════════════════════════════════════"
echo "Phase 2: Secondary Datasets (2-4 hours)"
echo "════════════════════════════════════════════════════════════════"
echo "NOTE: Using --use-cache to reuse approved drugs list"
echo ""

# 3. Drug Mechanisms
echo "⚙️  [3/9] Collecting Drug Mechanisms (~1,000 records, 30 min)..."
python src/scrapers/chembl/chembl_scraper.py --mechanisms-only --use-cache
echo "✅ Drug mechanisms complete!"

# 4. Drug Indications
echo ""
echo "🏥 [4/9] Collecting Drug Indications (~5,000 records, 1 hour)..."
python src/scrapers/chembl/chembl_scraper.py --indications-only --use-cache
echo "✅ Drug indications complete!"

# 5. Drug Targets
echo ""
echo "🎯 [5/9] Collecting Drug Targets (~1,000 targets, 1 hour)..."
python src/scrapers/chembl/chembl_scraper.py --targets-only --use-cache
echo "✅ Drug targets complete!"

# 6. Bioactivities
echo ""
echo "🧪 [6/9] Collecting Bioactivities (~50,000 records, 2-3 hours)..."
python src/scrapers/chembl/chembl_scraper.py --bioactivities-only --use-cache
echo "✅ Bioactivities complete!"

# 7. Drug Metabolism
echo ""
echo "💊 [7/9] Collecting Drug Metabolism (~500,000+ records, 2-3 hours)..."
python src/scrapers/chembl/chembl_scraper.py --metabolism-only --use-cache
echo "✅ Drug metabolism complete!"

# 8. Drug Warnings
echo ""
echo "⚠️  [8/9] Collecting Drug Warnings (~500 warnings, 30 min)..."
python src/scrapers/chembl/chembl_scraper.py --warnings-only --use-cache
echo "✅ Drug warnings complete!"

# 9. Toxicity Data
echo ""
echo "☠️  [9/9] Collecting Toxicity Data (~1,000 records, 30 min)..."
python src/scrapers/chembl/chembl_scraper.py --toxicity-only --use-cache
echo "✅ Toxicity data complete!"

echo ""
echo "════════════════════════════════════════════════════════════════"
echo "✅ ALL DATA COLLECTION COMPLETE!"
echo "════════════════════════════════════════════════════════════════"
echo ""
echo "End time: $(date)"
echo ""
echo "📂 Output files in: data/processed/"
ls -lh data/processed/chembl_*.csv
echo ""
echo "📊 Total storage used:"
du -sh data/processed/
echo ""
echo "════════════════════════════════════════════════════════════════"