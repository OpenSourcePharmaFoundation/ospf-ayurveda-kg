import { Card, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import type { DrugCandidate } from '@/types/drug-candidate';
import { getCandidateRanking } from '@/lib/candidate-tiers';
import type { CandidateTier } from '@/lib/candidate-tiers';

const TIER_STYLES: Record<string, { card: string; badge: string; label: string }> = {
  elite: {
    card: 'ring-[3px] ring-emerald-500 shadow-[0_0_20px_rgba(16,185,129,0.4),0_0_6px_rgba(16,185,129,0.25)] dark:ring-emerald-400 dark:shadow-[0_0_20px_rgba(16,185,129,0.3),0_0_6px_rgba(16,185,129,0.15)] bg-gradient-to-br from-emerald-50/60 to-card dark:from-emerald-950/20 dark:to-card',
    badge: 'bg-emerald-600 text-white border-emerald-700 font-semibold',
    label: 'Lead Candidate',
  },
  top: {
    card: 'ring-2 ring-amber-400/70 shadow-[0_0_12px_rgba(251,191,36,0.25)] dark:ring-amber-500/60 dark:shadow-[0_0_12px_rgba(251,191,36,0.15)]',
    badge: 'bg-amber-500 text-white border-amber-500',
    label: 'Top Candidate',
  },
  highlighted: {
    card: 'ring-2 ring-sky-400/50 dark:ring-sky-500/40',
    badge: 'bg-sky-100 text-sky-700 border-sky-300 dark:bg-sky-900/40 dark:text-sky-300 dark:border-sky-600',
    label: 'Candidate of Interest',
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

  const properties = [
    ...(ranking?.score ? [{ label: 'Score', value: String(ranking.score) }] : []),
    { label: 'MW', value: candidate.molecular_weight?.toFixed(1) },
    { label: 'LogP', value: candidate.alogp?.toFixed(2) },
    { label: 'PSA', value: candidate.psa?.toFixed(1) },
    { label: 'HBD', value: candidate.hbd?.toString() },
    { label: 'HBA', value: candidate.hba?.toString() },
  ].filter((p) => p.value && p.value !== '0' && p.value !== '0.0' && p.value !== '0.00');

  return (
    <Card
      className={`hover:shadow-md transition-shadow ${onClick ? 'cursor-pointer' : ''} ${tierStyle?.card ?? ''}`}
      onClick={() => onClick?.(candidate)}
    >
      <CardContent className="pt-4">
        <div className="flex items-start justify-between mb-2">
          <div className="min-w-0">
            <h3 className="font-semibold text-foreground text-sm truncate">
              {displayName}
            </h3>
            {candidate.chembl_id && (
              <span className="text-xs text-muted-foreground font-mono">
                {candidate.chembl_id}
              </span>
            )}
          </div>
          <div className="flex gap-1 shrink-0">
            {tierStyle && (
              <Badge variant="outline" className={`text-xs ${tierStyle.badge}`}>
                {tierStyle.label}
              </Badge>
            )}
            {candidate.is_natural_product && (
              <Badge variant="outline" className="text-xs border-primary/40 text-primary">
                Natural
              </Badge>
            )}
          </div>
        </div>

        {properties.length > 0 && (
          <div className="flex flex-wrap gap-2 my-3">
            {properties.map(({ label, value }) => (
              <div
                key={label}
                className="bg-muted/50 rounded px-2 py-1 text-xs"
              >
                <span className="text-muted-foreground">{label}: </span>
                <span className="font-mono font-medium text-foreground">{value}</span>
              </div>
            ))}
          </div>
        )}

        {topIndications.length > 0 && (
          <div className="mt-2">
            <p className="text-xs text-muted-foreground mb-1">Indications:</p>
            <div className="flex flex-wrap gap-1">
              {topIndications.map((ind) => (
                <span
                  key={ind}
                  className="text-xs bg-secondary text-secondary-foreground px-1.5 py-0.5 rounded"
                >
                  {ind}
                </span>
              ))}
              {candidate.indications.length > 3 && (
                <span className="text-xs text-muted-foreground">
                  +{candidate.indications.length - 3} more
                </span>
              )}
            </div>
          </div>
        )}
      </CardContent>
    </Card>
  );
}
