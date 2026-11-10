"""The four compounds, with every PK and physicochemical input sourced.

Plasma exposure is taken from the FDA label wherever one exists, because a
label PK table is the one number in this literature that has been audited by
someone whose job was to disbelieve it.  Pemafibrate has no FDA label (it is
approved in Japan only), so its exposure comes from a published steady-state
clinical pharmacology study and is cross-checked against the figure the
PARMODIA package insert reports.

Average steady-state concentration is derived as ``AUC(0-tau) / tau`` rather
than taken as Cmax, because a nuclear receptor at steady state sees the
average, not the peak.  Cmax is carried alongside so the margin can be quoted
both ways -- the peak is the best case and it is reported as such.
"""

from __future__ import annotations

import dataclasses
import math

from .parameters import ASSUMED, CONVERTED, MEASURED, Param


def _cv_to_ci(median: float, cv: float) -> tuple[float, float]:
    """95% interval of a lognormal with the given median and coefficient of
    variation.  Labels report CV%, the model needs an interval."""
    sigma = math.sqrt(math.log(1.0 + cv * cv))
    return median * math.exp(-1.959963984540054 * sigma), median * math.exp(
        1.959963984540054 * sigma
    )


@dataclasses.dataclass(frozen=True)
class Compound:
    key: str
    name: str
    chembl: str
    mw: float  # g/mol
    logp: float  # neutral-species logP
    pka: Param  # acidic pKa
    dose_mg: float  # mg/day at the labelled dose
    c_avg: Param  # total plasma concentration, ng/mL, average over tau
    c_max: Param  # total plasma concentration, ng/mL, peak
    fu_plasma: Param  # fraction unbound in human plasma
    ec50_gene: str  # the receptor the DR analysis cares about
    pk_source: str
    note: str = ""

    def c_avg_nM(self, ng_ml: float) -> float:
        return ng_ml * 1000.0 / self.mw


# --- ionisation ------------------------------------------------------------
# No experimental pKa is published for any of these four in PubChem's
# experimental-properties record, in ChEMBL (the ChemAxon-derived cx_most_apka
# and cx_logd fields now return null for every one of them), or in the papers
# reached by this search.  So pKa is ASSUMED, from the measured values of the
# unsubstituted parent acids of each headgroup -- phenoxyacetic acid pKa ~3.17,
# 2-aryloxy-2-methylpropanoic acids ~3.1-3.2 -- with a range wide enough to
# cover substituent effects.
#
# Internal check: the step description states logD(7.4) "roughly -0.5 against a
# nominal logP near 3.8".  With logP 3.81 (ChEMBL alogp for fenofibric acid),
# that figure is reproduced only at pKa 3.1:
#     logD = 3.81 - log10(1 + 10^(7.4 - 3.1)) = 3.81 - 4.30 = -0.49
# so the chemotype assignment and the brief's own number agree.

_PKA_ARYLOXY_DIMETHYL = dict(
    units="pKa",
    provenance=ASSUMED,
    source="measured pKa of the unsubstituted 2-aryloxy-2-methylpropanoic acid headgroup (~3.1-3.2); "
    "reproduces the brief's logD(7.4) = -0.5 at logP 3.81",
)
_PKA_ARYLOXY_ALKYL = dict(
    units="pKa",
    provenance=ASSUMED,
    source="2-aryloxybutanoic acid; alpha-alkyl substitution raises pKa slightly vs the acetic parent",
)
_PKA_ARYLOXYACETIC = dict(
    units="pKa",
    provenance=ASSUMED,
    source="phenoxyacetic acid measured pKa 3.17",
)


# --- the four compounds ----------------------------------------------------

_FFA_CAVG = 135.0 / (1.1 * 24.0) * 1000.0  # mg/day / (CL/F x tau) -> ng/mL

FENOFIBRIC_ACID = Compound(
    key="fenofibric_acid",
    name="Fenofibric acid",
    chembl="CHEMBL981",
    mw=318.76,
    logp=3.81,
    pka=Param.uniform("pka.fenofibric_acid", 2.8, 3.5, **_PKA_ARYLOXY_DIMETHYL),
    dose_mg=135.0,
    # Trilipix gives CL/F = 1.1 L/h but no Cmax in mass units, so Cavg is
    # CONVERTED from the label's own clearance.  The interval is widened above
    # a plain 40% CV to span the independently published Cmax 10-15 µg/mL /
    # trough 4-6 µg/mL band for 200 mg fenofibrate, which implies Cavg 6-8.
    c_avg=Param.lognormal_ci(
        "c_avg.fenofibric_acid",
        _FFA_CAVG,
        2600.0,
        11000.0,
        units="ng/mL",
        provenance=CONVERTED,
        source="Trilipix FDA label 12.3: CL/F 1.1 L/h, 135 mg/day -> 5114 ng/mL; "
        "interval spans the published Cmax 10-15 / trough 4-6 µg/mL band",
    ),
    c_max=Param.lognormal_ci(
        "c_max.fenofibric_acid",
        12000.0,
        7000.0,
        20000.0,
        units="ng/mL",
        provenance=MEASURED,
        source="published fenofibric acid Cmax after 200 mg micronised fenofibrate (label-equivalent dose)",
    ),
    fu_plasma=Param.lognormal_ci(
        "fu.fenofibric_acid",
        0.010,
        0.005,
        0.020,
        units="fraction",
        provenance=MEASURED,
        source="Trilipix FDA label 12.3: 'Serum protein binding is approximately 99%'; "
        "interval allows the rounding implied by 'approximately'",
    ),
    ec50_gene="PPARA",
    pk_source="Trilipix (fenofibric acid) FDA label, DailyMed setid 3057fc9c-ff77-43eb-b687-776660423742",
)

PEMAFIBRATE = Compound(
    key="pemafibrate",
    name="Pemafibrate",
    chembl="CHEMBL247951",
    mw=490.56,
    logp=5.55,
    pka=Param.uniform("pka.pemafibrate", 3.0, 3.7, **_PKA_ARYLOXY_ALKYL),
    dose_mg=0.2,
    c_avg=Param.lognormal_ci(
        "c_avg.pemafibrate",
        6.5 / 24.0,
        *_cv_to_ci(6.5 / 24.0, 0.635),
        units="ng/mL",
        provenance=CONVERTED,
        source="AUC(0-tau) 6.5 ng*h/mL (CV 63.5%), IR 0.2 mg/day fasted, 4 weeks, n=20, PMC11883216 Table",
    ),
    c_max=Param.lognormal_ci(
        "c_max.pemafibrate",
        2.1,
        *_cv_to_ci(2.1, 0.379),
        units="ng/mL",
        provenance=MEASURED,
        source="Cmax,ss 2.1 ng/mL (CV 37.9%), IR 0.2 mg/day fasted, PMC11883216; "
        "PARMODIA insert gives 3.57 ng/mL at the 0.4 mg/day maximum (via PMC9102038), consistent",
    ),
    # No accessible measured value.  Fibrate-class binding spans 95-99.8% and
    # pemafibrate's lipophilicity (alogp 5.55) puts it at the bound end, but
    # this is a prior, not a measurement, and the sensitivity analysis is
    # asked how much it matters.
    fu_plasma=Param.loguniform(
        "fu.pemafibrate",
        0.001,
        0.020,
        units="fraction",
        provenance=ASSUMED,
        source="NO accessible measured value: not in any FDA/EMA label (Japan-only approval) "
        "and not found in PubMed/PMC/Europe PMC; prior spans the fibrate class",
    ),
    ec50_gene="PPARA",
    pk_source="Clinical Pharmacology of Pemafibrate, PMC11883216 (steady state, 4 weeks)",
    note="approved dose in Japan is 0.2 mg/day; PROMINENT used 0.4 mg/day",
)

ELAFIBRANOR = Compound(
    key="elafibranor",
    name="Elafibranor (parent)",
    chembl="CHEMBL3707395",
    mw=384.50,
    logp=5.16,
    pka=Param.uniform("pka.elafibranor", 2.8, 3.5, **_PKA_ARYLOXY_DIMETHYL),
    dose_mg=80.0,
    c_avg=Param.lognormal_ci(
        "c_avg.elafibranor",
        3758.0 / 24.0,
        *_cv_to_ci(3758.0 / 24.0, 1749.0 / 3758.0),
        units="ng/mL",
        provenance=CONVERTED,
        source="AUC(0-24) 3758 (SD 1749) ng*h/mL at steady state, 80 mg QD, PBC patients, Iqirvo label Table 5",
    ),
    c_max=Param.lognormal_ci(
        "c_max.elafibranor",
        802.0,
        *_cv_to_ci(802.0, 443.0 / 802.0),
        units="ng/mL",
        provenance=MEASURED,
        source="Cmax,ss 802 (SD 443) ng/mL, Iqirvo label Table 5",
    ),
    fu_plasma=Param.lognormal_ci(
        "fu.elafibranor",
        0.003,
        0.0015,
        0.006,
        units="fraction",
        provenance=MEASURED,
        source="Iqirvo FDA label 12.3: 'Plasma protein binding of both elafibranor and GFT1007 was "
        "approximately 99.7% (mainly to serum albumin)'",
    ),
    ec50_gene="PPARA",
    pk_source="IQIRVO (elafibranor) FDA label, DailyMed setid d78aa14f-6ec1-4b1d-a4ae-e48658137a25",
)

# GFT1007 carries 3.2x the exposure of the parent and the label calls it the
# major ACTIVE metabolite, so leaving it out would understate elafibranor's
# retinal exposure by most of its total.  Its own PPARalpha EC50 has not been
# measured separately in the ChEMBL record, so it is modelled as equipotent
# with the parent and that is flagged in the note.
GFT1007 = Compound(
    key="gft1007",
    name="GFT1007 (elafibranor active metabolite)",
    chembl="CHEMBL3707395",
    mw=386.52,
    logp=4.60,
    pka=Param.uniform("pka.gft1007", 2.8, 3.5, **_PKA_ARYLOXY_DIMETHYL),
    dose_mg=80.0,
    c_avg=Param.lognormal_ci(
        "c_avg.gft1007",
        11985.0 / 24.0,
        *_cv_to_ci(11985.0 / 24.0, 7149.0 / 11985.0),
        units="ng/mL",
        provenance=CONVERTED,
        source="AUC(0-24) 11985 (SD 7149) ng*h/mL at steady state, 80 mg QD, Iqirvo label Table 5",
    ),
    c_max=Param.lognormal_ci(
        "c_max.gft1007",
        2058.0,
        *_cv_to_ci(2058.0, 459.0 / 2058.0),
        units="ng/mL",
        provenance=MEASURED,
        source="Cmax,ss 2058 (SD 459) ng/mL, Iqirvo label Table 5",
    ),
    fu_plasma=Param.lognormal_ci(
        "fu.gft1007",
        0.003,
        0.0015,
        0.006,
        units="fraction",
        provenance=MEASURED,
        source="Iqirvo FDA label 12.3, 99.7% for both elafibranor and GFT1007",
    ),
    ec50_gene="PPARA",
    pk_source="IQIRVO FDA label Table 5",
    note="logP estimated for the ketone-reduced alcohol; EC50 assumed equal to parent (not separately measured)",
)

SELADELPAR = Compound(
    key="seladelpar",
    name="Seladelpar",
    chembl="CHEMBL230158",
    mw=444.47,
    logp=5.05,
    pka=Param.uniform("pka.seladelpar", 2.8, 3.4, **_PKA_ARYLOXYACETIC),
    dose_mg=10.0,
    c_avg=Param.lognormal_ci(
        "c_avg.seladelpar",
        817.0 / 24.0,
        *_cv_to_ci(817.0 / 24.0, 0.44),
        units="ng/mL",
        provenance=CONVERTED,
        source="AUC 817 ng*h/mL (CV 44%) at steady state, 10 mg QD, PBC patients, Livdelzi label 12.3",
    ),
    c_max=Param.lognormal_ci(
        "c_max.seladelpar",
        90.5,
        *_cv_to_ci(90.5, 0.425),
        units="ng/mL",
        provenance=MEASURED,
        source="median Cmax,ss 90.5 ng/mL (CV 42.5%), Livdelzi label 12.3",
    ),
    fu_plasma=Param.loguniform(
        "fu.seladelpar",
        0.0010,
        0.010,
        units="fraction",
        provenance=MEASURED,
        source="Livdelzi FDA label 12.3: 'Seladelpar plasma protein binding is greater than 99%' -- "
        "a bound, not a value, so the prior runs from the bound downwards",
    ),
    ec50_gene="PPARD",
    pk_source="LIVDELZI (seladelpar lysine) FDA label, DailyMed setid 89f79d98-135c-40b2-a585-6996c04e599c",
    note="PPARdelta-selective: its PPARalpha EC50 is 750x weaker than its PPARdelta EC50, so both are computed",
)

COMPOUNDS = [FENOFIBRIC_ACID, PEMAFIBRATE, ELAFIBRANOR, GFT1007, SELADELPAR]
BY_KEY = {c.key: c for c in COMPOUNDS}

# The compound the barrier model is calibrated on.  Everything else is
# transferred from it, so it has to be the one with a measured ocular
# concentration -- which, for every fibrate in every species, means this one.
REFERENCE = FENOFIBRIC_ACID
