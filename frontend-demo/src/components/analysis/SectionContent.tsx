import { useMemo } from 'react';
import { MarkdownRenderer } from '@/components/markdown/MarkdownRenderer';
import { DataTableViz } from '@/components/visualization/DataTableViz';
import { extractTables } from '@/lib/table-extractor';
import type { Section } from '@/types/analysis';

interface SectionContentProps {
  section: Section;
}

export function SectionContent({ section }: SectionContentProps) {
  const tables = useMemo(() => extractTables(section.content), [section.content]);

  return (
    <div>
      <h2 className="text-xl font-semibold text-foreground mb-4 pb-2 border-b border-border">
        {section.title}
      </h2>
      {tables.map((table, i) => (
        <DataTableViz key={`${section.id}-table-${i}`} table={table} />
      ))}
      <MarkdownRenderer content={section.content} />
    </div>
  );
}
