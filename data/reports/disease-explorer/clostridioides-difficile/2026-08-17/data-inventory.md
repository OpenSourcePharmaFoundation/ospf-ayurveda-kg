# Data Inventory — Clostridioides difficile

## Project Data Availability

### ChemBL (data-backed)
- **chembl_approved_drugs.csv**: Contains metronidazole (CHEMBL137), vancomycin (CHEMBL262777), fidaxomicin (CHEMBL1255800), rifaximin (CHEMBL1617), vancomycin HCl (CHEMBL1200628), metronidazole HCl (CHEMBL1200869)
- All have "clostridium difficile infection" or "Clostridium Infections" in their indications
- **chembl_drug_indications.csv**: Searchable for C. diff related terms
- **chembl_drug_targets.csv**: Available for mechanism lookups
- **chembl_drug_mechanisms.csv**: Available for mechanism of action data
- **chembl_drug_warnings.csv**: Available for safety signals

### DisGeNET (NOT available for C. diff)
- Files are OM-specific (disgenet__OM_biomarkers.csv, etc.)
- No C. difficile gene-disease associations in current dataset
- Agents should use training knowledge for gene-disease relationships

### PubChem (partially relevant)
- **pubchem_phytochem_target_interactions.csv**: May contain target interaction data for berberine, conessine, etc.
- Worth searching for specific compound-target pairs

### IMPPAT (limited relevance)
- **imppat_plant_therapeutic_uses.json**: Indian medicinal plant data
- No berberine found — Coptis/Berberis may not be in IMPPAT
- Kutaja (Holarrhena antidysenterica) may be present — search for it
- **imppat_plant_part_phytochemicals.json**: Phytochemical data

### MedPlant (potentially relevant)
- **medicinal_plants_with_uses.csv**: May contain Holarrhena, Berberis entries

### TTD
- **ttd_drug_target_genes.csv**: Small file, may have relevant targets

### DrugBank
- **drugbank_drug_targets.csv**: May have vancomycin/metronidazole target data

## Summary
- **Data-backed**: ChemBL drug data for fidaxomicin, vancomycin, metronidazole, rifaximin
- **Partially data-backed**: PubChem target interactions, IMPPAT plant data
- **Knowledge-based**: All C. diff pathobiology, gene-disease associations, most repurposing candidates (ebselen, UDCA, niclosamide, aprepitant, ibezapolstat)
- **Overall**: Mixed data availability — ~30% data-backed, ~70% knowledge-based
