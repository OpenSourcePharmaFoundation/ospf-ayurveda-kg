"""Point the link-prediction model at the efflux axis.

The model (``local-llm/data/models/link_prediction/2026-09-14_Compound_TARGETS_Gene``)
was trained for compound-target prediction and has never been asked this
question.  Pointing it at the axis is the cheap part.  Reading the answer
correctly is not, for two reasons that this module makes explicit rather than
leaving in a model card:

**1.  The degree baseline beats the GNN on AUC.**  The model card reports GNN
AUC 0.716 against a pure-degree baseline at 0.838, and MRR 0.232 against 0.232
-- a dead heat.  So the raw sigmoid score is substantially a popularity
statistic.  Every axis gene sits in the 91st-98th percentile of compound-degree,
which means a naive top-k on raw score returns the compounds that are attached
to everything.  This module therefore reports three numbers per pair:

    ``score``       the model's raw probability, comparable to the published run
    ``z_gene``      the pair's score standardised within that gene's own column
    ``z_compound``  the same standardised within the compound's own row

A pair that is high on ``score`` but near zero on ``z_gene`` is telling you the
gene is popular.  A pair high on both is the model asserting something
*specific*, which is the only kind of claim worth carrying forward.  The
headline statistic ``z_min = min(z_gene, z_compound)`` demands specificity in
both directions.

**2.  The edge the model learned is not binding.**  ``Compound-TARGETS-Gene``
is rebuilt from ``pubchem_phytochem_target_interactions.csv``, which is 95%
Comparative Toxicogenomics Database.  On this axis the underlying statements
are overwhelmingly expression-change sentences, a large minority of them
third-order ("X inhibits the reaction [Y results in increased expression of
ABCA1]") and many with a dietary confound in the compound slot.  The semantics
are audited by ``edge_semantics`` below and reported in the note, because for
an EFFECTOR gene -- a transporter with no agonist site -- a high score cannot
mean binding and must be read as a transcriptional hypothesis.

The model also cannot score the 3,282 ``Drug`` nodes against genes: the graph
holds no ``Drug-TARGETS-Gene`` edge type at all, so Drug embeddings are shaped
entirely by indication space and their scores would be uncalibrated
extrapolation.  ``scoreable_node_type`` states that limit rather than papering
over it.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import torch

PROJECT_ROOT = Path(__file__).resolve().parents[3]
SUBPROJECT = PROJECT_ROOT / "local-llm"
if str(SUBPROJECT) not in sys.path:
    sys.path.insert(0, str(SUBPROJECT))

DEFAULT_GRAPH = SUBPROJECT / "data" / "graph" / "graph_heterodata.pt"
DEFAULT_MODEL = (
    SUBPROJECT
    / "data"
    / "models"
    / "link_prediction"
    / "2026-09-14_Compound_TARGETS_Gene"
    / "model.pt"
)
INTERACTIONS_CSV = (
    PROJECT_ROOT / "data" / "processed" / "pubchem_phytochem_target_interactions.csv"
)

SCOREABLE_NODE_TYPE = "Compound"


def load_model(model_path: Path = DEFAULT_MODEL, graph_path: Path = DEFAULT_GRAPH):
    """Encoder output plus the pieces needed to index it.

    Imported lazily so that the rest of the package does not require torch.
    """
    import torch_geometric.transforms as T
    from gnn.model import HeteroLinkPredictor
    from gnn.schema import load_graph

    raw, node_index = load_graph(graph_path)
    data = T.ToUndirected()(raw)
    ckpt = torch.load(model_path, weights_only=False)
    model = HeteroLinkPredictor.from_checkpoint(ckpt, data)
    edge_type = tuple(ckpt["target_edge"])
    with torch.no_grad():
        z = model.encode(data)
    return model, raw, data, node_index, edge_type, z


def _ordered(node_index: pd.DataFrame, label: str) -> pd.DataFrame:
    df = (
        node_index[node_index.label == label]
        .sort_values("index")
        .reset_index(drop=True)
    )
    assert (df["index"].to_numpy() == np.arange(len(df))).all()
    return df


@torch.no_grad()
def score_axis(symbols, model_path=DEFAULT_MODEL, graph_path=DEFAULT_GRAPH):
    """Score every Compound against every axis gene.

    Returns one row per (compound, gene) pair with the raw score, both
    standardised scores, the observed-edge flag, and the degree of each
    endpoint, so that a reader can see at a glance whether a high score is
    specificity or popularity.
    """
    model, raw, data, node_index, edge_type, z = load_model(model_path, graph_path)
    src_t, rel, dst_t = edge_type
    if src_t != SCOREABLE_NODE_TYPE:
        raise ValueError(f"unexpected source node type {src_t!r}")

    compounds, genes = _ordered(node_index, src_t), _ordered(node_index, dst_t)
    upper = genes.name.str.upper()
    missing = [s for s in symbols if not (upper == s).any()]
    if missing:
        raise KeyError(f"axis genes absent from the graph: {missing}")
    gidx = {s: int(genes.index[upper == s][0]) for s in symbols}

    ei = raw[edge_type].edge_index
    cdeg = torch.bincount(ei[0], minlength=raw[src_t].num_nodes).numpy()
    gdeg = torch.bincount(ei[1], minlength=raw[dst_t].num_nodes).numpy()
    observed = {(int(a), int(b)) for a, b in ei.t().tolist()}

    # Full [n_compound, n_gene] logit matrix: z_compound is only meaningful
    # against the whole gene population, not against the nine.
    logits_all = model.decoder.score_all(z[src_t], z[dst_t])
    probs_all = torch.sigmoid(logits_all).numpy()

    # Standardise down each gene column over all compounds, and across each
    # compound row over all genes.
    col_mu, col_sd = probs_all.mean(0), probs_all.std(0) + 1e-12
    row_mu, row_sd = probs_all.mean(1), probs_all.std(1) + 1e-12

    rows = []
    for sym in symbols:
        g = gidx[sym]
        col = probs_all[:, g]
        z_gene = (col - col_mu[g]) / col_sd[g]
        z_cmpd = (col - row_mu) / row_sd
        for c in range(len(compounds)):
            rows.append(
                {
                    "gene": sym,
                    "compound": compounds.at[c, "name"],
                    "pubchem_cid": compounds.at[c, "external_id"],
                    "score": float(col[c]),
                    "z_gene": float(z_gene[c]),
                    "z_compound": float(z_cmpd[c]),
                    "z_min": float(min(z_gene[c], z_cmpd[c])),
                    "observed_edge": (c, g) in observed,
                    "compound_degree": int(cdeg[c]),
                    "gene_degree": int(gdeg[g]),
                }
            )
    df = pd.DataFrame(rows)
    df["gene_degree_percentile"] = df.gene.map(
        {s: float((gdeg <= gdeg[gidx[s]]).mean() * 100) for s in symbols}
    ).round(2)
    return df


# --- what the edge actually asserts ----------------------------------------

_EXPRESSION = re.compile(
    r"expression|abundance|secretion|metabolism|transport of", re.I
)
_BINDING = re.compile(
    r"\bbinds?\b|\bbinding\b|affinity|agonis|antagonis|inhibitor\b", re.I
)
_NESTED = re.compile(r"\[.*\[", re.S)
_COTREAT = re.compile(r"co-treated with", re.I)


def edge_semantics(symbols, path: Path = INTERACTIONS_CSV) -> pd.DataFrame:
    """Audit what the Compound->Gene edges on the axis actually say.

    One row per gene: how many of its edges are expression statements rather
    than binding statements, how many are nested (the compound modifies a
    reaction between two *other* entities rather than acting on the gene), and
    how many name a co-treatment.  This is the evidence for reading an
    EFFECTOR-gene prediction as transcription and not as engagement.
    """
    df = pd.read_csv(path, dtype=str, low_memory=False)
    df = df[df.protein_name.isna() & df.gene_name.isin(symbols)]
    out = []
    for sym, g in df.groupby("gene_name"):
        act = g.action.fillna("")
        out.append(
            {
                "gene": sym,
                "n_edges": len(g),
                "n_expression": int(act.str.contains(_EXPRESSION).sum()),
                "n_binding_like": int(act.str.contains(_BINDING).sum()),
                "n_nested": int(act.str.contains(_NESTED).sum()),
                "n_cotreatment": int(act.str.contains(_COTREAT).sum()),
                "pct_ctd": round(
                    100.0 * g.info_source.str.contains("CTD", na=False).mean(), 1
                ),
            }
        )
    res = pd.DataFrame(out).sort_values("n_edges", ascending=False)
    for c in ("n_expression", "n_binding_like", "n_nested", "n_cotreatment"):
        res[c.replace("n_", "pct_")] = (100.0 * res[c] / res.n_edges).round(1)
    return res.reset_index(drop=True)


# --- does the model have any signal in the direction this step needs? ------


def benchmark_axis_retrieval(
    symbols, model_path=DEFAULT_MODEL, graph_path=DEFAULT_GRAPH
):
    """Can the model rank a gene's known binders above the other 920 compounds?

    This is the question Step 6 actually asks -- *rank compounds for a gene* --
    and it is the transpose of the question the model card evaluates, which is
    *rank genes for a compound* (one positive against 100 randomly drawn genes).
    The two are not interchangeable, and the difference is not cosmetic:

      corr(gene degree,     mean column score) = +0.957
      corr(compound degree, mean row score)    = -0.509

    Ranking down a column holds the gene fixed, so the only variance left is
    the compound-side term -- and that term is inverted.  A model can pass its
    own benchmark comfortably and still be anti-predictive on the transpose.

    Reported as the mean percentile rank of the known positives under four
    scorers, where 0.500 is random and 1.000 is perfect:

      ``raw``    the decoder probability, as ``predict.py`` would use it
      ``resid``  that score with its linear log-compound-degree trend removed
      ``knn``    cosine similarity in compound-embedding space to the gene's
                 known binders, leave-one-out
      ``degree`` log compound degree alone -- a scorer that knows nothing about
                 the gene and only asks how well studied the compound is

    The positives here were *in the training set*, so every column is an upper
    bound on held-out performance.
    """
    model, raw, data, node_index, edge_type, z = load_model(model_path, graph_path)
    src_t, _, dst_t = edge_type
    with torch.no_grad():
        mat = torch.sigmoid(model.decoder.score_all(z[src_t], z[dst_t])).numpy()
        zc = z[src_t].numpy()

    genes = _ordered(node_index, dst_t)
    upper = genes.name.str.upper()
    ei = raw[edge_type].edge_index
    cdeg = torch.bincount(ei[0], minlength=raw[src_t].num_nodes).numpy()
    log_cdeg = np.log1p(cdeg).astype(float)
    zcn = zc / (np.linalg.norm(zc, axis=1, keepdims=True) + 1e-12)

    positives: dict[int, set[int]] = {}
    for c, g in ei.t().tolist():
        positives.setdefault(int(g), set()).add(int(c))

    def mean_percentile(score: np.ndarray, pos: np.ndarray) -> float:
        order = np.argsort(-score)
        where = {int(v): i for i, v in enumerate(order)}
        r = np.array([where[int(p)] for p in pos])
        return float((1.0 - r / (len(order) - 1)).mean())

    rows = []
    for sym in symbols:
        g = int(genes.index[upper == sym][0])
        pos = np.array(sorted(positives.get(g, set())))
        if len(pos) == 0:
            continue
        col = mat[:, g]
        slope, intercept = np.polyfit(log_cdeg, col, 1)
        resid = col - (slope * log_cdeg + intercept)
        sim = zcn @ zcn[pos].T
        knn = sim.sum(1)
        for j, p in enumerate(pos):  # leave-one-out: a positive must not rank itself
            knn[p] -= sim[p, j]
        rows.append(
            {
                "gene": sym,
                "n_known_binders": len(pos),
                "raw": round(mean_percentile(col, pos), 3),
                "resid": round(mean_percentile(resid, pos), 3),
                "knn": round(mean_percentile(knn, pos), 3),
                "degree_only": round(mean_percentile(log_cdeg, pos), 3),
            }
        )
    df = pd.DataFrame(rows)
    df.loc[len(df)] = {
        "gene": "MEAN",
        "n_known_binders": int(df.n_known_binders.sum()),
        **{c: round(df[c].mean(), 3) for c in ("raw", "resid", "knn", "degree_only")},
    }
    return df
