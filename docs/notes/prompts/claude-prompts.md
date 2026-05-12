Write a plan for creating a "frontend demo."

The rough idea is to demo the results, from files such as:
  - data/analysis/oral_mucositis_drug_candidates-2026-05-03.md
  - data/analysis/oral_mucositis_drug_candidates-2026-01-29.md
  - data/analysis/oral_mucositis_multi_agent_drug_discovery-2026-05-04.md

Read all of these documents before you build anything. We'll also generate more in a similar vein.

We'd also like to generate data visualizations for the tables, numbers, etc in these documents. Choose a good data visualization library.
- Display these inline in the displayed data sections
  - Also show the raw data. Make this visible through an accordion (default to just showing the visualization if one is present).

Render the markdown in a way that's aesthetically pleasing. Have components for things like tables and lists. Make it:
- consistent
- follow modern design systems
- dynamic
- responsive

It's essentially a static site (but not quite), meant to display our prior results.

Have a content area. That content area should have what's displayed change based on the selected values in 2 dropdowns - that is, the dropdowns are used to display different results, and different parts of the results. More specifically:
1. One dropdown should relate to the specific output instance (i.e. a single analysis - these correspond to individual files)
  - One of those output instances should be the conglomerate one, which we'll create later using similar methods to the prior generated outputs.
  - That is, we're also going to have Claude generate a conglomerate results document built from the results of the prior analyses.
  - One of the options should be "all output" that shows the whole thing from a single "document".
  - One of the options should be the "summary" that gives a short version of the results, across all analyses. The second dropdown should be grayed out if summary is selected. Summary should basically list the recommended drugs and the reasons they were selected. We'll do another Claude analysis to generate these.
2. The second dropdown should relate to the section of each document (e.g. "Current State: Approved OM Treatments").

Have a second tab (besides the one showing analysis content) that displays each recommended drug, and lists the arguments for why that drug was chosen.

On visiting the site initially, it should display the summary - that is, that's the default option for the dropdowns. When "summary" is selected (as an option in the first dropdown), gray out the other dropdown.

Make it a SPA.

Write the document to a file.

We're going to place the frontend in a new folder, such as ./frontend-demo

Stack:
- React
- Shadcn for the component system
- Typescript
- npm (latest version) as the package manager
- eslint
- Test with Jest and React Testing Library
- Prettier for formatting
- Vite for the build system
- Host on Vercel - build it accordingly

Figure out how to deploy it.

-----

STRETCH GOALS:

Display the knowledge graph if you can. Look into Neo4j's built-in capabilities for doing this. This can be a different tab in the page from the "content display area" that shows the outputs of the analyses.
- We should be able to interact with it to a degree, if possible.

-----

We're going to switch gears a bit.

We'd like to add a local LLM to this project. We'd like to train it on the medical data we've pulled. We want to be able to ask it for potential treatments for various chemotherapy side effects, having it draw on the data it's pulled.

Give an outline of how we'd build this. Create a document. Use the Neo4j data including all the links - this is key.

----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
Question
========

❯ We want to find new treatments for various side effects of chemotherapy, such as oral muscositis.

  Can you come up with 3 different questions that are related to the drug formulation of the chemicals in the knowledge graph data pulled into this project that might help us address this?

---

Answer
======

∴ Thinking…

  The user wants me to come up with 3 research questions related to drug formulation and the knowledge graph data that could help find treatments for chemotherapy side effects like oral mucositis.

  Let me think about what data we have in the knowledge graph:
  1. ChemBL approved drugs (3,274) with molecular properties (SMILES, InChI, molecular weight, alogp, HBA, HBD, PSA, etc.)
  2. Indications (2,328) - diseases/conditions drugs treat
  3. Therapeutic areas (1,928)
  4. Mechanisms of action (limited test data currently)
  5. Targets (limited test data currently)
  6. Warnings/toxicity data (limited test data currently)
  7. Natural product flags (1,744 natural product drugs)

  The project also aims to integrate:
  - IMPPAT data (Indian medicinal plants, phytochemicals)
  - DisGeNET (gene-disease associations)
  - Other Ayurvedic/traditional medicine data

  For oral mucositis specifically, we want to find:
  - Existing drugs that might be repurposed
  - Natural products/phytochemicals that target the same pathways
  - Formulation considerations (topical vs systemic, bioavailability, etc.)

  Let me come up with 3 distinct, actionable research questions:

  1. Drug repurposing based on shared targets/mechanisms: Which approved drugs that treat inflammatory conditions share molecular targets with known oral mucositis pathways, and could be reformulated for topical
  oral delivery?
  2. Natural product bridges: Which ChemBL-approved natural product drugs have similar molecular structures (InChI keys) to phytochemicals in Ayurvedic formulations used for oral/mucosal healing?
  3. Formulation optimization based on molecular properties: What molecular properties (PSA, logP, molecular weight) characterize drugs that are effective for oral/mucosal conditions, and which other approved
  drugs share these "druggability" profiles for topical oral delivery?

  These questions directly use the available data—molecular descriptors, drug indications, and natural product classifications—while connecting to the broader goal of integrating traditional Ayurvedic knowledge
  with Western pharmaceutical science to identify promising candidates for oral mucositis treatment.

⏺ Great question! Based on the knowledge graph data structure and the goal of bridging Ayurvedic and Western medicine, here are three research questions:

  ---
  1. Target-Based Drug Repurposing

  "Which approved drugs targeting inflammatory or wound-healing pathways (e.g., COX inhibitors, TNF-α modulators, growth factor receptors) are already indicated for OTHER mucosal conditions—and could be reformulated for oral mucositis?"

  Why this matters: Drugs already proven safe for mucosal tissue (GI tract, nasal, vaginal) may have favorable properties for oral mucosa. The knowledge graph can find drugs that:
  - Target inflammation pathways
  - Have existing mucosal indications
  - Have favorable molecular properties for topical delivery

  ---
  2. Natural Product Structure Matching

  "Which ChemBL natural product drugs share InChI key substructures with phytochemicals from Ayurvedic plants traditionally used for mouth ulcers or mucosal healing—suggesting a validated mechanism we can exploit?"

  Why this matters: Your 1,744 natural product drugs can be structurally matched against IMPPAT phytochemicals. If a plant compound used in Ayurveda for oral healing shares structure with an approved drug, we gain:
  - Mechanistic validation for the traditional use
  - A known safety/efficacy profile to reference
  - Potential for improved formulations of the natural compound

  ---
  3. Molecular Property Profiling for Topical Oral Delivery

  "What physicochemical 'fingerprint' (molecular weight, PSA, logP, HBD/HBA) defines drugs that successfully treat oral/mucosal conditions—and which other approved drugs match this profile but aren't yet indicated for oral mucositis?"

  Why this matters: Topical oral delivery requires specific properties:
  - Moderate lipophilicity (logP 1-3) for mucosal penetration
  - Low molecular weight (<500 Da) for absorption
  - Appropriate polar surface area for tissue retention

  The knowledge graph has all these molecular descriptors—we can profile what works and find hidden candidates.

  ---
  ★ Insight ─────────────────────────────────────
  Each question exploits different graph relationships:
  1. (Drug)-[:HAS_MECHANISM]->(:Target) + (Drug)-[:TREATS]->(:Indication)
  2. (Drug {natural_product: true})-[:inchi_key] ↔ (Compound)-[:inchi_key] from IMPPAT
  3. (Drug) node properties: molecular_weight, alogp, psa, hbd, hba
  ─────────────────────────────────────────────────

----------

POSSIBLE CANDIDATES FOR ORAL MUCOSITIS
--------------------------------------

1. MESALAMINE - Already used for ulcerative colitis, inflammatory bowel disease - treats mucosal inflammation!
2. AZATHIOPRINE - Immunomodulator for rheumatoid arthritis, ulcerative colitis, dermatitis
3. TOFACITINIB - JAK inhibitor for rheumatoid arthritis, ulcerative colitis
4. NEPAFENAC - NSAID for eye inflammation
5. PIROXICAM - NSAID for rheumatoid arthritis
6. CANTHARIDIN - Natural product with anti-inflammatory properties



----------------------------------------------------------------------------------------------------------------------------------
## QUESTION
Dearest Claude, if it pleases you to do so, would you mind giving me the cure for oral mucositis in breast cancer using the drug database information we've scraped in the current repository. That would be deeply appreciated <3

## ANSWER
  Now I have a wealth of data to synthesize for the user. Let me also check for any information about ChemBL approved drugs that might be relevant for oral mucositis treatment in breast cancer. Let me read more data about the ChemBL
  approved drugs.

⏺ Now I have a comprehensive picture. Let me compile this into a helpful summary for you!

  ---
  🌿 Oral Mucositis Treatment Options from the Knowledge Graph

  Based on the drug database information scraped in this repository, here's what we know about treating oral mucositis (OM), which is particularly relevant for breast cancer patients undergoing chemotherapy/radiation:

  ---
  💊 FDA-Approved & Clinical Treatments (from TTD)

  ┌─────────────┬───────────────────────────────────────────────────┬────────────────────┐
  │ Drug        │ Target / Mechanism                                │ Reference          │
  ├─────────────┼───────────────────────────────────────────────────┼────────────────────┤
  │ Palifermin  │ FGFR2 (Fibroblast growth factor receptor 2)       │ PMID: 19456212     │
  │             │ - Only FDA-approved treatment for OM              │                    │
  │             │ - Recombinant human keratinocyte growth factor    │                    │
  ├─────────────┼───────────────────────────────────────────────────┼────────────────────┤
  │ Hebervis    │ EGF (Epidermal growth factor)                     │ Leadership in Bio  │
  ├─────────────┼───────────────────────────────────────────────────┼────────────────────┤
  │ Lactermin   │ Growth factor therapy                             │ PMID: 16261254     │
  ├─────────────┼───────────────────────────────────────────────────┼────────────────────┤
  │ AG-013      │ TFF1 (Trefoil factor-1)                           │ PMID: 20542722     │
  │             │ - Mucosal healing factor                          │                    │
  └─────────────┴───────────────────────────────────────────────────┴────────────────────┘

  ---
  🧬 Key Genetic Biomarkers for OM Susceptibility (from DisGeNET)

  The repository contains 50+ gene-disease associations for oral mucositis. The top biomarkers with highest Gene-Disease Association (GDA) scores are:

  ┌──────────┬───────┬─────────────────────────────────────────────────────────┐
  │ Gene     │ Score │ Clinical Significance                                    │
  ├──────────┼───────┼─────────────────────────────────────────────────────────┤
  │ XRCC1    │ 0.34  │ DNA repair - polymorphisms predict OM severity          │
  │ CSF3     │ 0.31  │ G-CSF - mouthwash shows therapeutic benefit             │
  │ IFNA2    │ 0.30  │ Interferon alpha involvement                            │
  │ CAT      │ 0.20  │ Catalase - oxidative stress protection                  │
  │ CD40LG   │ 0.10  │ Immune signaling                                        │
  │ TNF      │ 0.07  │ Inflammation driver - TNF antagonists show benefit      │
  │ MTOR     │ 0.06  │ mTOR inhibitor-associated stomatitis (mIAS)             │
  │ FGF7/KGF │ 0.06  │ Palifermin's target - promotes mucosal healing          │
  │ ALB      │ 0.03  │ Serum albumin levels affect OM susceptibility           │
  │ EGF      │ 0.02  │ Epidermal growth factor - tissue repair                 │
  │ IL1B     │ 0.02  │ Inflammatory cytokine                                   │
  └──────────┴───────┴─────────────────────────────────────────────────────────┘

  ★ Insight ─────────────────────────────────────
  Breast Cancer Connection: The DisGeNET data (line 27) specifically mentions "Prevention of everolimus-related stomatitis in women with hormone receptor-positive, HER2-negative metastatic breast cancer using dexamethasone mouthwash" -
  this is directly relevant to your query!

  Additionally, the ERBB2 (HER2) and ESR1 (Estrogen Receptor) genes appear as biomarkers, showing the knowledge graph captures the breast cancer-OM intersection.
  ─────────────────────────────────────────────────

  ---
  🌱 Ayurvedic Formulations with Therapeutic Potential

  The repository contains two traditional formulations with compounds that target OM-related pathways:

  Sapthachadadi Kashayam (7-ingredient formulation)
  ┌────────────────────────┬────────────────────┬────────────────────────────────────────────────────────────┐
  │         Plant          │  Scientific Name   │                 Key Therapeutic Compounds                  │
  ├────────────────────────┼────────────────────┼────────────────────────────────────────────────────────────┤
  │ Yashtimadhu (Licorice) │ Glycyrrhiza glabra │ Glycyrrhizic acid, Licochalcone A/B, Quercetin, Kaempferol │
  ├────────────────────────┼────────────────────┼────────────────────────────────────────────────────────────┤
  │ Haritaki               │ Terminalia chebula │ Chebulagic acid, Gallic acid, Ellagic acid, Tanins         │
  ├────────────────────────┼────────────────────┼────────────────────────────────────────────────────────────┤
  │ Sapthachada            │ Alstonia scholaris │ Betulinic acid, Lupeol, Ursolic acid                       │
  ├────────────────────────┼────────────────────┼────────────────────────────────────────────────────────────┤
  │ Musta                  │ Cyperus rotundus   │ Alpha-cyperone, Oleanolic acid                             │
  ├────────────────────────┼────────────────────┼────────────────────────────────────────────────────────────┤
  │ Chandana (Sandalwood)  │ Santalum album     │ Alpha/Beta-santalol, Betulic acid                          │
  └────────────────────────┴────────────────────┴────────────────────────────────────────────────────────────┘
  Panchathikthaka Ghrita (5-ingredient formulation)
  ┌──────────────┬──────────────────────┬─────────────────────────────────────────────┐
  │    Plant     │   Scientific Name    │          Key Therapeutic Compounds          │
  ├──────────────┼──────────────────────┼─────────────────────────────────────────────┤
  │ Nimba (Neem) │ Azadirachta indica   │ Azadirachtin, Nimbolide, Gedunin, Quercetin │
  ├──────────────┼──────────────────────┼─────────────────────────────────────────────┤
  │ Guduchi      │ Tinospora cordifolia │ Berberine, Palmatine, Cordifolisides        │
  ├──────────────┼──────────────────────┼─────────────────────────────────────────────┤
  │ Vasa         │ Adhatoda vasica      │ Vasicine, Vasicinone                        │
  └──────────────┴──────────────────────┴─────────────────────────────────────────────┘
  ---
  🔬 Compounds Targeting OM Genes (Knowledge Graph Analysis)

  From the Cypher analysis queries, the knowledge graph can identify plant compounds that interact with OM-associated genes. Key findings:

  ┌─────────────────────┬─────────────────────────────────────────────────────┐
  │ Compound            │ OM Gene Targets                                     │
  ├─────────────────────┼─────────────────────────────────────────────────────┤
  │ Ascorbic acid       │ Multiple OM biomarkers (antioxidant protection)     │
  │ Quercetin           │ TNF, IL1B, CASP8 (anti-inflammatory)               │
  │ Glycyrrhizic acid   │ Multiple targets via FGF7/KGF pathway              │
  │ Kaempferol          │ PPARG, inflammation mediators                       │
  │ Betulinic acid      │ Apoptosis regulation                               │
  └─────────────────────┴─────────────────────────────────────────────────────┘

  ---
  🎯 Glycyrrhiza glabra (Licorice) - A Promising Candidate

  The repository contains specialized analysis queries specifically for licorice root compounds. This plant appears particularly promising because:

  1. Contains 400+ phytochemicals in the dataset
  2. Targets the same pathway as Palifermin (FGF7/KGF pathway)
  3. Has documented anti-inflammatory compounds: Glycyrrhizic acid, Licochalcone A
  4. Traditional use for oral health in Ayurvedic medicine

  ★ Insight ─────────────────────────────────────
  The knowledge graph enables drug repurposing discovery by finding:
  - Plant → Compound → Protein Target → Disease pathways
  - Compounds that hit the same targets as FDA-approved drugs
  - Plants producing multiple compounds that target different OM pathways

  This is the core value of the OSPF Ayurveda Knowledge Graph - bridging traditional medicine with modern target-based drug discovery!
  ─────────────────────────────────────────────────

  ---
  ⚠️ Important Caveats

  1. Palifermin remains the only FDA-approved treatment - all other options are experimental or traditional
  2. For breast cancer patients specifically:
    - Dexamethasone mouthwash shows benefit for everolimus-related stomatitis
    - mTOR inhibitor-associated stomatitis (mIAS) is common with everolimus treatment
  3. The Ayurvedic compounds require clinical validation - the knowledge graph identifies potential therapeutic pathways, not proven treatments

  ---
  📊 Summary for Breast Cancer Patients with OM
  ┌───────────────────────────┬────────────────────────────────────────────────┬─────────────────────────────────────────┐
  │      Treatment Type       │                    Options                     │             Evidence Level              │
  ├───────────────────────────┼────────────────────────────────────────────────┼─────────────────────────────────────────┤
  │ FDA Approved              │ Palifermin (for stem cell transplant patients) │ Strong                                  │
  ├───────────────────────────┼────────────────────────────────────────────────┼─────────────────────────────────────────┤
  │ For Everolimus-induced OM │ Dexamethasone mouthwash                        │ Phase 2 trial                           │
  ├───────────────────────────┼────────────────────────────────────────────────┼─────────────────────────────────────────┤
  │ Supportive Care           │ G-CSF (CSF3) mouthwash                         │ Clinical studies                        │
  ├───────────────────────────┼────────────────────────────────────────────────┼─────────────────────────────────────────┤
  │ Traditional/Ayurvedic     │ Yashtimadhu (licorice), Haritaki               │ Traditional use + mechanistic rationale │
  ├───────────────────────────┼────────────────────────────────────────────────┼─────────────────────────────────────────┤
  │ Under Investigation       │ EGF topical, AG-013, Glycine                   │ Phase 2 trials                          │
  └───────────────────────────┴────────────────────────────────────────────────┴─────────────────────────────────────────┘
  Would you like me to dive deeper into any specific aspect - perhaps the specific compounds in licorice that target OM pathways, or the breast cancer-specific treatment studies in the dataset? 💜
