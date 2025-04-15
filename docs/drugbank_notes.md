------------------------------------------
Location
========
https://go.drugbank.com/drugs

------------------------------------------
What data do we need from drugbank?
===================================
- Drug name
- Assay
  - In vitro
  - In vivo
  - Toxicity profile
- Drug-drug interactions
- Target name (protein, transcription factor, etc)
- Pharmacodynamics
- Pharmacokinetics
- Clinical trials
- Mechanism of action
- Adverse events
  - SAEs (serious adverse events)
  - AEs (adverse events - standard, non-serious)
- Lipophilicity
- ADME properties (absorption, distribution, metabolism, excretion)

--------------------------------------------------------------------------------
What's the purpose of the data being gathered?
==============================================
From the drug bank, we want to see whether each particular drug matches with
a target disease of interest (such as, for example, oral mucositis).
We want to see if there's any overlap with the drugs in the plant database.

Why?
----
To start, we're building the infrastructure from oral mucositis.
  ...which is comprised of 10-15 different conditions
But it's not (just) about that.
Right now, we have only 2 specific treatments for oral mucositis
(Palifermin and Benzydamine).
We want to see if there are other drugs (existing drugs) that could be used by
looking at their targets proteins, pathways, mechanisms of action, side
effects, chemical structures, etc.

--------------------------------------------------------------------------------
How to scrape
=============
1. Create .csv file for drugbank data
  - Write headers based on data structure defined below
2. Visit https://go.drugbank.com/drugs?approved=1&c=name&d=up&page=1
3. For each row:
  - Grab link from first column
  - Follow link
  - Grab all items from data structure from followed link
  - Write row into .csv file
4. On reaching end of page:
  - Iterate the page number at the end of the URL by 1
  - Repeat steps 2 and 3
5. On reaching final row of final page:
  - Save .csv file

First pass structure
--------------------
- Name
- Summary
- List of indications, under Associated Conditions
- WIP

--------------------------------------------------------------------------------
Data structure
==============
Example locations
-----------------
- Alprazolam:   https://go.drugbank.com/drugs/DB00404
- Trazodone:    https://go.drugbank.com/drugs/DB00656
- Palifermin:   https://go.drugbank.com/drugs/DB00039
- Betulin:      https://go.drugbank.com/drugs/DB16890
- Morphine:     https://go.drugbank.com/drugs/DB00295 [path]
- Fluoxetine:   https://go.drugbank.com/drugs/DB00472 [path]
- Rifampin:     https://go.drugbank.com/drugs/DB01045
- Codeine:      https://go.drugbank.com/drugs/DB00318 [path]
- Tetracycline: https://go.drugbank.com/drugs/DB00759

REST API
--------
-   https://docs.drugbank.com/v1/#development-key

Schema
------
```yaml
# Data set:
{
  name: string,
  summary: string,
  brand_names: string[],
  drugbank_accession_number: string,
  background: string,
  drug_type:
    "small molecule" |
    "biologics" |
    "biotech" |
    "antibodies" |
    "vaccines" |
    string [WIP - look up others],

  # Found in "groups"
  is_approved: boolean,
  is_investigational: boolean,
  is_vet_approved: boolean,
  is_illicit: boolean,
  is_experimental: boolean,
  is_nutraceutical: boolean,
  synonyms: string[],
  external_ids: string[],

  # Will be the paragraph under "Indication"
  primary_indication_desc: string,

  associated_conditions: Array<{
    type:
      "Used in combination to treat" |
      "Used to treat" |
      "Used in combination to treat" |
      "Used in combination for symptomatic treatment of" |
      "Treatment of" |
      "Management of" |
      "Prophylaxis of" |
      "Adjunct therapy in management of" |
      string,

    # Aka condition
    # e.g. Schizophrenia, Oral mucositis, etc
    indication: string,
    # e.g. ["Diclofenac"] or ["codeine", "caffeine"]
    combined_product_details: string[],
  }>,

  # Contraindications and blackbox warnings
  # {{TODO section}}
  warnings: "{{TODO - need access to drugbank account}}",

  # Big paragraph of info
  pharmacodynamics: string,

  # Another big paragraph of info
  mechanism_of_action: string,

  binding_sites: Array<{
    # e.g. "GABA(A) Receptor", "Translocator protein"
    site: string,
    # e.g. "agonist", "antagonist", "ligand", "positive allosteric modulator"
    binding_type: string,
    # e.g. "Humans", "Rodents"
    organism: string
  }>,

  volume_of_distribution: string,

  protein binding: string,

  metabolism: string,
  route_of_elimination: string,
  half_life: string,

  clearance: string,

  # {{ TODO figure out how to get this data }}
  adverse_effects: WIP,

  # Example:
  # "LD50=808mg/kg (orally in mice)"
  toxicity: string,

  # Example:
  # [
  #   {
  #     name: "Codeine Metabolism Pathway",
  #     type: "Drug metabolism"
  #   },
  #   {
  #     name: "Codeine Action Pathway",
  #     type: "Drug action"
  #   }
  # ]
  pathway: Array<{
    name: string,
    type: string,
  }>

  # Note: all of this is accessible on downloading the drugbank HTML page
  #       It disappears when you look in "Elements", but the data is
  #       present in the initial raw HTML text downloaded at the page URL.
  #
  # TODO: add content grabbable from details_link (this is a separate task)
  # TODO: add content grabbable from defining_changes link
  #
  # Example:
  # {
  #   interacting_gene_enzyme: "Cytochrome P450 2D6",
  #   allele_name: "CYP2D6*4",
  #   genotype: "(A;A)",
  #   defining_changes: ["A Allele", "homozygote"],
  #   types: ["Effect", "Directly Studied"],
  #   description: "Patients with this genotype have reduced metabolism of codeine",
  #   details_link: "https://go.drugbank.com/pharmaco/genomics/DBSNPE000007"
  # }
  pharmacogenomic_effects: Array<{
    interacting_gene_enzyme: string,
    allele_name: string,
    genotype: string,
    defining_changes: string[],
    types: string[],
    details_link: string
  }>,

  # {{ TODO Add an account to scrape all of the data }}
  # Can view the first 15 without an account
  # Note that each button press requires a REST API call
  # These can be done automatically in the code.
  #
  # Example request:
  # https://go.drugbank.com/drugs/DB00759/drug_interactions.json?group=approved&draw=18&columns[0][data]=0&columns[0][name]=&columns[0][searchable]=true&columns[0][orderable]=false&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=1&columns[1][name]=&columns[1][searchable]=true&columns[1][orderable]=false&columns[1][search][value]=&columns[1][search][regex]=false&start=10&length=5&search[value]=&search[regex]=false&_=1736821046996
  # Modifying start and length params determines what's returned.
  #   You will need to attach an authentication cookie to do this.
  #
  # Example:
  #   [
  #     {
  #       name: "Abacavir",
  #       description: "Tetracycline may decrease the excretion rate of Abacavir which could result in a higher serum level"
  #     },
  #     {
  #       name: "Abametapir",
  #       description: "The serum concentration of Tetracycline can be increased when it is combined with Abametapir"
  #     }
  #   ]
  drug_interactions: Array<{
    name: string,
    description: string
  }>,

  #
  # Example:
  # [
  #   "Avoid milk and dairy products.",
  #   "Take on an empty stomach. Take at least 1 hour before or 2 hours after meals.",
  #   "Take with a full glass of water."
  # ]
  #
  food_interactions: string,

  # Example:
  # "[H][C@@]12C[C@@]3([H])C(=C(O)[C@]1(O)C(=O)C(C(N)=O)=C(O)[C@H]2N(C)C)C(=O)C1=C(O)C=CC=C1[C@@]3(C)O"
  SMILES: string,

  # Example:
  # [
  #   {
  #     phase: 	"Not Available",
  #     status: "Completed",
  #     purpose: 	"Not Available",
  #     conditions: "Head And Neck Cancer",
  #     count: 1
  #   }
  # ]
  clinical_trials: Array<{
    phase: string,
    status: string,
    purpose: string,
    conditions: string,
    count: number
  }>,

  # Example:
  # "https://patents.google.com/patent/US6350468"
  patent_url: string,

  targets: UniprotEntry[],
  enzymes: UniprotEntry[],
  transporters: UniprotEntry[],

  # {{TODO complete this - WIP}}
}

# Example:
#   {
#     uniprot_name: "30S ribosomal protein S7",
#     kind: "Protein",
#     organism: "Escherichia coli (strain K12)",
#     phamcological_action: true,
#     actions: ["Inhibitor"],
#     general_function: "One of the primary rRNA binding proteins, it...etc...",
#     specific_function: "mRNA binding",
#     gene_name: "rpsG",
#     uniprot_url: "http://www.uniprot.org/uniprot/P02359"
#   }
UniprotEntry: {
  uniprot_name: string,
  kind: string,
  organism: string,
  # Yes = true; No = false
  pharmacological_action: boolean,
  actions: string[],
  general_function: string,
  specific_function: string,
  gene_name: string,
  uniprot_url: string
}
```
