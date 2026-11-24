"""Gene panel for the retinal PPARA expression query.

The 43 DR panel genes come from ``data/processed/dr_gene_panel.csv`` (built in the
Step 1 data-gap closure).  Everything else here is a control, and the control
design is the point of the exercise:

* ``housekeeping_*``  - the baseline the task asks for, deliberately spanning two
  orders of magnitude.  Comparing a transcription factor to ACTB is a rigged
  comparison; comparing it to TBP or POLR2A is the fair one.
* ``heterodimer_partner`` - PPARA cannot regulate anything except as a
  PPARA::RXR heterodimer, so RXRA/B/G expression caps the functional complex
  independently of PPARA itself.
* ``nr_positive_control`` - nuclear receptors with established retinal
  expression.  These are the class-matched positive control: same molecule
  class, same typical abundance regime, same capture chemistry.
* ``druggable_positive_control`` - receptors that are the target of an actually
  marketed retinal drug (KDR/FLT1 for anti-VEGF), i.e. the empirical answer to
  "what does a druggable retinal target look like in these data".
* ``celltype_marker`` - annotation sanity check.
* ``negative_control`` - genes that should not be in retina at all.  These set
  the ambient-contamination / index-hopping floor, without which "2% of cells
  express PPARA" cannot be called detection.
* ``fgf21_receptor`` - the machinery a circulating FGF21 signal has to land on.
  FGF21 is the one PPARA effector that acts at a distance, so the hepatic-to-
  retinal relay in the DR analysis depends entirely on whether retina can
  receive it.  Added for the FGF21 concentration bridge
  (``docs/notes/fgf21-concentration-bridge.md``): KLB is the obligate co-receptor
  that confers FGF21 specificity on an otherwise promiscuous FGFR, so a retina
  without KLB cannot respond to FGF21 at any plasma concentration.  ADIPOQ /
  ADIPOR1 / ADIPOR2 are here because the published retinal protection is
  adiponectin-dependent, i.e. a second relay downstream of the first.
* ``barrier_transport`` - the transporters that set ``Kp,uu`` at the
  blood-retinal barrier for an anionic drug.  Added for the retinal exposure
  model (``docs/notes/retinal-exposure-model.md``).  Passive permeability
  cancels out of a steady-state partition ratio; what does not cancel is active
  efflux, so the fibrate exposure question reduces to which of these pumps the
  human retina actually expresses.  SLCO1B1/SLCO1B3 are here for the opposite
  reason: they are the hepatic uptake transporters that make pemafibrate
  hepatoselective, and if the retina lacks them then the property that makes
  the drug work in liver is the property that denies it the eye.
"""

import csv
import pathlib

_REPO = pathlib.Path(__file__).resolve().parents[3]
PANEL_CSV = _REPO / "data" / "processed" / "dr_gene_panel.csv"

CONTROLS: dict[str, str] = {
    # housekeeping - detection ceiling
    "ACTB": "housekeeping_high",
    "GAPDH": "housekeeping_high",
    "RPL13A": "housekeeping_high",
    "B2M": "housekeeping_high",
    # housekeeping - mid
    "PPIA": "housekeeping_mid",
    "UBC": "housekeeping_mid",
    "SDHA": "housekeeping_mid",
    # housekeeping - low, the fair scale for a transcription factor
    "TBP": "housekeeping_low",
    "POLR2A": "housekeeping_low",
    "HPRT1": "housekeeping_low",
    # obligate PPAR heterodimer partners
    "RXRA": "heterodimer_partner",
    "RXRB": "heterodimer_partner",
    "RXRG": "heterodimer_partner",
    # class-matched nuclear receptor positive controls
    "NR2E3": "nr_positive_control",
    "THRB": "nr_positive_control",
    "RORB": "nr_positive_control",
    "NR1H2": "nr_positive_control",
    "NR1H3": "nr_positive_control",
    "NR2F1": "nr_positive_control",
    "NR2F2": "nr_positive_control",
    "NR1D1": "nr_positive_control",
    "VDR": "nr_positive_control",
    "RARA": "nr_positive_control",
    "RARB": "nr_positive_control",
    "ESRRA": "nr_positive_control",
    # druggable retinal receptor positive controls
    "RHO": "druggable_positive_control",
    "FLT1": "druggable_positive_control",
    "ADRB2": "druggable_positive_control",
    "GRK1": "druggable_positive_control",
    # cell identity markers
    "ARR3": "celltype_marker",
    "PDE6H": "celltype_marker",
    "RLBP1": "celltype_marker",
    "GLUL": "celltype_marker",
    "RPE65": "celltype_marker",
    "BEST1": "celltype_marker",
    "TTR": "celltype_marker",
    "PECAM1": "celltype_marker",
    "CLDN5": "celltype_marker",
    "P2RY12": "celltype_marker",
    "AIF1": "celltype_marker",
    "RBPMS": "celltype_marker",
    "NEFL": "celltype_marker",
    "GFAP": "celltype_marker",
    "VWF": "celltype_marker",
    "GAD1": "celltype_marker",
    "ONECUT1": "celltype_marker",
    # FGF21 receptor module - can retina receive a circulating FGF21 signal?
    "KLB": "fgf21_receptor",
    "FGFR1": "fgf21_receptor",
    "FGFR2": "fgf21_receptor",
    "FGFR3": "fgf21_receptor",
    "FGFR4": "fgf21_receptor",
    "ADIPOQ": "fgf21_receptor",
    "ADIPOR1": "fgf21_receptor",
    "ADIPOR2": "fgf21_receptor",
    # blood-retinal barrier transport - what sets Kp,uu for an anionic drug
    "ABCG2": "barrier_transport",  # BCRP, apical efflux of anions
    "ABCB1": "barrier_transport",  # P-gp / MDR1
    "ABCC1": "barrier_transport",  # MRP1
    "ABCC4": "barrier_transport",  # MRP4, organic anion efflux
    "ABCC5": "barrier_transport",  # MRP5
    "SLC22A8": "barrier_transport",  # OAT3 - measured retina-to-blood efflux at rat iBRB
    "SLC22A6": "barrier_transport",  # OAT1
    "SLC22A11": "barrier_transport",  # OAT4
    "SLCO1A2": "barrier_transport",  # OATP1A2
    "SLCO2B1": "barrier_transport",  # OATP2B1
    "SLCO1B1": "barrier_transport",  # OATP1B1 - hepatic uptake, pemafibrate hepatoselectivity
    "SLCO1B3": "barrier_transport",  # OATP1B3
    "SLCO3A1": "barrier_transport",
    "SLCO4A1": "barrier_transport",
    "SLC16A1": "barrier_transport",  # MCT1, monocarboxylate
    # negative controls - ambient / mis-assignment floor
    "ALB": "negative_control",
    "INS": "negative_control",
    "MYH7": "negative_control",
    "PRM1": "negative_control",
    "CELA3A": "negative_control",
    "KRT1": "negative_control",
}


def load_panel() -> dict[str, str]:
    """gene symbol -> role, for the 43-gene DR panel."""
    out: dict[str, str] = {}
    with open(PANEL_CSV, newline="") as fh:
        for row in csv.DictReader(fh):
            out[row["gene"]] = row["role"]
    return out


def all_genes() -> dict[str, str]:
    """gene symbol -> category.  Panel roles win over control categories."""
    genes = dict(CONTROLS)
    genes.update(load_panel())
    return genes
