import { Badge } from '@/components/ui/badge';
import { Separator } from '@/components/ui/separator';
import { Drawer, DrawerContent } from '@/components/ui/drawer';
import type { DrugCandidate } from '@/types/drug-candidate';

interface CandidateDetailDrawerProps {
  candidate: DrugCandidate | null;
  open: boolean;
  onOpenChange: (open: boolean) => void;
}

const PHASE_LABELS: Record<number, string> = {
  0: 'Unknown',
  1: 'Phase I',
  2: 'Phase II',
  3: 'Phase III',
  4: 'Approved',
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

export function CandidateDetailDrawer({
  candidate,
  open,
  onOpenChange,
}: CandidateDetailDrawerProps) {
  if (!candidate) return null;

  const phaseLabel = PHASE_LABELS[candidate.max_phase] ?? `Phase ${candidate.max_phase}`;

  return (
    <Drawer open={open} onOpenChange={onOpenChange} swipeDirection="right">
      <DrawerContent
        title={candidate.drug_name}
        description={candidate.chembl_id || undefined}
      >
        <div className="px-6 py-5 space-y-6">
          <div className="flex flex-wrap gap-2">
            <Badge variant="outline">{phaseLabel}</Badge>
            {candidate.is_natural_product && (
              <Badge variant="outline" className="border-primary/40 text-primary">
                Natural Product
              </Badge>
            )}
          </div>

          <div>
            <h4 className="text-sm font-semibold text-foreground mb-1">Molecular Properties</h4>
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
            <h4 className="text-sm font-semibold text-foreground mb-1">
              Lipinski's Rule of Five
            </h4>
            <Separator className="mb-3" />
            <RuleOfFiveCheck candidate={candidate} />
          </div>

          {candidate.indications.length > 0 && (
            <div>
              <h4 className="text-sm font-semibold text-foreground mb-1">
                Indications ({candidate.indications.length})
              </h4>
              <Separator className="mb-3" />
              <div className="flex flex-wrap gap-1.5">
                {candidate.indications.map((ind) => (
                  <Badge key={ind} variant="secondary" className="text-xs">
                    {ind}
                  </Badge>
                ))}
              </div>
            </div>
          )}

          {candidate.chembl_id && (
            <div>
              <h4 className="text-sm font-semibold text-foreground mb-1">External Links</h4>
              <Separator className="mb-3" />
              <a
                href={`https://www.ebi.ac.uk/chembl/compound_report_card/${candidate.chembl_id}/`}
                target="_blank"
                rel="noopener noreferrer"
                className="text-sm text-primary hover:underline"
              >
                View on ChemBL →
              </a>
            </div>
          )}
        </div>
      </DrawerContent>
    </Drawer>
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
