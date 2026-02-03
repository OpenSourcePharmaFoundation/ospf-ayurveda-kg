# Local LLM Implementation Plan for Ayurveda Knowledge Graph

## Overview

This document outlines the approach for adding a local LLM to the OSPF Ayurveda Knowledge Graph project. The goal is to create a system that can answer questions about potential treatments for chemotherapy side effects (particularly Oral Mucositis) by reasoning over the relationships in our Neo4j knowledge graph.

## Why Graph-Aware RAG (Not Fine-Tuning)

For this use case, **Retrieval-Augmented Generation (RAG)** with graph traversal is superior to fine-tuning for several reasons:

| Approach | Pros | Cons |
|----------|------|------|
| **Fine-Tuning** | Fast inference, no retrieval latency | Expensive, data gets "baked in", can't update without retraining, hallucination risk |
| **Graph-Aware RAG** | Always uses current data, traceable answers, can cite sources, cheaper to update | Slightly higher latency, requires graph query infrastructure |

**Our recommendation: Graph-Aware RAG** — the relationships in Neo4j are the core value, and RAG lets the LLM traverse them dynamically while citing evidence.

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              User Interface                                  │
│                     (CLI / Web UI / API Endpoint)                           │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           Query Processing Layer                             │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐         │
│  │ Intent          │───▶│ Entity          │───▶│ Cypher Query    │         │
│  │ Classification  │    │ Extraction      │    │ Generation      │         │
│  └─────────────────┘    └─────────────────┘    └─────────────────┘         │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         Knowledge Retrieval Layer                            │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                        Neo4j Knowledge Graph                         │   │
│  │                                                                      │   │
│  │   ┌──────────┐    CONTAINS     ┌───────┐    PRODUCES    ┌────────┐  │   │
│  │   │Formulation│───────────────▶│ Plant │───────────────▶│Compound│  │   │
│  │   └──────────┘                 └───────┘                └────────┘  │   │
│  │                                    │                         │      │   │
│  │                                 TREATS                    TARGETS   │   │
│  │                                    │                         │      │   │
│  │                                    ▼                         ▼      │   │
│  │                           ┌─────────────────┐           ┌───────┐   │   │
│  │                           │Therapeutic_Area │           │ Gene  │   │   │
│  │                           └─────────────────┘           └───────┘   │   │
│  │                                                              │      │   │
│  │   ┌──────┐    TREATS      ┌─────────┐    TARGETS    ┌───────────┐  │   │
│  │   │ Drug │───────────────▶│ Disease │◀──────────────│  Protein  │  │   │
│  │   └──────┘                └─────────┘   (via Gene)  └───────────┘  │   │
│  │       │                                                     ▲      │   │
│  │       └─────────────────────TARGETS─────────────────────────┘      │   │
│  │                                                                     │   │
│  │   Relationship Properties:                                          │   │
│  │   • TARGETS: action, source, evidence, evidence_urls, pubchemId    │   │
│  │   • BIOMARKER/EXPRESSION_ASSOCIATION: gdaScore, pmid, interaction  │   │
│  │   • PRODUCES: part (e.g., root, leaf, stem)                        │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                          Response Generation Layer                           │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                         Local LLM (Ollama)                          │   │
│  │                                                                      │   │
│  │   Input: User question + Retrieved graph context + Evidence paths   │   │
│  │   Output: Natural language answer with citations                    │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Core Components

### 1. Local LLM Selection (via Ollama)

[Ollama](https://ollama.ai/) provides an easy way to run LLMs locally. Recommended models:

| Model | Size | Best For | RAM Required |
|-------|------|----------|--------------|
| **Llama 3.1 8B** | 4.7GB | Good balance of speed/quality | 8GB |
| **Llama 3.1 70B** | 40GB | Best reasoning, slower | 48GB+ |
| **Mistral 7B** | 4.1GB | Fast, good for simple queries | 8GB |
| **Mixtral 8x7B** | 26GB | Strong reasoning, moderate speed | 32GB |
| **Phi-3 Medium** | 7.9GB | Medical/scientific knowledge | 16GB |
| **Meditron 7B** | 4.1GB | Medical domain-specific | 8GB |

**Recommendation:** Start with **Llama 3.1 8B** for development, scale to **70B** or **Mixtral** for production quality.

### 2. Graph-to-Text Pipeline

The critical innovation is converting graph traversal results into coherent context for the LLM.

#### Key Relationship Paths to Extract

```cypher
// Path 1: Plant → Compound → Gene/Protein → Disease
// "What plants produce compounds that target genes associated with Oral Mucositis?"
MATCH path = (p:Plant)-[:PRODUCES]->(c:Compound)-[:TARGETS]->(g:Gene)-[:BIOMARKER|EXPRESSION_ASSOCIATION|VARIANT_ASSOCIATION]->(d:Disease)
WHERE d.name = 'Oral mucositis'
RETURN p.scientificName, c.name, g.name,
       [r IN relationships(path) | type(r)] as relationship_chain

// Path 2: Plant → Compound → Protein ← Drug (shared targets)
// "What plants produce compounds that hit the same targets as approved OM drugs?"
MATCH (plant:Plant)-[:PRODUCES]->(compound:Compound)-[:TARGETS]->(protein:Protein)<-[:TARGETS]-(drug:Drug)
WHERE (drug)-[:TREATS]->(:Disease {name: 'Oral mucositis'})
RETURN plant.scientificName, compound.name, protein.name, drug.name

// Path 3: Formulation → Plant → Compound → Target
// "What Ayurvedic formulations contain plants with compounds targeting OM pathways?"
MATCH (f:Formulation)-[:CONTAINS]->(p:Plant)-[:PRODUCES]->(c:Compound)-[:TARGETS]->(target)
WHERE (target)-[]->(:Disease {name: 'Oral mucositis'})
RETURN f.name, collect(DISTINCT p.scientificName), collect(DISTINCT c.name)
```

#### Evidence Extraction

Relationships contain valuable evidence metadata that MUST be included:

```cypher
// Extract evidence for citations
MATCH (c:Compound)-[r:TARGETS]->(g:Gene)-[assoc:BIOMARKER]->(d:Disease)
WHERE d.name = 'Oral mucositis'
RETURN c.name, g.name,
       r.action as mechanism,
       r.source as target_source,
       r.evidence_urls as target_evidence,
       assoc.gdaScore as association_strength,
       assoc.pmid as pubmed_id,
       assoc.interaction as interaction_description
```

### 3. Query Understanding Module

Translates natural language questions into graph traversals:

```python
# Example: Query intent classification
QUERY_PATTERNS = {
    "treatment_for_side_effect": {
        "keywords": ["treat", "help", "remedy", "for", "against"],
        "cypher_template": """
            MATCH (p:Plant)-[:PRODUCES]->(c:Compound)-[:TARGETS]->(g:Gene)
            WHERE (g)-[:BIOMARKER|EXPRESSION_ASSOCIATION]->(:Disease {name: $disease})
            RETURN p, c, g
        """
    },
    "mechanism_of_action": {
        "keywords": ["how", "mechanism", "work", "pathway"],
        "cypher_template": """
            MATCH path = (entity)-[*1..3]->(:Disease {name: $disease})
            WHERE entity.name = $entity_name
            RETURN path
        """
    },
    "plant_recommendations": {
        "keywords": ["plant", "herb", "natural", "ayurvedic"],
        "cypher_template": """
            MATCH (p:Plant)-[:PRODUCES]->(c:Compound)-[:TARGETS]->(target)
            WHERE (target)-[]->(:Disease {name: $disease})
            RETURN DISTINCT p.scientificName, p.sanskritName, collect(c.name)
        """
    }
}
```

---

## Implementation Phases

### Phase 1: Infrastructure Setup (Week 1-2)

#### 1.1 Install Ollama and Base Model

```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Pull recommended model
ollama pull llama3.1:8b

# Test basic functionality
ollama run llama3.1:8b "What is oral mucositis?"
```

#### 1.2 Create Python Integration Module

```
src/
└── llm/
    ├── __init__.py
    ├── ollama_client.py      # Ollama API wrapper
    ├── neo4j_retriever.py    # Graph query execution
    ├── query_parser.py       # NL to Cypher translation
    ├── context_builder.py    # Graph results to LLM context
    └── response_generator.py # Final answer generation
```

#### 1.3 Neo4j Connection Layer

```python
# src/llm/neo4j_retriever.py
from neo4j import GraphDatabase

class KnowledgeGraphRetriever:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def get_treatment_paths(self, disease_name: str, limit: int = 20):
        """Retrieve all treatment pathways for a given disease."""
        query = """
        MATCH path = (p:Plant)-[r1:PRODUCES]->(c:Compound)-[r2:TARGETS]->(g:Gene)-[r3:BIOMARKER|EXPRESSION_ASSOCIATION|VARIANT_ASSOCIATION]->(d:Disease)
        WHERE d.name = $disease
        RETURN p.scientificName as plant,
               p.sanskritName as sanskrit_name,
               r1.part as plant_part,
               c.name as compound,
               c.pubchemId as pubchem_id,
               type(r2) as target_relationship,
               r2.action as mechanism,
               r2.source as evidence_source,
               g.name as gene,
               type(r3) as association_type,
               r3.gdaScore as association_score,
               r3.pmid as pubmed_id,
               r3.interaction as interaction_description
        ORDER BY r3.gdaScore DESC
        LIMIT $limit
        """
        with self.driver.session() as session:
            result = session.run(query, disease=disease_name, limit=limit)
            return [dict(record) for record in result]
```

### Phase 2: RAG Pipeline (Week 3-4)

#### 2.1 Context Builder

Transform graph query results into structured context for the LLM:

```python
# src/llm/context_builder.py

def build_treatment_context(graph_results: list) -> str:
    """Convert graph query results into LLM-friendly context."""

    context_parts = []

    # Group by plant for coherent narrative
    plants = {}
    for row in graph_results:
        plant = row['plant']
        if plant not in plants:
            plants[plant] = {
                'sanskrit': row.get('sanskrit_name'),
                'compounds': []
            }
        plants[plant]['compounds'].append({
            'name': row['compound'],
            'part': row.get('plant_part', 'unspecified'),
            'mechanism': row.get('mechanism'),
            'target_gene': row['gene'],
            'association_type': row['association_type'],
            'evidence_score': row.get('association_score'),
            'pubmed_id': row.get('pubmed_id')
        })

    # Build narrative context
    context = "## Knowledge Graph Evidence\n\n"

    for plant_name, data in plants.items():
        sanskrit = f" ({data['sanskrit']})" if data['sanskrit'] else ""
        context += f"### {plant_name}{sanskrit}\n\n"

        for compound in data['compounds']:
            context += f"- **{compound['name']}** (from {compound['part']})\n"
            context += f"  - Targets: {compound['target_gene']} ({compound['association_type']})\n"
            if compound['mechanism']:
                context += f"  - Mechanism: {compound['mechanism']}\n"
            if compound['evidence_score']:
                context += f"  - Evidence strength: {compound['evidence_score']}\n"
            if compound['pubmed_id']:
                context += f"  - PubMed: {compound['pubmed_id']}\n"
        context += "\n"

    return context
```

#### 2.2 Prompt Engineering

```python
# src/llm/prompts.py

SYSTEM_PROMPT = """You are a research assistant specializing in drug repurposing and traditional medicine.
You have access to a knowledge graph containing:
- Ayurvedic formulations and their plant ingredients
- Medicinal plants and their bioactive compounds (phytochemicals)
- Gene and protein targets of these compounds
- Disease associations including Oral Mucositis (a chemotherapy side effect)
- Approved drugs and their mechanisms

When answering questions:
1. ONLY use information from the provided knowledge graph context
2. Always cite the evidence (PubMed IDs, evidence scores, sources)
3. Explain the biological pathway: Plant → Compound → Target → Disease
4. Note the strength of evidence (gdaScore, number of supporting studies)
5. Clearly distinguish between direct evidence and inferred connections
6. If the evidence is weak or uncertain, say so explicitly

IMPORTANT: You are providing research information, not medical advice. Always recommend consulting healthcare professionals."""

USER_PROMPT_TEMPLATE = """Based on the following knowledge graph data, answer this question:

**Question:** {question}

**Knowledge Graph Context:**
{context}

**Instructions:**
- Summarize the most promising treatment candidates
- Explain the mechanism of action for each
- Rate the evidence strength
- Cite specific PubMed IDs or sources when available
- Note any Ayurvedic formulations that contain relevant plants
"""
```

#### 2.3 Response Generation

```python
# src/llm/response_generator.py
import ollama

class TreatmentAdvisor:
    def __init__(self, retriever: KnowledgeGraphRetriever, model: str = "llama3.1:8b"):
        self.retriever = retriever
        self.model = model

    def answer_question(self, question: str, disease: str = "Oral mucositis") -> str:
        # Step 1: Retrieve relevant graph paths
        graph_results = self.retriever.get_treatment_paths(disease)

        # Step 2: Also get drug-shared targets
        drug_shared = self.retriever.get_shared_drug_targets(disease)

        # Step 3: Get relevant formulations
        formulations = self.retriever.get_formulations_for_disease(disease)

        # Step 4: Build context
        context = build_treatment_context(graph_results)
        context += build_drug_comparison_context(drug_shared)
        context += build_formulation_context(formulations)

        # Step 5: Generate response
        response = ollama.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": USER_PROMPT_TEMPLATE.format(
                    question=question,
                    context=context
                )}
            ]
        )

        return response['message']['content']
```

### Phase 3: Enhanced Query Understanding (Week 5-6)

#### 3.1 Entity Recognition

Use the LLM to extract entities from user questions:

```python
ENTITY_EXTRACTION_PROMPT = """Extract medical/scientific entities from this question.

Question: "{question}"

Return JSON with:
- diseases: list of disease names mentioned
- symptoms: list of symptoms mentioned
- plants: list of plant names mentioned
- compounds: list of compound/chemical names mentioned
- drugs: list of drug names mentioned

JSON:"""

def extract_entities(question: str) -> dict:
    response = ollama.chat(
        model="llama3.1:8b",
        messages=[{"role": "user", "content": ENTITY_EXTRACTION_PROMPT.format(question=question)}],
        format="json"
    )
    return json.loads(response['message']['content'])
```

#### 3.2 Dynamic Cypher Generation

For complex queries, let the LLM generate Cypher:

```python
CYPHER_GENERATION_PROMPT = """Generate a Neo4j Cypher query for this question.

Available node types: Plant, Compound, Gene, Protein, Drug, Disease, Formulation, Therapeutic_Area

Available relationships:
- (Plant)-[:PRODUCES {part}]->(Compound)
- (Compound)-[:TARGETS {action, source, evidence}]->(Gene)
- (Compound)-[:TARGETS {action, source, evidence}]->(Protein)
- (Gene)-[:TRANSLATION]->(Protein)
- (Gene)-[:BIOMARKER {gdaScore, pmid}]->(Disease)
- (Gene)-[:EXPRESSION_ASSOCIATION {gdaScore, pmid}]->(Disease)
- (Gene)-[:VARIANT_ASSOCIATION {gdaScore, pmid}]->(Disease)
- (Drug)-[:TARGETS]->(Protein)
- (Drug)-[:TREATS]->(Disease)
- (Formulation)-[:CONTAINS]->(Plant)
- (Plant)-[:TREATS]->(Therapeutic_Area)

Question: "{question}"

Return ONLY the Cypher query, no explanation:"""
```

### Phase 4: User Interface (Week 7-8)

#### 4.1 CLI Interface

```python
# src/llm/cli.py
import click

@click.command()
@click.option('--question', '-q', prompt='Your question', help='Question about treatments')
@click.option('--disease', '-d', default='Oral mucositis', help='Disease context')
@click.option('--model', '-m', default='llama3.1:8b', help='Ollama model to use')
@click.option('--verbose', '-v', is_flag=True, help='Show retrieved context')
def ask(question, disease, model, verbose):
    """Ask questions about potential treatments using the knowledge graph."""
    advisor = TreatmentAdvisor(model=model)

    if verbose:
        click.echo("\n📊 Retrieving from knowledge graph...")

    answer = advisor.answer_question(question, disease)

    click.echo(f"\n🔬 Answer:\n{answer}")

if __name__ == '__main__':
    ask()
```

#### 4.2 Simple Web Interface (Optional)

```python
# src/llm/web_app.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="OSPF Treatment Advisor")

class Query(BaseModel):
    question: str
    disease: str = "Oral mucositis"

@app.post("/ask")
async def ask_question(query: Query):
    advisor = TreatmentAdvisor()
    answer = advisor.answer_question(query.question, query.disease)
    return {"answer": answer}
```

---

## Advanced Features (Future Enhancements)

### Multi-Hop Reasoning

Enable the LLM to chain multiple graph queries:

```python
# Example: "What compounds from licorice root might help with chemotherapy-induced nausea?"
# Requires: Plant → Compound → Gene → Disease pathway discovery

def multi_hop_query(start_entity: str, target_disease: str, max_hops: int = 3):
    """Find all paths from entity to disease within N hops."""
    query = f"""
    MATCH path = (start {{name: $start}})-[*1..{max_hops}]->(d:Disease {{name: $disease}})
    RETURN path, length(path) as hops
    ORDER BY hops
    LIMIT 20
    """
    # Execute and return paths
```

### Confidence Scoring

Rate answer confidence based on evidence quality:

```python
def calculate_confidence(graph_results: list) -> float:
    """Calculate confidence score based on evidence quality."""
    scores = []
    for result in graph_results:
        score = 0
        # gdaScore indicates gene-disease association strength
        if result.get('association_score'):
            score += float(result['association_score']) * 0.4
        # PubMed citations add credibility
        if result.get('pubmed_id'):
            score += 0.3
        # Multiple evidence sources increase confidence
        if result.get('evidence_source'):
            score += 0.2
        scores.append(score)

    return sum(scores) / len(scores) if scores else 0.0
```

### Comparison Queries

Compare natural compounds to approved drugs:

```python
def compare_to_approved_drugs(compound_name: str, disease: str) -> dict:
    """Compare a compound's targets to approved drug targets."""
    query = """
    // Find compound's targets
    MATCH (c:Compound {name: $compound})-[:TARGETS]->(target)
    WITH collect(target) as compound_targets

    // Find approved drug targets for same disease
    MATCH (d:Drug)-[:TREATS]->(:Disease {name: $disease})
    MATCH (d)-[:TARGETS]->(drug_target)
    WITH compound_targets, collect(DISTINCT drug_target) as drug_targets

    // Calculate overlap
    RETURN
        size([t IN compound_targets WHERE t IN drug_targets]) as shared_targets,
        size(compound_targets) as compound_target_count,
        size(drug_targets) as drug_target_count
    """
```

---

## Data Requirements

### Current Data (Available)

| Dataset | Nodes | Relationships | Status |
|---------|-------|---------------|--------|
| IMPPAT Plants | ~1,000 Plants | PRODUCES → Compounds | ✅ Loaded |
| PubChem Interactions | ~5,000 Compounds | TARGETS → Genes/Proteins | ✅ Loaded |
| DisGeNET | ~200 Genes | BIOMARKER → Disease | ✅ Loaded |
| DrugBank | ~20 Drugs | TREATS/TARGETS | ✅ Loaded |
| TTD | ~10 Drugs | TARGETS → Proteins | ✅ Loaded |
| ChemBL | ~3,000 Drugs | (needs relationship loading) | ⚠️ Partial |

### Data Gaps to Address

1. **ChemBL Integration**: The `chembl_approved_drugs.csv` has rich data but needs Neo4j import scripts
2. **Formulation-Plant Links**: Need more Ayurvedic formulation data
3. **Side Effect Data**: Could add chemotherapy drug side effect profiles

---

## Example Interactions

### Example 1: Basic Treatment Query

```
User: What natural compounds might help with oral mucositis inflammation?

System: Based on the knowledge graph, several plant-derived compounds show promise
for targeting inflammatory pathways associated with oral mucositis:

1. **Glycyrrhizin** (from Glycyrrhiza glabra / Licorice root)
   - Targets: TNF, IL1B, CXCL8 genes (key inflammatory mediators)
   - Evidence: gdaScore 0.15 for TNF-OM association (PMID: 28763884)
   - Mechanism: Anti-inflammatory, NF-κB pathway inhibition

2. **Curcumin** (from Curcuma longa / Turmeric rhizome)
   - Targets: PPARG, CASP8 genes
   - Evidence: gdaScore 0.08 (PMID: 29521847)
   - Mechanism: COX-2 inhibition, antioxidant activity

These compounds share targets with approved OM treatments like Palifermin,
which also modulates inflammatory cytokine production.

⚠️ Note: This is research information. Consult healthcare providers before use.
```

### Example 2: Mechanism Query

```
User: How does licorice root potentially help with chemotherapy side effects?

System: Glycyrrhiza glabra (Licorice) produces multiple bioactive compounds that
interact with oral mucositis-related pathways:

**Pathway Analysis:**
```
Glycyrrhiza glabra (root)
    └── PRODUCES → Glycyrrhizinic acid
                        └── TARGETS → TNF gene
                                          └── BIOMARKER → Oral mucositis (gdaScore: 0.15)
    └── PRODUCES → Liquiritin
                        └── TARGETS → IL1B gene
                                          └── EXPRESSION_ASSOCIATION → Oral mucositis
```

**Shared Drug Targets:**
- TNF is also targeted by: Infliximab (approved for inflammatory conditions)
- IL1B pathway is modulated by: Anakinra

**Ayurvedic Context:**
Licorice appears in formulations: [Formulation names from graph]

Evidence Sources: PubMed IDs 28763884, 29102847
```

---

## Hardware Requirements

| Setup | RAM | GPU | Models Supported |
|-------|-----|-----|------------------|
| **Minimum** | 16GB | None (CPU) | Llama 3.1 8B, Mistral 7B |
| **Recommended** | 32GB | 8GB+ VRAM | Mixtral 8x7B, larger context |
| **Optimal** | 64GB+ | 24GB+ VRAM | Llama 3.1 70B, best quality |

---

## Development Checklist

- [ ] **Phase 1: Infrastructure**
  - [ ] Install Ollama locally
  - [ ] Test model downloads (llama3.1:8b)
  - [ ] Create `src/llm/` module structure
  - [ ] Set up Neo4j connection utility

- [ ] **Phase 2: Core RAG Pipeline**
  - [ ] Implement KnowledgeGraphRetriever
  - [ ] Build context formatting functions
  - [ ] Create prompt templates
  - [ ] Implement basic Q&A flow

- [ ] **Phase 3: Query Enhancement**
  - [ ] Add entity extraction
  - [ ] Implement query classification
  - [ ] Add dynamic Cypher generation

- [ ] **Phase 4: Interface**
  - [ ] Build CLI tool
  - [ ] Add verbose/debug modes
  - [ ] (Optional) Create web interface

- [ ] **Phase 5: Testing & Refinement**
  - [ ] Create evaluation dataset
  - [ ] Test with domain experts
  - [ ] Refine prompts based on feedback
  - [ ] Add confidence scoring

---

## Key Dependencies

```txt
# Add to requirements.txt
ollama>=0.1.0
neo4j>=5.0.0
click>=8.0.0
fastapi>=0.100.0  # optional, for web interface
uvicorn>=0.20.0   # optional, for web interface
```

---

## References

- [Ollama Documentation](https://github.com/ollama/ollama)
- [Neo4j Python Driver](https://neo4j.com/docs/python-manual/current/)
- [LangChain Neo4j Integration](https://python.langchain.com/docs/integrations/graphs/neo4j_cypher) (alternative approach)
- [GraphRAG Paper](https://arxiv.org/abs/2404.16130) (Microsoft Research)