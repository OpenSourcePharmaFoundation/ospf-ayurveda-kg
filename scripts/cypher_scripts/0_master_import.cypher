// ============================================================================
// OSPF Ayurveda Knowledge Graph - ChemBL Master Import Script
// ============================================================================
//
// This master script contains ALL ChemBL import operations in execution order.
//
// IMPORTANT: Neo4j Browser cannot run the entire file at once. You must run
// each numbered section separately (copy and paste each section individually).
//
// Execution Order:
//   Section 1: Constraints and Indexes
//   Section 2: Approved Drugs
//   Section 3: Therapeutic Areas
//   Section 4: Drug Mechanisms
//   Section 5: Mechanism-Target Links
//   Section 6: Target Details
//   Section 7: Drug Indications
//   Section 8: Drug Warnings
//   Section 9: Cross-Database Links (Proteins, Genes, Diseases)
//
// Prerequisites:
//   - ChemBL CSV files copied to Neo4j import directory
//   - APOC plugin installed and configured
//
// ============================================================================

// ============================================================================
// SECTION 1: CONSTRAINTS AND INDEXES
// ============================================================================
// Run this first to ensure data integrity during import.
// Execute each statement separately.

// 1.1 Drug ChemBL ID index (not unique - allows nulls for non-ChemBL drugs)
CREATE INDEX drug_chembl_id_index IF NOT EXISTS
FOR (d:Drug) ON (d.chembl_id);

// 1.2 ChemBL Target unique constraint
CREATE CONSTRAINT chembl_target_unique IF NOT EXISTS
FOR (t:Target) REQUIRE t.chembl_id IS UNIQUE;

// 1.3 Mechanism unique constraint
CREATE CONSTRAINT mechanism_unique IF NOT EXISTS
FOR (m:Mechanism) REQUIRE m.id IS UNIQUE;

// 1.4 Warning unique constraint
CREATE CONSTRAINT warning_unique IF NOT EXISTS
FOR (w:Warning) REQUIRE w.id IS UNIQUE;

// 1.5 Indication indexes (MeSH and EFO)
CREATE INDEX indication_mesh_index IF NOT EXISTS
FOR (i:Indication) ON (i.mesh_id);

CREATE INDEX indication_efo_index IF NOT EXISTS
FOR (i:Indication) ON (i.efo_id);

// 1.6 InChI Key indexes (for cross-database matching)
CREATE INDEX compound_inchi_key_index IF NOT EXISTS
FOR (c:Compound) ON (c.inchi_key);

CREATE INDEX drug_inchi_key_index IF NOT EXISTS
FOR (d:Drug) ON (d.inchi_key);


// ============================================================================
// SECTION 2: IMPORT APPROVED DRUGS
// ============================================================================
// Creates Drug nodes with comprehensive molecular data from ChemBL.
// Expected: ~4,376 approved drugs

LOAD CSV WITH HEADERS FROM 'file:///chembl_approved_drugs.csv' AS row

MERGE (d:Drug {chembl_id: row.chembl_id})

// Basic identification
SET d.chembl_id = row.chembl_id,
    d.name = COALESCE(d.name, row.pref_name),
    d.chembl_name = row.pref_name,
    d.synonyms = CASE WHEN row.synonyms IS NOT NULL AND row.synonyms <> ''
                      THEN split(replace(row.synonyms, '"', ''), '; ')
                      ELSE d.synonyms END

// Molecular structure identifiers
SET d.smiles = CASE WHEN row.smiles <> '' THEN row.smiles ELSE d.smiles END,
    d.inchi = CASE WHEN row.inchi <> '' THEN row.inchi ELSE d.inchi END,
    d.inchi_key = CASE WHEN row.inchi_key <> '' THEN row.inchi_key ELSE d.inchi_key END,
    d.molecular_formula = CASE WHEN row.molecular_formula <> '' THEN row.molecular_formula ELSE d.molecular_formula END

// Molecular properties
SET d.molecular_weight = CASE WHEN row.molecular_weight <> ''
                              THEN toFloat(row.molecular_weight)
                              ELSE d.molecular_weight END,
    d.alogp = CASE WHEN row.alogp <> '' THEN toFloat(row.alogp) ELSE d.alogp END,
    d.hba = CASE WHEN row.hba <> '' THEN toInteger(row.hba) ELSE d.hba END,
    d.hbd = CASE WHEN row.hbd <> '' THEN toInteger(row.hbd) ELSE d.hbd END,
    d.psa = CASE WHEN row.psa <> '' THEN toFloat(row.psa) ELSE d.psa END,
    d.rtb = CASE WHEN row.rtb <> '' THEN toInteger(row.rtb) ELSE d.rtb END,
    d.ro5_violations = CASE WHEN row.ro5_violations <> '' THEN toInteger(row.ro5_violations) ELSE d.ro5_violations END,
    d.aromatic_rings = CASE WHEN row.aromatic_rings <> '' THEN toInteger(row.aromatic_rings) ELSE d.aromatic_rings END,
    d.heavy_atoms = CASE WHEN row.heavy_atoms <> '' THEN toInteger(row.heavy_atoms) ELSE d.heavy_atoms END,
    d.qed_weighted = CASE WHEN row.qed_weighted <> '' THEN toFloat(row.qed_weighted) ELSE d.qed_weighted END

// Approval and status
SET d.first_approval = CASE WHEN row.first_approval <> ''
                            THEN toInteger(row.first_approval)
                            ELSE d.first_approval END,
    d.max_phase = CASE WHEN row.max_phase <> '' THEN toInteger(row.max_phase) ELSE d.max_phase END,
    d.molecule_type = row.molecule_type,
    d.natural_product = CASE WHEN row.natural_product = '1' OR row.natural_product = 'True'
                             THEN true ELSE false END,
    d.oral_bioavailability = row.oral_bioavailability,
    d.withdrawn_flag = CASE WHEN row.withdrawn_flag = '1' OR row.withdrawn_flag = 'True'
                            THEN true ELSE false END

// Classification
SET d.indication_class = CASE WHEN row.indication_class <> '' AND row.indication_class <> '""'
                              THEN row.indication_class
                              ELSE d.indication_class END

// Source tracking
SET d.sources = CASE WHEN d.sources IS NULL
                     THEN ['ChemBL']
                     ELSE CASE WHEN NOT 'ChemBL' IN d.sources
                               THEN d.sources + 'ChemBL'
                               ELSE d.sources END END;


// ============================================================================
// SECTION 3: THERAPEUTIC AREAS
// ============================================================================
// Links drugs to their therapeutic area classifications.

LOAD CSV WITH HEADERS FROM 'file:///chembl_approved_drugs.csv' AS row
WITH row WHERE row.therapeutic_areas IS NOT NULL
           AND row.therapeutic_areas <> ''
           AND row.therapeutic_areas <> '""'

MATCH (d:Drug {chembl_id: row.chembl_id})

WITH d, row, split(replace(replace(row.therapeutic_areas, '"', ''), '; ', ';'), ';') AS areas
UNWIND areas AS area
WITH d, trim(area) AS clean_area
WHERE clean_area <> ''

MERGE (ta:Therapeutic_Area {name: clean_area})
MERGE (d)-[:INDICATED_FOR]->(ta);


// ============================================================================
// SECTION 4: DRUG MECHANISMS
// ============================================================================
// Creates Mechanism nodes showing how drugs work (INHIBITOR, AGONIST, etc.)

LOAD CSV WITH HEADERS FROM 'file:///chembl_drug_mechanisms.csv' AS row

MATCH (d:Drug {chembl_id: row.chembl_id})

WITH d, row,
     row.chembl_id + '_' + COALESCE(row.target_chembl_id, 'unknown') + '_' + COALESCE(row.action_type, 'unknown') AS mech_id

MERGE (m:Mechanism {id: mech_id})
SET m.action_type = row.action_type,
    m.mechanism_of_action = row.mechanism_of_action,
    m.target_chembl_id = row.target_chembl_id,
    m.target_name = row.target_name,
    m.target_type = row.target_type,
    m.binding_site = CASE WHEN row.binding_site <> '' THEN row.binding_site ELSE null END,
    m.direct_interaction = CASE WHEN row.direct_interaction = 'True' OR row.direct_interaction = '1'
                                THEN true ELSE false END,
    m.molecular_mechanism = row.molecular_mechanism,
    m.disease_efficacy = CASE WHEN row.disease_efficacy = 'True' OR row.disease_efficacy = '1'
                              THEN true ELSE false END,
    m.mechanism_comment = CASE WHEN row.mechanism_comment <> '' THEN row.mechanism_comment ELSE null END,
    m.selectivity_comment = CASE WHEN row.selectivity_comment <> '' THEN row.selectivity_comment ELSE null END,
    m.source = 'ChemBL'

MERGE (d)-[:HAS_MECHANISM]->(m);


// ============================================================================
// SECTION 5: MECHANISM-TARGET LINKS
// ============================================================================
// Creates Target nodes and links them to Mechanisms.

LOAD CSV WITH HEADERS FROM 'file:///chembl_drug_mechanisms.csv' AS row
WITH row WHERE row.target_chembl_id IS NOT NULL AND row.target_chembl_id <> ''

WITH row,
     row.chembl_id + '_' + row.target_chembl_id + '_' + COALESCE(row.action_type, 'unknown') AS mech_id

MATCH (m:Mechanism {id: mech_id})

MERGE (t:Target {chembl_id: row.target_chembl_id})
SET t.name = row.target_name,
    t.target_type = row.target_type,
    t.source = 'ChemBL'

MERGE (m)-[:ACTS_ON]->(t);


// ============================================================================
// SECTION 6: TARGET DETAILS
// ============================================================================
// Enriches Target nodes with detailed information (organism, UniProt, genes).

LOAD CSV WITH HEADERS FROM 'file:///chembl_drug_targets.csv' AS row

MERGE (t:Target {chembl_id: row.target_chembl_id})
SET t.name = COALESCE(t.name, row.pref_name),
    t.chembl_name = row.pref_name,
    t.target_type = row.target_type,
    t.organism = row.organism,
    t.tax_id = CASE WHEN row.tax_id <> '' THEN toInteger(row.tax_id) ELSE null END,
    t.gene_names = CASE WHEN row.gene_names <> '' THEN row.gene_names ELSE null END,
    t.uniprot_accessions = CASE WHEN row.uniprot_accessions <> '' THEN row.uniprot_accessions ELSE null END,
    t.target_family = CASE WHEN row.target_family <> '' THEN row.target_family ELSE null END,
    t.target_class = CASE WHEN row.target_class <> '' THEN row.target_class ELSE null END,
    t.protein_class = CASE WHEN row.protein_class <> '' THEN row.protein_class ELSE null END,
    t.source = 'ChemBL';


// ============================================================================
// SECTION 7: DRUG INDICATIONS
// ============================================================================
// Creates Indication nodes (diseases/conditions drugs treat).

LOAD CSV WITH HEADERS FROM 'file:///chembl_drug_indications.csv' AS row

MATCH (d:Drug {chembl_id: row.chembl_id})

WITH d, row,
     CASE
       WHEN row.mesh_id IS NOT NULL AND row.mesh_id <> ''
         THEN row.mesh_id
       WHEN row.efo_id IS NOT NULL AND row.efo_id <> ''
         THEN row.efo_id
       ELSE row.chembl_id + '_' + COALESCE(row.mesh_heading, row.efo_term)
     END AS indication_id

WHERE indication_id IS NOT NULL

MERGE (i:Indication {id: indication_id})
SET i.mesh_id = CASE WHEN row.mesh_id <> '' THEN row.mesh_id ELSE null END,
    i.mesh_heading = CASE WHEN row.mesh_heading <> '' THEN row.mesh_heading ELSE null END,
    i.efo_id = CASE WHEN row.efo_id <> '' THEN row.efo_id ELSE null END,
    i.efo_term = CASE WHEN row.efo_term <> '' THEN row.efo_term ELSE null END,
    i.name = COALESCE(row.mesh_heading, row.efo_term),
    i.source = 'ChemBL'

MERGE (d)-[r:TREATS_INDICATION]->(i)
SET r.max_phase = CASE WHEN row.max_phase_for_ind <> ''
                       THEN toInteger(row.max_phase_for_ind)
                       ELSE null END,
    r.source = 'ChemBL';


// ============================================================================
// SECTION 8: DRUG WARNINGS
// ============================================================================
// Creates Warning nodes for drug safety information.

LOAD CSV WITH HEADERS FROM 'file:///chembl_drug_warnings.csv' AS row

MATCH (d:Drug {chembl_id: row.chembl_id})

WITH d, row,
     row.chembl_id + '_' +
     COALESCE(row.warning_type, 'unknown') + '_' +
     COALESCE(row.warning_class, 'unknown') AS warning_id

MERGE (w:Warning {id: warning_id})
SET w.warning_type = row.warning_type,
    w.warning_class = row.warning_class,
    w.description = CASE WHEN row.warning_description <> '' THEN row.warning_description ELSE null END,
    w.warning_text = CASE WHEN row.warning_text <> '' THEN row.warning_text ELSE null END,
    w.country = CASE WHEN row.warning_country <> '' THEN row.warning_country ELSE null END,
    w.year = CASE WHEN row.warning_year <> '' THEN toInteger(row.warning_year) ELSE null END,
    w.source = 'ChemBL'

MERGE (d)-[:HAS_WARNING]->(w);

// Create toxicity category relationships
MATCH (w:Warning)
WHERE w.warning_class IS NOT NULL AND w.warning_class <> ''
MERGE (tc:ToxicityCategory {name: w.warning_class})
MERGE (w)-[:CATEGORY]->(tc);


// ============================================================================
// SECTION 9: CROSS-DATABASE LINKS
// ============================================================================
// Links ChemBL data to existing nodes (Proteins, Genes, Diseases).
// Run these AFTER all other imports and only if you have existing data.

// 9.1 Link Targets to Proteins (via UniProt ID)
MATCH (t:Target)
WHERE t.uniprot_accessions IS NOT NULL

MATCH (p:Protein)
WHERE p.uniprotId IS NOT NULL
  AND p.uniprotId IN split(t.uniprot_accessions, ', ')

MERGE (t)-[:SAME_AS]->(p);

// 9.2 Link Targets to Genes (via gene name)
MATCH (t:Target)
WHERE t.gene_names IS NOT NULL

WITH t, split(t.gene_names, ', ') AS genes
UNWIND genes AS gene_name

MATCH (g:Gene {name: gene_name})
MERGE (t)-[:ENCODED_BY]->(g);

// 9.3 Link Indications to Diseases (name matching)
MATCH (i:Indication)
WHERE i.name IS NOT NULL

MATCH (d:Disease)
WHERE toLower(d.name) = toLower(i.name)
   OR toLower(d.name) CONTAINS toLower(i.name)
   OR toLower(i.name) CONTAINS toLower(d.name)

MERGE (i)-[:SAME_AS]->(d);

// 9.4 Special: Link Oral Mucositis-related indications
MATCH (i:Indication)
WHERE toLower(i.name) CONTAINS 'mucositis'
   OR toLower(i.name) CONTAINS 'stomatitis'
   OR toLower(i.mesh_heading) CONTAINS 'mucositis'
   OR toLower(i.mesh_heading) CONTAINS 'stomatitis'

MATCH (d:Disease {name: 'Oral mucositis'})
MERGE (i)-[:RELATED_TO]->(d);


// ============================================================================
// VALIDATION QUERIES
// ============================================================================
// Run these after import to verify success.

// Count ChemBL drugs
MATCH (d:Drug)
WHERE d.chembl_id IS NOT NULL
RETURN 'ChemBL Drugs' AS type, count(d) AS count;

// Count by relationship type
MATCH (d:Drug)-[r]->(n)
WHERE d.chembl_id IS NOT NULL
RETURN type(r) AS relationship, count(r) AS count
ORDER BY count DESC;

// Sample drug with full details
MATCH (d:Drug {chembl_id: 'CHEMBL2'})
OPTIONAL MATCH (d)-[:HAS_MECHANISM]->(m:Mechanism)
OPTIONAL MATCH (d)-[:TREATS_INDICATION]->(i:Indication)
OPTIONAL MATCH (d)-[:HAS_WARNING]->(w:Warning)
OPTIONAL MATCH (d)-[:INDICATED_FOR]->(ta:Therapeutic_Area)
RETURN d.chembl_id AS id,
       d.name AS name,
       d.molecular_weight AS mw,
       collect(DISTINCT m.action_type) AS mechanisms,
       collect(DISTINCT i.name) AS indications,
       collect(DISTINCT w.warning_class) AS warnings,
       collect(DISTINCT ta.name) AS therapeutic_areas;
