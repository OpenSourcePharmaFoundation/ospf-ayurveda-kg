import type { TableData } from '@/types/analysis';

export function extractTables(markdown: string): TableData[] {
  const lines = markdown.split('\n');
  const tables: TableData[] = [];
  let i = 0;

  while (i < lines.length) {
    if (isTableRow(lines[i]) && i + 1 < lines.length && isSeparatorRow(lines[i + 1])) {
      const context = findContext(lines, i);
      const headers = parseRow(lines[i]);
      i += 2; // skip header + separator

      const rows: Record<string, string>[] = [];
      while (i < lines.length && isTableRow(lines[i])) {
        const values = parseRow(lines[i]);
        const row: Record<string, string> = {};
        headers.forEach((h, idx) => {
          row[h] = values[idx] ?? '';
        });
        rows.push(row);
        i++;
      }

      const numericColumns = detectNumericColumns(headers, rows);

      if (headers.length > 0 && rows.length > 0) {
        tables.push({ headers, rows, numericColumns, context });
      }
    } else {
      i++;
    }
  }

  return tables;
}

function isTableRow(line: string): boolean {
  if (!line) return false;
  const trimmed = line.trim();
  return trimmed.startsWith('|') && trimmed.endsWith('|') && trimmed.includes('|');
}

function isSeparatorRow(line: string): boolean {
  if (!line) return false;
  const trimmed = line.trim();
  return /^\|[\s:]*-+[\s:]*(\|[\s:]*-+[\s:]*)*\|$/.test(trimmed);
}

function parseRow(line: string): string[] {
  return line
    .trim()
    .replace(/^\|/, '')
    .replace(/\|$/, '')
    .split('|')
    .map((cell) => cell.trim());
}

function findContext(lines: string[], tableStart: number): string {
  for (let j = tableStart - 1; j >= Math.max(0, tableStart - 5); j--) {
    const line = lines[j].trim();
    if (line.startsWith('#')) return line.replace(/^#+\s*/, '');
    if (line.length > 0 && !isTableRow(lines[j])) return line;
  }
  return '';
}

function detectNumericColumns(
  headers: string[],
  rows: Record<string, string>[],
): string[] {
  return headers.filter((header) => {
    if (rows.length === 0) return false;
    const numericCount = rows.filter((row) => {
      const val = row[header]?.replace(/[,%$]/g, '').trim();
      return val !== '' && !isNaN(Number(val));
    }).length;
    return numericCount / rows.length > 0.5;
  });
}
