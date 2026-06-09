import type { DrugRouteData, IndicationFrequencyMap } from '@/types/drug-candidate';

interface IndicationsTableProps {
  indications: string[];
  chemblId: string;
  routeData: DrugRouteData | undefined;
  indicationFrequency: IndicationFrequencyMap;
}

function titleCase(s: string): string {
  return s.replace(/\b\w/g, (c) => c.toUpperCase());
}

function getCommonality(count: number): { label: string; className: string } {
  if (count >= 15) return { label: 'Very Common', className: 'text-emerald-700 dark:text-emerald-400' };
  if (count >= 7) return { label: 'Common', className: 'text-sky-700 dark:text-sky-400' };
  if (count >= 3) return { label: 'Uncommon', className: 'text-amber-700 dark:text-amber-400' };
  return { label: 'Rare', className: 'text-muted-foreground' };
}

function getRoute(indication: string, routeData: DrugRouteData | undefined): string {
  if (!routeData) return '—';
  const direct = routeData.routes_by_indication[indication.toLowerCase()];
  if (direct) return direct;
  if (routeData.available_routes.length > 0) {
    return routeData.available_routes.join(', ');
  }
  return '—';
}

export function IndicationsTable({
  indications,
  chemblId,
  routeData,
  indicationFrequency,
}: IndicationsTableProps) {
  if (indications.length === 0) return null;

  return (
    <div className="overflow-x-auto">
      <table className="w-full text-sm">
        <thead>
          <tr className="border-b border-border text-left">
            <th className="pb-2 pr-4 text-xs font-semibold text-muted-foreground uppercase tracking-wide">
              Indication
            </th>
            <th className="pb-2 pr-4 text-xs font-semibold text-muted-foreground uppercase tracking-wide whitespace-nowrap">
              Commonality
            </th>
            <th className="pb-2 text-xs font-semibold text-muted-foreground uppercase tracking-wide whitespace-nowrap">
              Route
            </th>
          </tr>
        </thead>
        <tbody className="divide-y divide-border/50">
          {indications.map((ind) => {
            const freq = indicationFrequency.get(ind) ?? 1;
            const commonality = getCommonality(freq);
            const route = getRoute(ind, routeData);

            return (
              <tr key={ind} className="hover:bg-muted/30 transition-colors">
                <td className="py-2 pr-4 text-foreground">{titleCase(ind)}</td>
                <td className={`py-2 pr-4 whitespace-nowrap text-xs font-medium ${commonality.className}`}>
                  {commonality.label}
                </td>
                <td className="py-2 text-xs text-muted-foreground whitespace-nowrap">{route}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}
