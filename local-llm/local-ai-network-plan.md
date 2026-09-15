# Local AI Network Plan: SLM → GNN Pruning → Classical ML → LLM

_Created: 2026-09-14 | Branch: `local-llm-subproject`_

This plan turns the sketch from the Duerfeldt presentation notes into a buildable design:

> - Top-level: SLM (small language model) to take queries in
> - Shrink the knowledge graph to discrete relevant sections (structural pruning with GNNs)
> - Analyze those subsections with small AIs and classical ML (SVMs, random forests, MLPs)
> - Feed it back into an LLM to generate text output

It builds on three existing documents rather than replacing them:

| Document | What it already covers | What this plan adds |
|---|---|---|
| `docs/todos/2026-07-27-local-llm-todo.md` | GNN link prediction (R-GCN on PyG), Ollama setup, RAG-not-fine-tuning decision | How the GNN is *also* used for pruning, and how its outputs feed a classical ML tier |
| `docs/notes/local-llm-implementation-plan.md` | Single-LLM GraphRAG: Cypher templates, context builder, prompts | Splits that single LLM into an intake SLM and a synthesis LLM, with structured stages between them |
| `docs/next-steps/2026-09-01-week-plan.md` | Concrete week of GNN export + training tasks | Where that week's output slots into the larger network |

---

## 1. Why a network instead of one big LLM

The current pipeline (the Claude-driven `disease-explorer` skill) has three
problems the presentation notes call out: it is one-shot, it is token-expensive,
and it allows no back-and-forth. All three come from the same root cause: a
single large model does retrieval, reasoning, scoring, and writing in one pass
over the whole graph.

Splitting the work into tiers fixes each problem for a specific reason:

- **Back-and-forth** becomes possible because the expensive part (finding the
  relevant subgraph) is cached per session. A follow-up question re-runs only
  the cheap downstream tiers.
- **Cost** drops because the LLM only sees a few hundred nodes of pre-scored
  evidence, not the raw graph. Most of the compute is GNN inference and
  scikit-learn, which is effectively free on a laptop.
- **Auditability** improves because every tier emits a typed artifact. When an
  answer looks wrong, the failing tier is identifiable: bad entity linking, bad
  subgraph, bad score, or bad prose.

The guiding principle: **LLMs do language, not arithmetic.** Anything that is a
lookup, a traversal, or a score is done by Neo4j, the GNN, or scikit-learn, and
the language models only translate at the boundaries (question → structured
query, scored evidence → prose).

---

## 2. Architecture

```
 ┌──────────────────────────────────────────────────────────────────────────┐
 │ TIER 1 · INTAKE                                    small LM (3-4B)      │
 │ Natural-language question → QueryPlan (JSON)                             │
 │   intent, seed entities (linked to graph node IDs), constraints, task    │
 └───────────────────────────────┬──────────────────────────────────────────┘
                                 │ QueryPlan
                                 ▼
 ┌──────────────────────────────────────────────────────────────────────────┐
 │ TIER 2 · SUBGRAPH EXTRACTION + STRUCTURAL PRUNING     Neo4j + GNN        │
 │ a. Seed expansion: k-hop / Personalized PageRank from seed nodes         │
 │ b. GNN relevance scoring: node & edge importance w.r.t. the task         │
 │ c. Prune to a budgeted subgraph (e.g. ≤ 500 nodes, ≤ 2,000 edges)        │
 │ d. Attach GNN outputs: node embeddings, predicted-edge scores            │
 └───────────────────────────────┬──────────────────────────────────────────┘
                                 │ ScoredSubgraph (.pt + .json)
                                 ▼
 ┌──────────────────────────────────────────────────────────────────────────┐
 │ TIER 3 · ANALYSIS                              scikit-learn + small NNs  │
 │ Feature tables built from the subgraph → one model per question type:   │
 │   candidate ranking (RF / GBM), target-class prediction (SVM),           │
 │   mechanism clustering (k-means / HDBSCAN on embeddings), MLP re-scorer  │
 │ Output: ranked candidates with per-feature attributions                  │
 └───────────────────────────────┬──────────────────────────────────────────┘
                                 │ AnalysisResult (JSON)
                                 ▼
 ┌──────────────────────────────────────────────────────────────────────────┐
 │ TIER 4 · SYNTHESIS                                        LLM (7-14B)    │
 │ Evidence-grounded prose with citations; refuses to add facts not in the  │
 │ AnalysisResult; emits follow-up suggestions that map back to QueryPlans  │
 └──────────────────────────────────────────────────────────────────────────┘

 Session store (disk): QueryPlan → ScoredSubgraph → AnalysisResult → Answer.
 A follow-up question re-enters at the lowest tier whose inputs changed.
```

### Data contracts between tiers

Each tier is a Python function with a pydantic model in and out. This is what
makes the tiers independently testable and swappable.

```python
class QueryPlan(BaseModel):
    intent: Literal["find_candidates", "explain_mechanism", "compare",
                    "find_formulations", "predict_targets", "safety_check"]
    seeds: list[SeedEntity]          # {label: "Disease", node_key: "C0038362", surface: "stomatitis"}
    constraints: Constraints          # natural_product_only, max_phase >= 3, exclude_withdrawn, ...
    analysis_task: Literal["rank", "classify", "cluster", "none"]
    follow_up_of: str | None          # session id of the QueryPlan this refines

class ScoredSubgraph(BaseModel):
    session_id: str
    node_ids: dict[str, list[int]]    # per node label → Neo4j internal ids
    edge_index: dict[str, ...]        # per (src, rel, dst) → pairs
    node_relevance: dict[int, float]  # GNN relevance to the task
    predicted_edges: list[PredictedEdge]   # from the link predictor, score ≥ threshold
    embeddings_path: Path             # .pt with per-node vectors
    provenance: PruningTrace          # what was kept, dropped, and why

class AnalysisResult(BaseModel):
    task: str
    candidates: list[Candidate]       # node id, name, label, score, rank
    feature_attributions: dict[str, dict[str, float]]   # per candidate → feature → contribution
    model_card: ModelCard             # model type, training set, CV metric, date
    evidence: list[EvidencePath]      # concrete graph paths with PMIDs / sources
    caveats: list[str]                # e.g. "only 51 positive labels", "ChemBL mechanisms are test-only"
```

---

## 3. Tier 1: Intake SLM

### Job

Turn free text into a `QueryPlan`. Nothing else. The SLM does **not** write
Cypher, does not answer the question, and does not see the graph.

### Why a small model is enough here

Intake is a constrained extraction task: pick one of six intents, list the
entities mentioned, and fill a handful of boolean/numeric constraints. A 3-4B
instruction-tuned model with JSON-schema-constrained decoding does this
reliably, and it runs in well under a second on Apple Silicon. Candidates via
Ollama: `qwen2.5:3b-instruct`, `llama3.2:3b`, `phi4-mini`, `gemma3:4b`. Pick by
measuring intent accuracy on the evaluation set in section 9, not by reputation.

### Entity linking is deterministic, not generative

The SLM extracts *surface strings* ("turmeric", "TNF", "mouth sores"). Linking
those to graph nodes is a separate, non-LLM step, because an SLM will happily
invent a plausible-sounding ChemBL ID:

1. **Exact and normalised match** against a name index built from all node
   `name`/`pref_name`/`scientificName`/`synonyms` properties (the ChemBL
   `synonyms` column alone gives ~10 aliases per drug).
2. **Fuzzy match** (rapidfuzz, token-set ratio) for spelling variants and
   binomial-vs-common plant names (the medplant CSV has a `Common Name` column
   for this).
3. **Embedding nearest-neighbour** over node names with a small sentence
   encoder (`all-MiniLM-L6-v2` or `BioLORD`) for paraphrases like "mouth sores
   from chemo" → `Oral mucositis`. This is the Neo4j vector index the
   `src/RAG/retrieval/docs/retrieval-info.md` doc already describes.
4. If a surface string links to multiple node labels (e.g. "quercetin" is both
   a `Compound` from IMPPAT and possibly a `Drug` from ChemBL, joined by
   `SAME_AS`), keep all of them as seeds. Tier 2 handles the merge.

Unlinked entities are returned to the user as a clarification ("I couldn't
find 'X' in the graph. Did you mean …?") rather than silently dropped. This is
the first place the back-and-forth requirement is met.

### Deliverables

- `src/intake/` — `router.py` (Ollama call with JSON schema), `linker.py`
  (name index + fuzzy + vector), `schemas.py` (`QueryPlan`).
- A name index builder that runs after every Neo4j import and writes
  `data/processed/node_name_index.parquet`.
- 60-100 hand-written question → `QueryPlan` pairs for evaluation (section 9).

---

## 4. Tier 2: Subgraph extraction and GNN structural pruning

This is the tier the presentation sketch describes as "shrink the knowledge
graph to discrete relevant sections using GNNs". It has a cheap classical stage
and a learned stage, and the classical stage ships first.

### 4a. Seed expansion (classical, ships first)

From the `QueryPlan` seeds, pull a candidate region from Neo4j:

- **k-hop expansion** with k=3 along a whitelist of relationship types that
  matter for the intent. For `find_candidates` on a disease the chain is
  `Disease ← BIOMARKER|EXPRESSION_ASSOCIATION|VARIANT_ASSOCIATION ← Gene
  ← TRANSLATION → Protein ← TARGETS ← Drug|Compound ← PRODUCES ← Plant
  ← CONTAINS ← Formulation`. For `safety_check` it instead follows
  `HAS_WARNING`, `METABOLIZED_BY`, `CATEGORY`.
- **Personalized PageRank (PPR)** from the seeds (Neo4j GDS `pageRank` with
  `sourceNodes`, or NetworkX on the exported graph) to rank the k-hop region.
  PPR is the standard non-learned answer to "which nodes are structurally close
  to these seeds", and it gives a defensible baseline to beat.
- Hard cap the region (e.g. top 3,000 nodes by PPR) so the GNN stage runs in
  milliseconds.

On this graph a 3-hop region around `Oral mucositis` is a few hundred to low
thousands of nodes. The bottleneck is hub nodes: `TNF`, `IL6`, `Inflammation`
and a handful of promiscuous proteins connect to thousands of compounds via the
60K-row PubChem interaction table. PPR damps these, but the learned stage is
what really handles them.

### 4b. GNN relevance scoring (learned)

Two different GNN uses, sharing one trained encoder:

**Use 1: node relevance for pruning.** Train a heterogeneous GNN (the R-GCN
from the week plan, or HGT) to predict, for each node in a k-hop region, whether
it lies on a *validated* path from a seed to a known positive outcome. Positives
come from paths that end at known `Drug -[TREATS]-> Disease` or
`Drug -[TREATS_INDICATION]-> Indication` edges; negatives are nodes in the
region that lie on no such path. At inference, the node relevance score decides
what to keep. This is "structural pruning": the GNN learns that `CYP3A4` is
connected to everything but rarely explains a treatment, while `PTGS2` is a
smaller hub that often does.

**Use 2: predicted edges.** The link predictor from the week plan scores
Compound→Gene/Protein pairs that lack a `TARGETS` edge. Predictions above a
threshold are added to the subgraph as `PREDICTED_TARGETS` with the score as a
property. This is where the network finds things the source databases never
recorded, which is the whole repurposing premise.

**Explainability.** PyG's `GNNExplainer` / `PGExplainer` returns the edge mask
that most influenced a prediction. Store it in `PruningTrace` so Tier 4 can say
*why* a node survived pruning, not just that it did.

### 4c. Pruning to a budget

Given node relevance, PPR score, and predicted edges:

1. Always keep seeds and their direct neighbours.
2. Keep nodes in descending relevance until the node budget is hit.
3. Drop edges whose endpoints were dropped; drop nodes left isolated.
4. Always keep at least one full evidence path per surviving candidate
   (candidate → target → gene → disease) so Tier 4 can cite it.
5. Record every drop with its reason in `PruningTrace`.

Budgets are intent-dependent. `explain_mechanism` for one compound wants a
small, deep subgraph (≤ 100 nodes, all relationship types). `find_candidates`
wants a wide, shallow one (≤ 500 nodes, only the treatment chain).

### Deliverables

- `src/gnn/export_graph.py` and `src/gnn/train_link_prediction.py` — already
  planned for the Sept 1 week; unchanged.
- `src/gnn/train_relevance.py` — the node-relevance head (new).
- `src/subgraph/` — `expand.py` (k-hop + PPR), `prune.py` (budgeted pruning),
  `schemas.py` (`ScoredSubgraph`, `PruningTrace`).
- Cached subgraphs in `data/sessions/<session_id>/subgraph.pt`.

---

## 5. Tier 3: Analysis with classical ML and small models

### What "analyze the subsections" concretely means

Each intent maps to one supervised or unsupervised task on a **feature table
built from the pruned subgraph**. The table has one row per candidate node and
columns drawn from three sources:

| Feature group | Examples | Source |
|---|---|---|
| Molecular descriptors | molecular_weight, alogp, hba, hbd, psa, rtb, ro5_violations, aromatic_rings, qed_weighted, natural_product | `chembl_approved_drugs.csv` (Drug); PubChem descriptor fetch for Compound (open question in the July plan, now required) |
| Graph-structural | degree per relationship type, PPR score, GNN relevance, shortest path length to each seed, number of distinct evidence paths, number of distinct source DBs supporting the path | Computed on the subgraph |
| Learned | 128-dim GNN node embedding (from the encoder in 4b) | `embeddings_path` |
| Evidence quality | max/mean DisGeNET `gdaScore` on the path, PMID count, whether a `TARGETS` edge is observed vs `PREDICTED_TARGETS` | Edge properties |

### Models per task

| Intent | Task | Model | Why this model |
|---|---|---|---|
| `find_candidates` | Rank candidate Drugs/Compounds for a disease | Gradient-boosted trees or random forest | Handles mixed numeric/categorical features, gives per-feature importances for Tier 4 to narrate, robust with few hundred rows |
| `predict_targets` | Classify Compound→Protein pairs as likely interaction | SVM (RBF) on [compound descriptors ‖ protein embedding] or the GNN link predictor directly | SVM is a strong small-data baseline; compare against the GNN's AUC |
| `explain_mechanism` | Group a compound's targets into pathway-like clusters | k-means or HDBSCAN on GNN embeddings of the target nodes | Unsupervised; no labels needed; clusters become paragraphs in the answer |
| `compare` | Score similarity between a phytochemical and an approved drug | Cosine on GNN embeddings + Tanimoto on RDKit fingerprints | Two independent views (structural, graph-contextual); disagreement is itself informative |
| `safety_check` | Flag warnings/toxicity classes for a candidate | Rule lookup over `HAS_WARNING`, `CATEGORY`, `METABOLIZED_BY` edges; no ML | Labels are sparse and the stakes favour transparency |
| any | Re-score the ranked list with a small MLP over all feature groups | 2-layer MLP, dropout, early stopping | Only once the tree model is a proven baseline; the MLP must beat it on held-out data to be kept |

### The label problem, stated plainly

Supervised models need positives. This graph's OM-specific labels are small:

| Label source | Rows today | Use |
|---|---|---|
| DrugBank drug→target for OM drugs (`drugbank_drug_targets.csv`) | 18 | Positive Drug→Protein pairs |
| TTD drug→target genes (`ttd_drug_target_genes.csv`) | 3 | Positive Drug→Gene pairs |
| DisGeNET OM biomarkers / variants / expression | 51 / 35 / 7 | Gene→Disease positives (with `gdaScore`) |
| ChemBL drug→indication (`chembl_drug_indications.csv`) | 79 (test run; ~2,500 expected after full scrape) | Drug→Disease positives across *all* diseases |
| ChemBL mechanisms / targets | 10 / 43 (test run) | Drug→Target positives across all diseases |
| PubChem compound→target interactions | 60,521 | Compound→Gene/Protein positives, all diseases |

Two consequences drive the design:

1. **Train disease-agnostic, apply disease-specific.** The ranking model is
   trained on the task "given a (candidate, disease) pair and its subgraph
   features, is there a TREATS/INDICATED_FOR edge?" across every disease in
   ChemBL. OM is then just one disease at inference time. This is why the full
   ChemBL scrape in the week plan is a prerequisite for Tier 3, not a nice-to-have.
2. **Report label counts as caveats.** `AnalysisResult.caveats` must carry the
   positive count that trained each model, and Tier 4 must surface it. A ranking
   trained on 18 positives is a hypothesis generator, and the prose must say so.

### Cross-validation must be graph-aware

Random row splits leak: a drug appearing in the training fold and a near-identical
drug in the test fold inflates scores. Use **scaffold splits** for compounds
(RDKit Murcko scaffolds) and **disease-held-out splits** for the ranker (train on
all diseases but OM, test on OM). Report both.

### Deliverables

- `src/classical_ml/` — `features.py` (subgraph → feature table),
  `rank.py`, `classify.py`, `cluster.py`, `compare.py`, `safety.py`,
  `schemas.py` (`AnalysisResult`, `ModelCard`).
- Trained models under `data/models/<task>/<date>/` with a `model_card.json`.
- `requirements.txt` additions: `scikit-learn`, `rdkit`, `rapidfuzz`, `pydantic`.

---

## 6. Tier 4: Synthesis LLM

### Job

Turn an `AnalysisResult` into prose that a researcher can act on. It receives:
the original question, the `QueryPlan` (so it knows the intent), the ranked
candidates with attributions, the evidence paths with PMIDs, the model card,
and the caveats. It does **not** receive the raw subgraph.

### Constraints on the model

- **Closed-world prompting.** The system prompt from
  `local-llm-implementation-plan.md` already says "ONLY use information from
  the provided context." Enforce it: a post-generation check extracts every
  entity name and PMID from the answer and verifies each appears in the
  `AnalysisResult`. Unverifiable claims are flagged inline or the paragraph is
  regenerated.
- **Structured sections.** Candidates, mechanism, evidence strength, caveats,
  suggested follow-ups. The follow-ups are emitted as `QueryPlan` stubs so the
  UI can offer them as one-click refinements.
- **Model size.** 7-14B via Ollama (`llama3.1:8b`, `qwen2.5:14b`,
  `mistral-nemo:12b`). A biomedical-tuned model (BioMistral-7B, Meditron) is
  worth a comparison run but is not assumed better: it only needs to write
  clearly about evidence it is handed, not recall biomedicine from weights.

### Deliverables

- `src/RAG/synthesis/` — `prompts.py`, `generate.py`, `verify.py`
  (closed-world check).
- Extends the existing `src/RAG/` slice rather than adding a new one.

---

## 7. Orchestration and the back-and-forth loop

### Keep it a Python pipeline, not a framework

Four functions and a session store. LangChain/LlamaIndex add abstraction the
project does not need yet, and they make the per-tier artifacts harder to
inspect. Revisit if a UI needs streaming or tool-calling.

```python
def answer(question: str, session: Session | None) -> Answer:
    plan = intake.route(question, session)              # Tier 1
    if plan.needs_clarification:
        return Answer.clarify(plan)
    subgraph = subgraph.get_or_build(plan, session)     # Tier 2, cached by seed set + intent
    result = classical_ml.analyze(plan, subgraph)       # Tier 3
    return synthesis.write(question, plan, result)      # Tier 4
```

### What "discussion" means mechanically

A session is a directory under `data/sessions/<id>/` holding every artifact.
A follow-up question is routed with the previous `QueryPlan` as context, and
the pipeline re-enters at the lowest tier whose inputs changed:

| Follow-up | Re-runs from |
|---|---|
| "Only natural products" | Tier 3 (same subgraph, new constraint filter) |
| "Why is curcumin ranked third?" | Tier 4 only (attributions already in `AnalysisResult`) |
| "What about stomatitis instead?" | Tier 2 (new seed, but `Stomatitis` and `Oral mucositis` share most genes, so the cache hit rate on the k-hop region is high) |
| "Which of these are in Triphala?" | Tier 2 with a `Formulation` seed added, then Tier 3 |

This is the concrete answer to the presentation's "allows back and forth
discussion" point: the graph work is done once, and refinements are cheap.

### Interfaces

- CLI first (`python -m src.pipeline ask "…" --session <id>`), matching the
  existing pattern of runnable modules.
- A thin FastAPI wrapper later so the Vercel frontend can call it. Every
  response includes the `session_id` and the artifact paths for a debug view.

---

## 8. Data readiness

What the tiers need from the graph, and the current state:

| Requirement | Tier | Status | Action |
|---|---|---|---|
| Full ChemBL mechanisms, targets, indications (not the 10-record test set) | 2, 3 | Missing (flagged #1 gap in `bridging-the-gap.md`) | Run `chembl_scraper.py` full; 8-12 h unattended |
| Molecular descriptors for IMPPAT Compounds | 3 | Missing (only `pubchemId`) | Add a PubChem descriptor fetch to `src/scrapers/pubchem/` keyed on the 921 mapped IDs; ~1 h with rate limits |
| `SAME_AS` edges between ChemBL Drugs and IMPPAT Compounds | 2 | Partial (`src/integration/chembl_imppat_mapper.py` exists) | Verify coverage; InChIKey match is the right join key and both sides have it |
| Node name index for entity linking | 1 | Missing | Build from Neo4j after import |
| Neo4j GDS plugin (for PPR) | 2 | Unknown | Install via Neo4j Desktop, or use NetworkX on the export |
| Evidence properties on edges (`pmid`, `gdaScore`, `evidences`, `source`) | 3, 4 | Present | None |
| Formulation → Plant data | 2 | Thin | Out of scope for this plan; note as a caveat |

Volumes today, from `data/processed/`:

```
┌────────────────────────────────────────────┬─────────┐
│ File                                       │ Rows    │
├────────────────────────────────────────────┼─────────┤
│ pubchem_phytochem_target_interactions.csv  │ 60,521  │
│ chembl_drug_metabolism.csv                 │ 10,000  │
│ chembl_approved_drugs.csv                  │  3,276  │
│ medicinal_plants_with_uses.csv             │  1,915  │
│ phytochem_imppatid_pubchem_id_url.csv      │    921  │
│ chembl_drug_indications.csv (test run)     │     79  │
│ disgenet__OM_biomarkers.csv                │     51  │
│ chembl_drug_targets.csv (test run)         │     43  │
│ disgenet__OM_genvars.csv                   │     35  │
│ drugbank_drug_targets.csv                  │     18  │
│ chembl_drug_mechanisms.csv (test run)      │     10  │
└────────────────────────────────────────────┴─────────┘
```

---

## 9. Evaluation, per tier

Each tier gets its own metric and its own small gold set, so regressions are
localised.

| Tier | Gold set | Metric | Baseline to beat |
|---|---|---|---|
| 1 Intake | 60-100 hand-written questions with expected `QueryPlan` | Intent accuracy; entity linking precision/recall | Keyword rules from `QUERY_PATTERNS` in the July plan |
| 2 Pruning | For each known OM drug (DrugBank/TTD), does its evidence path survive pruning at the default budget? | Recall of known-positive paths at budget N; subgraph size | PPR-only pruning (no GNN) |
| 2 Link prediction | Held-out `TARGETS` edges (already in the week plan) | AUC-ROC, MRR, Hits@10 | Random; shortest-path heuristic |
| 3 Ranking | Disease-held-out: train on all ChemBL indications except OM, rank OM candidates | Where do the known OM drugs (palifermin, benzydamine, etc.) land? Mean rank, Hits@20 | PPR score alone; degree alone |
| 4 Synthesis | 20 `AnalysisResult`s, answers reviewed by a domain expert (the presentation's stated need) | Closed-world violation rate (automated); expert rubric: correct, useful, appropriately hedged (manual) | Single-LLM GraphRAG from the July plan on the same inputs |
| End-to-end | The C. difficile and OM `disease-explorer` reports | Overlap between top-10 candidates from this pipeline and the consensus reports; token and wall-clock cost | The `disease-explorer` run itself |

The end-to-end comparison is the one to show Adam Duerfeldt: same question, one
answer from the token-heavy Claude pipeline, one from the local network, side
by side, with cost.

---

## 10. Roadmap

The Sept 1 week plan (export + link predictor) is Phase A here. Phases are
ordered by dependency; several can overlap.

| Phase | Deliverable | Depends on | Effort | Exit criterion |
|---|---|---|---|---|
| **A** GNN foundation | `export_graph.py`, `train_link_prediction.py`, predictions CSV | Full ChemBL scrape running in parallel | 1 week (the existing week plan) | AUC beats shortest-path baseline |
| **B** Classical pruning | `src/subgraph/expand.py` + `prune.py` with PPR, no GNN | Neo4j export from A | 2-3 days | Known OM drug paths survive at budget 500 |
| **C** Intake | `src/intake/` with SLM router + deterministic linker + gold set | Name index from Neo4j | 3-4 days | ≥ 90% intent accuracy on gold set |
| **D** Ranker | `src/classical_ml/features.py` + `rank.py` with disease-held-out CV | A (embeddings), B (subgraph), full ChemBL, PubChem descriptors | 1 week | Known OM drugs in top-20 on held-out OM |
| **E** Synthesis + verify | `src/RAG/synthesis/` with closed-world check | D | 3-4 days | Zero unverifiable entities on 20 test results |
| **F** Orchestrator + sessions | `src/pipeline/` CLI, session store, re-entry logic | C, D, E | 3-4 days | Follow-up questions re-run only the changed tiers |
| **G** GNN relevance pruning | `train_relevance.py`, swap into `prune.py` | A, B, D (for labels) | 1 week | Beats PPR-only on path recall at equal budget |
| **H** Remaining Tier 3 tasks | `classify.py`, `cluster.py`, `compare.py`, `safety.py`, MLP re-scorer | D | 1 week | Each ships with a model card and beats its baseline |
| **I** API + frontend hookup | FastAPI wrapper, debug view of artifacts | F | 3-4 days | Vercel frontend can drive a session |
| **J** Expert review | 20 answers in front of a domain expert | E, F | External | Rubric scores recorded; prompt/feature fixes filed |

Phases B and C have no dependency on each other or on A's *training* (only its
export), so they can run while the GNN trains. Realistic total: 6-8 weeks of
part-time work to Phase F, with G-J following.

---

## 11. Module layout (vertical slices)

```
src/
├── intake/            # Tier 1: router.py, linker.py, schemas.py, gold/questions.jsonl
├── gnn/               # Tier 2 learned parts: export_graph.py, train_link_prediction.py,
│                      #   train_relevance.py, explain.py, models/
├── subgraph/          # Tier 2 extraction + pruning: expand.py, prune.py, schemas.py
├── classical_ml/      # Tier 3: features.py, rank.py, classify.py, cluster.py,
│                      #   compare.py, safety.py, schemas.py
├── RAG/
│   ├── retrieval/     # existing: vector index + Cypher retrieval docs
│   └── synthesis/     # Tier 4: prompts.py, generate.py, verify.py
├── pipeline/          # orchestrator: answer.py, session.py, cli.py, api.py
└── scrapers/pubchem/  # add: descriptors.py (molecular descriptors for Compounds)

data/
├── models/<task>/<date>/         # trained sklearn/torch models + model_card.json
├── sessions/<session_id>/        # QueryPlan, subgraph.pt, analysis.json, answer.md
└── processed/node_name_index.parquet
```

Each slice owns its schemas and can be run and tested alone. The orchestrator is
the only module that imports from more than one slice.

---

## 12. Risks and open questions

- **Label scarcity is the dominant risk.** Everything in Tier 3 hinges on the
  full ChemBL indication and mechanism data. If the scrape stalls, Tier 3 ships
  as PPR + rule-based ranking with an explicit "unsupervised" caveat.
- **Hub nodes.** `TNF`, `IL6`, `CYP3A4` and similar connect to a large share of
  the graph. PPR damping and the GNN relevance head are the mitigations; if
  neither suffices, per-relationship-type degree normalisation on edges is the
  next lever.
- **Compound descriptor coverage.** Only 921 IMPPAT compounds have PubChem IDs
  mapped. Compounds without descriptors get imputed or graph-only features and a
  per-row caveat.
- **SLM JSON reliability.** Constrained decoding (Ollama `format` with a JSON
  schema) mostly solves this. Keep a retry-with-repair path and log failures.
- **Closed-world enforcement vs. readability.** Strict verification can make
  answers stilted. Allow the LLM general biomedical framing sentences, but
  require every named entity, number, and citation to be verifiable.
- **Apple Silicon and PyG.** Confirm `torch-geometric` installs and runs on the
  MPS backend before Phase A; fall back to CPU (the graph is small enough).
- **Validation of novel predictions.** A `PREDICTED_TARGETS` edge with score
  0.9 is still a hypothesis. The literature-review step from the
  `disease-explorer` pipeline is the natural downstream check, and could itself
  become a Tier 3 task later (retrieve abstracts, classify support/refute).
- **Biomedical vs. general LLM for Tier 4.** Undecided; run the comparison in
  Phase E on the same 20 inputs.

---

## 13. How this changes the existing plans

- `docs/todos/2026-07-27-local-llm-todo.md`: Part 1 (GNN) stands; Part 2
  (local LLM) is now split into Tier 1 and Tier 4; Part 3 (subgraph splitting)
  becomes Tier 2 and gains the GNN relevance head.
- `docs/notes/local-llm-implementation-plan.md`: its Cypher templates move into
  `src/subgraph/expand.py` as intent-specific expansion patterns; its prompts
  move into `src/RAG/synthesis/prompts.py`; its `QUERY_PATTERNS` keyword rules
  become the Tier 1 baseline.
- `docs/next-steps/2026-09-01-week-plan.md`: unchanged; it is Phase A.
