# Local LLM Subproject

Home for the local AI network: a small language model for query intake, GNN-based
subgraph pruning, classical ML analysis, and a local LLM for synthesis, all running
against the Neo4j knowledge graph without cloud calls.

## Documents here

- [`local-ai-network-plan.md`](local-ai-network-plan.md) — the comprehensive plan:
  four-tier architecture, data contracts, per-tier evaluation, roadmap, module layout.

## Related documents elsewhere in the repo

- `docs/todos/2026-07-27-local-llm-todo.md` — original GNN + local LLM plan and library choices
- `docs/notes/local-llm-implementation-plan.md` — single-LLM GraphRAG design (Cypher templates, prompts)
- `docs/next-steps/2026-09-01-week-plan.md` — GNN export and link-prediction week (Phase A of the plan)
- `docs/notes/gnn-message-passing.md` — how message passing works on this graph
- `docs/glossary-llm.md` — LLM and graph ML terminology
- `docs/presenting-for-adam-duerfeldt.md` — presentation notes that motivated this direction
- `src/RAG/retrieval/docs/retrieval-info.md` — GraphRAG retrieval strategies

## Code

Code for the subproject lives here, one vertical slice per tier (see section 11
of the plan for the full layout): `gnn/` today, with `intake/`, `subgraph/`,
`classical_ml/`, `synthesis/` and `pipeline/` to follow. Scripts read the
repo-level `data/processed/` inputs and write everything they produce under
`local-llm/data/`.

Run scripts from the repo root with the project venv:

```bash
source ./venv/bin/activate

# Phase A — GNN foundation
python local-llm/gnn/export_graph.py                  # Neo4j if NEO4J_PASSWORD is set, else CSV mirror
python local-llm/gnn/export_graph.py --validate       # reload the saved graph and print counts
python local-llm/gnn/train_link_prediction.py         # Compound -[TARGETS]-> Gene, with baselines
python local-llm/gnn/predict.py                       # rank unobserved pairs → data/predictions/
python local-llm/gnn/predict.py --pair Curcumin TNF   # score one named pair
```

| Path | What |
|---|---|
| `gnn/schema.py` | `GraphTables` intermediate, feature standardisation, `HeteroData` builder |
| `gnn/export_graph.py` | `Neo4jSource` (schema-agnostic) and `CsvSource` (mirrors the Cypher import scripts) |
| `gnn/model.py` | Hetero GraphSAGE encoder via `to_hetero` + dot / MLP edge decoder |
| `gnn/evaluate.py` | AUC, AP, MRR, Hits@K; random, degree and shortest-path baselines |
| `gnn/train_link_prediction.py` | 80/10/10 `RandomLinkSplit`, early stopping, model card |
| `gnn/predict.py` | Batch scoring of missing edges; single-pair queries |
| `data/graph/` | `graph_heterodata.pt` + `graph_node_index.csv` (tensor row → name / external id) |
| `data/models/link_prediction/<run>/` | `model.pt`, `embeddings.pt`, `metrics.json`, `training_curve.csv`, `model_card.json` |
| `data/predictions/` | `gnn_predicted_targets.csv` |

`data/models/` and the `.pt` graph file are regenerable and git-ignored; the
node index and prediction CSVs are kept.

### Phase A status (2026-09-14)

Built and run end to end against the CSV mirror of the graph (Neo4j was not
running; re-run `export_graph.py` with `NEO4J_PASSWORD` set to export the live
database instead). Graph: 25,200 nodes, 113,106 edges, 14 node types, 19
relationship types.

Test-set results, each true edge ranked against 100 sampled non-edges of the
same compound:

| Target edge | Positives | Model | MRR | Hits@10 | AUC |
|---|---|---|---|---|---|
| Compound → Gene | 44,613 | GNN | **0.232** | **0.377** | 0.716 |
| | | degree heuristic | 0.232 | 0.374 | 0.838 |
| | | shortest path | 0.030 | 0.011 | 0.589 |
| | | random | 0.052 | 0.098 | 0.492 |
| Compound → Protein | 1,605 | GNN | **0.174** | **0.350** | 0.524 |
| | | degree heuristic | 0.167 | 0.325 | 0.868 |
| | | shortest path | 0.090 | 0.219 | 0.634 |

The Phase A exit criterion (beat the shortest-path baseline) is met for both
edge types. The more honest comparison is against the degree heuristic, which
the GNN only ties. Two things explain that and both are data, not model:

- **Sparse genes.** 15.6K genes share 44.6K edges, so most genes have one or two
  edges and no structure to learn from. A held-out edge to such a gene is
  unpredictable except through popularity.
- **Global AUC is misleading here.** Most of the 921 compounds have no
  interactions at all, so random negative pairs are trivially separable by
  "does this compound have any edges"; the degree heuristic scores 0.84 AUC
  for that reason. Model selection therefore uses validation MRR, not AUC.

What would move the numbers: the full ChemBL scrape (mechanisms, targets,
indications) and PubChem descriptors for the 921 compounds, both already on the
data-readiness list in the plan. The pipeline is ready to re-run on the richer
graph without code changes.

### Reading the predictions

`data/predictions/gnn_predicted_targets.csv` holds the 5,000 highest-scoring
unobserved Compound → Gene pairs. Because the model has learned gene popularity,
the global list concentrates on hub genes (CAT, TNF, CASP3, PTGS2, IL6). For a
per-compound hit list use `--per-source-top 25`, which spreads across ~150
genes. Compounds with no known interactions get scores driven purely by the
gene side; treat those rows as priors, not predictions. Every score is a
hypothesis for literature checking, as the model card's caveats say.
