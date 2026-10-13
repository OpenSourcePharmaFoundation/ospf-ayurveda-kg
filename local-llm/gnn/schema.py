"""Shared intermediate representation for the GNN slice.

Both graph sources (live Neo4j, or the CSV mirror of the Cypher import scripts)
produce a :class:`GraphTables`. One builder turns that into a PyG ``HeteroData``
plus a node-index table, so the model code never cares where the graph came from.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from torch_geometric.data import HeteroData

log = logging.getLogger(__name__)

# Numeric node properties exported as feature tensors, per node label.
# Everything not listed here gets a learnable embedding only (see model.py).
NUMERIC_FEATURES: dict[str, list[str]] = {
    "Drug": [
        "molecular_weight",
        "alogp",
        "hba",
        "hbd",
        "psa",
        "rtb",
        "ro5_violations",
        "aromatic_rings",
        "heavy_atoms",
        "qed_weighted",
        "natural_product",
    ],
    # max DisGeNET gene-disease score over the gene's association edges
    "Gene": ["gda_score_max"],
}

NODE_COLUMNS = ["label", "key", "name", "external_id"]
EDGE_COLUMNS = ["src_label", "rel", "dst_label", "src_key", "dst_key"]


@dataclass
class GraphTables:
    """Flat node and edge tables.

    nodes:  one row per node. ``key`` is unique within ``label``. ``name`` is the
            human-readable name, ``external_id`` an optional cross-DB identifier
            (pubchemId, chembl_id, uniprotId, ncbiId). Extra numeric columns are
            picked up as features if listed in :data:`NUMERIC_FEATURES`.
    edges:  one row per directed relationship, endpoints referenced by
            (label, key). Duplicates are collapsed at build time.
    """

    nodes: pd.DataFrame
    edges: pd.DataFrame
    source: str = "unknown"
    notes: list[str] = field(default_factory=list)

    def summary(self) -> str:
        n = self.nodes.groupby("label").size().sort_values(ascending=False)
        e = (
            self.edges.drop_duplicates(EDGE_COLUMNS)
            .groupby(["src_label", "rel", "dst_label"])
            .size()
            .sort_values(ascending=False)
        )
        lines = [f"source: {self.source}", f"nodes: {len(self.nodes):,}"]
        lines += [f"  {lbl:<18} {cnt:>8,}" for lbl, cnt in n.items()]
        lines.append(f"edges (deduplicated): {int(e.sum()):,}")
        lines += [
            f"  {s:<14} -[{r}]-> {d:<16} {cnt:>8,}" for (s, r, d), cnt in e.items()
        ]
        return "\n".join(lines)


def _feature_matrix(
    df: pd.DataFrame, cols: list[str]
) -> tuple[torch.Tensor, list[str]]:
    """Standardise numeric columns; append a missing-indicator per column.

    Missing values become 0 after standardisation (i.e. the mean), and the
    indicator lets the model tell "average" from "unknown".
    """
    present = [c for c in cols if c in df.columns]
    if not present:
        return torch.zeros((len(df), 0)), []
    raw = df[present].apply(pd.to_numeric, errors="coerce").to_numpy(dtype=np.float64)
    missing = np.isnan(raw)
    mean = np.nanmean(raw, axis=0)
    std = np.nanstd(raw, axis=0)
    mean = np.where(np.isnan(mean), 0.0, mean)
    std = np.where((std == 0) | np.isnan(std), 1.0, std)
    z = (raw - mean) / std
    z[missing] = 0.0
    x = np.concatenate([z, missing.astype(np.float64)], axis=1)
    names = present + [f"{c}__missing" for c in present]
    return torch.tensor(x, dtype=torch.float32), names


def build_hetero_data(tables: GraphTables) -> tuple[HeteroData, pd.DataFrame]:
    """Turn :class:`GraphTables` into a ``HeteroData`` and a node-index table.

    Returns
    -------
    data:       HeteroData with ``num_nodes`` (and ``x`` where features exist)
                per node type, and ``edge_index`` per (src, rel, dst) triple.
    node_index: DataFrame(label, index, key, name, external_id) mapping every
                tensor row back to its graph identity.
    """
    nodes = tables.nodes.copy()
    for col in NODE_COLUMNS:
        if col not in nodes.columns:
            nodes[col] = None
    nodes = nodes.drop_duplicates(["label", "key"]).reset_index(drop=True)

    edges = tables.edges[EDGE_COLUMNS].drop_duplicates().reset_index(drop=True)

    # Drop node labels that take part in no edge at all: isolated types carry
    # no signal for message passing and break to_hetero().
    labels_in_edges = set(edges.src_label) | set(edges.dst_label)
    isolated = sorted(set(nodes.label) - labels_in_edges)
    if isolated:
        log.warning("dropping isolated node labels (no edges): %s", isolated)
        nodes = nodes[nodes.label.isin(labels_in_edges)]

    data = HeteroData()
    index_frames = []
    key_to_idx: dict[tuple[str, str], int] = {}

    for label, grp in nodes.groupby("label", sort=True):
        grp = grp.sort_values("key", kind="stable").reset_index(drop=True)
        data[label].num_nodes = len(grp)
        feats = NUMERIC_FEATURES.get(label, [])
        x, feat_names = _feature_matrix(grp, feats)
        if x.shape[1] > 0:
            data[label].x = x
            data[label].feature_names = feat_names
        for i, k in enumerate(grp["key"].tolist()):
            key_to_idx[(label, k)] = i
        idx = grp[NODE_COLUMNS].copy()
        idx.insert(1, "index", range(len(grp)))
        index_frames.append(idx)

    node_index = pd.concat(index_frames, ignore_index=True)

    dropped_total = 0
    for (s, r, d), grp in edges.groupby(["src_label", "rel", "dst_label"], sort=True):
        src = [key_to_idx.get((s, k)) for k in grp.src_key]
        dst = [key_to_idx.get((d, k)) for k in grp.dst_key]
        pairs = [(a, b) for a, b in zip(src, dst) if a is not None and b is not None]
        dropped = len(grp) - len(pairs)
        if dropped:
            dropped_total += dropped
            log.warning(
                "%s -[%s]-> %s: %d edges reference unknown nodes; dropped",
                s,
                r,
                d,
                dropped,
            )
        if not pairs:
            continue
        ei = torch.tensor(pairs, dtype=torch.long).t().contiguous()
        data[(s, r, d)].edge_index = ei
    if dropped_total:
        tables.notes.append(f"{dropped_total} edges dropped for missing endpoints")

    return data, node_index


def describe_hetero(data: HeteroData) -> str:
    lines = ["node types:"]
    for nt in data.node_types:
        store = data[nt]
        feat = f", x={tuple(store.x.shape)}" if "x" in store else ""
        lines.append(f"  {nt:<18} n={store.num_nodes:>8,}{feat}")
    lines.append("edge types:")
    for et in data.edge_types:
        lines.append(
            f"  {et[0]:<14} -[{et[1]}]-> {et[2]:<16} E={data[et].edge_index.size(1):>8,}"
        )
    return "\n".join(lines)


def save_graph(data: HeteroData, node_index: pd.DataFrame, out_pt: Path) -> Path:
    out_pt = Path(out_pt)
    out_pt.parent.mkdir(parents=True, exist_ok=True)
    torch.save(data, out_pt)
    out_csv = out_pt.with_name(
        out_pt.stem.replace("_heterodata", "") + "_node_index.csv"
    )
    node_index.to_csv(out_csv, index=False)
    return out_csv


def load_graph(pt_path: Path) -> tuple[HeteroData, pd.DataFrame]:
    pt_path = Path(pt_path)
    data = torch.load(pt_path, weights_only=False)
    idx_path = pt_path.with_name(
        pt_path.stem.replace("_heterodata", "") + "_node_index.csv"
    )
    node_index = pd.read_csv(idx_path, dtype=str, keep_default_na=False)
    node_index["index"] = node_index["index"].astype(int)
    return data, node_index
