import { useState, useCallback } from 'react';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { PageShell } from '@/components/layout/PageShell';
import { AppHeader } from '@/components/layout/AppHeader';
import { AnalysisView } from '@/components/analysis/AnalysisView';
import { DrugCandidatesView } from '@/components/drug-candidates/DrugCandidatesView';
import { readParam, useUrlState } from '@/hooks/use-url-state';

const VALID_TABS = ['candidates', 'analysis'];

function getInitialTab(): string {
  const param = readParam('tab');
  if (param && VALID_TABS.includes(param)) return param;
  return 'candidates';
}

export default function App() {
  const { update } = useUrlState();
  const [tab, setTab] = useState(getInitialTab);
  const [selectedAnalysis, setSelectedAnalysis] = useState(() => readParam('analysis') || 'summary');
  const [selectedSection, setSelectedSection] = useState<string | null>(() => readParam('section'));

  const handleTabChange = useCallback((value: string) => {
    setTab(value);
    update({
      tab: value === 'candidates' ? null : value,
      analysis: null,
      section: null,
      drug: null,
    });
  }, [update]);

  const handleAnalysisChange = useCallback((id: string) => {
    setSelectedAnalysis(id);
    setSelectedSection(null);
    update({ analysis: id === 'summary' ? null : id, section: null });
  }, [update]);

  const handleSectionChange = useCallback((id: string | null) => {
    setSelectedSection(id);
    update({ section: id });
  }, [update]);

  return (
    <PageShell>
      <AppHeader />
      <main className="max-w-7xl mx-auto px-4 sm:px-6 py-6">
        <Tabs value={tab} onValueChange={handleTabChange} className="w-full">
          <TabsList className="mb-6">
            <TabsTrigger value="candidates">Drug Candidates</TabsTrigger>
            <TabsTrigger value="analysis">Analysis</TabsTrigger>
          </TabsList>

          <TabsContent value="candidates">
            <DrugCandidatesView />
          </TabsContent>

          <TabsContent value="analysis">
            <AnalysisView
              selectedAnalysis={selectedAnalysis}
              onAnalysisChange={handleAnalysisChange}
              selectedSection={selectedSection}
              onSectionChange={handleSectionChange}
            />
          </TabsContent>
        </Tabs>
      </main>
    </PageShell>
  );
}
