GNN Message-Passing: How It Actually Works
===========================================

The glossary defines GNN message-passing as "each node aggregates information
from its neighbors, updates its own representation, and repeats for multiple
layers." This document explains the concrete mechanics behind that abstraction.


## Step 0 — Every Node Starts as a Vector

Before message-passing begins, every node gets an initial numerical vector (its
"feature vector"). A Drug node might start as a 128-dimensional vector derived
from its properties — molecular weight, approval status, therapeutic areas
encoded numerically. A Gene node might get its vector from disease association
scores or functional annotations.

Starting vectors can come from:
- A **learned lookup table** (random initialization tuned during training)
- **Pre-computed embeddings** from a language model encoding the node's text
- **Feature engineering** from structured properties in the graph


## Step 1 — "Message" = Transform a Neighbor's Vector

For each edge, the source node's current vector is multiplied by a **learned
weight matrix** — a grid of numbers that the model adjusts during training. This
matrix multiplication IS the "message."

If Gene node TNF has current vector `[0.3, -0.1, 0.7, ...]` (128 numbers) and
the learned weight matrix `W` is 128×128:

    message = W × [0.3, -0.1, 0.7, ...]
            = [0.15, 0.42, -0.03, ...]     # new 128-dim vector

The weight matrix controls what information gets amplified, suppressed, or
rotated as it flows along an edge.

**Relationship-specific weights (R-GCN):** In a Relational GCN — the
architecture planned for this project — there is a separate weight matrix for
each relationship type. Information flowing along a TARGETS edge uses a different
matrix than information flowing along a TREATS edge. This is how the model learns
that "being targeted by a drug" carries different semantics than "being treated
by a drug."


## Step 2 — "Aggregate" = Combine All Incoming Messages

Each node collects every message arriving from its neighbors and combines them
into a single vector. The simplest method is **mean aggregation** — averaging all
incoming vectors element-by-element.

Example: Drug node Ibuprofen has three neighbors sending messages:

    message from Gene:TNF     = [0.15,  0.42, -0.03, ...]
    message from Gene:COX2    = [0.28, -0.11,  0.55, ...]
    message from Disease:OM   = [0.07,  0.33,  0.12, ...]

    aggregated = mean = [0.167, 0.213, 0.213, ...]

Other aggregation strategies:
- **Sum:** preserves magnitude (distinguishes highly-connected from sparse nodes)
- **Max:** captures the strongest signal from any single neighbor
- **Attention-weighted:** learned weights that let the node decide which
  neighbors matter most (this is what HGT uses)

All produce one combined vector from the set of incoming messages.


## Step 3 — "Update" = Merge Aggregated Info with the Node's Own Vector

The node mixes the aggregated neighbor information with its own current vector,
then passes the result through a **nonlinear activation function** (typically
ReLU, which zeroes out negative values):

    new_vector = ReLU(W_self × old_vector + aggregated_message)

`W_self` is another learned weight matrix. The nonlinearity is critical — without
it, stacking multiple layers would mathematically collapse into a single linear
transformation, and the model could not learn complex patterns.

After this step, Ibuprofen's vector encodes not just "what Ibuprofen is" but
"what Ibuprofen is PLUS a summary of its immediate neighbors."


## Step 4 — Repeat for L Layers (Expanding the Receptive Field)

The entire process repeats. In layer 2, each node collects messages from
neighbors whose vectors were already updated in layer 1 — so those vectors
already contain information about THEIR neighbors.

**Each layer expands the receptive field by one hop:**

| Layers | What the node "sees"                                         |
|--------|--------------------------------------------------------------|
| 1      | Direct neighbors (1-hop)                                     |
| 2      | Neighbors-of-neighbors (2-hop)                               |
| 3      | 3-hop neighborhood                                           |
| L      | Everything within L hops                                     |

For a biomedical knowledge graph, 2-3 layers is typical. More layers cause
**oversmoothing**: all node vectors converge toward the same value because every
node has effectively seen the entire graph, washing out local structural signal.


## Worked Example: This Project's Graph

Consider this subgraph:

    Curcumin --[TARGETS]--> TNF --[ASSOCIATED_WITH]--> Oral Mucositis
                                       ^
    Ibuprofen --[TARGETS]--------------/

**Layer 1:**

- **TNF** aggregates messages from Curcumin (via TARGETS), Ibuprofen (via
  TARGETS), and Oral Mucositis (via ASSOCIATED_WITH). TNF's vector now encodes:
  "I am targeted by an approved NSAID and a plant-derived compound, and I am
  associated with OM."

- **Curcumin** aggregates messages from TNF (via TARGETS). Its vector now
  encodes: "I target something."

- **Oral Mucositis** aggregates messages from TNF (via ASSOCIATED_WITH). Its
  vector now encodes: "I have this gene associated with me."

**Layer 2:**

- **Curcumin** aggregates messages from TNF again — but TNF's vector was updated
  in layer 1 to contain info about Ibuprofen and OM. So Curcumin's vector now
  encodes: "I target a gene that is also targeted by an approved drug AND is
  associated with OM."

- Curcumin has never been directly connected to Oral Mucositis or Ibuprofen, but
  after 2 layers, its embedding encodes information about both.

This is how the GNN learns to predict a TREATS edge between Curcumin and Oral
Mucositis — their final embeddings end up geometrically close because they share
structural patterns with known drug-disease pairs.


## Key Takeaways

1. **No magic involved.** Message-passing is matrix multiplication + averaging +
   a nonlinearity, repeated. The learning happens entirely in the weight
   matrices, tuned by backpropagation like any neural network.

2. **The graph structure IS the data.** A GNN does not read text or inspect
   images. The pattern of connections is what it learns from. Two nodes in
   structurally similar neighborhoods will end up with similar embeddings, even
   if their raw features differ.

3. **Layer count = hop radius.** A 2-layer GNN literally cannot incorporate
   information from beyond 2 hops. This is deliberate — most biological
   relevance is local, and going deeper risks oversmoothing.

4. **Relationship-aware models (R-GCN) use separate weight matrices per edge
   type.** This is why R-GCN suits our heterogeneous graph with TARGETS, TREATS,
   CONTAINS, PRODUCES, and ASSOCIATED_WITH edges carrying different semantics.
