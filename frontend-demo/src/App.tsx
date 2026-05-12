import { useState } from 'react';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { PageShell } from '@/components/layout/PageShell';
import { AppHeader } from '@/components/layout/AppHeader';
import { AnalysisView } from '@/components/analysis/AnalysisView';
import { DrugCandidatesView } from '@/components/drug-candidates/DrugCandidatesView';

export default function App() {
  const [selectedAnalysis, setSelectedAnalysis] = useState('summary');
  const [selectedSection, setSelectedSection] = useState<string | null>(null);

  return (
    <PageShell>
      <AppHeader />
      <main className="max-w-7xl mx-auto px-4 sm:px-6 py-6">
        <Tabs defaultValue="analysis" className="w-full">
          <TabsList className="mb-6">
            <TabsTrigger value="analysis">Analysis</TabsTrigger>
            <TabsTrigger value="candidates">Drug Candidates</TabsTrigger>
          </TabsList>

          <TabsContent value="analysis">
            <AnalysisView
              selectedAnalysis={selectedAnalysis}
              onAnalysisChange={setSelectedAnalysis}
              selectedSection={selectedSection}
              onSectionChange={setSelectedSection}
            />
          </TabsContent>

          <TabsContent value="candidates">
            <DrugCandidatesView />
          </TabsContent>
        </Tabs>
      </main>
    </PageShell>
  );
}
