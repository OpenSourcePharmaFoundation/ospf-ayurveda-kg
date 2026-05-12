import { Card, CardContent } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import type { DrugCandidate } from '@/types/drug-candidate';

interface CandidateCardProps {
  candidate: DrugCandidate;
}

export function CandidateCard({ candidate }: CandidateCardProps) {
  const properties = [
    { label: 'MW', value: candidate.molecular_weight?.toFixed(1) },
    { label: 'LogP', value: candidate.alogp?.toFixed(2) },
    { label: 'PSA', value: candidate.psa?.toFixed(1) },
    { label: 'HBD', value: candidate.hbd?.toString() },
    { label: 'HBA', value: candidate.hba?.toString() },
  ].filter((p) => p.value && p.value !== '0' && p.value !== '0.0' && p.value !== '0.00');

  const topIndications = candidate.indications.slice(0, 3);

  return (
    <Card className="hover:shadow-md transition-shadow">
      <CardContent className="pt-4">
        <div className="flex items-start justify-between mb-2">
          <div className="min-w-0">
            <h3 className="font-semibold text-foreground text-sm truncate">
              {candidate.drug_name}
            </h3>
            {candidate.chembl_id && (
              <span className="text-xs text-muted-foreground font-mono">
                {candidate.chembl_id}
              </span>
            )}
          </div>
          <div className="flex gap-1 shrink-0">
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
