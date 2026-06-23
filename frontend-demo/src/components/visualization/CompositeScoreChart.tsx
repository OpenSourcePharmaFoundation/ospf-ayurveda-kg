import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Cell,
} from 'recharts';
import { useIsMobile } from '@/hooks/use-media-query';

interface CandidateScore {
  name: string;
  score: number;
  safety: 'GREEN' | 'YELLOW' | 'ORANGE' | 'RED';
}

const CONSENSUS_CANDIDATES: CandidateScore[] = [
  { name: 'Dexamethasone mouthwash', score: 72, safety: 'GREEN' },
  { name: 'Budesonide mucoadhesive', score: 67.5, safety: 'GREEN' },
  { name: 'Mesalamine topical', score: 62.5, safety: 'GREEN' },
  { name: 'Melatonin oral gel', score: 61, safety: 'GREEN' },
  { name: 'NAC rinse', score: 59.5, safety: 'GREEN' },
  { name: 'Pentoxifylline', score: 58, safety: 'YELLOW' },
  { name: 'Apremilast', score: 57.5, safety: 'YELLOW' },
  { name: 'Glycyrrhizin (Yashtimadhu)', score: 56.5, safety: 'YELLOW' },
];

const safetyColors: Record<string, string> = {
  GREEN: 'hsl(152, 60%, 42%)',
  YELLOW: 'hsl(45, 93%, 47%)',
  ORANGE: 'hsl(27, 87%, 55%)',
  RED: 'hsl(0, 72%, 51%)',
};

function truncateName(name: string, max: number): string {
  return name.length > max ? name.slice(0, max - 1) + '…' : name;
}

export function CompositeScoreChart() {
  const isMobile = useIsMobile();
  const axisWidth = isMobile ? 90 : 125;
  const leftMargin = isMobile ? 95 : 130;
  const tickSize = isMobile ? 10 : 11;

  return (
    <div className="bg-card border border-border rounded-lg p-3 sm:p-4">
      <h3 className="text-sm font-semibold text-foreground mb-3">
        Consensus Drug Candidate Rankings
      </h3>
      <ResponsiveContainer width="100%" height={isMobile ? 280 : 320}>
        <BarChart
          data={CONSENSUS_CANDIDATES}
          layout="vertical"
          margin={{ top: 5, right: isMobile ? 15 : 30, left: leftMargin, bottom: 5 }}
        >
          <CartesianGrid strokeDasharray="3 3" stroke="hsl(0, 0%, 90%)" />
          <XAxis type="number" domain={[0, 100]} tick={{ fontSize: tickSize }} />
          <YAxis
            dataKey="name"
            type="category"
            tick={{ fontSize: tickSize }}
            width={axisWidth}
            tickFormatter={(name: string) => truncateName(name, isMobile ? 14 : 25)}
          />
          <Tooltip
            formatter={(value) => [`${value}/100`, 'Composite Score']}
            contentStyle={{
              background: 'white',
              border: '1px solid hsl(0, 0%, 90%)',
              borderRadius: '6px',
              fontSize: '12px',
            }}
          />
          <Bar dataKey="score" radius={[0, 4, 4, 0]}>
            {CONSENSUS_CANDIDATES.map((entry) => (
              <Cell key={entry.name} fill={safetyColors[entry.safety]} />
            ))}
          </Bar>
        </BarChart>
      </ResponsiveContainer>
      <div className="flex flex-wrap gap-3 sm:gap-4 mt-2 text-xs text-muted-foreground justify-center">
        {Object.entries(safetyColors).map(([label, color]) => (
          <span key={label} className="flex items-center gap-1">
            <span
              className="inline-block w-3 h-3 rounded-sm"
              style={{ backgroundColor: color }}
            />
            {label}
          </span>
        ))}
      </div>
    </div>
  );
}
