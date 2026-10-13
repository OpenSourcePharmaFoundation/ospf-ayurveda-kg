"""GNN slice: Neo4j → PyG export, heterogeneous link prediction, evaluation, prediction.

Phase A of ``local-llm/local-ai-network-plan.md``.

Modules
-------
schema                 GraphTables intermediate + HeteroData builder
export_graph           Neo4j (or CSV mirror) → local-llm/data/graph/graph_heterodata.pt
model                  Heterogeneous GraphSAGE encoder + edge decoder
evaluate               AUC / MRR / Hits@K and non-learned baselines
train_link_prediction  Train, early-stop, evaluate, write model card
predict                Score missing edges → local-llm/data/predictions/gnn_predicted_targets.csv
"""
