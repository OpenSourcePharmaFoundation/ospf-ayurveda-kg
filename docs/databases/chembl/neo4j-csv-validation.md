# Neo4j CSV Compatibility Report

**Generated:** 2025-12-08T20:35:06.463641
**Data Directory:** `data/processed`

---

## 📊 Summary

| Status | Count |
|--------|-------|
| ✅ Passed | 6 |
| ⚠️ Warnings | 3 |
| ❌ Failed | 0 |
| **Total** | **9** |


### ⚠️ Overall: READY WITH CAUTIONS

Files can be imported but review warnings below.

## 📁 File Details

### ⚠️ WARNINGS `chembl_approved_drugs.csv`

- **Size:** 3,641,364 bytes
- **Rows:** 4,376
- **Columns:** 35
- **Encoding:** UTF-8 ✓
- **BOM:** None ✓

**⚠️ Warnings:**
- [WARNING] Mixed line endings detected - may cause inconsistent behavior
- [INFO] Column "inchi" appears to contain list data - may need split() in Cypher
- [INFO] Column "therapeutic_areas" appears to contain list data - may need split() in Cypher

**List columns (need split()):** inchi, therapeutic_areas


### ✅ PASSED `chembl_bioactivities.csv`

- **Size:** 4,971 bytes
- **Rows:** 24
- **Columns:** 16
- **Encoding:** UTF-8 ✓
- **BOM:** None ✓


### ⚠️ WARNINGS `chembl_drug_indications.csv`

- **Size:** 17,793 bytes
- **Rows:** 80
- **Columns:** 8
- **Encoding:** UTF-8 ✓
- **BOM:** None ✓

**⚠️ Warnings:**
- [INFO] Column "indication_refs" appears to contain list data - may need split() in Cypher

**List columns (need split()):** indication_refs


### ✅ PASSED `chembl_drug_mechanisms.csv`

- **Size:** 1,940 bytes
- **Rows:** 11
- **Columns:** 14
- **Encoding:** UTF-8 ✓
- **BOM:** None ✓


### ✅ PASSED `chembl_drug_metabolism.csv`

- **Size:** 3,076,831 bytes
- **Rows:** 10,001
- **Columns:** 14
- **Encoding:** UTF-8 ✓
- **BOM:** None ✓


### ✅ PASSED `chembl_drug_targets.csv`

- **Size:** 3,736 bytes
- **Rows:** 44
- **Columns:** 11
- **Encoding:** UTF-8 ✓
- **BOM:** None ✓


### ✅ PASSED `chembl_drug_warnings.csv`

- **Size:** 2,628 bytes
- **Rows:** 10
- **Columns:** 9
- **Encoding:** UTF-8 ✓
- **BOM:** None ✓


### ⚠️ WARNINGS `chembl_natural_products.csv`

- **Size:** 13,032 bytes
- **Rows:** 26
- **Columns:** 34
- **Encoding:** UTF-8 ✓
- **BOM:** None ✓

**⚠️ Warnings:**
- [INFO] Column "inchi" appears to contain list data - may need split() in Cypher
- [INFO] Column "therapeutic_areas" appears to contain list data - may need split() in Cypher

**List columns (need split()):** inchi, therapeutic_areas


### ✅ PASSED `chembl_toxicity.csv`

- **Size:** 399 bytes
- **Rows:** 2
- **Columns:** 16
- **Encoding:** UTF-8 ✓
- **BOM:** None ✓


## 💡 Neo4j Import Tips

### Basic LOAD CSV Pattern
```cypher
LOAD CSV WITH HEADERS FROM 'file:///chembl_approved_drugs.csv' AS row
CREATE (d:Drug {
  chembl_id: row.chembl_id,
  name: row.pref_name,
  molecular_weight: toFloat(row.molecular_weight)
})
```

### Handling List Fields
```cypher
// For comma-separated values in synonyms field:
WITH row, split(row.synonyms, ',') AS synonym_list
UNWIND synonym_list AS synonym
// ... create relationships
```

### Handling Null Values
```cypher
// Check for empty strings before conversion:
molecular_weight: CASE WHEN row.molecular_weight = '' THEN null
                       ELSE toFloat(row.molecular_weight) END
```
