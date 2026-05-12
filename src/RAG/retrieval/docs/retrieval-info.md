# GraphRAG Retrieval: How It Works for This Project

## What is GraphRAG Retrieval?

GraphRAG combines two retrieval strategies to feed an LLM grounded context from a knowledge graph. Unlike vanilla RAG (which retrieves flat text chunks), GraphRAG retrieves **subgraphs** — nodes, relationships, and paths — preserving the relational meaning between entities.

This matters for our project because our data is inherently relational: a compound's relevance depends on what plant produces it, what protein it targets, and whether that protein is implicated in Oral Mucositis. Flat text chunks lose these multi-hop connections.

## The Two Retrieval Strategies

### Strategy 1: Structured Retrieval (Cypher Queries)

An LLM translates a natural language question into a Cypher query. Neo4j executes it and returns precise, structured results.

**Example:**

User asks: *"What plants contain compounds that target TNF for oral mucositis?"*

The LLM generates:

```cypher
MATCH (p:Plant)-[:PRODUCES]->(c:Compound)-[:TARGETS]->(g:Gene)-[:ASSOCIATED_WITH]->(d:Disease)
WHERE d.name = 'Oral mucositis' AND g.name = 'TNF'
RETURN p.scientificName, c.name, g.name
```

This is the "database queries" half of retrieval. It handles precise, well-structured questions where the entities and relationships are clear.

### Strategy 2: Semantic Retrieval (Vector Similarity)

Handles fuzzy, ambiguous queries that can't be directly translated to Cypher. Works by:

1. **Embedding node properties** — converting text descriptions into high-dimensional numerical vectors using a neural network
2. **Storing vectors on Neo4j nodes** — using Neo4j's native vector index (available since v5.11)
3. **At query time** — embedding the user's question and finding the most semantically similar nodes

**Example:**

User asks: *"What's useful for mouth sores from chemotherapy?"*

No node is literally named "mouth sores from chemotherapy," but a vector similarity search on `Disease` and `Indication` nodes surfaces "Oral mucositis" as semantically close. From there, graph traversal expands outward.

```cypher
CALL db.index.vector.queryNodes('indication_embeddings', 5, $queryEmbedding)
YIELD node AS indication, score
MATCH (d:Drug)-[:TREATS_INDICATION]->(indication)
MATCH (d)-[:HAS_MECHANISM]->(m:Mechanism)-[:ACTS_ON]->(t:Target)
RETURN d.name, m.description, t.pref_name, score
ORDER BY score DESC
```

### Strategy 3: Hybrid (What Makes It *Graph*RAG)

The real power comes from combining both — use vector similarity to find **entry points** into the graph, then use graph traversal to **expand context** along relationships.

```
User Question
    |
    v
+---------------------+
|  Intent Classifier   |  <-- LLM determines query type
+---------+-----------+
          |
    +-----+------+
    v            v
+--------+  +----------+
| Precise |  |  Fuzzy   |
| -> Cypher|  | -> Vector |
+---+----+  +----+-----+
    |            |
    +-----+------+
          v
+---------------------+
|  Graph Traversal     |  <-- Expand from entry points
|  (1-3 hops out)      |     along relationships
+---------+-----------+
          v
+---------------------+
|  Context Assembly    |  <-- Subgraph -> text for LLM
+---------+-----------+
          v
+---------------------+
|  LLM Response Gen    |  <-- Answer with citations
+---------------------+
```

## Key Concepts

### Vector Embeddings

A numerical representation of text as an array of floating-point numbers (e.g. 384 dimensions). Semantically similar inputs produce geometrically close vectors:

```
"Ibuprofen: Anti-inflammatory" -> [0.23, -0.87, 0.41, ..., -0.15]   (384 numbers)
"Advil: NSAID for inflammation" -> [0.21, -0.85, 0.39, ..., -0.13]  (384 numbers)
```

These two vectors are geometrically close (high cosine similarity) even though the strings share almost no characters. This enables meaning-based retrieval rather than exact string matching.

A node ends up with both:
- `name: "Ibuprofen"` — for exact matching in Cypher (`WHERE d.name = 'Ibuprofen'`)
- `embedding: [0.23, -0.87, ...]` — for semantic similarity search

### Vector Index

A regular Neo4j index (like on `Drug.name`) is a B-tree that organizes strings for exact lookups. A **vector index** uses HNSW (Hierarchical Navigable Small World) to organize embedding arrays for nearest-neighbor search.

Without the index: compute cosine similarity against every node — O(n).
With the index: approximately O(log n).

```cypher
CREATE VECTOR INDEX drug_embeddings IF NOT EXISTS
FOR (d:Drug) ON (d.embedding)
OPTIONS {indexConfig: {
    `vector.dimensions`: 384,
    `vector.similarity_function`: 'cosine'
}}
```

### Vector Query Procedure

`db.index.vector.queryNodes` is Neo4j's built-in procedure for similarity search:

```cypher
CALL db.index.vector.queryNodes(
    'drug_embeddings',   -- which vector index to search
    5,                   -- return top 5 nearest
    $queryEmbedding      -- the user's question, already embedded
)
YIELD node, score        -- matching node + similarity score (0 to 1)
```

## Implementation for This Project

### Which Nodes to Embed

| Node Type   | Properties to Embed                          | Use Case                        |
|-------------|----------------------------------------------|---------------------------------|
| Drug        | `pref_name` + `indication_class` + synonyms  | Fuzzy drug name matching        |
| Indication  | `mesh_heading` + `efo_term`                  | Semantic disease matching       |
| Mechanism   | `description` + `action_type`                | "How does it work?" queries     |
| Plant       | `scientificName` + uses text                 | Ayurvedic name resolution       |
| Compound    | `name` + target descriptions                 | Chemical function matching      |

### Embedding Generation

```python
from sentence_transformers import SentenceTransformer
from neo4j import GraphDatabase

model = SentenceTransformer('all-MiniLM-L6-v2')  # 384-dim, fast, good quality

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

with driver.session() as session:
    results = session.run(
        "MATCH (d:Drug) RETURN d.name AS name, d.indication_class AS indication"
    )

    for record in results:
        text = f"{record['name']}: {record['indication'] or ''}"
        embedding = model.encode(text).tolist()

        session.run(
            "MATCH (d:Drug {name: $name}) SET d.embedding = $embedding",
            name=record['name'], embedding=embedding
        )
```

**Note on embedding model choice:** `all-MiniLM-L6-v2` is a solid general-purpose starting point. For biomedical text (drug names, protein targets, disease ontologies), domain-specific models like `dmis-lab/biobert-base-cased-v1.2` or `microsoft/BiomedNLP-BiomedBERT` give better semantic matching for queries like "COX-2 inhibitor for mucosal inflammation."

### Proposed Module Structure

```
src/RAG/
└── retrieval/
    ├── __init__.py
    ├── embedder.py          # Embed queries & nodes
    ├── cypher_generator.py  # NL -> Cypher via LLM
    ├── graph_retriever.py   # Hybrid retrieval orchestrator
    ├── context_builder.py   # Subgraph -> text for LLM
    └── docs/
        └── retrieval-info.md  # This file
```

### Hybrid Retrieval Orchestrator

The core function that combines both strategies:

```python
def retrieve(question: str, neo4j_session, embed_model, llm):
    # 1. Vector search: find semantically similar entry points
    query_embedding = embed_model.encode(question).tolist()
    vector_results = neo4j_session.run("""
        CALL db.index.vector.queryNodes('drug_embeddings', 5, $embedding)
        YIELD node, score
        RETURN node.name AS name, score
    """, embedding=query_embedding)

    # 2. Cypher generation: let LLM write a structured query
    cypher = llm.generate_cypher(question, schema_context)
    structured_results = neo4j_session.run(cypher)

    # 3. Graph expansion: traverse outward from entry points
    for entry_node in vector_results:
        neighbors = neo4j_session.run("""
            MATCH (n {name: $name})-[r*1..2]-(neighbor)
            RETURN n, r, neighbor
        """, name=entry_node['name'])

    # 4. Assemble context for LLM
    return build_context(vector_results, structured_results, neighbors)
```

### Context Assembly

Converts raw graph results into natural language text for LLM consumption:

```python
def build_context(vector_results, structured_results, neighbors):
    """Convert graph data into natural language context for the LLM."""
    context_parts = []

    for drug in structured_results:
        context_parts.append(
            f"Drug: {drug['name']} targets {drug['target']} via {drug['mechanism']}. "
            f"It treats {drug['indication']}. Source: ChemBL."
        )

    for plant_path in neighbors:
        context_parts.append(
            f"Plant {plant_path['plant']} produces {plant_path['compound']} "
            f"which targets {plant_path['gene']} "
            f"(OM association score: {plant_path['gda_score']})"
        )

    return "\n".join(context_parts)
```

The LLM receives this context alongside the original question and generates a grounded answer — this is the "augmented generation" in R-A-G.

### Cypher Generation

The `llm.generate_cypher()` call wraps a local LLM (Llama 3.1 8B via Ollama, per the plan in `docs/notes/local-llm-implementation-plan.md`) prompted with:

1. **The graph schema** — so it knows what nodes, relationships, and properties exist
2. **The user's natural language question**
3. **Few-shot examples** — pairs of (question -> correct Cypher)

The LLM returns a Cypher string, which gets validated and executed. This would live at `src/RAG/retrieval/cypher_generator.py`.

## Required Dependencies

Current `requirements.txt` has: `beautifulsoup4`, `pandas`, `requests`.

For GraphRAG retrieval, add:

```
neo4j>=5.14.0              # Python driver (already used by setup_neo4j.py but unlisted)
sentence-transformers>=2.2  # Embedding generation
llama-cpp-python>=0.2       # Local LLM inference
```

## Prerequisites

Before implementing retrieval, the graph data needs to be complete:

- Several ChemBL secondary datasets (mechanisms, indications, targets) are at test-sample size
- The ChemBL-IMPPAT mapping has only been run on sample data
- MedPlant data needs graph import

The retrieval layer is only as good as the graph it searches.
