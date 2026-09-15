# Local LLM & Graph Neural Network Plan

_Created: 2026-07-27 | Updated: 2026-08-31_

This plan covers two complementary systems: a **Graph Neural Network (GNN)** that learns from the knowledge graph's structure to predict new drug-target connections, and a **local LLM** that provides a natural language interface over the graph and GNN outputs. They serve different purposes and can be built independently.

---

## Part 1: Graph Neural Network (GNN)

### What a GNN actually does

A GNN operates on the **graph structure itself** — nodes, edges, and their properties — not on text. It learns vector representations ("embeddings") for every node by aggregating information from each node's neighbors. After training, these embeddings encode the "meaning" of each node's position and properties within the graph.

The core task for this project is **link prediction**: given a Compound node and a Gene/Protein node that have no direct edge between them, the GNN predicts how likely it is that a TARGETS relationship should exist. This is exactly the question the analysis queries already ask ("which plants produce compounds that interact with OM drug targets?"), but the GNN can find connections the explicit data misses.

### How it works on our graph

Our Neo4j graph has these node types and relationships:

```
Plant -[PRODUCES]-> Compound -[TARGETS]-> Gene/Protein
Drug  -[TARGETS]->  Protein  -[TRANSLATION]<- Gene
Gene  -[EXPRESSION_ASSOCIATION|BIOMARKER|VARIANT_ASSOCIATION]-> Disease
Drug  -[TREATS]->   Disease
Plant -[TREATS]->   Therapeutic_Area
Drug  -[INDICATED_FOR]-> Therapeutic_Area
Formulation -[CONTAINS]-> Plant
```

Node features available for the GNN:
- **Drug**: molecular_weight, alogp, hba, hbd, psa, rtb, ro5_violations, aromatic_rings, heavy_atoms, qed_weighted, natural_product flag
- **Compound**: type, source, pubchemId (can fetch molecular descriptors)
- **Gene**: ncbiId, gdaScore (from DisGeNET edges)
- **Protein**: uniprotId, drugbankId
- **Disease/Therapeutic_Area/Plant/Formulation**: primarily name-based (use as categorical or learn embeddings)

### Step 1: Export the graph to a GNN-ready format

```
[ ] Write a Neo4j export script (Python + neo4j driver)
    - Export all nodes with their properties as node feature matrices
    - Export all edges as edge index pairs
    - Map node types to integer type IDs
    - Map relationship types to integer edge type IDs
    - Output: PyG HeteroData object or DGL heterograph saved as .pt / .bin
```

This is a **heterogeneous graph** (multiple node types, multiple edge types), so we need a library that supports heterogeneous GNNs.

### Step 2: Choose and set up the GNN library

**Recommended: PyTorch Geometric (PyG)**

```
[ ] Install PyG and dependencies
    pip install torch torch-geometric
    pip install pyg-lib torch-scatter torch-sparse  # optional accelerators
```

Why PyG over alternatives:
- **PyG** — Best documented, largest community, native heterogeneous graph support via `HeteroData` and `to_hetero()`. First choice.
- **DGL (Deep Graph Library)** — Comparable to PyG, strong heterogeneous support. Good alternative if PyG has installation issues on macOS.
- **StellarGraph** — Higher-level API, easier to start, but less flexibility and slower development.
- **GraphSAGE / node2vec** — Simpler embedding methods (not full GNNs). Good for a quick first pass before investing in GNN training.

### Step 3: Build the training pipeline

```
[ ] Define the heterogeneous graph schema in PyG
    - Node types: Drug, Compound, Gene, Protein, Disease, Plant, Formulation, Therapeutic_Area
    - Edge types: all relationship types above
    - Node feature vectors: numerical properties where available, learnable embeddings where not

[ ] Implement link prediction training
    - Task: predict missing TARGETS edges (Compound->Gene, Compound->Protein, Drug->Protein)
    - Split existing TARGETS edges into train/val/test (e.g., 80/10/10)
    - Negative sampling: generate fake edges that don't exist as negative examples
    - Model: R-GCN (Relational Graph Convolutional Network) or HGT (Heterogeneous Graph Transformer)
    - Loss: binary cross-entropy on (real edge vs fake edge) pairs

[ ] Train and evaluate
    - Metrics: AUC-ROC, MRR (Mean Reciprocal Rank), Hits@K
    - Baseline comparison: random predictor, shortest-path heuristic
```

### Step 4: Generate predictions

```
[ ] Run the trained GNN on all Compound-Gene and Compound-Protein pairs that lack a TARGETS edge
    - Score each potential edge
    - Rank by predicted probability
    - Output: CSV of "predicted novel TARGETS relationships" with confidence scores

[ ] Optionally write predictions back to Neo4j as a new relationship type (e.g., PREDICTED_TARGETS)
    - Include the confidence score as a property
    - This lets the existing analysis queries incorporate GNN predictions
```

### How you "talk to" a GNN — input/output interface

A GNN is **not conversational**. You don't type prompts into it. It's more like a function:

**Input:** The entire graph (or a subgraph) + a query like "score the potential edge between Compound X and Gene Y"

**Output:** A number (0.0 to 1.0) representing how likely that edge is to be real

Concretely, the interaction modes are:

1. **Batch prediction** — Feed it all missing edges, get a ranked list back. This is the main use case: "give me the top 50 compound-gene links the data doesn't explicitly have but the GNN thinks should exist."

2. **Single-query prediction** — Ask about a specific pair: "How likely is it that Quercetin targets TNF?" Returns a score.

3. **Node similarity** — "Which compounds have embeddings most similar to Drug X?" Returns nearest neighbors in embedding space. Useful for finding phytochemicals that behave like known drugs.

4. **Subgraph explanation** — Using GNN explainability tools (like GNNExplainer in PyG), ask "why does the GNN predict this edge?" and get back the subgraph neighborhood that most influenced the prediction.

These all happen through Python function calls, not a chat interface. The local LLM (Part 2) is what provides the natural language layer on top.

---

## Part 2: Local LLM

### Purpose

The local LLM serves as a natural language interface that can:
1. Translate questions like "Which Ayurvedic plants might treat oral mucositis?" into graph queries
2. Summarize and explain GNN predictions in plain language
3. Reason about the combined evidence (graph data + GNN scores + literature)

### Step 1: Get a base model running locally

```
[ ] Install Ollama (simplest local LLM runtime for macOS)
    brew install ollama
    ollama pull llama3.1:8b         # Good general-purpose starting point
    ollama pull mistral:7b-instruct  # Alternative, strong at instruction-following

[ ] Verify it runs fully offline
    - Disable network and confirm inference still works
    - Test basic biomedical questions to assess baseline knowledge
```

Why Ollama: zero-config, runs on Apple Silicon via Metal, no Python dependency hell. Alternatives (llama.cpp, vLLM, LocalAI) offer more control but more setup.

Model size guidance for this Mac:
- **7-8B parameters**: Runs comfortably on 16GB+ RAM, fast inference
- **13B parameters**: Needs 16GB+, slower but noticeably smarter
- **70B parameters**: Needs 64GB+ RAM or quantized to fit, much smarter but slow

### Step 2: Give the LLM access to graph data (RAG, not fine-tuning)

Fine-tuning a model on ~77K CSV rows of biomedical data is expensive, fragile, and hard to update when new data arrives. Instead, use **Retrieval-Augmented Generation (RAG)**: the LLM retrieves relevant graph data at query time and reasons over it.

```
[ ] Build a graph-aware RAG pipeline
    - On each user question:
      1. Extract entities (drug names, gene names, plant names) from the question
      2. Run targeted Cypher queries against Neo4j to pull relevant subgraphs
      3. Format the subgraph data as context for the LLM
      4. Send (context + question) to the local LLM
      5. LLM generates a natural language answer grounded in the retrieved data

[ ] Optionally: also include GNN prediction scores in the retrieved context
    - "Quercetin -> TNF: predicted_score=0.87, no explicit TARGETS edge"
    - This lets the LLM reason about both known and predicted connections
```

This is the **bridge between the GNN and natural language**. The GNN produces scores, the RAG pipeline retrieves those scores alongside graph facts, and the LLM explains them.

### Step 3: Cypher generation (stretch goal)

```
[ ] Fine-tune or few-shot prompt the LLM to generate Cypher queries
    - Use the existing analysis_queries.txt as training examples
    - User asks: "Which plants produce compounds that target TNF?"
    - LLM generates: MATCH (p:Plant)-[:PRODUCES]->(c:Compound)-[:TARGETS]->(g:Gene {name:'TNF'}) RETURN p, c
    - Execute against Neo4j, feed results back to LLM for summarization
```

---

## Part 3: Subgraph splitting for analysis

The full graph may be too large for the GNN to train efficiently or for the LLM context window. Strategies:

```
[ ] Disease-centric subgraphs
    - Extract everything within N hops of Disease{name:'Oral mucositis'}
    - This captures all OM-relevant genes, their targeting drugs/compounds, and upstream plants
    - Typical size: hundreds to low thousands of nodes (manageable)

[ ] Mini-batch training (built into PyG)
    - PyG's NeighborLoader samples subgraphs on the fly during training
    - No manual splitting needed — handles graphs with millions of nodes
    - Configure: num_neighbors=[10, 5] for 2-hop sampling per batch

[ ] Target-centric subgraphs for analysis
    - Given a specific protein target, pull its 2-hop neighborhood
    - Feed to the GNN for focused prediction or to the LLM for explanation
```

---

## Implementation order

| Phase | What | Depends on | Estimated effort |
|-------|------|-----------|-----------------|
| **0** | Fill out glossary, finish data aggregation | — | Already in progress |
| **1** | Neo4j → PyG export script | Phase 0 | 1-2 days |
| **2** | Basic GNN link prediction (R-GCN) | Phase 1 | 3-5 days |
| **3** | GNN evaluation + prediction export | Phase 2 | 1-2 days |
| **4** | Install Ollama + baseline local LLM | — (independent) | 1 hour |
| **5** | Graph-aware RAG pipeline | Phase 3 + Phase 4 | 3-5 days |
| **6** | Integrate GNN scores into RAG context | Phase 3 + Phase 5 | 1-2 days |
| **7** | Cypher generation (stretch) | Phase 5 | 3-5 days |

Phases 1-3 (GNN) and Phase 4 (local LLM install) can happen in parallel.

---

## Key libraries

| Library | Purpose | Install |
|---------|---------|---------|
| `torch` | Neural network foundation | `pip install torch` |
| `torch-geometric` | GNN framework (heterogeneous graph support) | `pip install torch-geometric` |
| `neo4j` | Python driver to export graph data | `pip install neo4j` |
| `ollama` | Local LLM runtime | `brew install ollama` |
| `langchain` or `llama-index` | RAG orchestration (optional, can build from scratch) | `pip install langchain` |
| `sentence-transformers` | Embedding text for RAG retrieval (optional) | `pip install sentence-transformers` |

---

## Open questions

- [ ] How much molecular descriptor data should we fetch for Compound nodes? (PubChem has rich descriptor sets, but adds scraping work)
- [ ] Should we use a biomedical-specialized LLM (e.g., BioMistral, PMC-LLaMA) instead of a general model?
- [ ] Do we want the GNN to predict other edge types beyond TARGETS? (e.g., TREATS, EXPRESSION_ASSOCIATION)
- [ ] How do we validate GNN predictions? (Literature search? Wet lab? Expert review?)
