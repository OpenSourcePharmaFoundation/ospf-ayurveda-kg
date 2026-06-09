import { useState, useEffect } from 'react';
import { loadDrugCandidates, loadRouteData } from '@/lib/csv-loader';
import type { DrugCandidate, RouteDataMap, IndicationFrequencyMap } from '@/types/drug-candidate';

interface UseDrugCandidatesResult {
  candidates: DrugCandidate[];
  routeData: RouteDataMap;
  indicationFrequency: IndicationFrequencyMap;
  loading: boolean;
  error: string | null;
}

export function useDrugCandidates(): UseDrugCandidatesResult {
  const [candidates, setCandidates] = useState<DrugCandidate[]>([]);
  const [routeData, setRouteData] = useState<RouteDataMap>({});
  const [indicationFrequency, setIndicationFrequency] = useState<IndicationFrequencyMap>(new Map());
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    Promise.all([
      loadDrugCandidates('/data/analysis/oral_mucositis_candidates.csv'),
      loadRouteData('/data/analysis/drug_indication_routes.json'),
    ])
      .then(([csvResult, routes]) => {
        setCandidates(csvResult.candidates);
        setIndicationFrequency(csvResult.indicationFrequency);
        setRouteData(routes);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  return { candidates, routeData, indicationFrequency, loading, error };
}
