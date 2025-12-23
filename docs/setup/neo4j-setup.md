# Neo4j Setup Guide for OSPF Ayurveda Knowledge Graph

This guide walks through setting up Neo4j Desktop for the Ayurveda Knowledge Graph project.

## Step 1: Download Neo4j Desktop

1. Go to: https://neo4j.com/download/
2. Click **"Download Neo4j Desktop"**
3. Fill in the form (or skip with a throwaway email)
4. Download the `.dmg` file for macOS
5. **Save the activation key** shown on the download page (you'll need it!)

## Step 2: Install Neo4j Desktop

```bash
# Open the downloaded DMG
open ~/Downloads/neo4j-desktop-*.dmg

# Drag Neo4j Desktop to Applications
# Then open it from Applications
```

When first launched:
1. Enter the **activation key** from the download page
2. Accept the license agreement
3. Wait for initial setup to complete

## Step 3: Create a New Project and Database

1. Click **"New"** → **"Create project"**
2. Name it: `OSPF Ayurveda KG`
3. Click **"Add"** → **"Local DBMS"**
4. Configure:
   - Name: `AyurvedaKG`
   - Password: Choose a password (remember it!)
   - Version: Latest (5.x recommended)
5. Click **"Create"**

## Step 4: Install APOC Plugin

APOC (Awesome Procedures on Cypher) is required for JSON imports.

1. Click on your new database (`AyurvedaKG`)
2. Click the **"Plugins"** tab on the right
3. Find **"APOC"** and click **"Install"**
4. Wait for installation to complete

## Step 5: Configure APOC for File Imports

1. Click the **three dots (...)** next to your database
2. Select **"Open folder"** → **"Configuration"**
3. This opens the database configuration folder in Finder
4. Copy the `apoc.conf` file from this project:

```bash
# Find your Neo4j config folder (shown when you clicked "Open folder")
# It will be something like:
# ~/Library/Application Support/Neo4j Desktop/Application/relate-data/dbmss/dbms-XXXXX/conf/

# Copy the apoc.conf file
cp /Users/andrew.faulkner/projects/ospf/ospf-ayurveda-kg/scripts/cypher_scripts/apoc.conf \
   "PASTE_YOUR_NEO4J_CONF_PATH_HERE/"
```

## Step 6: Copy CSV Files to Import Folder

1. Click the **three dots (...)** next to your database
2. Select **"Open folder"** → **"Import"**
3. Copy all CSV files to this folder:

```bash
# For test import (100 drugs):
cp /Users/andrew.faulkner/projects/ospf/ospf-ayurveda-kg/data/test_import/*.csv \
   "PASTE_YOUR_NEO4J_IMPORT_PATH_HERE/"

# OR for full import (3,274 drugs):
cp /Users/andrew.faulkner/projects/ospf/ospf-ayurveda-kg/data/processed/*.csv \
   "PASTE_YOUR_NEO4J_IMPORT_PATH_HERE/"
```

## Step 7: Start the Database

1. Click **"Start"** on your database
2. Wait for it to show "Running" (green indicator)
3. Click **"Open"** to launch Neo4j Browser

## Step 8: Run Import Scripts

In Neo4j Browser, run the Cypher scripts in order:

### 8.1 Create Constraints (run once)
Copy contents of `scripts/cypher_scripts/4_chembl_constraints.txt`

### 8.2 Import Approved Drugs
Copy contents of `scripts/cypher_scripts/5_chembl_approved_drugs.txt`

### 8.3 Import Mechanisms and Targets
Copy contents of `scripts/cypher_scripts/6_chembl_mechanisms_targets.txt`

### 8.4 Import Indications
Copy contents of `scripts/cypher_scripts/7_chembl_indications.txt`

### 8.5 Import Warnings
Copy contents of `scripts/cypher_scripts/8_chembl_warnings.txt`

### 8.6 Validate Import
Copy contents of `scripts/cypher_scripts/9_chembl_test_import.txt`

## Step 9: Verify Installation

Run this query to verify data was imported:

```cypher
MATCH (d:Drug) WHERE d.chembl_id IS NOT NULL
RETURN count(d) AS chembl_drugs;
```

Expected result:
- Test import: 100 drugs
- Full import: ~3,274 drugs

## Troubleshooting

### "File not found" errors
- Ensure CSV files are in the `import` folder
- Check file permissions: `chmod 644 *.csv`
- Verify APOC is installed and database was restarted after installing

### "apoc.load.json" not found
- APOC plugin not installed or enabled
- Copy `apoc.conf` to the `conf` folder
- Restart the database

### Slow imports
- For large files, increase memory:
  1. Stop database
  2. Click **...** → **Settings**
  3. Increase `dbms.memory.heap.max_size` to `2G` or more
  4. Restart database

## Quick Reference

| Action | Location |
|--------|----------|
| Open Neo4j Browser | Click "Open" on running database |
| Find import folder | **...** → Open folder → Import |
| Find config folder | **...** → Open folder → Configuration |
| View logs | **...** → Open folder → Logs |
| Change settings | **...** → Settings |
