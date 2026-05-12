import { useAnalysisDocument } from '@/hooks/use-analysis-document';
import { MarkdownRenderer } from '@/components/markdown/MarkdownRenderer';
import { Separator } from '@/components/ui/separator';
import { ANALYSIS_REGISTRY } from '@/lib/analysis-registry';
import type { AnalysisEntry } from '@/types/analysis';

const documentEntries = ANALYSIS_REGISTRY.filter(
  (e): e is AnalysisEntry & { filename: string } => e.filename !== null,
);

function DocumentBlock({ entry, showSeparator }: { entry: AnalysisEntry & { filename: string }; showSeparator: boolean }) {
  const { document, loading, error } = useAnalysisDocument(entry.filename);

  if (loading) return <div className="text-muted-foreground py-4">Loading {entry.label}...</div>;
  if (error) return <div className="text-destructive text-sm">Failed to load {entry.label}</div>;
  if (!document) return null;

  const fullContent = [document.preamble, ...document.sections.map((s) => s.content)]
    .filter(Boolean)
    .join('\n\n');

  return (
    <div>
      {showSeparator && <Separator className="my-8" />}
      <div className="mb-4">
        <span className="text-xs font-medium text-primary bg-primary/10 px-2 py-1 rounded">
          {entry.label}
        </span>
        {entry.date && (
          <span className="text-xs text-muted-foreground ml-2">{entry.date}</span>
        )}
      </div>
      <MarkdownRenderer content={fullContent} />
    </div>
  );
}

export function AllOutputView() {
  return (
    <div className="space-y-8">
      <div>
        <h2 className="text-2xl font-bold text-foreground mb-2">All Output</h2>
        <p className="text-muted-foreground">
          Complete output from all {documentEntries.length} analysis documents
        </p>
      </div>
      {documentEntries.map((entry, i) => (
        <DocumentBlock key={entry.id} entry={entry} showSeparator={i > 0} />
      ))}
    </div>
  );
}
