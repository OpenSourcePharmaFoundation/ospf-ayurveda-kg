export type CandidateTier = 'elite' | 'top' | 'highlighted' | null;

export type SafetyVerdict = 'GREEN' | 'YELLOW' | 'ORANGE' | 'RED';

export interface CandidateRanking {
  tier: CandidateTier;
  score: number;
  safety?: SafetyVerdict;
  rationale: string;
  displayName?: string;
}

const CANDIDATE_RANKINGS = new Map<string, CandidateRanking>([
  // Elite: Consensus #1-#3
  ['CHEMBL384467', {
    tier: 'elite', score: 72, safety: 'GREEN', displayName: 'Dexamethasone mouthwash',
    rationale: 'Clinical standard benchmark for OM management. Dexamethasone mouthwash is already the de facto treatment — well-characterized safety in cancer patients with decades of clinical use. Potent corticosteroid that suppresses the inflammatory cascade driving mucosal breakdown. Scored highest across all 15 expert agents for combined efficacy, safety, and deployability.',
  }],
  ['CHEMBL1370', {
    tier: 'elite', score: 67.5, safety: 'GREEN', displayName: 'Budesonide mucoadhesive',
    rationale: 'Superior mucosal selectivity over dexamethasone — 90% first-pass metabolism means the drug acts locally on oral tissue with minimal systemic absorption. This dramatically reduces immunosuppression risk in cancer patients who are already vulnerable. Mucoadhesive formulation enables sustained contact with ulcerated tissue. Proven track record in other mucosal inflammatory conditions (IBD, eosinophilic esophagitis).',
  }],
  ['CHEMBL704', {
    tier: 'elite', score: 62.5, safety: 'GREEN', displayName: 'Mesalamine topical',
    rationale: 'Anti-inflammatory WITHOUT immunosuppression — a critical advantage for cancer patients undergoing chemotherapy. Mesalamine (5-ASA) treats the same type of mucosal inflammation seen in OM, already proven effective in ulcerative colitis and Crohn\'s. Ideal molecular profile for topical oral delivery: MW 153 Da and LogP 0.67 enable excellent mucosal penetration. The only candidate that addresses inflammation while preserving immune function.',
  }],

  // Top: Consensus #4-#7
  ['CHEMBL45', {
    tier: 'top', score: 61, safety: 'GREEN', displayName: 'Melatonin oral gel',
    rationale: 'The only candidate targeting Phase 1 (initiation) of OM pathobiology — where reactive oxygen species (ROS) from radiation/chemo damage basal epithelial cells and trigger the inflammatory cascade. Melatonin is a potent endogenous antioxidant that scavenges free radicals and is radioprotective for normal tissue while not protecting tumor cells. As an oral gel, it offers the best risk/reward ratio of any candidate: extremely safe (already OTC as a supplement) with strong mechanistic rationale.',
  }],
  ['CHEMBL600', {
    tier: 'top', score: 59.5, safety: 'GREEN', displayName: 'NAC rinse',
    rationale: 'Immediately deployable — already available OTC as N-Acetylcysteine. Functions as a direct ROS scavenger by replenishing glutathione, the body\'s primary antioxidant. Proven mucosal protectant in multiple clinical settings (acetaminophen overdose, contrast nephropathy). As a rinse formulation, it can be used alongside any other treatment. The lowest barrier to clinical adoption of any candidate.',
  }],
  ['CHEMBL628', {
    tier: 'top', score: 58, safety: 'YELLOW', displayName: 'Pentoxifylline oral',
    rationale: 'Novel repurposing discovery from knowledge graph analysis — not previously identified as an OM candidate. Pentoxifylline is a methylxanthine that suppresses TNF-alpha, one of the key cytokines driving the ulcerative phase of OM. Already approved for peripheral vascular disease with a well-understood safety profile. Oral formulation with favorable pharmacokinetics for sustained anti-inflammatory effect.',
  }],
  ['CHEMBL514800', {
    tier: 'top', score: 57.5, safety: 'YELLOW', displayName: 'Apremilast oral',
    rationale: 'Already FDA-approved for Behcet\'s disease oral ulcers — the closest phenotypic analog to OM in terms of oral mucosal ulceration. Apremilast is a PDE4 inhibitor that modulates the inflammatory response by reducing TNF-alpha, IL-17, and IL-23 while increasing the anti-inflammatory cytokine IL-10. Strong clinical precedent for treating oral ulceration specifically, not just inflammation generally.',
  }],

  // Top: Tier 1 candidates
  ['CHEMBL1542', {
    tier: 'top', score: 55, displayName: 'Azathioprine oral',
    rationale: 'Proven immunomodulator in mucosal disease — already treats ulcerative colitis, where the same mucosal inflammatory pathways are active. Azathioprine is a purine analog that suppresses T-cell proliferation and reduces inflammatory cytokine production. Extensive clinical history in autoimmune conditions provides a deep safety database. Caution warranted in cancer patients due to immunosuppressive mechanism.',
  }],
  ['CHEMBL221959', {
    tier: 'top', score: 54, displayName: 'Tofacitinib topical',
    rationale: 'JAK inhibitor that blocks IL-6 and IFN-gamma cytokine signaling — both directly implicated in OM pathogenesis. Already approved for ulcerative colitis and rheumatoid arthritis, demonstrating efficacy in mucosal inflammation. Tofacitinib targets the JAK-STAT pathway, which amplifies the inflammatory signal in Phase 2-3 of OM. Oral formulation available, though topical delivery would be preferred to limit systemic immunosuppression.',
  }],
  ['CHEMBL19019', {
    tier: 'top', score: 53, displayName: 'Low-dose Naltrexone oral',
    rationale: 'Low-dose naltrexone (LDN) shows anti-inflammatory effects on mucosal tissue through a paradoxical mechanism — at low doses, transient opioid receptor blockade triggers upregulation of endogenous opioids (endorphins, enkephalins) and opioid growth factor, which modulate immune function and reduce inflammation. Growing clinical evidence in Crohn\'s disease and other mucosal inflammatory conditions. Excellent safety profile at low doses.',
  }],

  // Highlighted: Tier 2 anti-inflammatory
  ['CHEMBL1021', {
    tier: 'highlighted', score: 50,
    rationale: 'NSAID already proven effective on mucosal tissue — approved for ocular inflammation, demonstrating that it can reduce inflammation in delicate mucosal environments without damaging them. Nepafenac is a prodrug that converts to amfenac at the site of action, providing targeted COX inhibition. Favorable molecular profile (MW 254, LogP 1.53) for mucosal penetration.',
  }],
  ['CHEMBL527', {
    tier: 'highlighted', score: 49,
    rationale: 'NSAID with extensive mucosal experience — used in rheumatic disease and eye inflammation. Piroxicam inhibits both COX-1 and COX-2, providing broad anti-inflammatory coverage. Available in topical/gel formulations that could be adapted for oral mucosal application. Long half-life enables once-daily dosing for patient compliance.',
  }],
  ['CHEMBL48449', {
    tier: 'highlighted', score: 48,
    rationale: 'Natural product with anti-inflammatory properties — cantharidin is a terpenoid from blister beetles with a long history in traditional medicine. Low molecular weight (196 Da) and LogP (0.64) provide favorable mucosal absorption characteristics. Anti-inflammatory mechanism could complement other candidates in combination therapy.',
  }],
  ['CHEMBL1169', {
    tier: 'highlighted', score: 47,
    rationale: 'Same active scaffold as mesalamine (5-aminosalicylic acid) — shares the mechanism of mucosal anti-inflammatory action without immunosuppression. Already treats ulcerative colitis and Crohn\'s disease. Identical molecular properties to mesalamine (MW 153, LogP 0.67). Could serve as an alternative formulation option if mesalamine topical encounters manufacturing challenges.',
  }],

  // Highlighted: Tier 3 JAK inhibitors
  ['CHEMBL3655081', {
    tier: 'highlighted', score: 45,
    rationale: 'JAK1 selective inhibitor — more targeted than pan-JAK inhibitors like tofacitinib, potentially reducing immunosuppressive side effects while still blocking the IL-6/IFN-gamma signaling that drives OM. Approved for atopic eczema, demonstrating efficacy in inflammatory skin/mucosal conditions. Selectivity advantage makes it a promising next-generation candidate.',
  }],
  ['CHEMBL4085457', {
    tier: 'highlighted', score: 44,
    rationale: 'JAK3/TEC family kinase inhibitor with a differentiated mechanism — targets a more specific branch of the JAK pathway. Already in trials for ulcerative colitis and Crohn\'s, both mucosal inflammatory diseases. The TEC kinase inhibition provides additional anti-inflammatory activity beyond JAK alone.',
  }],
  ['CHEMBL3137308', {
    tier: 'highlighted', score: 43,
    rationale: 'Pan-JAK inhibitor approved for rheumatoid arthritis and in trials for ulcerative colitis. Peficitinib\'s broad JAK coverage means it blocks multiple inflammatory cytokine pathways simultaneously, which may be advantageous given the complex multi-cytokine environment of OM.',
  }],
  ['CHEMBL3301607', {
    tier: 'highlighted', score: 42,
    rationale: 'JAK1 selective inhibitor approved for rheumatoid arthritis and ulcerative colitis. Filgotinib has demonstrated mucosal healing in UC clinical trials — direct evidence that it can promote repair of damaged mucosal tissue, which is the ultimate goal of OM treatment.',
  }],
  ['CHEMBL4298167', {
    tier: 'highlighted', score: 42,
    rationale: 'Maleate salt form of filgotinib — same mechanism and rationale. Salt form may offer different pharmacokinetic properties useful for topical formulation development.',
  }],
  ['CHEMBL2103743', {
    tier: 'top', score: 54,
    rationale: 'Citrate salt form of tofacitinib — same JAK inhibitor mechanism targeting IL-6/IFN-gamma signaling in OM. Salt form may provide different solubility characteristics relevant to mouthwash or topical gel formulation.',
  }],

  // Highlighted: Breast cancer intersection
  ['CHEMBL1444', {
    tier: 'highlighted', score: 38,
    rationale: 'Dual-purpose opportunity — letrozole is already a first-line aromatase inhibitor for breast cancer. Patients already receiving this drug could potentially benefit from its secondary anti-inflammatory effects on oral mucosa. Fits the oral delivery profile with favorable MW (285 Da) and LogP (2.66).',
  }],
  ['CHEMBL294199', {
    tier: 'highlighted', score: 37,
    rationale: 'Topical analgesic already used for cancer pain management. Capsaicin desensitizes TRPV1 pain receptors and could directly address the severe pain component of OM — one of the most debilitating symptoms that affects patient quality of life and treatment compliance. Available as a topical formulation.',
  }],
  ['CHEMBL30', {
    tier: 'highlighted', score: 36,
    rationale: 'H2 receptor blocker with emerging anti-inflammatory properties beyond acid suppression. Cimetidine shows immune-modulating effects relevant to cancer patients and has an ideal molecular profile for mucosal delivery (MW 252, LogP 0.60). Already used in breast cancer for immune modulation.',
  }],
  ['CHEMBL3187723', {
    tier: 'highlighted', score: 35,
    rationale: 'MEK inhibitor that targets the MAPK cascade — directly relevant to OM pathogenesis, where MAPK signaling amplifies the inflammatory and apoptotic responses in mucosal epithelial cells. Already used as a targeted therapy in cancer treatment, providing a dual-purpose opportunity.',
  }],
  ['CHEMBL960', {
    tier: 'highlighted', score: 34,
    rationale: 'Pyrimidine synthesis inhibitor with anti-proliferative and anti-inflammatory properties. Leflunomide is an immunomodulator used in rheumatoid arthritis that could suppress the aberrant immune activation in OM while also having antiproliferative effects relevant to the disease mechanism.',
  }],
  ['CHEMBL1567', {
    tier: 'highlighted', score: 33,
    rationale: 'Multi-kinase inhibitor with anti-angiogenic properties. Sunitinib targets VEGF and PDGF receptors — aberrant angiogenesis contributes to the inflammatory microenvironment in OM. As a targeted cancer therapy, it offers a dual-purpose rationale for patients already on this regimen.',
  }],
  ['CHEMBL513', {
    tier: 'highlighted', score: 32,
    rationale: 'Alkylating agent already part of cancer treatment regimens. Carmustine is classified as a natural product with ideal molecular properties for mucosal delivery (MW 214, LogP 1.16). Its presence in cancer protocols means no additional drug burden for patients.',
  }],
  ['CHEMBL852', {
    tier: 'highlighted', score: 31,
    rationale: 'Alkylating agent already used in cancer treatment — fits the mucosal delivery profile (MW 305, LogP 1.93). As with carmustine, the dual-purpose rationale means patients already receiving this agent could potentially benefit from its effects on OM without additional medications.',
  }],
  ['CHEMBL1200544', {
    tier: 'highlighted', score: 30,
    rationale: 'Antibiotic that addresses secondary infections in OM — during the ulcerative phase, bacterial colonization of open mucosal lesions worsens inflammation and delays healing. Cephalexin provides targeted antimicrobial coverage to break this cycle. Already used for infection management in cancer patients.',
  }],
  ['CHEMBL1790041', {
    tier: 'highlighted', score: 29,
    rationale: 'H2 blocker with anti-inflammatory potential on mucosal tissue. Ranitidine\'s mechanism extends beyond acid suppression — it has demonstrated anti-inflammatory and immune-modulating properties. Already used for GI side effect management in cancer patients, providing a low-barrier repurposing opportunity.',
  }],
]);

export function getCandidateTier(chemblId: string): CandidateTier {
  return CANDIDATE_RANKINGS.get(chemblId)?.tier ?? null;
}

export function getCandidateScore(chemblId: string): number {
  return CANDIDATE_RANKINGS.get(chemblId)?.score ?? 0;
}

export function getCandidateRanking(chemblId: string): CandidateRanking | null {
  return CANDIDATE_RANKINGS.get(chemblId) ?? null;
}

const EXISTING_OM_DRUGS = new Map<string, string>([
  ['CHEMBL384467', 'De facto clinical standard for OM (mouthwash)'],
  ['CHEMBL45',     'Studied for OM — oral mucositis is a listed indication'],
  ['CHEMBL600',    'Studied for OM — mucositis and oral mucositis are listed indications'],
  ['CHEMBL514800', 'FDA-approved for Behcet\'s oral ulcers — closest phenotypic analog to OM'],
]);

export function getExistingOmStatus(chemblId: string): string | null {
  return EXISTING_OM_DRUGS.get(chemblId) ?? null;
}
