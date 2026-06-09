import { useState, useMemo, useCallback } from 'react';
import { ChevronUp, ChevronDown } from 'lucide-react';
import type { DrugRouteData, IndicationFrequencyMap } from '@/types/drug-candidate';

interface IndicationsTableProps {
  indications: string[];
  chemblId: string;
  routeData: DrugRouteData | undefined;
  indicationFrequency: IndicationFrequencyMap;
}

type SortColumn = 'indication' | 'commonality' | 'route';
type SortDirection = 'asc' | 'desc';

function titleCase(s: string): string {
  return s.replace(/\b\w/g, (c) => c.toUpperCase());
}

function getCommonality(count: number): { label: string; className: string; rank: number } {
  if (count >= 15) return { label: 'Very Common', className: 'text-emerald-700 dark:text-emerald-400', rank: 4 };
  if (count >= 7) return { label: 'Common', className: 'text-sky-700 dark:text-sky-400', rank: 3 };
  if (count >= 3) return { label: 'Uncommon', className: 'text-amber-700 dark:text-amber-400', rank: 2 };
  return { label: 'Rare', className: 'text-muted-foreground', rank: 1 };
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

function SortIcon({ column, sortColumn, sortDirection }: { column: SortColumn; sortColumn: SortColumn; sortDirection: SortDirection }) {
  if (column !== sortColumn) {
    return <ChevronDown className="size-3 opacity-0 group-hover:opacity-40 transition-opacity" />;
  }
  return sortDirection === 'desc'
    ? <ChevronDown className="size-3" />
    : <ChevronUp className="size-3" />;
}

export function IndicationsTable({
  indications,
  chemblId,
  routeData,
  indicationFrequency,
}: IndicationsTableProps) {
  const [sortColumn, setSortColumn] = useState<SortColumn>('commonality');
  const [sortDirection, setSortDirection] = useState<SortDirection>('desc');

  const handleSort = useCallback((column: SortColumn) => {
    setSortColumn((prev) => {
      if (prev === column) {
        setSortDirection((d) => (d === 'desc' ? 'asc' : 'desc'));
        return prev;
      }
      setSortDirection(column === 'indication' ? 'asc' : 'desc');
      return column;
    });
  }, []);

  const sorted = useMemo(() => {
    const rows = indications.map((ind) => {
      const freq = indicationFrequency.get(ind) ?? 1;
      return {
        name: ind,
        freq,
        commonality: getCommonality(freq),
        route: getRoute(ind, routeData),
      };
    });

    rows.sort((a, b) => {
      let cmp = 0;
      switch (sortColumn) {
        case 'indication':
          cmp = a.name.localeCompare(b.name);
          break;
        case 'commonality':
          cmp = a.freq - b.freq;
          break;
        case 'route':
          cmp = a.route.localeCompare(b.route);
          break;
      }
      return sortDirection === 'desc' ? -cmp : cmp;
    });

    return rows;
  }, [indications, indicationFrequency, routeData, sortColumn, sortDirection]);

  if (indications.length === 0) return null;

  const thClass =
    'group pb-2 pr-4 text-xs font-semibold text-muted-foreground uppercase tracking-wide cursor-pointer select-none hover:text-foreground transition-colors';

  return (
    <div className="overflow-x-auto">
      <table className="w-full text-sm">
        <thead>
          <tr className="border-b border-border text-left">
            <th className={thClass} onClick={() => handleSort('indication')}>
              <span className="inline-flex items-center gap-1">
                Indication
                <SortIcon column="indication" sortColumn={sortColumn} sortDirection={sortDirection} />
              </span>
            </th>
            <th className={`${thClass} whitespace-nowrap`} onClick={() => handleSort('commonality')}>
              <span className="inline-flex items-center gap-1">
                Commonality
                <SortIcon column="commonality" sortColumn={sortColumn} sortDirection={sortDirection} />
              </span>
            </th>
            <th className={`${thClass} whitespace-nowrap`} onClick={() => handleSort('route')}>
              <span className="inline-flex items-center gap-1">
                Route
                <SortIcon column="route" sortColumn={sortColumn} sortDirection={sortDirection} />
              </span>
            </th>
          </tr>
        </thead>
        <tbody className="divide-y divide-border/50">
          {sorted.map((row) => (
            <tr key={row.name} className="hover:bg-muted/30 transition-colors">
              <td className="py-2 pr-4 text-foreground">{titleCase(row.name)}</td>
              <td className={`py-2 pr-4 whitespace-nowrap text-xs font-medium ${row.commonality.className}`}>
                {row.commonality.label}
              </td>
              <td className="py-2 text-xs text-muted-foreground whitespace-nowrap">{row.route}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
