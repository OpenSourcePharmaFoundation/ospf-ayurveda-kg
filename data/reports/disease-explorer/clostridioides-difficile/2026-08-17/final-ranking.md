# Final Candidate Ranking — CDI Drug Discovery Pipeline

Source: `agents/p3-ranker.md` (646 lines, lexicographic gate architecture)

## Methodology Change

The Ranker replaced weighted averaging with a **lexicographic gate architecture** after the Devil's Advocate established that averaging was the pipeline's most serious defect. Efficacy evidence (`E`) is the dominant anchor, with bounded modifiers (`A` axis allocation, `D` durability, `I` immunocompromised usability, `F` feasibility) that can reorder within a tier but never overturn a tier gap. A multiplicative coupling filter (`K`) penalizes candidates where efficacy and toxicity share a single molecular property.

## Final Ranking

| # | Candidate | Composite | E | ΣM | K | Tier | Axis |
|---|-----------|-----------|---|-----|---|------|------|
| — | Fidaxomicin (SOC) | 9.0–9.5 | 8.5+ | +1.0 | 1.0 | Benchmark | C2·C3·C8 |
| **1** | **Ribaxamase** | **7.9** | 8.5→EV | +1.2 | 1.00 | FUND (gated) | **C7** |
| **2** | **CamSA** (NCE) | **6.9** | 5.5 | +1.1 | **1.05** | FUND (gated) | **C1** |
| **3** | **Niclosamide** | **6.4** | 6.5 | +1.0 | **0.85** | FUND (gated) | C4 |
| 4 | Ibezapolstat | 5.4 | 6.0 | −0.6 | 1.00 | Buy option | C2 |
| 5 | Berberine | 5.3 | 6.5 | −0.6 | 0.90 | Buy option | C5 |
| 6 | UDCA | 4.2 | 3.0 | +1.4 | 0.95 | Buy option | C1 |
| 7 | Nitazoxanide | 4.0 | 5.0 | −1.0 | 1.00 | Buy option | C2 |
| 8 | HCQ | 3.7 | 2.5 | +1.2 | 1.00 | Buy option | C4 |
| 9-12 | Chenodiol, TUDCA, Colostrum/IgY, Urso-CamSA | 2.6–3.3 | — | — | — | Free rider | — |
| 13 | Aprepitant | 0.9 | — | — | — | KILL | — |
| 14 | Ebselen | 0.8 | — | — | — | KILL | — |
| 15 | Conessine | 0.0 | — | — | — | KILL | — |
| — | Bezlotoxumab | WITHDRAWN | — | — | — | — | C4→vacated |

## Single Best Programme: Ribaxamase (gated on $150–300K diligence)

Escapes all five field-wide CDI failure modes structurally. Only asset with positive human Phase 2b. Only C7 occupant. Orphaned for capital, not pharmacodynamics. **#1 recommendation rests on a claim no agent in this pipeline verified** — hence the gate.

## Portfolio: Staged Option Book ($370–730K Stage 0)

Fund gates for the entire top eight before committing to any programme. Total is under 1% of the cheapest development programme.

Then Stage 1: two programmes on independent axes with uncorrelated failure modes:
- **Programme A (prevention):** Ribaxamase — C7, human Phase 2b evidence
- **Programme B (the white space):** CamSA ± UDCA — C1 germination/reservoir, serving immunocompromised need #1

## Key Findings

1. **Evidence anchor dominates.** 14/15 candidates at E≤6.5; one at 8.5. The field's problem is not mechanisms but testing.
2. **Coupling is the most under-priced dimension.** Only CamSA has favorable coupling (K=1.05).
3. **C6 (barrier/repair) has ZERO coverage** — unfilled after 15 candidates and 3 rounds.
4. **Needs are ranked inversely to evidence** — the highest-value needs have the weakest evidence.
5. **Class question unresolved:** Can ANY anti-germinant hold a spore reservoir? Four candidates + the fallback programme depend on this.
