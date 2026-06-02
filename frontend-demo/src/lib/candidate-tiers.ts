export type CandidateTier = 'top' | 'highlighted' | null;

// Top 10: Consensus-ranked + Tier 1 (mucosal inflammation) + Tier 2 (anti-inflammatory)
// Source: multi-agent consensus ranking + May 2026-05-03 tier analysis
const TOP_CHEMBL_IDS = new Set([
  'CHEMBL704',       // Mesalamine — #3 consensus, Tier 1
  'CHEMBL1370',      // Budesonide — #2 consensus
  'CHEMBL1542',      // Azathioprine — Tier 1
  'CHEMBL221959',    // Tofacitinib — Tier 1
  'CHEMBL19019',     // Naltrexone — Tier 1
  'CHEMBL1021',      // Nepafenac — Tier 2
  'CHEMBL527',       // Piroxicam — Tier 2
  'CHEMBL48449',     // Cantharidin — Tier 2
  'CHEMBL1169',      // Aminosalicylic Acid — Tier 2
  'CHEMBL3655081',   // Abrocitinib — Tier 3 lead (JAK1 selective)
]);

// Next 20: Tier 3 (JAK inhibitors) + breast cancer intersection + safety-noted candidates
// Source: Tier 3 analysis + breast cancer dual-purpose candidates
const HIGHLIGHTED_CHEMBL_IDS = new Set([
  'CHEMBL4085457',   // Ritlecitinib — Tier 3
  'CHEMBL3137308',   // Peficitinib — Tier 3
  'CHEMBL3301607',   // Filgotinib — Tier 3
  'CHEMBL4298167',   // Filgotinib Maleate (salt form)
  'CHEMBL2103743',   // Tofacitinib Citrate (salt form)
  'CHEMBL1444',      // Letrozole — breast cancer intersection
  'CHEMBL294199',    // Capsaicin — breast cancer, topical analgesic
  'CHEMBL30',        // Cimetidine — breast cancer, anti-inflammatory
  'CHEMBL3187723',   // Binimetinib — MEK/MAPK cascade
  'CHEMBL960',       // Leflunomide — anti-proliferative
  'CHEMBL1567',      // Sunitinib — multi-kinase inhibitor
  'CHEMBL513',       // Carmustine — alkylating agent
  'CHEMBL852',       // Melphalan — alkylating agent
  'CHEMBL1200544',   // Cephalexin — secondary infection management
  'CHEMBL1790041',   // Ranitidine — anti-inflammatory on mucosa
  'CHEMBL2110372',   // Ranitidine Hydrochloride
  'CHEMBL480',       // Lansoprazole — emerging anti-inflammatory
  'CHEMBL107',       // Colchicine — anti-inflammatory (safety concerns)
  'CHEMBL1789941',   // Ruxolitinib — JAK inhibitor
  'CHEMBL1077',      // Bromfenac — NSAID, mucosal tissue
]);

export function getCandidateTier(chemblId: string): CandidateTier {
  if (TOP_CHEMBL_IDS.has(chemblId)) return 'top';
  if (HIGHLIGHTED_CHEMBL_IDS.has(chemblId)) return 'highlighted';
  return null;
}
