"""Heterogeneous link-prediction model.

Encoder: a 2-layer GraphSAGE lifted to the heterogeneous graph with PyG's
``to_hetero`` (one weight matrix per relationship type, summed per node type),
which is the relational-GCN family the July/September plans describe. Every node
type gets a learnable embedding; node types with numeric features (Drug, Gene)
add a linear projection of those features, and every node type adds a projection
of its log-degree *on the message graph it is given* (so a held-out edge never
leaks into the feature of its endpoints).

Decoder: MLP over the concatenated endpoint embeddings (default) or a dot
product, producing a logit per candidate edge.
"""

from __future__ import annotations

import torch
import torch.nn.functional as F
from torch import Tensor, nn
from torch_geometric.data import HeteroData
from torch_geometric.nn import SAGEConv, to_hetero


def log_degree_dict(data: HeteroData, node_types: list[str]) -> dict[str, Tensor]:
    """log(1 + total degree) per node, counted over every edge type present in ``data``."""
    device = _device_of(data)
    deg = {nt: torch.zeros(data[nt].num_nodes, device=device) for nt in node_types}
    for (s, _, d), ei in data.edge_index_dict.items():
        deg[s] += torch.bincount(ei[0], minlength=data[s].num_nodes).float()
        deg[d] += torch.bincount(ei[1], minlength=data[d].num_nodes).float()
    return {nt: torch.log1p(v).unsqueeze(-1) for nt, v in deg.items()}


def _device_of(data: HeteroData) -> torch.device:
    for ei in data.edge_index_dict.values():
        return ei.device
    return torch.device("cpu")


class GNNEncoder(nn.Module):
    def __init__(self, hidden: int, num_layers: int = 2, dropout: float = 0.1):
        super().__init__()
        self.convs = nn.ModuleList([SAGEConv((-1, -1), hidden) for _ in range(num_layers)])
        self.dropout = nn.Dropout(dropout)

    def forward(self, x: Tensor, edge_index: Tensor) -> Tensor:
        for i, conv in enumerate(self.convs):
            x = conv(x, edge_index)
            if i < len(self.convs) - 1:
                x = F.relu(x)
                x = self.dropout(x)
        return x


class DotDecoder(nn.Module):
    def forward(self, z_src: Tensor, z_dst: Tensor, edge_label_index: Tensor) -> Tensor:
        return (z_src[edge_label_index[0]] * z_dst[edge_label_index[1]]).sum(dim=-1)

    def score_all(self, z_src: Tensor, z_dst: Tensor) -> Tensor:
        """Dense [num_src, num_dst] logits; used by predict.py."""
        return z_src @ z_dst.t()


class MLPDecoder(nn.Module):
    def __init__(self, hidden: int):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(2 * hidden, hidden), nn.ReLU(), nn.Linear(hidden, 1))

    def forward(self, z_src: Tensor, z_dst: Tensor, edge_label_index: Tensor) -> Tensor:
        h = torch.cat([z_src[edge_label_index[0]], z_dst[edge_label_index[1]]], dim=-1)
        return self.net(h).squeeze(-1)

    def score_all(self, z_src: Tensor, z_dst: Tensor, chunk: int = 64) -> Tensor:
        out = []
        n_dst = z_dst.size(0)
        for start in range(0, z_src.size(0), chunk):
            zs = z_src[start : start + chunk]
            b = zs.size(0)
            pair_src = zs.unsqueeze(1).expand(b, n_dst, -1)
            pair_dst = z_dst.unsqueeze(0).expand(b, n_dst, -1)
            out.append(self.net(torch.cat([pair_src, pair_dst], dim=-1)).squeeze(-1))
        return torch.cat(out, dim=0)


class HeteroLinkPredictor(nn.Module):
    """Embeddings (+ feature and degree projections) → hetero GraphSAGE → edge decoder."""

    def __init__(
        self,
        metadata: tuple[list[str], list[tuple[str, str, str]]],
        num_nodes: dict[str, int],
        in_dims: dict[str, int],
        hidden: int = 128,
        num_layers: int = 2,
        dropout: float = 0.1,
        decoder: str = "mlp",
        use_degree: bool = True,
    ):
        super().__init__()
        self.node_types, self.edge_types = metadata
        self.use_degree = use_degree
        self.config = dict(
            hidden=hidden,
            num_layers=num_layers,
            dropout=dropout,
            decoder=decoder,
            use_degree=use_degree,
            num_nodes=dict(num_nodes),
            in_dims=dict(in_dims),
        )
        self.emb = nn.ModuleDict({nt: nn.Embedding(num_nodes[nt], hidden) for nt in self.node_types})
        self.lin = nn.ModuleDict({nt: nn.Linear(d, hidden) for nt, d in in_dims.items() if d > 0})
        if use_degree:
            self.deg_lin = nn.ModuleDict({nt: nn.Linear(1, hidden) for nt in self.node_types})
        self.encoder = to_hetero(GNNEncoder(hidden, num_layers, dropout), metadata, aggr="sum")
        self.decoder = DotDecoder() if decoder == "dot" else MLPDecoder(hidden)
        for e in self.emb.values():
            nn.init.normal_(e.weight, std=0.1)

    def encode(self, data: HeteroData) -> dict[str, Tensor]:
        deg = log_degree_dict(data, self.node_types) if self.use_degree else None
        x_dict = {}
        for nt in self.node_types:
            h = self.emb[nt].weight
            if nt in self.lin and "x" in data[nt]:
                h = h + self.lin[nt](data[nt].x)
            if deg is not None:
                h = h + self.deg_lin[nt](deg[nt])
            x_dict[nt] = h
        return self.encoder(x_dict, data.edge_index_dict)

    def decode(self, z: dict[str, Tensor], edge_type: tuple[str, str, str], edge_label_index: Tensor) -> Tensor:
        return self.decoder(z[edge_type[0]], z[edge_type[2]], edge_label_index)

    def forward(self, data: HeteroData, edge_type, edge_label_index: Tensor) -> Tensor:
        return self.decode(self.encode(data), edge_type, edge_label_index)

    # -- persistence ----------------------------------------------------------
    def checkpoint(self, **extra) -> dict:
        return dict(
            state_dict=self.state_dict(),
            metadata=(list(self.node_types), [tuple(e) for e in self.edge_types]),
            config=self.config,
            **extra,
        )

    @classmethod
    def from_checkpoint(cls, ckpt: dict, data: HeteroData) -> "HeteroLinkPredictor":
        cfg = ckpt["config"]
        node_types, edge_types = ckpt["metadata"]
        model = cls(
            (node_types, [tuple(e) for e in edge_types]),
            cfg["num_nodes"],
            cfg["in_dims"],
            cfg["hidden"],
            cfg["num_layers"],
            cfg["dropout"],
            cfg["decoder"],
            cfg.get("use_degree", False),
        )
        with torch.no_grad():  # materialise lazy shapes before loading weights
            model.encode(data)
        model.load_state_dict(ckpt["state_dict"])
        model.eval()
        return model
