import { useState, useMemo, useCallback } from 'react';
import { ChevronUp, ChevronDown, Check } from 'lucide-react';
import type { DrugRouteData, IndicationFrequencyMap } from '@/types/drug-candidate';

interface IndicationsTableProps {
  indications: string[];
  routeData: DrugRouteData | undefined;
  indicationFrequency: IndicationFrequencyMap;
}

const ROUTES = [
  { key: 'Oral', label: 'Oral' },
  { key: 'Topical', label: 'Top.' },
  { key: 'Topical (oral cavity)', label: 'Rinse' },
  { key: 'IV', label: 'IV' },
  { key: 'Injection', label: 'Inj.' },
  { key: 'Inhaled', label: 'Inh.' },
  { key: 'Nasal', label: 'Nasal' },
  { key: 'Ophthalmic', label: 'Ophth.' },
  { key: 'Otic', label: 'Otic' },
] as const;

type RouteKey = (typeof ROUTES)[number]['key'];
type SortColumn = 'indication' | 'commonality' | RouteKey;
type SortDirection = 'asc' | 'desc';

function titleCase(s: string): string {
  return s.replace(/\b\w/g, (c) => c.toUpperCase());
}

function getCommonality(count: number): { label: string; className: string } {
  if (count >= 15) return { label: 'Very Common', className: 'text-emerald-700 dark:text-emerald-400' };
  if (count >= 7) return { label: 'Common', className: 'text-sky-700 dark:text-sky-400' };
  if (count >= 3) return { label: 'Uncommon', className: 'text-amber-700 dark:text-amber-400' };
  return { label: 'Rare', className: 'text-muted-foreground' };
}

function getRoutes(indication: string, routeData: DrugRouteData | undefined): Set<string> {
  if (!routeData) return new Set();
  const direct = routeData.routes_by_indication[indication.toLowerCase()];
  if (direct) {
    return new Set(direct.split('/').map((r) => r.trim()));
  }
  if (routeData.available_routes.length > 0) {
    return new Set(routeData.available_routes);
  }
  return new Set();
}

interface RowData {
  name: string;
  freq: number;
  commonality: { label: string; className: string };
  routes: Set<string>;
  routeCount: number;
}

function SortIcon({ active, direction }: { active: boolean; direction: SortDirection }) {
  if (!active) {
    return <ChevronDown className="size-3 opacity-0 group-hover:opacity-40 transition-opacity" />;
  }
  return direction === 'desc'
    ? <ChevronDown className="size-3" />
    : <ChevronUp className="size-3" />;
}

export function IndicationsTable({
  indications,
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

  const activeRoutes = useMemo(() => {
    const active = new Set<string>();
    for (const ind of indications) {
      for (const r of getRoutes(ind, routeData)) {
        active.add(r);
      }
    }
    return ROUTES.filter((r) => active.has(r.key));
  }, [indications, routeData]);

  const sorted = useMemo(() => {
    const rows: RowData[] = indications.map((ind) => {
      const freq = indicationFrequency.get(ind) ?? 1;
      const routes = getRoutes(ind, routeData);
      return {
        name: ind,
        freq,
        commonality: getCommonality(freq),
        routes,
        routeCount: routes.size,
      };
    });

    rows.sort((a, b) => {
      let cmp = 0;
      if (sortColumn === 'indication') {
        cmp = a.name.localeCompare(b.name);
      } else if (sortColumn === 'commonality') {
        cmp = a.freq - b.freq;
      } else {
        const aHas = a.routes.has(sortColumn) ? 1 : 0;
        const bHas = b.routes.has(sortColumn) ? 1 : 0;
        cmp = aHas - bHas;
      }
      return sortDirection === 'desc' ? -cmp : cmp;
    });

    return rows;
  }, [indications, indicationFrequency, routeData, sortColumn, sortDirection]);

  if (indications.length === 0) return null;

  const thBase =
    'group pb-2 text-xs font-semibold text-muted-foreground uppercase tracking-wide cursor-pointer select-none hover:text-foreground transition-colors';

  return (
    <div className="overflow-x-auto">
      <table className="w-full text-sm">
        <thead>
          <tr className="border-b border-border text-left">
            <th className={`${thBase} pr-4`} onClick={() => handleSort('indication')}>
              <span className="inline-flex items-center gap-1">
                Indication
                <SortIcon active={sortColumn === 'indication'} direction={sortDirection} />
              </span>
            </th>
            <th className={`${thBase} pr-4 whitespace-nowrap`} onClick={() => handleSort('commonality')}>
              <span className="inline-flex items-center gap-1">
                Commonality
                <SortIcon active={sortColumn === 'commonality'} direction={sortDirection} />
              </span>
            </th>
            {activeRoutes.map((r) => (
              <th
                key={r.key}
                className={`${thBase} px-1.5 text-center whitespace-nowrap`}
                title={r.key}
                onClick={() => handleSort(r.key)}
              >
                <span className="inline-flex items-center gap-0.5 justify-center">
                  {r.label}
                  <SortIcon active={sortColumn === r.key} direction={sortDirection} />
                </span>
              </th>
            ))}
          </tr>
        </thead>
        <tbody className="divide-y divide-border/50">
          {sorted.map((row) => (
            <tr key={row.name} className="hover:bg-muted/30 transition-colors">
              <td className="py-2 pr-4 text-foreground">{titleCase(row.name)}</td>
              <td className={`py-2 pr-4 whitespace-nowrap text-xs font-medium ${row.commonality.className}`}>
                {row.commonality.label}
              </td>
              {activeRoutes.map((r) => (
                <td key={r.key} className="py-2 px-1.5 text-center">
                  {row.routes.has(r.key) && (
                    <Check className="size-3.5 text-primary mx-auto" />
                  )}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
