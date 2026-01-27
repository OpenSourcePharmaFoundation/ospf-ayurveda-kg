# Neo4j Setup Guide for OSPF Ayurveda Knowledge Graph

This guide walks through setting up a Neo4j database instance for the ChemBL drug data integration.

## Prerequisites

- **Neo4j Desktop 2.1.0** - Already installed and running
- **Neo4j Database Version**: 5.x (this guide tested with 5.26.0 - latest in 5.x series)
- ChemBL data files in `data/processed/` directory

> **Note on Neo4j Version**: Neo4j Desktop 2.1.0 supports Neo4j 5.x databases. Version 5.1.0 was an early 5.x release; the current stable is 5.26.0. All Cypher scripts are compatible with any 5.x version.

---

## Quick Start (Automated)

For experienced users, run these commands from the project root:

```bash
# 1. Run the setup script to prepare files for import
./scripts/setup/neo4j-prepare-import.sh

# 2. Follow the Neo4j Desktop steps in Section 2 below

# 3. After starting Neo4j, run the master import script in Neo4j Browser
# (Copy contents of scripts/cypher_scripts/0_master_import.cypher)
```

---

## 1. Create New Database in Neo4j Desktop

### Step 1.1: Open Neo4j Desktop

Launch Neo4j Desktop from your Applications folder.

### Step 1.2: Create a New Project (Optional)

1. Click **"New"** → **"Create project"** in the left sidebar
2. Name it: `OSPF Ayurveda KG`
3. Click anywhere outside the name field to save

### Step 1.3: Create a New DBMS

1. Inside your project, click **"Add"** → **"Local DBMS"**
2. Configure the DBMS:
   - **Name**: `ospf-ayurveda-kg`
   - **Password**: `neo4jneo4j`
   - **Version**: Select **5.26.0** (or latest 5.x available)
3. Click **"Create"**

> **Important**: The password `neo4jneo4j` matches the credentials stored in `docs/neo4j-access.md`. You can use a different password, but update that file accordingly.

### Step 1.4: Install APOC Plugin

APOC (Awesome Procedures on Cypher) is required for advanced import operations.

1. Click on your new DBMS (`ospf-ayurveda-kg`)
2. Click the **"Plugins"** tab on the right panel
3. Find **"APOC"** in the list
4. Click **"Install"**
5. Wait for installation to complete

### Step 1.5: Configure APOC [DONE]

1. Click **"..."** (three dots) next to your DBMS
2. Select **"Open folder"** → **"Configuration"**
3. In the Finder window that opens, look for or create `apoc.conf`
4. Add this content to `apoc.conf`:

```properties
# APOC Configuration for OSPF Ayurveda KG
apoc.import.file.enabled=true
apoc.import.file.use_neo4j_config=true
apoc.export.file.enabled=true
```

> **Alternatively**, copy the pre-configured file:
> ```bash
> cp scripts/cypher_scripts/apoc.conf /path/to/neo4j-config-folder/
> ```

---

## 2. Credentials Storage

Credentials are stored in `docs/neo4j-access.md`:

```
username: neo4j
password: neo4jneo4j
```

These credentials are used for:
- Neo4j Browser login
- Any programmatic access (Python scripts, etc.)

---

## 3. Prepare Data Files for Import

[**CONTINUE FROM THIS POINT**]

Neo4j can only import CSV files from its designated `import` folder.

### Step 3.1: Locate the Import Directory

1. In Neo4j Desktop, click **"..."** next to your DBMS
2. Select **"Open folder"** → **"Import"**
3. Note this path (typically: `~/.neo4jDesktop/relate-data/dbmss/dbms-XXXXX/import/`)

### Step 3.2: Copy ChemBL CSV Files

Run the preparation script from the project root:

```bash
./scripts/setup/neo4j-prepare-import.sh
```

Or manually copy files:

```bash
# Get the import directory path from Neo4j Desktop, then:
NEO4J_IMPORT="/path/to/neo4j/import"

# Copy all ChemBL data files (excluding samples)
cp data/processed/chembl_approved_drugs.csv "$NEO4J_IMPORT/"
cp data/processed/chembl_drug_mechanisms.csv "$NEO4J_IMPORT/"
cp data/processed/chembl_drug_targets.csv "$NEO4J_IMPORT/"
cp data/processed/chembl_drug_indications.csv "$NEO4J_IMPORT/"
cp data/processed/chembl_drug_warnings.csv "$NEO4J_IMPORT/"
cp data/processed/chembl_bioactivities.csv "$NEO4J_IMPORT/"
cp data/processed/chembl_natural_products.csv "$NEO4J_IMPORT/"
cp data/processed/chembl_drug_metabolism.csv "$NEO4J_IMPORT/"
cp data/processed/chembl_toxicity.csv "$NEO4J_IMPORT/"
```

---

## 4. Start the Database

1. In Neo4j Desktop, click the **"Start"** button on your DBMS
2. Wait for the status to show **"Active"** (green indicator)
3. Click **"Open"** to launch Neo4j Browser

### Login Credentials

- **Username**: `neo4j`
- **Password**: `neo4jneo4j`

---

## 5. Import ChemBL Data

The Cypher import scripts must be run **in order**. Each script builds on the previous one.

### Import Execution Order

| Script | Purpose | Estimated Time |
|--------|---------|----------------|
| `4_chembl_constraints.txt` | Create indexes and constraints | < 1 second |
| `5_chembl_approved_drugs.txt` | Import ~4,376 approved drugs | 30-60 seconds |
| `6_chembl_mechanisms_targets.txt` | Import mechanisms and targets | 10-20 seconds |
| `7_chembl_indications.txt` | Import drug indications | 10-20 seconds |
| `8_chembl_warnings.txt` | Import safety warnings | 5-10 seconds |

### Step 5.1: Run Each Script

1. Open Neo4j Browser (click "Open" in Neo4j Desktop)
2. For each script in `scripts/cypher_scripts/`:
   - Open the `.txt` file
   - Copy the entire contents
   - Paste into Neo4j Browser's query editor
   - Click the **Play** button (▶) to execute

> **Warning**: Each step in a script must be run separately. The scripts contain comments separating logical steps. Run one `LOAD CSV` block at a time.

### Step 5.2: Verify Import

After running all import scripts, execute the validation queries in `9_chembl_test_import.txt`:

```cypher
// Count all ChemBL drugs
MATCH (d:Drug)
WHERE d.chembl_id IS NOT NULL
RETURN 'ChemBL Drugs' AS type, count(d) AS count;
```

Expected results (with current test data):
```
┌─────────────────┬───────┐
│ type            │ count │
├─────────────────┼───────┤
│ "ChemBL Drugs"  │ 4376  │
└─────────────────┴───────┘
```

---

## 6. Directory Structure After Setup

```
scripts/
├── setup/
│   └── neo4j-prepare-import.sh    # Helper script for file copying
├── cypher_scripts/
│   ├── apoc.conf                  # APOC configuration
│   ├── 4_chembl_constraints.txt   # Index/constraint creation
│   ├── 5_chembl_approved_drugs.txt
│   ├── 6_chembl_mechanisms_targets.txt
│   ├── 7_chembl_indications.txt
│   ├── 8_chembl_warnings.txt
│   └── 9_chembl_test_import.txt   # Validation queries
└── ...

docs/
├── neo4j-access.md                # Stored credentials
└── setup/
    └── neo4j-setup.md             # This document
```

---

## 7. Troubleshooting

### "File not found" errors during LOAD CSV

- Ensure files are in the Neo4j import directory
- Verify file names match exactly (case-sensitive)
- Check that `apoc.import.file.enabled=true` is set

### "Constraint already exists" errors

- This is normal if re-running constraint scripts
- The `IF NOT EXISTS` clause handles this gracefully

### Slow import performance

- For large datasets, consider increasing Neo4j heap memory:
  1. Click "..." → "Settings"
  2. Adjust `server.memory.heap.initial_size` and `server.memory.heap.max_size`

### Cannot connect to database

- Verify the database is running (green "Active" status)
- Check that port 7687 (Bolt) is not blocked
- Try restarting the DBMS

---

## 8. Next Steps

After successful import:

1. **Explore the data** using queries in `9_chembl_test_import.txt`
2. **Run analysis queries** from `analysis_queries.txt` (if exists)
3. **Integrate with other data sources** (DisGeNET, IMPPAT, etc.)

---

## Quick Reference

| Item | Value |
|------|-------|
| Neo4j Desktop Version | 2.1.0 |
| Neo4j Database Version | 5.26.0 (or latest 5.x) |
| Username | `neo4j` |
| Password | `neo4jneo4j` |
| Bolt Port | 7687 |
| HTTP Port | 7474 |
| Default Database | `neo4j` |
