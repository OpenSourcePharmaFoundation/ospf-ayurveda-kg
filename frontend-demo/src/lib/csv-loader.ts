import Papa from 'papaparse';
import type { DrugCandidate } from '@/types/drug-candidate';

export async function loadDrugCandidates(url: string): Promise<DrugCandidate[]> {
  const response = await fetch(url);
  const text = await response.text();

  return new Promise((resolve, reject) => {
    Papa.parse<Record<string, string>>(text, {
      header: true,
      skipEmptyLines: true,
      transformHeader: (h) => h.trim(),
      transform: (value) => value.trim().replace(/^"|"$/g, ''),
      complete: (results) => {
        const candidates = results.data.map(transformRow).filter(Boolean) as DrugCandidate[];
        sortIndicationsByFrequency(candidates);
        resolve(candidates);
      },
      error: (error: Error) => reject(error),
    });
  });
}

function sortIndicationsByFrequency(candidates: DrugCandidate[]): void {
  const freq = new Map<string, number>();
  for (const c of candidates) {
    for (const ind of c.indications) {
      freq.set(ind, (freq.get(ind) ?? 0) + 1);
    }
  }
  for (const c of candidates) {
    c.indications.sort((a, b) => (freq.get(b) ?? 0) - (freq.get(a) ?? 0));
  }
}

function clean(value: string | undefined): string {
  return (value ?? '').trim().replace(/^"|"$/g, '');
}

function transformRow(row: Record<string, string>): DrugCandidate | null {
  const name = clean(row['drug_name']) || clean(row['pref_name']) || clean(row['Drug']);
  if (!name) return null;

  const indications = (
    clean(row['indications']) || clean(row['current_indications']) || clean(row['mesh_heading'])
  )
    .split(/;\s*/)
    .map((s) => s.trim())
    .filter(Boolean);

  const naturalRaw = clean(row['is_natural_product']) || clean(row['natural_product']);

  return {
    drug_name: name,
    chembl_id: clean(row['chembl_id']) || clean(row['molecule_chembl_id']),
    molecular_weight: parseFloat(clean(row['molecular_weight']) || clean(row['mw_freebase']) || '0'),
    alogp: parseFloat(clean(row['alogp']) || clean(row['logP']) || '0'),
    psa: parseFloat(clean(row['psa']) || clean(row['polar_surface_area']) || '0'),
    hbd: parseFloat(clean(row['hbd']) || clean(row['h_bond_donors']) || '0'),
    hba: parseFloat(clean(row['hba']) || clean(row['h_bond_acceptors']) || '0'),
    is_natural_product: naturalRaw.toLowerCase() === 'true' || naturalRaw === '1',
    indications,
    indication_count: parseInt(clean(row['indication_count']) || String(indications.length), 10),
    max_phase: parseInt(clean(row['max_phase']) || '4', 10),
  };
}
