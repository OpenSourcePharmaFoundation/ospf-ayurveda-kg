import { Badge } from '@/components/ui/badge';
import type { DrugCandidate } from '@/types/drug-candidate';
import { getCandidateRanking } from '@/lib/candidate-tiers';
import type { CandidateTier } from '@/lib/candidate-tiers';

const TIER_STYLES: Record<string, { row: string; badge: string; label: string; accent: string }> = {
  elite: {
    row: 'border-l-[3px] border-l-emerald-500 bg-gradient-to-r from-emerald-50/50 to-transparent dark:from-emerald-950/20',
    badge: 'bg-emerald-600 text-white border-emerald-700 font-semibold',
    label: 'Lead',
    accent: 'text-emerald-700 dark:text-emerald-400',
  },
  top: {
    row: 'border-l-[3px] border-l-amber-400 bg-gradient-to-r from-amber-50/40 to-transparent dark:from-amber-950/15',
    badge: 'bg-amber-500 text-white border-amber-500',
    label: 'Top',
    accent: 'text-amber-600 dark:text-amber-400',
  },
  highlighted: {
    row: 'border-l-[3px] border-l-sky-400 bg-gradient-to-r from-sky-50/30 to-transparent dark:from-sky-950/10',
    badge: 'bg-sky-100 text-sky-700 border-sky-300 dark:bg-sky-900/40 dark:text-sky-300 dark:border-sky-600',
    label: 'Interest',
    accent: 'text-sky-600 dark:text-sky-400',
  },
};

interface CandidateCardProps {
  candidate: DrugCandidate;
  tier?: CandidateTier;
  onClick?: (candidate: DrugCandidate) => void;
}

export function CandidateCard({ candidate, tier, onClick }: CandidateCardProps) {
  const ranking = getCandidateRanking(candidate.chembl_id);
  const displayName = ranking?.displayName || candidate.drug_name;
  const tierStyle = tier ? TIER_STYLES[tier] : null;
  const topIndications = candidate.indications.slice(0, 3);

  return (
    <div
      className={`flex items-center gap-4 px-4 py-3 rounded-lg border border-border transition-colors hover:bg-muted/40 ${onClick ? 'cursor-pointer' : ''} ${tierStyle?.row ?? ''}`}
      onClick={() => onClick?.(candidate)}
    >
      {/* Score */}
      <div className="w-12 shrink-0 text-center">
        {ranking?.score ? (
          <span className={`text-lg font-bold font-mono ${tierStyle?.accent ?? 'text-muted-foreground'}`}>
            {ranking.score}
          </span>
        ) : (
          <span className="text-sm text-muted-foreground/40">—</span>
        )}
      </div>

      {/* Name + ChemBL ID */}
      <div className="w-52 shrink-0 min-w-0">
        <div className="font-semibold text-sm text-foreground truncate">{displayName}</div>
        {candidate.chembl_id && (
          <div className="text-xs text-muted-foreground font-mono">{candidate.chembl_id}</div>
        )}
      </div>

      {/* Tier badge */}
      <div className="w-16 shrink-0">
        {tierStyle && (
          <Badge variant="outline" className={`text-xs ${tierStyle.badge}`}>
            {tierStyle.label}
          </Badge>
        )}
      </div>

      {/* Molecular properties */}
      <div className="hidden md:flex items-center gap-3 shrink-0">
        <PropPill label="MW" value={candidate.molecular_weight?.toFixed(0)} />
        <PropPill label="LogP" value={candidate.alogp?.toFixed(1)} />
        <PropPill label="PSA" value={candidate.psa?.toFixed(0)} />
      </div>

      {/* Badges */}
      <div className="flex items-center gap-1.5 shrink-0 ml-auto">
        {candidate.is_natural_product && (
          <Badge variant="outline" className="text-xs border-primary/40 text-primary">
            Natural
          </Badge>
        )}
      </div>

      {/* Indications (hidden on small screens) */}
      <div className="hidden lg:flex items-center gap-1 min-w-0 max-w-xs">
        {topIndications.slice(0, 2).map((ind) => (
          <span
            key={ind}
            className="text-xs bg-secondary text-secondary-foreground px-1.5 py-0.5 rounded truncate max-w-[120px]"
          >
            {ind}
          </span>
        ))}
        {candidate.indications.length > 2 && (
          <span className="text-xs text-muted-foreground shrink-0">
            +{candidate.indications.length - 2}
          </span>
        )}
      </div>
    </div>
  );
}

function PropPill({ label, value }: { label: string; value?: string }) {
  if (!value || value === '0') return null;
  return (
    <div className="bg-muted/50 rounded px-1.5 py-0.5 text-xs whitespace-nowrap">
      <span className="text-muted-foreground">{label} </span>
      <span className="font-mono font-medium text-foreground">{value}</span>
    </div>
  );
}
