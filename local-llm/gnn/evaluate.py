"""Link-prediction metrics and non-learned baselines.

Metrics
-------
AUC-ROC / average precision on labelled (edge, 0/1) pairs, and ranking metrics
(MRR, Hits@K) where each true edge (u, v) is ranked against ``num_neg`` random
non-edges (u, v') sharing the same source node.

Baselines (all expressed as ``score_fn(src_idx, dst_idx) -> scores``)
---------
random          uniform noise — the floor.
degree          preferential attachment: deg(u) * deg(v) on the message graph.
shortest_path   1 / BFS distance between u and v on the message graph with all
                relationship types collapsed and made undirected; 0 if unreachable.
"""

from __future__ import annotations

from typing import Callable

import numpy as np
import torch
from scipy.sparse import coo_matrix, csr_matrix
from scipy.sparse.csgraph import dijkstra
from sklearn.metrics import average_precision_score, roc_auc_score
from torch import Tensor
from torch_geometric.data import HeteroData

ScoreFn = Callable[[Tensor, Tensor], Tensor]


# --------------------------------------------------------------------------- #
# Classification metrics
# --------------------------------------------------------------------------- #
def classification_metrics(scores: Tensor, labels: Tensor) -> dict[str, float]:
    y = labels.detach().cpu().numpy()
    s = scores.detach().cpu().numpy()
    if len(np.unique(y)) < 2:
        return {"auc": float("nan"), "ap": float("nan")}
    return {
        "auc": float(roc_auc_score(y, s)),
        "ap": float(average_precision_score(y, s)),
    }


# --------------------------------------------------------------------------- #
# Ranking metrics
# --------------------------------------------------------------------------- #
def _pair_codes(src: Tensor, dst: Tensor, num_dst: int) -> Tensor:
    return src.to(torch.int64) * num_dst + dst.to(torch.int64)


@torch.no_grad()
def ranking_metrics(
    score_fn: ScoreFn,
    pos_edge_index: Tensor,
    known_edge_index: Tensor,
    num_dst: int,
    num_neg: int = 100,
    ks: tuple[int, ...] = (1, 3, 10),
    seed: int = 0,
    batch_size: int = 512,
) -> dict[str, float]:
    """Rank every positive (u, v) against ``num_neg`` sampled (u, v') non-edges.

    ``known_edge_index`` should hold *all* true edges of the target type (train,
    val and test) so sampled negatives are genuinely unobserved pairs.
    """
    g = torch.Generator().manual_seed(seed)
    known = torch.unique(_pair_codes(known_edge_index[0], known_edge_index[1], num_dst))
    ranks = []
    P = pos_edge_index.size(1)
    for start in range(0, P, batch_size):
        u = pos_edge_index[0, start : start + batch_size]
        v = pos_edge_index[1, start : start + batch_size]
        B = u.size(0)
        cand = torch.randint(0, num_dst, (B, num_neg), generator=g)
        # resample collisions with known edges a few times, then mask leftovers
        for _ in range(3):
            bad = torch.isin(
                _pair_codes(u.unsqueeze(1).expand_as(cand), cand, num_dst), known
            )
            if not bad.any():
                break
            cand[bad] = torch.randint(0, num_dst, (int(bad.sum()),), generator=g)
        bad = torch.isin(
            _pair_codes(u.unsqueeze(1).expand_as(cand), cand, num_dst), known
        )

        pos_s = score_fn(u, v)
        neg_s = score_fn(
            u.unsqueeze(1).expand_as(cand).reshape(-1), cand.reshape(-1)
        ).view(B, num_neg)
        neg_s = neg_s.masked_fill(bad, float("-inf"))
        # rank = 1 + number of negatives strictly better (ties broken pessimistically by half)
        greater = (neg_s > pos_s.unsqueeze(1)).sum(1).float()
        ties = (neg_s == pos_s.unsqueeze(1)).sum(1).float()
        ranks.append(1.0 + greater + 0.5 * ties)
    r = torch.cat(ranks)
    out = {"mrr": float((1.0 / r).mean())}
    for k in ks:
        out[f"hits@{k}"] = float((r <= k).float().mean())
    out["num_positives"] = int(P)
    out["num_negatives_per_positive"] = int(num_neg)
    return out


# --------------------------------------------------------------------------- #
# Baselines
# --------------------------------------------------------------------------- #
def random_baseline(seed: int = 0) -> ScoreFn:
    g = torch.Generator().manual_seed(seed)

    def fn(src: Tensor, dst: Tensor) -> Tensor:
        return torch.rand(src.shape, generator=g)

    return fn


def degree_baseline(data: HeteroData, edge_type: tuple[str, str, str]) -> ScoreFn:
    """deg(u) * deg(v), degrees counted over every relationship type in ``data``."""
    src_t, _, dst_t = edge_type
    deg = {nt: torch.zeros(data[nt].num_nodes) for nt in data.node_types}
    for (s, _, d), store in data.edge_index_dict.items():
        deg[s] += torch.bincount(store[0], minlength=data[s].num_nodes).float()
        deg[d] += torch.bincount(store[1], minlength=data[d].num_nodes).float()

    def fn(src: Tensor, dst: Tensor) -> Tensor:
        return deg[src_t][src] * deg[dst_t][dst]

    return fn


def homogeneous_adjacency(data: HeteroData) -> tuple[csr_matrix, dict[str, int]]:
    """Collapse all node/edge types into one undirected sparse adjacency."""
    offsets, total = {}, 0
    for nt in data.node_types:
        offsets[nt] = total
        total += data[nt].num_nodes
    rows, cols = [], []
    for (s, _, d), ei in data.edge_index_dict.items():
        rows.append(ei[0].numpy() + offsets[s])
        cols.append(ei[1].numpy() + offsets[d])
    r = np.concatenate(rows)
    c = np.concatenate(cols)
    adj = coo_matrix(
        (np.ones(len(r), dtype=np.float32), (r, c)), shape=(total, total)
    ).tocsr()
    adj = adj + adj.T
    adj.data[:] = 1.0
    return adj.tocsr(), offsets


def shortest_path_baseline(
    data: HeteroData, edge_type: tuple[str, str, str], max_dist: int = 6
) -> ScoreFn:
    """1 / BFS distance on the collapsed message graph (0 when unreachable)."""
    adj, offsets = homogeneous_adjacency(data)
    src_t, _, dst_t = edge_type
    src_off, dst_off = offsets[src_t], offsets[dst_t]
    cache: dict[int, np.ndarray] = {}

    def dist_row(u: int) -> np.ndarray:
        if u not in cache:
            d = dijkstra(
                adj,
                directed=False,
                indices=[u + src_off],
                unweighted=True,
                limit=max_dist,
            )[0]
            cache[u] = d.astype(np.float32)
        return cache[u]

    def fn(src: Tensor, dst: Tensor) -> Tensor:
        src_np = src.cpu().numpy()
        dst_np = dst.cpu().numpy() + dst_off
        out = np.zeros(len(src_np), dtype=np.float32)
        for u in np.unique(src_np):
            m = src_np == u
            d = dist_row(int(u))[dst_np[m]]
            out[m] = np.where(np.isfinite(d) & (d > 0), 1.0 / np.maximum(d, 1.0), 0.0)
        return torch.from_numpy(out)

    return fn


def evaluate_score_fn(
    score_fn: ScoreFn,
    edge_label_index: Tensor,
    edge_label: Tensor,
    known_edge_index: Tensor,
    num_dst: int,
    num_neg: int = 100,
    seed: int = 0,
) -> dict[str, float]:
    """Classification metrics on labelled pairs + ranking metrics on the positives."""
    scores = score_fn(edge_label_index[0], edge_label_index[1])
    out = classification_metrics(scores, edge_label)
    pos = edge_label_index[:, edge_label.bool()]
    out.update(
        ranking_metrics(
            score_fn, pos, known_edge_index, num_dst, num_neg=num_neg, seed=seed
        )
    )
    return out


def format_table(
    rows: dict[str, dict[str, float]],
    cols=("auc", "ap", "mrr", "hits@1", "hits@3", "hits@10"),
) -> str:
    name_w = max(len(k) for k in rows) + 2
    head = f"{'model':<{name_w}}" + "".join(f"{c:>10}" for c in cols)
    lines = [head, "-" * len(head)]
    for name, m in rows.items():
        lines.append(
            f"{name:<{name_w}}"
            + "".join(f"{m.get(c, float('nan')):>10.4f}" for c in cols)
        )
    return "\n".join(lines)
