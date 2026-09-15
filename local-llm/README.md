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
