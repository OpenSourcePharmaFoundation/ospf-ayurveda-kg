import { useState, useMemo, useCallback } from 'react';
import { useDrugCandidates } from '@/hooks/use-drug-candidates';
import { CandidateCard } from './CandidateCard';
import { CandidateDetailPanel } from './CandidateDetailPanel';
import { getCandidateTier, getCandidateScore } from '@/lib/candidate-tiers';
import type { DrugCandidate } from '@/types/drug-candidate';

export function DrugCandidatesView() {
  const { candidates, routeData, indicationFrequency, loading, error } = useDrugCandidates();
  const [search, setSearch] = useState('');
  const [filterNatural, setFilterNatural] = useState(false);
  const [selectedCandidate, setSelectedCandidate] = useState<DrugCandidate | null>(null);

  const handleCardClick = useCallback((candidate: DrugCandidate) => {
    setSelectedCandidate(candidate);
  }, []);

  const handleClose = useCallback(() => {
    setSelectedCandidate(null);
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

  const hasSelection = selectedCandidate !== null;

  return (
    <div className={hasSelection ? 'flex gap-0 -mx-4 sm:-mx-6' : ''}>
      {/* List panel */}
      <div
        className={
          hasSelection
            ? 'w-72 shrink-0 border-r border-border flex flex-col h-[calc(100vh-12rem)]'
            : ''
        }
      >
        <div className={hasSelection ? 'px-3 pt-3 pb-2 space-y-2 shrink-0' : ''}>
          {/* Search */}
          <div className={hasSelection ? '' : 'flex flex-col sm:flex-row gap-3 mb-6'}>
            <div className={hasSelection ? '' : 'flex-1'}>
              <input
                type="text"
                placeholder={hasSelection ? 'Search...' : 'Search by name, ChemBL ID, or indication...'}
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                className="w-full px-3 py-2 rounded-md border border-input bg-background text-sm placeholder:text-muted-foreground focus:outline-none focus:ring-2 focus:ring-ring"
              />
            </div>
            {!hasSelection && (
              <label className="flex items-center gap-2 text-sm text-muted-foreground cursor-pointer shrink-0">
                <input
                  type="checkbox"
                  checked={filterNatural}
                  onChange={(e) => setFilterNatural(e.target.checked)}
                  className="rounded border-input"
                />
                Natural products only
              </label>
            )}
          </div>

          {/* Legend + count */}
          {!hasSelection && (
            <div className="flex flex-wrap items-center gap-x-4 gap-y-1 text-sm text-muted-foreground mb-4">
              <span>Showing {filtered.length} of {candidates.length} candidates</span>
              <span className="flex items-center gap-1.5">
                <span className="inline-block w-3 h-3 rounded-sm ring-[3px] ring-emerald-500 bg-gradient-to-br from-emerald-100 to-emerald-50" />
                Lead Candidates
                <span className="text-amber-400">★</span>
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
          )}

          {hasSelection && (
            <div className="text-xs text-muted-foreground">
              {filtered.length} candidates
            </div>
          )}
        </div>

        {/* Candidate list */}
        <div
          className={
            hasSelection
              ? 'flex-1 overflow-y-auto px-2 pb-2 space-y-0.5'
              : 'flex flex-col gap-1.5'
          }
        >
          {filtered.map((candidate) => (
            <CandidateCard
              key={candidate.chembl_id || candidate.drug_name}
              candidate={candidate}
              tier={getCandidateTier(candidate.chembl_id)}
              compact={hasSelection}
              selected={hasSelection && selectedCandidate?.chembl_id === candidate.chembl_id}
              onClick={handleCardClick}
            />
          ))}
        </div>

        {filtered.length === 0 && (
          <div className="text-center py-12 text-muted-foreground">
            No candidates match your filters.
          </div>
        )}
      </div>

      {/* Detail panel */}
      {selectedCandidate && (
        <div className="flex-1 min-w-0 h-[calc(100vh-12rem)]">
          <CandidateDetailPanel
            key={selectedCandidate.chembl_id}
            candidate={selectedCandidate}
            routeData={routeData}
            indicationFrequency={indicationFrequency}
            onClose={handleClose}
          />
        </div>
      )}
    </div>
  );
}
