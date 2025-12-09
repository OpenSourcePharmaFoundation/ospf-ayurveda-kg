# Quick Commands Reference - ChemBL Data Collection

## 📂 Data Location
```
/Users/andrew.faulkner/projects/ospf/ospf-ayurveda-kg/data/processed/
```

**All ChemBL data files:**
- `chembl_approved_drugs.csv`
- `chembl_natural_products.csv`
- `chembl_drug_mechanisms.csv`
- `chembl_drug_indications.csv`
- `chembl_drug_metabolism.csv`
- `chembl_drug_targets.csv`
- `chembl_bioactivities.csv`
- `chembl_drug_warnings.csv`
- `chembl_toxicity.csv`

---

## 🚀 OPTION 1: Collect Everything (One Command)

### Automated Script (8-12 hours):
```bash
cd /Users/andrew.faulkner/projects/ospf/ospf-ayurveda-kg
./collect_all_chembl_data.sh
```

**What it does:**
- Activates virtual environment automatically
- Collects all 9 datasets sequentially
- Shows progress for each phase
- Displays summary at completion

---

## 🚀 OPTION 2: Manual Collection (Step-by-Step)

### Activate Environment (REQUIRED FIRST):
```bash
cd /Users/andrew.faulkner/projects/ospf/ospf-ayurveda-kg
source venv/bin/activate
```

### Phase 1: Foundation Datasets (Run First)

#### 1. Approved Drugs (REQUIRED - 4-6 hours):
```bash
python src/scrapers/chembl/chembl_scraper.py --approved-drugs-only
```

#### 2. Natural Products (2-3 hours):
```bash
python src/scrapers/chembl/chembl_scraper.py --natural-products-only
```

### Phase 2: Secondary Datasets (Run After Phase 1)

**IMPORTANT:** Use `--use-cache` flag to reuse approved drugs list

#### 3. Drug Mechanisms (30 min):
```bash
python src/scrapers/chembl/chembl_scraper.py --mechanisms-only --use-cache
```

#### 4. Drug Indications (1 hour):
```bash
python src/scrapers/chembl/chembl_scraper.py --indications-only --use-cache
```

#### 5. Drug Targets (1 hour):
```bash
python src/scrapers/chembl/chembl_scraper.py --targets-only --use-cache
```

#### 6. Bioactivities (2-3 hours):
```bash
python src/scrapers/chembl/chembl_scraper.py --bioactivities-only --use-cache
```

#### 7. Drug Metabolism (2-3 hours):
```bash
python src/scrapers/chembl/chembl_scraper.py --metabolism-only --use-cache
```

#### 8. Drug Warnings (30 min):
```bash
python src/scrapers/chembl/chembl_scraper.py --warnings-only --use-cache
```

#### 9. Toxicity Data (30 min):
```bash
python src/scrapers/chembl/chembl_scraper.py --toxicity-only --use-cache
```

---

## 🔧 OPTION 3: Collect Smaller Batches (Testing/Development)

### Limit to specific number of records:
```bash
# Activate environment first
source venv/bin/activate

# Collect 200 approved drugs
python src/scrapers/chembl/chembl_scraper.py --approved-drugs-only --limit 200

# Collect 500 natural products
python src/scrapers/chembl/chembl_scraper.py --natural-products-only --limit 500

# Collect with time limit (e.g., 60 minutes)
python src/scrapers/chembl/chembl_scraper.py --approved-drugs-only --time-limit 60
```

---

## 📊 Monitor Progress

### Watch file sizes grow:
```bash
# In another terminal
while true; do clear; ls -lh data/processed/chembl_*.csv; sleep 30; done
```

### Count records collected:
```bash
wc -l data/processed/chembl_*.csv
```

### Check latest record:
```bash
tail -1 data/processed/chembl_approved_drugs.csv | cut -d',' -f1-3
```

---

## 🛑 Stop/Resume Collection

### To stop a running collection:
- Press `Ctrl+C` in the terminal

### To resume:
- Just run the same command again
- The scraper creates new files (doesn't append)
- Consider using `--time-limit` for controlled runs

---

## 📋 Validate Collected Data

### View statistics:
```bash
source venv/bin/activate
./scripts/chembl_display.py --stats
```

### Export for review:
```bash
./scripts/chembl_display.py --export review.csv
```

### View sample records:
```bash
./scripts/chembl_display.py --vertical --max 5
```

---

## 💡 Tips

1. **Overnight Runs:** Use `--time-limit` to control collection duration
   ```bash
   # 8-hour overnight run
   python src/scrapers/chembl/chembl_scraper.py --time-limit 480
   ```

2. **Parallel Collection:** Run Phase 1 collections in separate terminals:
   - Terminal 1: `--approved-drugs-only`
   - Terminal 2: `--natural-products-only`

3. **Background Execution:**
   ```bash
   nohup ./collect_all_chembl_data.sh > collection.log 2>&1 &
   tail -f collection.log  # Monitor progress
   ```

4. **Storage Check:**
   ```bash
   df -h .  # Check available disk space
   du -sh data/processed/  # Check data directory size
   ```

---

## 📞 Support

- **Documentation:** See `docs/databases/chembl/chembl-scraping-plan.md`
- **Full Commands:** See `RUN_FULL_COLLECTION.md`
- **Scraper Code:** `src/scrapers/chembl/chembl_scraper.py`
