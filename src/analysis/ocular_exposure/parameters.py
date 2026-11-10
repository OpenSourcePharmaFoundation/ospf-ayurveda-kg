"""Every input to the ocular exposure model, as a distribution with provenance.

The rule this module enforces is the one the chain exists to enforce: a number
that enters the model carries a source and an uncertainty, and the three kinds
of number are never conflated.

    MEASURED   read directly from a published result or a regulatory label
    CONVERTED  a measured value transformed by stated arithmetic (units,
               molarity, protein normalisation).  No new assumption
    ASSUMED    a distribution chosen to span a published spread, or a prior
               where no measurement exists.  Judgement, justified at the point
               of use and reported as such

``Param.sample`` is the only way a number reaches the model, so a point
estimate cannot be smuggled in: a parameter with no uncertainty has to be
declared ``point()`` explicitly and shows up as such in the parameter table.
"""

from __future__ import annotations

import dataclasses
import math

import numpy as np

MEASURED = "MEASURED"
CONVERTED = "CONVERTED"
ASSUMED = "ASSUMED"

_Z95 = 1.959963984540054


@dataclasses.dataclass(frozen=True)
class Param:
    """One model input.

    ``kind`` is one of ``lognormal_ci``, ``normal``, ``uniform``,
    ``loguniform`` or ``point``; ``a``/``b``/``c`` are read according to it.
    ``provenance`` is MEASURED / CONVERTED / ASSUMED and ``source`` is the
    citation that a reader has to be able to check.
    """

    name: str
    kind: str
    a: float
    b: float = 0.0
    c: float = 0.0
    units: str = ""
    provenance: str = ASSUMED
    source: str = ""
    note: str = ""

    # -- constructors ----------------------------------------------------
    @staticmethod
    def lognormal_ci(name, median, lo95, hi95, **kw) -> "Param":
        """Lognormal pinned by its median and a 95% interval."""
        return Param(name, "lognormal_ci", median, lo95, hi95, **kw)

    @staticmethod
    def normal(name, mean, sd, **kw) -> "Param":
        return Param(name, "normal", mean, sd, **kw)

    @staticmethod
    def uniform(name, lo, hi, **kw) -> "Param":
        return Param(name, "uniform", lo, hi, **kw)

    @staticmethod
    def loguniform(name, lo, hi, **kw) -> "Param":
        return Param(name, "loguniform", lo, hi, **kw)

    @staticmethod
    def point(name, value, **kw) -> "Param":
        return Param(name, "point", value, **kw)

    # -- use -------------------------------------------------------------
    def ppf(self, u: np.ndarray) -> np.ndarray:
        """Inverse CDF.  Sobol sampling needs the quantile transform, not a
        draw, so everything is defined this way and ``sample`` goes through it.
        """
        u = np.clip(np.asarray(u, dtype=float), 1e-12, 1 - 1e-12)
        if self.kind == "point":
            return np.full_like(u, self.a)
        if self.kind == "uniform":
            return self.a + u * (self.b - self.a)
        if self.kind == "loguniform":
            return np.exp(math.log(self.a) + u * (math.log(self.b) - math.log(self.a)))
        if self.kind == "normal":
            return self.a + self.b * _norm_ppf(u)
        if self.kind == "lognormal_ci":
            mu = math.log(self.a)
            # The interval is not required to be symmetric in log space; take
            # the wider half so the stated CI is covered rather than clipped.
            sig = max(
                (math.log(self.c) - mu) / _Z95,
                (mu - math.log(self.b)) / _Z95,
            )
            return np.exp(mu + sig * _norm_ppf(u))
        raise ValueError(f"unknown distribution kind {self.kind!r}")

    def sample(self, rng: np.random.Generator, n: int) -> np.ndarray:
        return self.ppf(rng.random(n))

    def summary(self) -> str:
        if self.kind == "point":
            return f"{self.a:g}"
        if self.kind in ("uniform", "loguniform"):
            return f"{self.a:g} - {self.b:g}"
        if self.kind == "normal":
            return f"{self.a:g} ± {self.b:g} (SD)"
        return f"{self.a:g} [{self.b:g} - {self.c:g}]"


def _norm_ppf(u: np.ndarray) -> np.ndarray:
    """Standard-normal inverse CDF (Acklam), so the package needs no scipy."""
    a = [
        -3.969683028665376e01,
        2.209460984245205e02,
        -2.759285104469687e02,
        1.383577518672690e02,
        -3.066479806614716e01,
        2.506628277459239e00,
    ]
    b = [
        -5.447609879822406e01,
        1.615858368580409e02,
        -1.556989798598866e02,
        6.680131188771972e01,
        -1.328068155288572e01,
    ]
    c = [
        -7.784894002430293e-03,
        -3.223964580411365e-01,
        -2.400758277161838e00,
        -2.549732539343734e00,
        4.374664141464968e00,
        2.938163982698783e00,
    ]
    d = [
        7.784695709041462e-03,
        3.224671290700398e-01,
        2.445134137142996e00,
        3.754408661907416e00,
    ]
    plow, phigh = 0.02425, 1 - 0.02425
    q = np.empty_like(u)

    lo = u < plow
    if lo.any():
        t = np.sqrt(-2 * np.log(u[lo]))
        q[lo] = (
            ((((c[0] * t + c[1]) * t + c[2]) * t + c[3]) * t + c[4]) * t + c[5]
        ) / ((((d[0] * t + d[1]) * t + d[2]) * t + d[3]) * t + 1)
    hi = u > phigh
    if hi.any():
        t = np.sqrt(-2 * np.log(1 - u[hi]))
        q[hi] = -(
            ((((c[0] * t + c[1]) * t + c[2]) * t + c[3]) * t + c[4]) * t + c[5]
        ) / ((((d[0] * t + d[1]) * t + d[2]) * t + d[3]) * t + 1)
    mid = ~(lo | hi)
    if mid.any():
        t = u[mid] - 0.5
        r = t * t
        q[mid] = (
            (((((a[0] * r + a[1]) * r + a[2]) * r + a[3]) * r + a[4]) * r + a[5])
            * t
            / (((((b[0] * r + b[1]) * r + b[2]) * r + b[3]) * r + b[4]) * r + 1)
        )
    return q


# ---------------------------------------------------------------------------
# 1.  The calibration anchor: the only measured ocular concentration of any
#     fibrate after SYSTEMIC dosing, in any species.
#
#     Huang et al. 2021, Biology (Basel) 10(12):1328, PMID 34943243,
#     PMCID PMC8698460, Table 1.  C57BL/6J mice, fenofibrate 2 mg/kg/day
#     intraperitoneally for 7 days, LC-MS 6 h after the final dose.
#
#     Both the tissue and the plasma column are reported in "ng/mg of total
#     protein".  That the two are on one common scale is not an assumption:
#     the paper's own Discussion divides choroid by plasma -- 8.469 / 1.726 =
#     4.9 -- and calls the result "approximately five-fold higher than the
#     concentration in the peripheral blood".  The authors take the ratio
#     directly, so the units are common.
# ---------------------------------------------------------------------------

ANCHOR = {
    "retina_ffa": Param.normal(
        "anchor.retina_ffa",
        0.140,
        0.044,
        units="ng/mg total protein",
        provenance=MEASURED,
        source="Huang 2021 PMC8698460 Table 1, vitreous/retina, IP arm (mean ± SEM, n=5-12)",
        note="pooled vitreous + retina, not retina alone -- see barrier.py",
    ),
    "plasma_ffa": Param.normal(
        "anchor.plasma_ffa",
        86.304,
        22.780,
        units="ng/mg total protein",
        provenance=MEASURED,
        source="Huang 2021 PMC8698460 Table 1, plasma, IP arm (mean ± SEM)",
    ),
    # Geometry needed to turn a per-protein number for a POOLED vitreous+retina
    # sample into a free concentration.  Vitreous carries drug but almost no
    # protein, so it inflates a per-protein figure; ignoring it would overstate
    # retinal exposure.
    "retina_protein_mg": Param.uniform(
        "anchor.retina_protein_mg",
        0.20,
        0.45,
        units="mg protein / mouse retina",
        provenance=ASSUMED,
        source="spans the range quoted for adult mouse neural retina (~2.5-3.5 mg wet, ~10% protein)",
    ),
    "vitreous_vol_ul": Param.uniform(
        "anchor.vitreous_vol_ul",
        4.4,
        6.0,
        units="µL",
        provenance=ASSUMED,
        source="adult mouse vitreous volume, published range",
    ),
    "retina_vol_ul": Param.uniform(
        "anchor.retina_vol_ul",
        2.2,
        3.5,
        units="µL",
        provenance=ASSUMED,
        source="adult mouse neural retina wet weight 2.3-3.7 mg at ~1.05 g/mL",
    ),
    "plasma_protein_mouse": Param.uniform(
        "anchor.plasma_protein_mouse",
        45.0,
        65.0,
        units="mg/mL",
        provenance=ASSUMED,
        source="mouse total plasma protein, published reference interval",
    ),
    "fu_plasma_mouse_ffa": Param.lognormal_ci(
        "anchor.fu_plasma_mouse_ffa",
        0.010,
        0.004,
        0.030,
        units="fraction",
        provenance=ASSUMED,
        source="human fenofibric acid fu = 0.01 (Trilipix label); spread allows a 3x species difference either way",
    ),
    "fu_tissue_retina": Param.uniform(
        "anchor.fu_tissue_retina",
        0.15,
        0.80,
        units="fraction",
        provenance=ASSUMED,
        source="free fraction of an anion in a low-lipid neural tissue homogenate; no fibrate value exists",
    ),
    # A single 6 h time point on a falling plasma curve is not a steady-state
    # ratio.  For a slowly-equilibrating tissue the late ratio overstates
    # Kp,uu; the prior is therefore centred at 1 but skewed to >1.
    "late_sample_bias": Param.lognormal_ci(
        "anchor.late_sample_bias",
        1.3,
        0.7,
        3.0,
        units="x",
        provenance=ASSUMED,
        source="direction argued from PK first principles; magnitude is judgement",
        note="divides the measured ratio",
    ),
}


# ---------------------------------------------------------------------------
# 2.  Barrier transfer between compounds.
# ---------------------------------------------------------------------------

BARRIER = {
    # Passive transcellular permeability rises with logD but sub-linearly in
    # this lipophilicity range.  The slope is carried as an uncertainty
    # because it is the whole basis for transferring the fenofibric-acid
    # anchor to the other three compounds.
    "perm_logd_slope": Param.uniform(
        "barrier.perm_logd_slope",
        0.30,
        1.00,
        units="d log10 P / d logD",
        provenance=ASSUMED,
        source="typical slope of log Papp vs logD within a congeneric series",
    ),
    "perm_mw_slope": Param.uniform(
        "barrier.perm_mw_slope",
        0.000,
        0.010,
        units="d log10 P / Da",
        provenance=ASSUMED,
        source="size penalty on passive permeability; 0 = none, 0.01 = strong",
        note="applied as -slope x (MW - MW_ref)",
    ),
    # What fraction of the reference compound's net retinal clearance is
    # active efflux rather than bulk flow out of the eye.  Only the efflux
    # part is compound-specific, so this sets how much of the calibrated
    # anchor is allowed to move when the compound changes.
    "efflux_share": Param.uniform(
        "barrier.efflux_share",
        0.0,
        1.0,
        units="fraction of CL_other",
        provenance=ASSUMED,
        source="unmeasured split between active efflux and bulk flow at the BRB",
    ),
    # Relative affinity of each compound for the barrier efflux pumps, versus
    # fenofibric acid.  Nobody has measured any of these for any fibrate at
    # any ocular barrier.  This is the honest "we do not know" in the model
    # and the sensitivity analysis is asked to rank it.
    "efflux_rel": Param.loguniform(
        "barrier.efflux_rel",
        0.2,
        5.0,
        units="x vs fenofibric acid",
        provenance=ASSUMED,
        source="no fibrate efflux-ratio measurement exists at any ocular barrier",
    ),
    # Fraction of luminal free concentration retained inside the endothelial
    # cytosol, after ATP-driven efflux back to blood.  Human retinal vascular
    # endothelium expresses ABCB1 507 nCPM, ABCC4 178, ABCG2 142
    # (data/processed/retina_hpa_celltype_ncpm.tsv), so this is well below 1,
    # but no fibrate is a confirmed substrate of any of them.
    "endo_retention": Param.loguniform(
        "barrier.endo_retention",
        0.10,
        1.00,
        units="fraction",
        provenance=ASSUMED,
        source="bounded by measured ABC transporter abundance in human retinal endothelium; no substrate data",
    ),
    # RPE is the one compartment that can exceed plasma free concentration:
    # it expresses the concentrative organic-anion UPTAKE transporters OAT3
    # (SLC22A8, 465 nCPM) and OAT1 (SLC22A6, 64 nCPM) alongside the efflux
    # pump ABCC5 (823 nCPM).  Net direction is genuinely unknown, so the prior
    # spans both sides of unity.
    "rpe_net": Param.loguniform(
        "barrier.rpe_net",
        0.10,
        10.0,
        units="x plasma free",
        provenance=ASSUMED,
        source="measured OAT1/OAT3/ABCC5 abundance in human RPE; net transport direction unmeasured",
    ),
}


# ---------------------------------------------------------------------------
# 3.  Assay conditions behind a published EC50.
# ---------------------------------------------------------------------------

ASSAY = {
    # Serum content of the medium the ligand was actually dosed into.  The one
    # PPAR transactivation protocol in this literature that states it in full
    # (Kamata 2022, PMC9102038: cells in DMEM + 1% FBS, ligand added in 25 µL
    # serum-free DMEM into 100 µL, i.e. ~0.7% final) sits at the bottom of the
    # usual 1-10% range.  Most ChEMBL assay descriptions state nothing, so the
    # prior spans the range and the correction is reported with that spread
    # rather than applied as a single factor.
    "serum_fraction": Param.loguniform(
        "assay.serum_fraction",
        0.005,
        0.10,
        units="fraction of neat serum",
        provenance=ASSUMED,
        source="0.7% measured for the one fully-specified PPAR protocol (PMC9102038); 10% is the common default",
    ),
    "fbs_albumin_ratio": Param.uniform(
        "assay.fbs_albumin_ratio",
        0.40,
        0.75,
        units="x human plasma albumin",
        provenance=ASSUMED,
        source="bovine serum albumin ~20-30 g/L vs human plasma albumin ~40-45 g/L",
    ),
}


def table(group: dict[str, Param]) -> list[tuple[str, str, str, str, str]]:
    """Rows for the parameter table in the note."""
    return [
        (p.name, p.summary(), p.units, p.provenance, p.source) for p in group.values()
    ]


# Calculated-logP error.  Every logP in ``compounds.py`` is ChEMBL ``alogp``;
# none of the four compounds has a published shake-flask logP.  Only the
# difference from the reference compound enters the model, so a single error
# term on that difference is carried.
LOGP_ERROR = Param.normal(
    "compound.logp",
    0.0,
    0.7,
    units="log units",
    provenance=ASSUMED,
    source="typical RMSE of a calculated logP against experiment; no measured logP exists for these four",
)
