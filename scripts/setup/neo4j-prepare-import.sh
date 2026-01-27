#!/bin/bash
# =============================================================================
# Neo4j Import Preparation Script
# =============================================================================
# This script copies all ChemBL CSV files to the Neo4j import directory.
#
# Usage:
#   ./scripts/setup/neo4j-prepare-import.sh [NEO4J_IMPORT_PATH]
#
# If no path is provided, the script will attempt to find the Neo4j import
# directory automatically, or prompt you for the path.
# =============================================================================

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Get the project root directory (where this script lives)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Data directory
DATA_DIR="$PROJECT_ROOT/data/processed"

echo -e "${BLUE}============================================${NC}"
echo -e "${BLUE}  Neo4j Import Preparation Script${NC}"
echo -e "${BLUE}============================================${NC}"
echo ""

# Check if data directory exists
if [ ! -d "$DATA_DIR" ]; then
    echo -e "${RED}Error: Data directory not found: $DATA_DIR${NC}"
    exit 1
fi

# Function to find Neo4j import directory
find_neo4j_import() {
    # Common locations for Neo4j Desktop import directories
    local possible_paths=(
        "$HOME/.neo4jDesktop/relate-data/dbmss"
        "$HOME/Library/Application Support/com.Neo4j.Relate/Data/dbmss"
    )

    for base_path in "${possible_paths[@]}"; do
        if [ -d "$base_path" ]; then
            # Find the most recently modified DBMS directory
            local latest_dbms=$(ls -td "$base_path"/dbms-* 2>/dev/null | head -1)
            if [ -n "$latest_dbms" ] && [ -d "$latest_dbms/import" ]; then
                echo "$latest_dbms/import"
                return 0
            fi
        fi
    done

    return 1
}

# Determine Neo4j import path
if [ -n "$1" ]; then
    NEO4J_IMPORT="$1"
elif NEO4J_IMPORT=$(find_neo4j_import); then
    echo -e "${YELLOW}Auto-detected Neo4j import directory:${NC}"
    echo "  $NEO4J_IMPORT"
    echo ""
    read -p "Is this correct? [Y/n] " confirm
    if [[ "$confirm" =~ ^[Nn] ]]; then
        echo ""
        echo "Please provide the Neo4j import directory path:"
        echo "(Find it in Neo4j Desktop: ... → Open folder → Import)"
        read -p "Path: " NEO4J_IMPORT
    fi
else
    echo -e "${YELLOW}Could not auto-detect Neo4j import directory.${NC}"
    echo ""
    echo "To find it:"
    echo "  1. Open Neo4j Desktop"
    echo "  2. Click '...' next to your DBMS"
    echo "  3. Select 'Open folder' → 'Import'"
    echo "  4. Copy the path from Finder"
    echo ""
    read -p "Enter the Neo4j import directory path: " NEO4J_IMPORT
fi

# Validate the import directory
if [ ! -d "$NEO4J_IMPORT" ]; then
    echo -e "${RED}Error: Import directory does not exist: $NEO4J_IMPORT${NC}"
    echo "Please create the directory or provide a valid path."
    exit 1
fi

echo ""
echo -e "${BLUE}Source directory:${NC} $DATA_DIR"
echo -e "${BLUE}Target directory:${NC} $NEO4J_IMPORT"
echo ""

# List of ChemBL files to copy (excluding sample files)
CHEMBL_FILES=(
    "chembl_approved_drugs.csv"
    "chembl_drug_mechanisms.csv"
    "chembl_drug_targets.csv"
    "chembl_drug_indications.csv"
    "chembl_drug_warnings.csv"
    "chembl_bioactivities.csv"
    "chembl_natural_products.csv"
    "chembl_drug_metabolism.csv"
    "chembl_toxicity.csv"
)

echo -e "${BLUE}Copying ChemBL data files...${NC}"
echo ""

copied=0
skipped=0

for file in "${CHEMBL_FILES[@]}"; do
    source_file="$DATA_DIR/$file"
    target_file="$NEO4J_IMPORT/$file"

    if [ -f "$source_file" ]; then
        # Get file size
        size=$(du -h "$source_file" | cut -f1)

        cp "$source_file" "$target_file"
        echo -e "  ${GREEN}✓${NC} $file ($size)"
        ((copied++))
    else
        echo -e "  ${YELLOW}⚠${NC} $file (not found - skipping)"
        ((skipped++))
    fi
done

echo ""
echo -e "${BLUE}============================================${NC}"
echo -e "${GREEN}Copied: $copied files${NC}"
if [ $skipped -gt 0 ]; then
    echo -e "${YELLOW}Skipped: $skipped files (not found)${NC}"
fi
echo -e "${BLUE}============================================${NC}"
echo ""

# List files in import directory
echo -e "${BLUE}Files in Neo4j import directory:${NC}"
ls -lh "$NEO4J_IMPORT"/*.csv 2>/dev/null || echo "  (no CSV files found)"

echo ""
echo -e "${GREEN}Done!${NC} You can now run the Cypher import scripts in Neo4j Browser."
echo ""
echo "Next steps:"
echo "  1. Start your Neo4j DBMS in Neo4j Desktop"
echo "  2. Open Neo4j Browser"
echo "  3. Run scripts in order: 4 → 5 → 6 → 7 → 8"
echo "  4. Validate with script 9"
echo ""
