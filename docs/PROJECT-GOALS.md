# Project Goals

## What This Project Is

The OSPF Ayurveda Knowledge Graph is a **drug repurposing engine for Oral Mucositis (OM)** - a painful side effect of chemotherapy that currently has only 4 approved treatments. It finds existing compounds, both pharmaceutical drugs and Ayurvedic plant-derived compounds, that could treat OM.

## What Makes It Unique

The project builds a bridge between two medical traditions:

- The **Western pharmacology side** has 3,276 approved drugs with known molecular targets, mechanisms, and safety data (from ChemBL, DisGeNET, DrugBank, TTD)
- The **Ayurvedic medicine side** has formulations containing plants with 60,000+ documented phytochemical-protein interactions (from IMPPAT, PubChem, MedPlant DB)
- The **Neo4j knowledge graph** connects them through shared molecular targets and genes

The core hypothesis: if an Ayurvedic plant compound hits the same protein target as an approved drug that treats inflammation, and that protein is linked to OM through gene-disease associations, then that compound is a repurposing candidate worth investigating.

## Best Uses

1. **Identifying drug repurposing candidates** - Query the graph: "Which approved drugs target genes associated with oral mucositis?" Only 4 drugs are approved for OM today; this graph can surface hundreds of candidates from the 3,276 drugs already in it.

2. **Validating Ayurvedic formulations scientifically** - Trace the path: Ayurvedic formulation -> plant ingredients -> phytochemicals -> protein targets -> OM-associated genes. This gives traditional medicine a molecular-level evidence base.

3. **Prioritizing research directions** - Instead of testing compounds randomly, researchers can use the graph to rank candidates by how many OM-relevant targets they hit, their safety profiles, and their drug-likeness properties.

4. **Network pharmacology** - Ayurvedic formulations are inherently multi-compound, multi-target. The graph can analyze whether a formulation's compounds work synergistically across multiple OM pathways (something single-drug approaches miss).

5. **Academic publication / grant support** - The structured data pipeline and knowledge graph are a publishable methodology for computational drug repurposing in traditional medicine.

## The Translation

This project turns:

> "This plant has been used in Ayurveda for mouth sores for centuries"

Into:

> "This plant contains compound X, which inhibits protein Y, which is overexpressed in oral mucositis tissue, and approved drug Z works through the same mechanism."

That's the translation from traditional knowledge to testable scientific hypotheses.
