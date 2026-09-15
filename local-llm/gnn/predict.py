"""Score unobserved edges with a trained link predictor.

Batch mode (default) scores every (src, dst) pair of the model's target edge type
that has no edge in the graph and writes the top-ranked ones to CSV:

    python local-llm/gnn/predict.py                                 # latest model, top 5000
    python local-llm/gnn/predict.py --top-k 20000 --per-source-top 50
    python local-llm/gnn/predict.py --model local-llm/data/models/link_prediction/<run>/model.pt

Single-pair mode scores named pairs (case-insensitive name match):

    python local-llm/gnn/predict.py --pair Curcumin TNF --pair Quercetin IL6
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd
import torch
import torch_geometric.transforms as T

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from gnn.model import HeteroLinkPredictor  # noqa: E402
from gnn.schema import load_graph  # noqa: E402

SUBPROJECT = Path(__file__).resolve().parents[1]  # local-llm/
REPO_ROOT = SUBPROJECT.parent
DEFAULT_GRAPH = SUBPROJECT / "data" / "graph" / "graph_heterodata.pt"
MODELS_DIR = SUBPROJECT / "data" / "models" / "link_prediction"
DEFAULT_OUT = SUBPROJECT / "data" / "predictions" / "gnn_predicted_targets.csv"


def latest_model() -> Path:
    runs = sorted(p for p in MODELS_DIR.glob("*/model.pt"))
    if not runs:
        sys.exit(
            f"no trained model under {MODELS_DIR}; run train_link_prediction first"
        )
    return runs[-1]


def load(model_path: Path, graph_path: Path):
    raw, node_index = load_graph(graph_path)
    data = T.ToUndirected()(raw)
    ckpt = torch.load(model_path, weights_only=False)
    model = HeteroLinkPredictor.from_checkpoint(ckpt, data)
    edge_type = tuple(ckpt["target_edge"])
    with torch.no_grad():
        z = model.encode(data)
    return model, data, node_index, edge_type, z


def _names(node_index: pd.DataFrame, label: str) -> pd.DataFrame:
    df = (
        node_index[node_index.label == label]
        .sort_values("index")
        .reset_index(drop=True)
    )
    assert (df["index"].to_numpy() == range(len(df))).all()
    return df


@torch.no_grad()
def batch_predict(
    model,
    data,
    node_index,
    edge_type,
    z,
    top_k: int,
    per_source_top: int | None,
    min_score: float,
) -> pd.DataFrame:
    src_t, rel, dst_t = edge_type
    logits = model.decoder.score_all(z[src_t], z[dst_t])  # [num_src, num_dst]
    known = data[edge_type].edge_index
    logits[known[0], known[1]] = float("-inf")  # only unobserved pairs
    probs = torch.sigmoid(logits)

    if per_source_top:
        k = min(per_source_top, probs.size(1))
        vals, idx = probs.topk(k, dim=1)
        src = torch.arange(probs.size(0)).unsqueeze(1).expand_as(idx).reshape(-1)
        dst, score = idx.reshape(-1), vals.reshape(-1)
    else:
        flat = probs.reshape(-1)
        k = min(top_k, flat.numel())
        score, flat_idx = flat.topk(k)
        src, dst = flat_idx // probs.size(1), flat_idx % probs.size(1)

    keep = torch.isfinite(score) & (score >= min_score)
    src, dst, score = src[keep], dst[keep], score[keep]
    order = score.argsort(descending=True)[:top_k]
    src, dst, score = src[order], dst[order], score[order]

    s_names, d_names = _names(node_index, src_t), _names(node_index, dst_t)
    out = pd.DataFrame(
        {
            "rank": range(1, len(score) + 1),
            "source_label": src_t,
            "source_name": s_names.loc[src.numpy(), "name"].to_numpy(),
            "source_id": s_names.loc[src.numpy(), "external_id"].to_numpy(),
            "relation": f"PREDICTED_{rel}",
            "target_label": dst_t,
            "target_name": d_names.loc[dst.numpy(), "name"].to_numpy(),
            "target_id": d_names.loc[dst.numpy(), "external_id"].to_numpy(),
            "score": score.numpy().round(4),
            "source_index": src.numpy(),
            "target_index": dst.numpy(),
        }
    )
    return out


@torch.no_grad()
def score_pairs(
    model, data, node_index, edge_type, z, pairs: list[tuple[str, str]]
) -> pd.DataFrame:
    src_t, rel, dst_t = edge_type
    s_names, d_names = _names(node_index, src_t), _names(node_index, dst_t)
    s_lookup = {n.lower(): i for i, n in zip(s_names["index"], s_names["name"])}
    d_lookup = {n.lower(): i for i, n in zip(d_names["index"], d_names["name"])}
    known = set(map(tuple, data[edge_type].edge_index.t().tolist()))
    rows = []
    for s, d in pairs:
        si, di = s_lookup.get(s.lower()), d_lookup.get(d.lower())
        if si is None or di is None:
            rows.append(
                {
                    "source": s,
                    "target": d,
                    "score": None,
                    "known_edge": None,
                    "note": f"not found: {'source' if si is None else ''} {'target' if di is None else ''}".strip(),
                }
            )
            continue
        logit = model.decoder(z[src_t], z[dst_t], torch.tensor([[si], [di]]))
        rows.append(
            {
                "source": s_names.loc[si, "name"],
                "target": d_names.loc[di, "name"],
                "score": round(float(torch.sigmoid(logit)), 4),
                "known_edge": (si, di) in known,
                "note": "",
            }
        )
    return pd.DataFrame(rows)


def main(argv=None):
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument(
        "--model", type=Path, default=None, help="model.pt (default: latest run)"
    )
    ap.add_argument("--graph", type=Path, default=DEFAULT_GRAPH)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--top-k", type=int, default=5000)
    ap.add_argument(
        "--per-source-top",
        type=int,
        default=None,
        help="keep the top N targets per source node instead of a global top-k",
    )
    ap.add_argument("--min-score", type=float, default=0.0)
    ap.add_argument(
        "--pair", nargs=2, action="append", metavar=("SRC_NAME", "DST_NAME")
    )
    args = ap.parse_args(argv)

    model_path = args.model or latest_model()
    model, data, node_index, edge_type, z = load(model_path, args.graph)
    print(f"model: {model_path}\ntarget edge: {edge_type}")

    if args.pair:
        df = score_pairs(
            model, data, node_index, edge_type, z, [tuple(p) for p in args.pair]
        )
        print(df.to_string(index=False))
        return

    df = batch_predict(
        model,
        data,
        node_index,
        edge_type,
        z,
        args.top_k,
        args.per_source_top,
        args.min_score,
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(args.out, index=False)
    print(f"wrote {len(df):,} predicted {edge_type[1]} edges to {args.out}")
    print(
        df.head(15)[["rank", "source_name", "target_name", "score"]].to_string(
            index=False
        )
    )


if __name__ == "__main__":
    main()
