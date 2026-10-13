"""Train and evaluate heterogeneous link prediction on one relationship type.

Default task: predict ``Compound -[TARGETS]-> Gene`` edges. Edges are split
80/10/10 with PyG's ``RandomLinkSplit`` (reverse edges removed alongside, so no
leakage through message passing). Training negatives are resampled every epoch
as (same compound, random gene) pairs; val/test negatives are fixed 1:1 samples.

Model selection uses validation MRR (each true edge ranked against sampled
non-edges of the *same source node*), not AUC: on this graph most compounds have
no interactions at all, so global AUC mostly measures "does this compound have
any edges" and a degree heuristic scores ~0.84 on it. Per-source ranking is the
metric that reflects the repurposing question ("which genes does compound X hit").

Usage
-----
    python local-llm/gnn/train_link_prediction.py                      # defaults below
    python local-llm/gnn/train_link_prediction.py --target-edge Compound TARGETS Protein
    python local-llm/gnn/train_link_prediction.py --decoder dot --no-degree   # ablation

Writes ``local-llm/data/models/link_prediction/<date>_<src>_<rel>_<dst>/`` with
``model.pt``, ``metrics.json``, ``training_curve.csv``, ``model_card.json`` and
``embeddings.pt`` (per-node-type embeddings on the full graph, for Tier 3).
"""

from __future__ import annotations

import argparse
import copy
import json
import logging
import sys
import time
from datetime import date
from pathlib import Path

import pandas as pd
import torch
import torch.nn.functional as F
import torch_geometric.transforms as T

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from gnn import evaluate as ev  # noqa: E402
from gnn.model import HeteroLinkPredictor  # noqa: E402
from gnn.schema import load_graph  # noqa: E402

log = logging.getLogger("gnn.train")

SUBPROJECT = Path(__file__).resolve().parents[1]  # local-llm/
REPO_ROOT = SUBPROJECT.parent
DEFAULT_GRAPH = SUBPROJECT / "data" / "graph" / "graph_heterodata.pt"
MODELS_DIR = SUBPROJECT / "data" / "models" / "link_prediction"


def pick_device(name: str) -> torch.device:
    if name == "auto":
        return torch.device(
            "cuda" if torch.cuda.is_available() else "cpu"
        )  # MPS: scatter ops still patchy in PyG
    return torch.device(name)


def split_graph(data, edge_type, val_ratio, test_ratio, seed):
    rev = (edge_type[2], f"rev_{edge_type[1]}", edge_type[0])
    data = T.ToUndirected()(data)
    if edge_type not in data.edge_types:
        sys.exit(f"edge type {edge_type} not in graph; have: {data.edge_types}")
    torch.manual_seed(seed)
    split = T.RandomLinkSplit(
        num_val=val_ratio,
        num_test=test_ratio,
        disjoint_train_ratio=0.0,
        neg_sampling_ratio=1.0,
        add_negative_train_samples=False,
        edge_types=[edge_type],
        rev_edge_types=[rev],
    )
    train, val, test = split(data)
    return data, train, val, test


def sample_train_negatives(
    pos: torch.Tensor, num_dst: int, ratio: int, gen: torch.Generator
) -> torch.Tensor:
    src = pos[0].repeat(ratio)
    dst = torch.randint(0, num_dst, (src.size(0),), generator=gen)
    return torch.stack([src, dst])


@torch.no_grad()
def eval_split(
    model, split_data, edge_type, known, num_dst, num_neg, max_pos, seed, device
) -> dict:
    """Classification metrics on the split's labelled pairs + ranking on (a sample of) its positives."""
    model.eval()
    z = {k: v.cpu() for k, v in model.encode(split_data.to(device)).items()}
    store = split_data[edge_type]
    eli, lab = store.edge_label_index.cpu(), store.edge_label.cpu()
    src_t, _, dst_t = edge_type

    def fn(s, d):
        return model.decoder(z[src_t], z[dst_t], torch.stack([s, d]).to(device)).cpu()

    out = ev.classification_metrics(fn(eli[0], eli[1]), lab)
    pos = eli[:, lab.bool()]
    if max_pos and pos.size(1) > max_pos:
        pos = pos[
            :,
            torch.randperm(pos.size(1), generator=torch.Generator().manual_seed(seed))[
                :max_pos
            ],
        ]
    out.update(ev.ranking_metrics(fn, pos, known, num_dst, num_neg=num_neg, seed=seed))
    return out, z


def train(args) -> Path:
    device = pick_device(args.device)
    torch.manual_seed(args.seed)
    gen = torch.Generator().manual_seed(args.seed)

    raw, node_index = load_graph(args.graph)
    edge_type = tuple(args.target_edge)
    full, train_data, val_data, test_data = split_graph(
        raw, edge_type, args.val_ratio, args.test_ratio, args.seed
    )
    src_t, rel, dst_t = edge_type
    num_dst = full[dst_t].num_nodes
    known = full[
        edge_type
    ].edge_index  # every true edge, so ranking negatives are real non-edges

    n_train = train_data[edge_type].edge_label_index.size(1)
    n_val = int(val_data[edge_type].edge_label.sum())
    n_test = int(test_data[edge_type].edge_label.sum())
    print(
        f"target edge {edge_type}: train={n_train:,} val={n_val:,} test={n_test:,} positives "
        f"({full[edge_type].edge_index.size(1):,} total)"
    )

    num_nodes = {nt: full[nt].num_nodes for nt in full.node_types}
    in_dims = {
        nt: (full[nt].x.size(1) if "x" in full[nt] else 0) for nt in full.node_types
    }
    model = HeteroLinkPredictor(
        full.metadata(),
        num_nodes,
        in_dims,
        args.hidden,
        args.layers,
        args.dropout,
        args.decoder,
        not args.no_degree,
    )
    with torch.no_grad():
        model.encode(train_data)  # lazy shape init
    model = model.to(device)
    train_data = train_data.to(device)
    opt = torch.optim.Adam(
        model.parameters(), lr=args.lr, weight_decay=args.weight_decay
    )
    n_params = sum(p.numel() for p in model.parameters())
    print(
        f"model: hetero GraphSAGE x{args.layers}, hidden={args.hidden}, decoder={args.decoder}, "
        f"degree_input={not args.no_degree}, params={n_params:,}, device={device}"
    )

    pos = train_data[edge_type].edge_label_index
    sel = args.select_metric
    curve, best, best_state, best_epoch, stale = [], float("-inf"), None, 0, 0
    t0 = time.time()
    for epoch in range(1, args.epochs + 1):
        model.train()
        opt.zero_grad()
        z = model.encode(train_data)
        neg = sample_train_negatives(pos.cpu(), num_dst, args.neg_ratio, gen).to(device)
        eli = torch.cat([pos, neg], dim=1)
        labels = torch.cat([torch.ones(pos.size(1)), torch.zeros(neg.size(1))]).to(
            device
        )
        logits = model.decode(z, edge_type, eli)
        loss = F.binary_cross_entropy_with_logits(logits, labels)
        loss.backward()
        opt.step()

        row = {"epoch": epoch, "train_loss": loss.item()}
        if epoch % args.eval_every == 0 or epoch == args.epochs:
            val_m, _ = eval_split(
                model,
                val_data,
                edge_type,
                known,
                num_dst,
                args.val_rank_negatives,
                args.val_rank_positives,
                args.seed,
                device,
            )
            row.update(
                {f"val_{k}": v for k, v in val_m.items() if isinstance(v, float)}
            )
            print(
                f"epoch {epoch:4d}  loss {loss.item():.4f}  val auc {val_m['auc']:.4f}  "
                f"val mrr {val_m['mrr']:.4f}  val hits@10 {val_m['hits@10']:.4f}  ({time.time() - t0:5.1f}s)"
            )
            if val_m[sel] > best:
                best, best_epoch, stale = val_m[sel], epoch, 0
                best_state = copy.deepcopy(model.state_dict())
            else:
                stale += 1
                if stale >= args.patience:
                    print(
                        f"early stop at epoch {epoch}; best val {sel} {best:.4f} @ epoch {best_epoch}"
                    )
                    curve.append(row)
                    break
        curve.append(row)

    if best_state is not None:
        model.load_state_dict(best_state)

    # ---- test: GNN vs baselines -------------------------------------------
    model.eval()
    test_store = test_data[edge_type]
    eli, lab = test_store.edge_label_index.cpu(), test_store.edge_label.cpu()
    with torch.no_grad():
        z_test = {k: v.cpu() for k, v in model.encode(test_data.to(device)).items()}

    def gnn_fn(s, d):
        return model.decoder(
            z_test[src_t], z_test[dst_t], torch.stack([s, d]).to(device)
        ).cpu()

    msg_graph = (
        test_data.cpu()
    )  # what any method may see at test time: train + val edges
    baselines = {
        "shortest_path": ev.shortest_path_baseline(msg_graph, edge_type),
        "degree": ev.degree_baseline(msg_graph, edge_type),
        "random": ev.random_baseline(args.seed),
    }
    results = {
        "gnn": ev.evaluate_score_fn(
            gnn_fn, eli, lab, known, num_dst, args.rank_negatives, args.seed
        )
    }
    for name, fn in baselines.items():
        results[name] = ev.evaluate_score_fn(
            fn, eli, lab, known, num_dst, args.rank_negatives, args.seed
        )

    print(
        f"\ntest set (positives ranked against {args.rank_negatives} sampled negatives each):"
    )
    print(ev.format_table(results))
    g, sp, dg = results["gnn"], results["shortest_path"], results["degree"]
    beats_sp = g["mrr"] > sp["mrr"] and g["hits@10"] > sp["hits@10"]
    beats_deg = g["mrr"] > dg["mrr"] and g["hits@10"] > dg["hits@10"]
    print(
        f"\nPhase A exit criterion — GNN beats shortest-path on MRR and Hits@10: {'PASS' if beats_sp else 'FAIL'}"
    )
    print(
        f"Stronger check           — GNN beats degree heuristic on MRR and Hits@10: {'PASS' if beats_deg else 'FAIL'}"
    )

    # ---- persist -----------------------------------------------------------
    out_dir = (
        args.out_dir or MODELS_DIR / f"{date.today().isoformat()}_{src_t}_{rel}_{dst_t}"
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    with torch.no_grad():
        z_full = {k: v.cpu() for k, v in model.encode(full.to(device)).items()}
    torch.save(
        model.cpu().checkpoint(
            target_edge=list(edge_type),
            graph_file=str(
                args.graph.relative_to(REPO_ROOT)
                if args.graph.is_absolute() and args.graph.is_relative_to(REPO_ROOT)
                else args.graph
            ),
        ),
        out_dir / "model.pt",
    )
    torch.save(z_full, out_dir / "embeddings.pt")
    pd.DataFrame(curve).to_csv(out_dir / "training_curve.csv", index=False)
    (out_dir / "metrics.json").write_text(
        json.dumps(
            {
                "test": results,
                "selection_metric": sel,
                "best_val": best,
                "best_epoch": best_epoch,
            },
            indent=2,
        )
    )
    card = {
        "task": "link_prediction",
        "target_edge": list(edge_type),
        "model": (
            f"HeteroLinkPredictor: {args.layers}-layer GraphSAGE via to_hetero (per-relation weights, sum aggr), "
            f"{args.decoder} decoder, log-degree input={'on' if not args.no_degree else 'off'}"
        ),
        "hidden": args.hidden,
        "params": n_params,
        "graph_file": str(args.graph),
        "graph_nodes": {nt: int(n) for nt, n in num_nodes.items()},
        "positives": {"train": n_train, "val": n_val, "test": n_test},
        "split": {
            "val_ratio": args.val_ratio,
            "test_ratio": args.test_ratio,
            "seed": args.seed,
            "method": "RandomLinkSplit, reverse edges removed",
        },
        "training": {
            "epochs_run": curve[-1]["epoch"],
            "best_epoch": best_epoch,
            "selection_metric": f"val_{sel}",
            "lr": args.lr,
            "weight_decay": args.weight_decay,
            "dropout": args.dropout,
            "neg_ratio": args.neg_ratio,
            "early_stopping_patience_evals": args.patience,
        },
        "metrics": {"best_val": {sel: best}, "test": results},
        "beats_shortest_path_baseline": bool(beats_sp),
        "beats_degree_baseline": bool(beats_deg),
        "date": date.today().isoformat(),
        "caveats": [
            f"trained on {n_train:,} positive {src_t}->{dst_t} edges; the source data is CTD-dominated (text-mined), so predictions inherit that bias",
            "random edge split, not scaffold- or disease-held-out; scores are optimistic for structurally similar compounds",
            "most genes have one or two edges, so their embeddings carry little structure; a degree heuristic is a strong competitor and is reported alongside",
            "ChemBL secondary data (mechanisms/targets/indications) is the 10-record test set unless the full scrape has been re-imported",
            "a high score is a hypothesis to check in the literature, not an observed interaction",
        ],
    }
    (out_dir / "model_card.json").write_text(json.dumps(card, indent=2))
    print(
        f"\nsaved model, embeddings, metrics, training curve and model card to {out_dir}"
    )
    return out_dir


def main(argv=None):
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--graph", type=Path, default=DEFAULT_GRAPH)
    ap.add_argument(
        "--target-edge",
        nargs=3,
        metavar=("SRC", "REL", "DST"),
        default=["Compound", "TARGETS", "Gene"],
    )
    ap.add_argument("--epochs", type=int, default=400)
    ap.add_argument("--eval-every", type=int, default=5)
    ap.add_argument(
        "--patience",
        type=int,
        default=12,
        help="evaluations without improvement before stopping",
    )
    ap.add_argument("--select-metric", choices=["mrr", "hits@10", "auc"], default="mrr")
    ap.add_argument("--hidden", type=int, default=128)
    ap.add_argument("--layers", type=int, default=2)
    ap.add_argument("--dropout", type=float, default=0.3)
    ap.add_argument("--decoder", choices=["mlp", "dot"], default="mlp")
    ap.add_argument(
        "--no-degree",
        action="store_true",
        help="disable the log-degree input projection",
    )
    ap.add_argument("--lr", type=float, default=0.002)
    ap.add_argument("--weight-decay", type=float, default=1e-5)
    ap.add_argument("--neg-ratio", type=int, default=3)
    ap.add_argument("--val-ratio", type=float, default=0.1)
    ap.add_argument("--test-ratio", type=float, default=0.1)
    ap.add_argument(
        "--rank-negatives",
        type=int,
        default=100,
        help="negatives per positive for test MRR / Hits@K",
    )
    ap.add_argument("--val-rank-negatives", type=int, default=50)
    ap.add_argument(
        "--val-rank-positives",
        type=int,
        default=2000,
        help="val positives sampled for ranking each eval (0=all)",
    )
    ap.add_argument("--device", default="cpu")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--out-dir", type=Path, default=None)
    args = ap.parse_args(argv)
    logging.basicConfig(level=logging.WARNING)
    train(args)


if __name__ == "__main__":
    main()
