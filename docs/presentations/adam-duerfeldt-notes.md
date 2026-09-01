# Local LLM & GNN Plan - Summary for Adam Duerfeldt

## The big picture

We've built a knowledge graph in Neo4j that connects Ayurvedic medicinal plants to Western drug targets for Oral Mucositis. It links plants to the compounds they produce, those compounds to the genes and proteins they interact with, and those same genes/proteins to the disease. We also have approved drugs in there targeting the same proteins. The graph already lets us run queries like "which plants produce compounds that hit the same targets as known OM drugs?" -- but it's limited to connections that are *explicitly documented* in the data.

## The plan has two parts

### 1. A Graph Neural Network (GNN) to predict missing connections

Think of it as a machine learning model that looks at the *shape* of the graph -- which nodes are connected, how, and through what intermediaries -- and learns patterns. Then it scores pairs of compounds and protein targets that *don't* have a documented interaction, predicting how likely it is that they actually do interact. The output is a ranked list: "here are the top 50 compound-target links the literature doesn't explicitly show, but the network structure strongly suggests." It's basically computational hypothesis generation -- the GNN says "based on how everything else is connected, Compound X probably hits Protein Y," and that becomes something you could validate experimentally or through deeper literature review.

### 2. A local language model (LLM) as a natural-language interface

Instead of writing database queries by hand, you'd ask questions in plain English -- "Which Ayurvedic plants might treat oral mucositis through TNF modulation?" -- and the system retrieves the relevant graph data (including GNN prediction scores) and gives you a synthesized answer. It uses retrieval-augmented generation (RAG), meaning the LLM doesn't memorize the data; it pulls the relevant subgraph at query time and reasons over it. This keeps it grounded in your actual data rather than hallucinating.

## How they connect

The GNN produces numerical scores (e.g., "Quercetin -> TNF: 0.87 confidence"). The RAG pipeline feeds those scores alongside the known graph facts to the LLM. So when you ask a question, the answer draws on both documented interactions *and* predicted ones, clearly labeled as such.

## Implementation

It's phased: export the graph into a format the GNN can train on, train a link-prediction model, generate and rank predictions, set up the local LLM, and then wire them together through the RAG pipeline. The GNN and LLM setup can happen in parallel since they're independent until the integration step.

## Open questions

- How much additional molecular descriptor data to pull for the compound nodes
- Whether to use a biomedical-specialized LLM versus a general one
- How to validate the GNN's predictions (literature? expert review? wet lab?)
