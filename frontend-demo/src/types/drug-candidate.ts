export interface DrugCandidate {
  drug_name: string;
  chembl_id: string;
  molecular_weight: number;
  alogp: number;
  psa: number;
  hbd: number;
  hba: number;
  is_natural_product: boolean;
  indications: string[];
  indication_count: number;
  max_phase: number;
}
