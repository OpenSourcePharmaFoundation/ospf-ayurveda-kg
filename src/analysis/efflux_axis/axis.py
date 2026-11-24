"""The reverse-cholesterol-transport axis, as targets.

Step 6 of ``docs/prompts/dr-solve-open-questions-prompt.md``.  Every one of the
29 compounds the DR analysis considered reduces what *arrives* in the retina.
None accelerates what leaves.  This module names the leaving side.

The nine genes are not nine targets.  They fall into three classes that take
different kinds of evidence, and conflating them is the specific error this
module exists to prevent:

``RECEPTOR``
    A nuclear receptor with a ligand-binding pocket.  NR1H3 (LXR-alpha) and
    NR1H2 (LXR-beta) are the only members of the axis that a small molecule
    can bind in the conventional sense, and therefore the only ones for which
    "compound X engages gene Y" has a dissociation constant behind it.
    **The structural opening of this step lives here**: the PPAR-alpha pocket
    mandates a lipophilic *acid*, which is what couples potency to
    hepatoselectivity and costs four log units of logD at pH 7.4.  The LXR
    pocket binds oxysterols -- neutral.  Ionisation is not locked in.

``EFFECTOR``
    ABCA1, ABCG1, APOA1, APOE.  These are the readouts of the axis, not
    pockets.  ABCA1 and ABCG1 are ABC transporters with no agonist
    pharmacology -- no small molecule binds ABCA1 and makes it pump faster;
    what the literature calls an "ABCA1 inducer" is an agent acting upstream,
    almost always at LXR.  APOA1 and APOE are apolipoproteins: the acceptor
    *is* the protein, so the way to raise them is to administer them, not to
    bind them.  A prediction of "compound X targets ABCA1" is therefore a
    prediction about transcription, and must be read as such.

``SCAVENGER``
    CD36, OLR1 (LOX-1), MSR1 (SR-A).  The uptake side, included for
    completeness because burden is influx over clearance and the influx term
    is theirs.  CD36 has genuine small-molecule pharmacology; OLR1 and MSR1
    have almost none.

``ligandable`` encodes that distinction as a boolean so downstream code cannot
silently rank an expression hypothesis against a binding constant.
"""

from __future__ import annotations

import dataclasses

RECEPTOR = "RECEPTOR"
EFFECTOR = "EFFECTOR"
SCAVENGER = "SCAVENGER"

EFFLUX = "efflux"
UPTAKE = "uptake"


@dataclasses.dataclass(frozen=True)
class AxisGene:
    symbol: str
    uniprot: str
    name: str
    gene_class: str
    arm: str
    ligandable: bool
    rationale: str


AXIS: tuple[AxisGene, ...] = (
    AxisGene(
        "NR1H3",
        "Q13133",
        "Oxysterols receptor LXR-alpha",
        RECEPTOR,
        EFFLUX,
        True,
        "Master transcriptional switch for ABCA1/ABCG1/APOE. Neutral oxysterol pocket - "
        "the one node on this axis whose ligand is not required to be an acid. Also the "
        "isoform that drives hepatic SREBF1 and therefore the steatosis liability.",
    ),
    AxisGene(
        "NR1H2",
        "P55055",
        "Oxysterols receptor LXR-beta",
        RECEPTOR,
        EFFLUX,
        True,
        "The ubiquitously expressed LXR isoform, including in retina. Drives the same "
        "ABCA1/ABCG1 programme with far less hepatic lipogenic output than LXR-alpha, "
        "so beta-selectivity is the whole safety argument for this class.",
    ),
    AxisGene(
        "ABCA1",
        "O95477",
        "Phospholipid-transporting ATPase ABCA1",
        EFFECTOR,
        EFFLUX,
        False,
        "Rate-limiting efflux of free cholesterol to lipid-poor apoA-I. The clearance "
        "term of the two-compartment lesion. No orthosteric agonist site exists.",
    ),
    AxisGene(
        "ABCG1",
        "P45844",
        "ATP-binding cassette sub-family G member 1",
        EFFECTOR,
        EFFLUX,
        False,
        "Efflux to mature HDL; acts downstream of ABCA1. Same absence of agonist "
        "pharmacology.",
    ),
    AxisGene(
        "APOA1",
        "P02647",
        "Apolipoprotein A-I",
        EFFECTOR,
        EFFLUX,
        False,
        "The extracellular acceptor itself. Not a pocket - the therapeutic form of "
        "'more APOA1' is administered protein or peptide, which is the direct-acceptor "
        "arm this step is asked to evaluate against transporter induction.",
    ),
    AxisGene(
        "APOE",
        "P02649",
        "Apolipoprotein E",
        EFFECTOR,
        EFFLUX,
        False,
        "The retina's locally synthesised acceptor: RPE and Mueller glia secrete APOE, "
        "so unlike APOA1 this acceptor need not cross the blood-retinal barrier.",
    ),
    AxisGene(
        "CD36",
        "P16671",
        "Platelet glycoprotein 4",
        SCAVENGER,
        UPTAKE,
        True,
        "Scavenger receptor for oxidised LDL; the principal influx term in RPE and "
        "retinal microglia. Has real small-molecule pharmacology, unlike the other two.",
    ),
    AxisGene(
        "OLR1",
        "P78380",
        "Oxidised low-density lipoprotein receptor 1 (LOX-1)",
        SCAVENGER,
        UPTAKE,
        False,
        "Endothelial oxLDL receptor; induced by hyperglycaemia and the entry route at "
        "the inner blood-retinal barrier.",
    ),
    AxisGene(
        "MSR1",
        "P21757",
        "Macrophage scavenger receptor types I and II (SR-A)",
        SCAVENGER,
        UPTAKE,
        False,
        "Microglial/macrophage uptake of modified lipoprotein; the foam-cell arm.",
    ),
)

BY_SYMBOL = {g.symbol: g for g in AXIS}
SYMBOLS = tuple(g.symbol for g in AXIS)
LIGANDABLE = tuple(g.symbol for g in AXIS if g.ligandable)
EFFLUX_ARM = tuple(g.symbol for g in AXIS if g.arm == EFFLUX)
UPTAKE_ARM = tuple(g.symbol for g in AXIS if g.arm == UPTAKE)
