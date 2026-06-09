import { useState, useCallback } from 'react';
import { Badge } from '@/components/ui/badge';
import { Separator } from '@/components/ui/separator';
import { X, ChevronDown } from 'lucide-react';
import { getCandidateRanking, getExistingOmStatus } from '@/lib/candidate-tiers';
import type { CandidateRanking, SafetyVerdict } from '@/lib/candidate-tiers';
import type { DrugCandidate, RouteDataMap, IndicationFrequencyMap } from '@/types/drug-candidate';
import { IndicationsTable } from './IndicationsTable';

function titleCase(name: string): string {
  return name
    .toLowerCase()
    .replace(/\b\w/g, (c) => c.toUpperCase());
}

interface CandidateDetailPanelProps {
  candidate: DrugCandidate;
  routeData: RouteDataMap;
  indicationFrequency: IndicationFrequencyMap;
  onClose: () => void;
}

const PHASE_LABELS: Record<number, string> = {
  0: 'Unknown',
  1: 'Phase I',
  2: 'Phase II',
  3: 'Phase III',
  4: 'Approved',
};

const SAFETY_STYLES: Record<SafetyVerdict, { bg: string; text: string; label: string }> = {
  GREEN: { bg: 'bg-emerald-500/10', text: 'text-emerald-700 dark:text-emerald-400', label: 'Low Risk' },
  YELLOW: { bg: 'bg-amber-500/10', text: 'text-amber-700 dark:text-amber-400', label: 'Moderate Risk' },
  ORANGE: { bg: 'bg-orange-500/10', text: 'text-orange-700 dark:text-orange-400', label: 'Elevated Risk' },
  RED: { bg: 'bg-red-500/10', text: 'text-red-700 dark:text-red-400', label: 'High Risk' },
};

const TIER_LABELS: Record<string, string> = {
  elite: 'Lead Candidate',
  top: 'Top Candidate',
  highlighted: 'Candidate of Interest',
};

function PropertyRow({ label, value, unit }: { label: string; value: string; unit?: string }) {
  return (
    <div className="flex items-center justify-between py-2">
      <span className="text-sm text-muted-foreground">{label}</span>
      <span className="text-sm font-mono font-medium text-foreground">
        {value}
        {unit && <span className="text-muted-foreground ml-1">{unit}</span>}
      </span>
    </div>
  );
}

export function CandidateDetailPanel({ candidate, routeData, indicationFrequency, onClose }: CandidateDetailPanelProps) {
  const phaseLabel = PHASE_LABELS[candidate.max_phase] ?? `Phase ${candidate.max_phase}`;
  const ranking = getCandidateRanking(candidate.chembl_id);
  const displayName = ranking?.displayName || titleCase(candidate.drug_name);
  const omStatus = getExistingOmStatus(candidate.chembl_id);

  return (
    <div className="h-full flex flex-col">
      <div className="flex items-start justify-between border-b border-border px-6 py-4 shrink-0">
        <div className="min-w-0 pr-4">
          <h2 className="text-xl font-semibold text-foreground">{displayName}</h2>
          {candidate.chembl_id && (
            <span className="text-sm text-muted-foreground font-mono">{candidate.chembl_id}</span>
          )}
        </div>
        <button
          onClick={onClose}
          className="shrink-0 rounded-md p-1.5 text-muted-foreground hover:text-foreground hover:bg-muted transition-colors"
        >
          <X className="size-5" />
        </button>
      </div>

      <div className="flex-1 overflow-y-auto">
        <div className="px-6 py-5 space-y-6 max-w-3xl">
          <div className="flex flex-wrap gap-2">
            <Badge variant="outline">{phaseLabel}</Badge>
            {omStatus && (
              <Badge variant="outline" className="border-violet-400 text-violet-600 dark:text-violet-400 dark:border-violet-500">
                Existing OM Drug
              </Badge>
            )}
            {candidate.is_natural_product && (
              <Badge variant="outline" className="border-primary/40 text-primary">
                Natural Product
              </Badge>
            )}
          </div>

          {omStatus && (
            <div className="rounded-md bg-violet-500/10 px-3 py-2 text-sm text-violet-700 dark:text-violet-300">
              {omStatus}
            </div>
          )}

          {ranking && <RankingSection ranking={ranking} />}

          <ChemPropertiesSection candidate={candidate} ranking={ranking} displayName={displayName} />

          {candidate.indications.length > 0 && (
            <div>
              <h4 className="text-sm font-semibold text-foreground mb-1">
                Indications ({candidate.indications.length})
              </h4>
              <Separator className="mb-3" />
              <IndicationsTable
                indications={candidate.indications}
                chemblId={candidate.chembl_id}
                routeData={routeData[candidate.chembl_id]}
                indicationFrequency={indicationFrequency}
              />
            </div>
          )}

          {candidate.chembl_id && (
            <div>
              <h4 className="text-sm font-semibold text-foreground mb-1">External Links</h4>
              <Separator className="mb-3" />
              <a
                href={`https://www.ebi.ac.uk/chembl/explore/compound/${candidate.chembl_id}`}
                target="_blank"
                rel="noopener noreferrer"
                className="text-sm text-primary hover:underline"
              >
                View on ChemBL →
              </a>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

function ChemPropertiesSection({
  candidate,
  ranking,
  displayName,
}: {
  candidate: DrugCandidate;
  ranking: CandidateRanking | null;
  displayName: string;
}) {
  const [expanded, setExpanded] = useState(false);

  return (
    <div
      className="rounded-lg border border-border bg-muted/30 overflow-hidden cursor-pointer transition-colors hover:bg-muted/50"
      onClick={() => setExpanded((v) => !v)}
    >
      <div className="p-4">
        <div className="flex items-center justify-between">
          <span className="text-sm font-semibold text-foreground">Chemical Properties</span>
          <button
            type="button"
            className="flex items-center gap-1 text-xs text-primary hover:text-primary/80 transition-colors"
            onClick={(e) => {
              e.stopPropagation();
              setExpanded((v) => !v);
            }}
          >
            <ChevronDown
              className={`size-3.5 transition-transform ${expanded ? 'rotate-180' : ''}`}
            />
            {expanded ? 'Hide' : 'Show'}
          </button>
        </div>
      </div>

      {expanded && (
        <div className="px-4 pb-4 pt-0 border-t border-border/50">
          {candidate.chembl_id && ranking && (ranking.tier === 'elite' || ranking.tier === 'top') && (
            <div className="pt-3">
              <MoleculeStructure chemblId={candidate.chembl_id} name={displayName} />
            </div>
          )}

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 pt-3">
            <div>
              <h4 className="text-xs font-semibold text-muted-foreground uppercase tracking-wide mb-1.5">
                Molecular Properties
              </h4>
              <Separator />
              <div className="divide-y divide-border">
                <PropertyRow
                  label="Molecular Weight"
                  value={candidate.molecular_weight?.toFixed(2) || '—'}
                  unit="Da"
                />
                <PropertyRow
                  label="LogP (Lipophilicity)"
                  value={candidate.alogp?.toFixed(2) || '—'}
                />
                <PropertyRow
                  label="Polar Surface Area"
                  value={candidate.psa?.toFixed(1) || '—'}
                  unit="Å²"
                />
                <PropertyRow
                  label="H-Bond Donors"
                  value={candidate.hbd?.toString() ?? '—'}
                />
                <PropertyRow
                  label="H-Bond Acceptors"
                  value={candidate.hba?.toString() ?? '—'}
                />
              </div>
            </div>

            <div>
              <h4 className="text-xs font-semibold text-muted-foreground uppercase tracking-wide mb-1.5">
                Lipinski's Rule of Five
              </h4>
              <Separator className="mb-3" />
              <RuleOfFiveCheck candidate={candidate} />
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

function RankingSection({ ranking }: { ranking: CandidateRanking }) {
  const [expanded, setExpanded] = useState(false);
  const tierLabel = ranking.tier ? TIER_LABELS[ranking.tier] : null;
  const safetyStyle = ranking.safety ? SAFETY_STYLES[ranking.safety] : null;

  return (
    <div
      className="rounded-lg border border-border bg-muted/30 overflow-hidden cursor-pointer transition-colors hover:bg-muted/50"
      onClick={() => setExpanded((v) => !v)}
    >
      <div className="p-4 space-y-3">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            {tierLabel && (
              <span className="text-sm font-semibold text-foreground">{tierLabel}</span>
            )}
            {safetyStyle && (
              <span className={`text-xs px-2 py-0.5 rounded-full ${safetyStyle.bg} ${safetyStyle.text}`}>
                {safetyStyle.label}
              </span>
            )}
          </div>
          <span className="text-lg font-bold font-mono text-foreground">
            {ranking.score}
            <span className="text-sm font-normal text-muted-foreground">/100</span>
          </span>
        </div>

        <div>
          <h4 className="text-xs font-semibold text-muted-foreground uppercase tracking-wide mb-1.5">
            Why this candidate?
          </h4>
          <p className="text-sm text-foreground leading-relaxed">{ranking.rationale}</p>
        </div>

        <button
          type="button"
          className="flex items-center gap-1 text-xs text-primary hover:text-primary/80 transition-colors"
          onClick={() => setExpanded((v) => !v)}
        >
          <ChevronDown
            className={`size-3.5 transition-transform ${expanded ? 'rotate-180' : ''}`}
          />
          {expanded ? 'Less detail' : 'More detail'}
        </button>
      </div>

      {expanded && (
        <div className="px-4 pb-4 pt-0 border-t border-border/50 space-y-3">
          {ranking.safety && (
            <div className="pt-3">
              <h4 className="text-xs font-semibold text-muted-foreground uppercase tracking-wide mb-1.5">
                Safety Profile
              </h4>
              <p className="text-sm text-foreground leading-relaxed">
                {ranking.safety === 'GREEN' &&
                  'Well-characterized safety profile suitable for cancer patients. No significant concerns for the proposed formulation and delivery route.'}
                {ranking.safety === 'YELLOW' &&
                  'Generally safe but requires monitoring. Some considerations around drug interactions or systemic effects in immunocompromised patients.'}
                {ranking.safety === 'ORANGE' &&
                  'Elevated risk — requires careful dose management and patient selection. Significant drug interaction potential with common chemotherapy regimens.'}
                {ranking.safety === 'RED' &&
                  'High risk — serious safety concerns including black box warnings or fatal drug-drug interaction potential. Use only when benefits clearly outweigh risks.'}
              </p>
            </div>
          )}

          <div>
            <h4 className="text-xs font-semibold text-muted-foreground uppercase tracking-wide mb-1.5">
              Scoring Methodology
            </h4>
            <p className="text-sm text-muted-foreground leading-relaxed">
              Composite score from 15-agent multi-round evaluation assessing efficacy evidence,
              safety profile, developability, ADMET properties, phase coverage, and Ayurvedic bridge potential.
            </p>
          </div>
        </div>
      )}
    </div>
  );
}

function MoleculeStructure({ chemblId, name }: { chemblId: string; name: string }) {
  const [failed, setFailed] = useState(false);
  const handleError = useCallback(() => setFailed(true), []);

  if (failed) return null;

  return (
    <div>
      <h4 className="text-sm font-semibold text-foreground mb-1">Molecular Structure</h4>
      <Separator className="mb-3" />
      <div className="rounded-lg border border-border bg-white p-4 inline-block">
        <img
          src={`https://www.ebi.ac.uk/chembl/api/data/image/${chemblId}.svg`}
          alt={`${name} molecular structure`}
          className="max-w-[280px] max-h-[280px]"
          onError={handleError}
        />
      </div>
    </div>
  );
}

function RuleOfFiveCheck({ candidate }: { candidate: DrugCandidate }) {
  const rules = [
    { label: 'MW ≤ 500', pass: candidate.molecular_weight <= 500, value: candidate.molecular_weight?.toFixed(0) },
    { label: 'LogP ≤ 5', pass: candidate.alogp <= 5, value: candidate.alogp?.toFixed(2) },
    { label: 'HBD ≤ 5', pass: candidate.hbd <= 5, value: candidate.hbd?.toString() },
    { label: 'HBA ≤ 10', pass: candidate.hba <= 10, value: candidate.hba?.toString() },
  ];

  const violations = rules.filter((r) => !r.pass).length;

  return (
    <div className="space-y-2">
      <div className="grid grid-cols-2 gap-2">
        {rules.map((rule) => (
          <div
            key={rule.label}
            className={`rounded-md px-3 py-2 text-xs ${
              rule.pass
                ? 'bg-emerald-500/10 text-emerald-700 dark:text-emerald-400'
                : 'bg-destructive/10 text-destructive'
            }`}
          >
            <span className="mr-1.5">{rule.pass ? '✓' : '✗'}</span>
            {rule.label}
            <span className="ml-1 opacity-70">({rule.value})</span>
          </div>
        ))}
      </div>
      <p className="text-xs text-muted-foreground">
        {violations === 0
          ? 'Passes all Ro5 criteria — good oral bioavailability predicted.'
          : `${violations} violation${violations > 1 ? 's' : ''} — may have reduced oral bioavailability.`}
      </p>
    </div>
  );
}
