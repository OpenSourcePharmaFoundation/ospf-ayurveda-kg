import { useState, useMemo, useCallback, useEffect, useRef } from 'react';
import { useDrugCandidates } from '@/hooks/use-drug-candidates';
import { CandidateCard } from './CandidateCard';
import { CandidateDetailPanel } from './CandidateDetailPanel';
import { getCandidateTier, getCandidateScore, getExistingOmStatus } from '@/lib/candidate-tiers';
import { readParam, useUrlState } from '@/hooks/use-url-state';
import type { DrugCandidate } from '@/types/drug-candidate';

export function DrugCandidatesView() {
  const { candidates, routeData, indicationFrequency, loading, error } = useDrugCandidates();
  const { update } = useUrlState();
  const [search, setSearch] = useState('');
  const [filterNatural, setFilterNatural] = useState(false);
  const [filterExistingOm, setFilterExistingOm] = useState(true);
  const [selectedCandidate, setSelectedCandidate] = useState<DrugCandidate | null>(null);
  const restoredFromUrl = useRef(false);

  useEffect(() => {
    if (restoredFromUrl.current || candidates.length === 0) return;
    restoredFromUrl.current = true;
    const drugParam = readParam('drug');
    if (drugParam) {
      const match = candidates.find((c) => c.chembl_id === drugParam);
      if (match) {
        if (getExistingOmStatus(match.chembl_id) !== null) setFilterExistingOm(false);
        setSelectedCandidate(match);
      }
    }
  }, [candidates]);

  const handleCardClick = useCallback((candidate: DrugCandidate) => {
    setSelectedCandidate(candidate);
    update({ drug: candidate.chembl_id || null });
  }, [update]);

  const handleClose = useCallback(() => {
    setSelectedCandidate(null);
    update({ drug: null });
  }, [update]);

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
    if (filterExistingOm) {
      result = result.filter((c) => getExistingOmStatus(c.chembl_id) === null);
    }
    return [...result].sort((a, b) => {
      const sa = getCandidateScore(a.chembl_id);
      const sb = getCandidateScore(b.chembl_id);
      return sb - sa;
    });
  }, [candidates, search, filterNatural, filterExistingOm]);

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
              <div className="flex items-center gap-4 shrink-0">
                <label className="flex items-center gap-2 text-sm text-muted-foreground cursor-pointer">
                  <input
                    type="checkbox"
                    checked={filterNatural}
                    onChange={(e) => setFilterNatural(e.target.checked)}
                    className="rounded border-input"
                  />
                  <span title="Show only compounds derived from natural sources (plants, fungi, etc.)">Natural products only</span>
                </label>
                <label className="flex items-center gap-2 text-sm text-muted-foreground cursor-pointer">
                  <input
                    type="checkbox"
                    checked={filterExistingOm}
                    onChange={(e) => setFilterExistingOm(e.target.checked)}
                    className="rounded border-input"
                  />
                  <span title="Hide existing drugs for Oral Mucositis">Hide existing OM drugs</span>
                </label>
              </div>
            )}
          </div>

          {/* Legend + count */}
          {!hasSelection && (
            <div className="flex flex-wrap items-center gap-x-4 gap-y-1 text-sm text-muted-foreground mb-4">
              <span>Showing {filtered.length} of {candidates.length} candidates</span>
              <span className="flex items-center gap-1.5" title="Top-scoring candidates (score >= 55) — strongest evidence for OM treatment">
                <span className="inline-block w-3 h-3 rounded-sm ring-[3px] ring-emerald-500 bg-gradient-to-br from-emerald-100 to-emerald-50" />
                Lead Candidates
                <span className="text-amber-400">★</span>
              </span>
              <span className="flex items-center gap-1.5" title="Strong candidates (score >= 45) with good mechanistic rationale">
                <span className="inline-block w-3 h-3 rounded-sm ring-2 ring-amber-400/70 bg-amber-400/20" />
                Top Candidates
              </span>
              <span className="flex items-center gap-1.5" title="Scored candidates with potential but lower overall evidence or deprioritized concerns">
                <span className="inline-block w-3 h-3 rounded-sm ring-2 ring-sky-400/50 bg-sky-400/10" />
                Candidates of Interest
              </span>
            </div>
          )}

          {hasSelection && (
            <div className="space-y-1.5">
              <div className="flex flex-col gap-1">
                <label className="flex items-center gap-1.5 text-xs text-muted-foreground cursor-pointer">
                  <input
                    type="checkbox"
                    checked={filterNatural}
                    onChange={(e) => setFilterNatural(e.target.checked)}
                    className="rounded border-input"
                  />
                  <span title="Show only compounds derived from natural sources (plants, fungi, etc.)">Natural only</span>
                </label>
                <label className="flex items-center gap-1.5 text-xs text-muted-foreground cursor-pointer">
                  <input
                    type="checkbox"
                    checked={filterExistingOm}
                    onChange={(e) => setFilterExistingOm(e.target.checked)}
                    className="rounded border-input"
                  />
                  <span title="Hide existing drugs for Oral Mucositis">Hide existing OM</span>
                </label>
              </div>
              <div className="text-xs text-muted-foreground">
                {filtered.length} candidates
              </div>
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
