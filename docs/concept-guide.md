How This System Works
=====================

## The one-sentence version

An LLM translates your question into graph operations, specialized agents reason over a biomedical knowledge graph to find answers, and the LLM translates the results back into English.

## What replaces "language"

An LLM learns relationships between *words* from text. We use the same math — vectors, learned parameters, geometric distance — but learn relationships between *biomedical entities* (drugs, genes, diseases, compounds, plants) from graph structure. This is called **Knowledge Graph Embedding (KGE)**.

A KGE model places every entity and every relation type (TARGETS, TREATS, ASSOCIATED_WITH) into a shared vector space where known facts are geometrically consistent: `Drug_vector + TARGETS_vector ≈ Gene_vector`. Once trained, scoring a hypothetical triple like (Curcumin, TREATS, Oral_Mucositis) is just a distance calculation. This is **link prediction** — the graph equivalent of next-token prediction.

## What the LLM actually does

The LLM is the interface, not the reasoning engine. It handles three things:

1. **Entity extraction** — maps your words to graph nodes ("curcumin" → Compound, "TNF-alpha" → Gene, "mucositis" → Disease)
2. **Query decomposition** — breaks a complex question into sub-tasks ("find OM-associated genes in NF-kB pathway, then find drugs targeting those genes, then check for plant sources")
3. **Synthesis** — assembles the agents' structured findings into a readable answer

The LLM never reasons about drug efficacy or biological mechanisms. It translates between human language and graph operations.

## What does the reasoning

**Reasoning agents** — specialized modules that each handle one type of inference over the graph. A target profiler queries gene-disease associations. A repurposing scorer runs link predictions. A pathway analyst traces multi-hop routes (Drug → Target → Pathway → Disease). A safety agent checks interaction risks.

The agents retrieve relevant subgraphs via **GraphRAG** (graph-based retrieval rather than text-chunk retrieval) and reason over them using KGE scores, path traversal, and rule-based logic. This combination of neural (learned embeddings) and symbolic (explicit graph structure) reasoning is called **neuro-symbolic AI**.

## How it connects to what we've built

The knowledge graph we've assembled from ChemBL, DisGeNET, IMPPAT, PubChem, and MedPlant is the training data. Its nodes are the vocabulary. Its relation types are the grammar. Paths through it are the sentences. **Knowledge graph completion** — inferring relationships not stated in any single database — is the core task. The graph is incomplete by nature; the system's job is to fill in the gaps.

## The pipeline

```
User question
  → LLM: entity extraction + query decomposition
    → Reasoning agents: graph traversal + link prediction + path scoring
      → LLM: synthesize findings into natural language answer
```

This fixed sequence — rather than letting the LLM freestyle — is the **structured flow pipeline**. Each step uses the right tool: language models for language, graph models for graphs.

## Term cheat sheet

| Term | What it means here |
|---|---|
| KGE | Embedding drugs/genes/diseases as vectors, like word embeddings but for graph entities |
| GNN | Neural network that learns from graph structure via neighbor message-passing |
| Link prediction | Scoring the likelihood of a missing graph edge (e.g., Drug→TREATS→Disease) |
| Knowledge graph completion | Filling in facts missing from our assembled databases |
| GraphRAG | Retrieving relevant subgraphs (not text chunks) to answer a query |
| Query decomposition | LLM breaking a complex question into graph sub-operations |
| Entity extraction / NER | Mapping words in a question to specific graph nodes |
| Neuro-symbolic | Combining learned embeddings (neural) with structured knowledge (symbolic) |
| Reasoning agents | Specialized modules that run graph inference — the LLM orchestrates them |
| Text-attributed graph | A graph where nodes carry text descriptions (ours does — mechanism text, annotations) |
| GNN-LLM alignment | Mapping graph embeddings and text embeddings into the same vector space |
| Latent space | The learned coordinate system where entities live after training |
