import { useMemo } from 'react';
import { AnalysisToolbar } from '@/components/layout/AnalysisToolbar';
import { SummaryView } from './SummaryView';
import { AllOutputView } from './AllOutputView';
import { SectionContent } from './SectionContent';
import { MarkdownRenderer } from '@/components/markdown/MarkdownRenderer';
import { useAnalysisDocument } from '@/hooks/use-analysis-document';
import { getAnalysisById } from '@/lib/analysis-registry';
import type { Section } from '@/types/analysis';

interface AnalysisViewProps {
  selectedAnalysis: string;
  onAnalysisChange: (id: string) => void;
  selectedSection: string | null;
  onSectionChange: (id: string | null) => void;
}

export function AnalysisView({
  selectedAnalysis,
  onAnalysisChange,
  selectedSection,
  onSectionChange,
}: AnalysisViewProps) {
  const entry = getAnalysisById(selectedAnalysis);
  const { document, loading, error } = useAnalysisDocument(entry?.filename ?? null);

  const sections: Section[] = useMemo(() => document?.sections ?? [], [document]);

  const renderContent = () => {
    if (selectedAnalysis === 'summary') return <SummaryView />;
    if (selectedAnalysis === 'all-output') return <AllOutputView />;

    if (loading) {
      return (
        <div className="flex items-center justify-center py-12">
          <div className="text-muted-foreground">Loading analysis...</div>
        </div>
      );
    }

    if (error) {
      return (
        <div className="text-destructive p-4 rounded-lg border border-destructive/20 bg-destructive/5">
          Failed to load: {error}
        </div>
      );
    }

    if (!document) return null;

    if (selectedSection) {
      const section = sections.find((s) => s.id === selectedSection);
      if (section) return <SectionContent section={section} />;
    }

    const fullContent = [document.preamble, ...sections.map((s) => `## ${s.title}\n\n${s.content}`)]
      .filter(Boolean)
      .join('\n\n');

    return <MarkdownRenderer content={fullContent} />;
  };

  return (
    <div>
      <AnalysisToolbar
        selectedAnalysis={selectedAnalysis}
        onAnalysisChange={onAnalysisChange}
        selectedSection={selectedSection}
        onSectionChange={onSectionChange}
        sections={sections}
      />
      {renderContent()}
    </div>
  );
}
