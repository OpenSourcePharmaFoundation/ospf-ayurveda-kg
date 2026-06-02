import { useState, useMemo, useCallback } from 'react';
import { useDrugCandidates } from '@/hooks/use-drug-candidates';
import { CandidateCard } from './CandidateCard';
import { CandidateDetailDrawer } from './CandidateDetailDrawer';
import { getCandidateTier, getCandidateScore } from '@/lib/candidate-tiers';
import type { DrugCandidate } from '@/types/drug-candidate';

export function DrugCandidatesView() {
  const { candidates, loading, error } = useDrugCandidates();
  const [search, setSearch] = useState('');
  const [filterNatural, setFilterNatural] = useState(false);
  const [selectedCandidate, setSelectedCandidate] = useState<DrugCandidate | null>(null);
  const [drawerOpen, setDrawerOpen] = useState(false);

  const handleCardClick = useCallback((candidate: DrugCandidate) => {
    setSelectedCandidate(candidate);
    setDrawerOpen(true);
  }, []);

  const filtered = useMemo(() => {
    let result = candidates;
    if (search) {
      const q = search.toLowerCase();
      result = result.filter(
        (c) =>
          c.drug_name.toLowerCase().includes(q) ||
          c.chembl_id.toLowerCase().includes(q) ||
          c.indications.some((ind) => ind.toLowerCase().includes(q)),
      );
    }
    if (filterNatural) {
      result = result.filter((c) => c.is_natural_product);
    }
    return [...result].sort((a, b) => {
      const sa = getCandidateScore(a.chembl_id);
      const sb = getCandidateScore(b.chembl_id);
      return sb - sa;
    });
  }, [candidates, search, filterNatural]);

  if (loading) {
    return (
      <div className="flex items-center justify-center py-12">
        <div className="text-muted-foreground">Loading drug candidates...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="text-destructive p-4 rounded-lg border border-destructive/20 bg-destructive/5">
        Failed to load candidates: {error}
      </div>
    );
  }

  return (
    <div>
      <div className="flex flex-col sm:flex-row gap-3 mb-6">
        <div className="flex-1">
          <input
            type="text"
            placeholder="Search by name, ChemBL ID, or indication..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="w-full px-3 py-2 rounded-md border border-input bg-background text-sm placeholder:text-muted-foreground focus:outline-none focus:ring-2 focus:ring-ring"
          />
        </div>
        <label className="flex items-center gap-2 text-sm text-muted-foreground cursor-pointer shrink-0">
          <input
            type="checkbox"
            checked={filterNatural}
            onChange={(e) => setFilterNatural(e.target.checked)}
            className="rounded border-input"
          />
          Natural products only
        </label>
      </div>

      <div className="flex flex-wrap items-center gap-x-4 gap-y-1 text-sm text-muted-foreground mb-4">
        <span>Showing {filtered.length} of {candidates.length} candidates</span>
        <span className="flex items-center gap-1.5">
          <span className="inline-block w-3 h-3 rounded-sm ring-[3px] ring-emerald-500 bg-gradient-to-br from-emerald-100 to-emerald-50" />
          Lead Candidates
        </span>
        <span className="flex items-center gap-1.5">
          <span className="inline-block w-3 h-3 rounded-sm ring-2 ring-amber-400/70 bg-amber-400/20" />
          Top Candidates
        </span>
        <span className="flex items-center gap-1.5">
          <span className="inline-block w-3 h-3 rounded-sm ring-2 ring-sky-400/50 bg-sky-400/10" />
          Candidates of Interest
        </span>
      </div>

      <div className="flex flex-col gap-1.5">
        {filtered.map((candidate) => (
          <CandidateCard
            key={candidate.chembl_id || candidate.drug_name}
            candidate={candidate}
            tier={getCandidateTier(candidate.chembl_id)}
            onClick={handleCardClick}
          />
        ))}
      </div>

      {filtered.length === 0 && (
        <div className="text-center py-12 text-muted-foreground">
          No candidates match your filters.
        </div>
      )}

      <CandidateDetailDrawer
        candidate={selectedCandidate}
        open={drawerOpen}
        onOpenChange={setDrawerOpen}
      />
    </div>
  );
}
