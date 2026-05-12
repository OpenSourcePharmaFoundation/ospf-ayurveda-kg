import { useState, useEffect } from 'react';
import { loadDrugCandidates } from '@/lib/csv-loader';
import type { DrugCandidate } from '@/types/drug-candidate';

interface UseDrugCandidatesResult {
  candidates: DrugCandidate[];
  loading: boolean;
  error: string | null;
}

export function useDrugCandidates(): UseDrugCandidatesResult {
  const [candidates, setCandidates] = useState<DrugCandidate[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    loadDrugCandidates('/data/analysis/oral_mucositis_candidates.csv')
      .then((data) => {
        setCandidates(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  return { candidates, loading, error };
}
