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

export interface DrugRouteData {
  routes_by_indication: Record<string, string>;
  available_routes: string[];
}

export type RouteDataMap = Record<string, DrugRouteData>;

export type IndicationFrequencyMap = Map<string, number>;
