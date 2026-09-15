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

Code for the subproject lives under `src/` as vertical slices (`intake/`, `gnn/`,
`subgraph/`, `classical_ml/`, `RAG/synthesis/`, `pipeline/`); see section 11 of the plan.
