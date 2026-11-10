"""Direct extracellular acceptor versus transporter inducer.

The brief states the lesion as a two-compartment system and draws the
consequence: burden is influx over clearance, and *as clearance approaches
zero the system has no steady state*.  It integrates, and a supply-lowering
agent buys only delay.  This module writes that down and solves it, because
the conclusion turns on a structural property of the two interventions that
an argument can assert but only algebra can settle.

The model
---------
Let ``L`` be retinal lipid burden (free + esterified cholesterol in RPE and
microglia, arbitrary units).  Three terms move it::

    dL/dt  =  J_in  -  k_t * E * L  -  k_a * A * L

``J_in``  influx: scavenger-mediated uptake of modified lipoprotein.  The 29
          compounds the analysis considered act here, lowering ``J_in``.
``k_t*E`` transporter-mediated efflux.  ``E`` is ABCA1/ABCG1 activity relative
          to healthy retina, and the lesion is that ``E`` is driven toward
          zero: oxidised-LDL loading and the inflammasome suppress ABCA1.
          **A transporter inducer multiplies E.**
``k_a*A`` direct removal by an administered extracellular acceptor at
          concentration ``A`` -- an apoA-I mimetic peptide, reconstituted HDL,
          or a cyclodextrin.  **An acceptor adds a term.**

That difference is the whole argument.  Steady state is::

    L_ss = J_in / (k_t*E + k_a*A)

so with no acceptor, ``L_ss = J_in / (k_t*E)``, which diverges as ``E -> 0``:
there is no steady state, and burden grows without bound at rate ``J_in``.
Multiplying a vanishing ``E`` by an inducer's fold-induction ``F`` gives
``J_in / (k_t*E*F)`` -- still divergent, merely divided by F.  **An inducer
cannot rescue a compartment whose transporter is off, however potent it is,
because it scales a term that is already zero.**  An acceptor sets a floor
``L_ss <= J_in / (k_a*A)`` that holds at ``E = 0`` exactly.

A supply-lowering agent scales ``J_in``.  At ``E -> 0`` that multiplies a
divergent quantity by a constant below one: it lowers the slope of an
unbounded ramp, which is delay, not control.  The brief's claim is therefore
exactly right, and the ordering it says the analysis carried -- inducer
preferred over acceptor -- is backwards *in the regime that defines the
disease*.

The qualification that matters
------------------------------
The argument depends on ``E`` actually being near zero, and on ``k_a*A`` being
reachable in the retina.  Both are stated here as declared ranges rather than
assumed: ``E`` is swept across the whole interval, and the acceptor term is
reported as the ``k_a*A`` needed to hold burden at a target, so that a reader
can ask whether that is deliverable instead of being told that it is.

ApoA-I mimetic peptides and cyclodextrins are not small molecules that cross
the blood-retinal barrier.  The acceptor route is therefore an *intravitreal*
proposition, which is a different development path from an oral fibrate -- but
it is the path the retina already uses: the eye is dosed intravitreally as
standard of care for this exact disease.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

# Transporter activity relative to healthy retina.  The lesion drives this
# down; how far is unmeasured in human retina, so the sweep spans the range.
E_GRID = (1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01, 0.0)

# Fold induction an LXR agonist achieves on ABCA1/ABCG1 at full engagement.
# 2-5x is the usual cell-culture range for a potent LXR agonist; 10x is
# generous.  ASSUMED -- no measurement in retinal cells at achievable
# concentration exists.
INDUCTION_FOLD = (1.0, 3.0, 10.0)

# Fractional reduction in influx from a supply-lowering agent -- the arm the
# 29 compounds occupy.  0.5 is a strong effect for a systemic agent.
INFLUX_REDUCTION = (1.0, 0.5)

# Acceptor-mediated clearance relative to healthy transporter clearance.
ACCEPTOR_REL = (0.0, 0.1, 0.5, 1.0)

J_IN = 1.0  # influx, normalised
K_T = 1.0  # healthy transporter clearance rate constant, normalised


def steady_state(j_in: float, k_t_e: float, k_a_a: float) -> float:
    """Burden at steady state; ``inf`` when total clearance is zero."""
    cl = k_t_e + k_a_a
    return np.inf if cl <= 0 else j_in / cl


def time_to_threshold(
    j_in: float, k_t_e: float, k_a_a: float, threshold: float, l0: float = 1.0
) -> float:
    """Time for burden to reach ``threshold`` from ``l0``.

    With clearance ``c = k_t*E + k_a*A`` the solution of the linear ODE is
    ``L(t) = J/c + (L0 - J/c) e^{-ct}``, so the threshold is reached only if
    the steady state lies above it.  At ``c = 0`` burden ramps linearly,
    ``L(t) = L0 + J t``, and the time is finite for every threshold -- which
    is the formal statement of "a supply-lowering agent buys only delay".
    """
    c = k_t_e + k_a_a
    if c <= 0:
        return (threshold - l0) / j_in if j_in > 0 else np.inf
    ss = j_in / c
    if ss <= threshold:
        return np.inf  # controlled: never reaches the threshold
    return -np.log((threshold - ss) / (l0 - ss)) / c


def sweep(threshold: float = 5.0) -> pd.DataFrame:
    """Every combination of the three interventions across the ``E`` grid.

    ``threshold`` is the burden at which the lesion is taken to be established
    (5x the healthy steady state).  ``time_to_threshold`` is reported in units
    of 1/k_t -- the time a healthy retina takes to clear one burden unit -- so
    the comparison is dimensionless and does not pretend to a calendar.
    """
    rows = []
    for e in E_GRID:
        for fold in INDUCTION_FOLD:
            for infl in INFLUX_REDUCTION:
                for arel in ACCEPTOR_REL:
                    j = J_IN * infl
                    k_t_e = K_T * e * fold
                    k_a_a = K_T * arel
                    ss = steady_state(j, k_t_e, k_a_a)
                    rows.append(
                        {
                            "transporter_activity_E": e,
                            "inducer_fold": fold,
                            "influx_fraction": infl,
                            "acceptor_rel_clearance": arel,
                            "arm": _arm(fold, infl, arel),
                            "steady_state_burden": ss,
                            "controlled": bool(np.isfinite(ss) and ss <= threshold),
                            "time_to_threshold": time_to_threshold(
                                j, k_t_e, k_a_a, threshold
                            ),
                        }
                    )
    return pd.DataFrame(rows)


def _arm(fold: float, infl: float, arel: float) -> str:
    parts = []
    if fold > 1:
        parts.append(f"inducer x{fold:g}")
    if infl < 1:
        parts.append(f"influx x{infl:g}")
    if arel > 0:
        parts.append(f"acceptor {arel:g}")
    return " + ".join(parts) if parts else "untreated"


def headline(threshold: float = 5.0) -> pd.DataFrame:
    """The comparison the verdict rests on, at a collapsed transporter.

    Holds ``E`` at 0.02 -- a transporter at 2% of healthy, which is the regime
    the lesion describes -- and asks what each single-agent arm achieves.
    """
    e = 0.02
    rows = []
    for label, fold, infl, arel in (
        ("untreated", 1.0, 1.0, 0.0),
        ("supply-lowering agent (the 29 compounds)", 1.0, 0.5, 0.0),
        ("transporter inducer, 3x", 3.0, 1.0, 0.0),
        ("transporter inducer, 10x", 10.0, 1.0, 0.0),
        ("direct acceptor, 0.1x healthy clearance", 1.0, 1.0, 0.1),
        ("direct acceptor, 0.5x healthy clearance", 1.0, 1.0, 0.5),
        ("acceptor 0.1 + inducer 3x", 3.0, 1.0, 0.1),
    ):
        j, k_t_e, k_a_a = J_IN * infl, K_T * e * fold, K_T * arel
        ss = steady_state(j, k_t_e, k_a_a)
        rows.append(
            {
                "arm": label,
                "steady_state_burden": round(ss, 2) if np.isfinite(ss) else np.inf,
                "fold_vs_untreated": (
                    round(ss / (J_IN / (K_T * e)), 3) if np.isfinite(ss) else np.nan
                ),
                "controlled_at_threshold": bool(np.isfinite(ss) and ss <= threshold),
            }
        )
    return pd.DataFrame(rows)


def zero_transporter() -> pd.DataFrame:
    """The limiting case: ``E = 0`` exactly.

    This is the table that settles the ordering.  Every arm that works by
    multiplying ``E`` returns an infinite burden, regardless of how large the
    multiplier is; the acceptor arm returns a finite number.
    """
    rows = []
    for label, fold, infl, arel in (
        ("untreated", 1.0, 1.0, 0.0),
        ("supply-lowering agent, influx halved", 1.0, 0.5, 0.0),
        ("supply-lowering agent, influx cut 10x", 1.0, 0.1, 0.0),
        ("transporter inducer, 10x", 10.0, 1.0, 0.0),
        ("transporter inducer, 1000x", 1000.0, 1.0, 0.0),
        ("direct acceptor, 0.1x healthy clearance", 1.0, 1.0, 0.1),
    ):
        j, k_t_e, k_a_a = J_IN * infl, 0.0 * fold, K_T * arel
        ss = steady_state(j, k_t_e, k_a_a)
        rows.append(
            {
                "arm": label,
                "steady_state_burden": ss,
                "time_to_5x_threshold": time_to_threshold(j, k_t_e, k_a_a, 5.0),
            }
        )
    return pd.DataFrame(rows)


def crossover_E(acceptor_rel: float, inducer_fold: float) -> float:
    """Transporter activity below which the acceptor beats the inducer.

    The two arms contribute ``k_t*E*F`` and ``k_a*A`` to total clearance, so
    the inducer's *incremental* clearance over no treatment is
    ``k_t*E*(F - 1)`` and the acceptor's is ``k_a*A``.  They cross where

        E*  =  (k_a*A) / (k_t * (F - 1))

    Above ``E*`` the inducer contributes more; below it the acceptor does, and
    at ``E = 0`` the inducer contributes nothing at all for any ``F``.  This
    is the precise form of the verdict: the ordering is not simply backwards,
    it *inverts* at a transporter activity this function names.
    """
    if inducer_fold <= 1:
        return np.inf
    return float((K_T * acceptor_rel) / (K_T * (inducer_fold - 1)))


def crossover_table() -> pd.DataFrame:
    rows = []
    for arel in (0.05, 0.1, 0.25, 0.5):
        for fold in (2.0, 3.0, 5.0, 10.0):
            rows.append(
                {
                    "acceptor_rel_clearance": arel,
                    "inducer_fold": fold,
                    "crossover_E": round(crossover_E(arel, fold), 4),
                    "note": "acceptor wins below this transporter activity",
                }
            )
    return pd.DataFrame(rows)
