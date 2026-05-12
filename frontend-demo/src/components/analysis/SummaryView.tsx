import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { CompositeScoreChart } from '@/components/visualization/CompositeScoreChart';

const KEY_FINDINGS = [
  'Only one FDA-approved treatment exists (Palifermin) — but it costs ~$5,000/dose and is limited to stem cell transplant patients',
  'Knowledge graph analysis of 3,276 approved drugs identified 20+ repurposing candidates with favorable oral mucosal profiles',
  'Multi-agent consensus (15 expert agents) converged on 8 ranked candidates with composite scores 56-72/100',
  'Two combination strategies recommended: MesaPento Rinse (Western) and Yashtimadhu-Haritaki Kavala (Ayurvedic)',
  'Glycyrrhiza glabra (Licorice) emerged as the strongest Ayurvedic bridge — with unique HMGB1 inhibition mechanism',
];

const TOP_CANDIDATES = [
  {
    rank: 1,
    name: 'Dexamethasone mouthwash',
    score: 72,
    safety: 'GREEN' as const,
    rationale: 'Clinical standard benchmark; well-characterized safety in cancer patients',
  },
  {
    rank: 2,
    name: 'Budesonide mucoadhesive',
    score: 67.5,
    safety: 'GREEN' as const,
    rationale: 'Superior mucosal selectivity; 90% first-pass metabolism minimizes systemic exposure',
  },
  {
    rank: 3,
    name: 'Mesalamine topical',
    score: 62.5,
    safety: 'GREEN' as const,
    rationale: 'Anti-inflammatory WITHOUT immunosuppression; ideal MW/LogP for oral delivery',
  },
  {
    rank: 4,
    name: 'Melatonin oral gel',
    score: 61,
    safety: 'GREEN' as const,
    rationale: 'Only Phase 1 ROS agent; radioprotective for normal tissue; best risk/reward ratio',
  },
  {
    rank: 5,
    name: 'NAC rinse',
    score: 59.5,
    safety: 'GREEN' as const,
    rationale: 'Immediately deployable (OTC); ROS scavenger; proven mucosal protectant',
  },
  {
    rank: 6,
    name: 'Pentoxifylline',
    score: 58,
    safety: 'YELLOW' as const,
    rationale: 'TNF-alpha suppression; novel repurposing find from the knowledge graph',
  },
  {
    rank: 7,
    name: 'Apremilast',
    score: 57.5,
    safety: 'YELLOW' as const,
    rationale: "FDA-approved for Behcet's oral ulcers; phenotypic analog to OM",
  },
  {
    rank: 8,
    name: 'Glycyrrhizin (Yashtimadhu)',
    score: 56.5,
    safety: 'YELLOW' as const,
    rationale: 'Highest Ayurvedic bridge score; unique HMGB1 inhibition not available in any drug',
  },
];

const safetyVariants: Record<string, 'default' | 'secondary' | 'destructive' | 'outline'> = {
  GREEN: 'default',
  YELLOW: 'secondary',
  ORANGE: 'outline',
  RED: 'destructive',
};

export function SummaryView() {
  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-2xl font-bold text-foreground mb-2">
          Drug Discovery Summary
        </h2>
        <p className="text-muted-foreground">
          Cross-analysis findings from 3 independent analyses spanning Jan-May 2026
        </p>
      </div>

      <Card>
        <CardHeader>
          <CardTitle className="text-base">Key Findings</CardTitle>
        </CardHeader>
        <CardContent>
          <ul className="space-y-2">
            {KEY_FINDINGS.map((finding, i) => (
              <li key={i} className="flex gap-3 text-sm text-foreground/80">
                <span className="text-primary font-semibold shrink-0">{i + 1}.</span>
                <span>{finding}</span>
              </li>
            ))}
          </ul>
        </CardContent>
      </Card>

      <CompositeScoreChart />

      <Card>
        <CardHeader>
          <CardTitle className="text-base">Ranked Drug Candidates</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-3">
            {TOP_CANDIDATES.map((candidate) => (
              <div
                key={candidate.rank}
                className="flex items-start gap-3 p-3 rounded-lg hover:bg-muted/50 transition-colors"
              >
                <span className="text-lg font-bold text-primary w-8 shrink-0">
                  #{candidate.rank}
                </span>
                <div className="flex-1 min-w-0">
                  <div className="flex items-center gap-2 mb-1">
                    <span className="font-semibold text-foreground">{candidate.name}</span>
                    <Badge variant={safetyVariants[candidate.safety]}>
                      {candidate.score}/100
                    </Badge>
                  </div>
                  <p className="text-sm text-muted-foreground">{candidate.rationale}</p>
                </div>
              </div>
            ))}
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle className="text-base">Recommended Combination Strategies</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid gap-4 md:grid-cols-2">
            <div className="p-4 rounded-lg border border-border bg-muted/20">
              <h4 className="font-semibold text-foreground mb-2">
                Track 1: MesaPento Rinse
              </h4>
              <p className="text-sm text-muted-foreground mb-2">Western pharmaceutical approach</p>
              <ul className="text-sm space-y-1 text-foreground/80">
                <li>Mesalamine 50mg/5mL</li>
                <li>Pentoxifylline 100mg/5mL</li>
                <li>NAC 500mg/5mL</li>
              </ul>
            </div>
            <div className="p-4 rounded-lg border border-primary/30 bg-primary/5">
              <h4 className="font-semibold text-foreground mb-2">
                Track 2: Yashtimadhu-Haritaki Kavala
              </h4>
              <p className="text-sm text-muted-foreground mb-2">Ayurvedic formulation approach</p>
              <ul className="text-sm space-y-1 text-foreground/80">
                <li>Glycyrrhiza glabra (Licorice root)</li>
                <li>Terminalia chebula (Haritaki)</li>
              </ul>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
