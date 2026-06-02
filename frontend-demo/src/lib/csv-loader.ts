import Papa from 'papaparse';
import type { DrugCandidate } from '@/types/drug-candidate';

export async function loadDrugCandidates(url: string): Promise<DrugCandidate[]> {
  const response = await fetch(url);
  const text = await response.text();

  return new Promise((resolve, reject) => {
    Papa.parse<Record<string, string>>(text, {
      header: true,
      skipEmptyLines: true,
      complete: (results) => {
        const candidates = results.data.map(transformRow).filter(Boolean) as DrugCandidate[];
        resolve(candidates);
      },
      error: (error: Error) => reject(error),
    });
  });
}

function transformRow(row: Record<string, string>): DrugCandidate | null {
  const name = row['drug_name'] || row['pref_name'] || row['Drug'] || '';
  if (!name) return null;

  const indications = (
    row['indications'] || row['current_indications'] || row['mesh_heading'] || ''
  )
    .split(/;\s*/)
    .map((s) => s.trim())
    .filter(Boolean);

  const naturalRaw = (row['is_natural_product'] || row['natural_product'] || '').trim();

  return {
    drug_name: name,
    chembl_id: row['chembl_id'] || row['molecule_chembl_id'] || '',
    molecular_weight: parseFloat(row['molecular_weight'] || row['mw_freebase'] || '0'),
    alogp: parseFloat(row['alogp'] || row['logP'] || '0'),
    psa: parseFloat(row['psa'] || row['polar_surface_area'] || '0'),
    hbd: parseFloat(row['hbd'] || row['h_bond_donors'] || '0'),
    hba: parseFloat(row['hba'] || row['h_bond_acceptors'] || '0'),
    is_natural_product: naturalRaw.toLowerCase() === 'true' || naturalRaw === '1',
    indications,
    indication_count: parseInt(row['indication_count'] || String(indications.length), 10),
    max_phase: parseInt(row['max_phase'] || '4', 10),
  };
}
