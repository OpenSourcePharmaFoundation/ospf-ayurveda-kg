import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from '@/components/ui/accordion';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from 'recharts';
import type { TableData } from '@/types/analysis';

interface DataTableVizProps {
  table: TableData;
}

export function DataTableViz({ table }: DataTableVizProps) {
  const hasChart = table.numericColumns.length > 0 && table.rows.length > 1;
  const entityCol = findEntityColumn(table);

  if (!hasChart) return null;

  const chartData = table.rows
    .map((row) => {
      const entry: Record<string, string | number> = {};
      if (entityCol) entry.name = row[entityCol] ?? '';
      table.numericColumns.forEach((col) => {
        const val = parseFloat(row[col]?.replace(/[,%$]/g, '') ?? '0');
        if (!isNaN(val)) entry[col] = val;
      });
      return entry;
    })
    .filter((d) => d.name || Object.keys(d).length > 1)
    .slice(0, 20);

  if (chartData.length === 0) return null;

  const colors = [
    'hsl(173, 58%, 39%)',
    'hsl(45, 93%, 47%)',
    'hsl(197, 37%, 24%)',
    'hsl(43, 74%, 66%)',
    'hsl(27, 87%, 67%)',
  ];

  return (
    <div className="my-4">
      <div className="bg-card border border-border rounded-lg p-4">
        {table.context && (
          <p className="text-xs font-medium text-muted-foreground mb-3 uppercase tracking-wider">
            {table.context}
          </p>
        )}
        <ResponsiveContainer width="100%" height={Math.min(300, chartData.length * 40 + 60)}>
          <BarChart
            data={chartData}
            layout={entityCol ? 'vertical' : 'horizontal'}
            margin={{ top: 5, right: 20, left: entityCol ? 100 : 5, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" stroke="hsl(0, 0%, 90%)" />
            {entityCol ? (
              <>
                <XAxis type="number" tick={{ fontSize: 11 }} />
                <YAxis
                  dataKey="name"
                  type="category"
                  tick={{ fontSize: 11 }}
                  width={95}
                />
              </>
            ) : (
              <>
                <XAxis dataKey="name" tick={{ fontSize: 11 }} />
                <YAxis tick={{ fontSize: 11 }} />
              </>
            )}
            <Tooltip
              contentStyle={{
                background: 'white',
                border: '1px solid hsl(0, 0%, 90%)',
                borderRadius: '6px',
                fontSize: '12px',
              }}
            />
            {table.numericColumns.slice(0, 5).map((col, i) => (
              <Bar
                key={col}
                dataKey={col}
                fill={colors[i % colors.length]}
                radius={[2, 2, 0, 0]}
                name={col}
              />
            ))}
          </BarChart>
        </ResponsiveContainer>
      </div>

      <Accordion className="mt-2">
        <AccordionItem value="raw-data" className="border-none">
          <AccordionTrigger className="text-xs text-muted-foreground hover:text-foreground py-2">
            View raw data
          </AccordionTrigger>
          <AccordionContent>
            <div className="overflow-x-auto rounded border border-border">
              <table className="min-w-full text-xs">
                <thead className="bg-muted/50">
                  <tr>
                    {table.headers.map((h) => (
                      <th key={h} className="px-3 py-2 text-left font-medium text-muted-foreground">
                        {h}
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {table.rows.map((row, i) => (
                    <tr key={i} className="border-t border-border/50 hover:bg-muted/20">
                      {table.headers.map((h) => (
                        <td key={h} className="px-3 py-1.5">
                          {row[h]}
                        </td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </AccordionContent>
        </AccordionItem>
      </Accordion>
    </div>
  );
}

function findEntityColumn(table: TableData): string | undefined {
  const entityPatterns = ['drug', 'candidate', 'name', 'compound', 'plant', 'gene', 'rank'];
  return table.headers.find((h) =>
    entityPatterns.some((p) => h.toLowerCase().includes(p)),
  );
}
