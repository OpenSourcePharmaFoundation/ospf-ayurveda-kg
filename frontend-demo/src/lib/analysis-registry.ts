import type { AnalysisEntry } from '@/types/analysis';

export const ANALYSIS_REGISTRY: AnalysisEntry[] = [
  {
    id: 'summary',
    label: 'Summary',
    filename: null,
    date: null,
    type: 'summary',
    description: 'Cross-analysis summary of key findings and recommended candidates',
  },
  {
    id: 'all-output',
    label: 'All Output',
    filename: null,
    date: null,
    type: 'conglomerate',
    description: 'Full conglomerate of all analysis documents',
  },
  {
    id: 'may-04-multi-agent',
    label: 'Multi-Agent Consensus (May 2026)',
    filename: 'oral_mucositis_multi_agent_drug_discovery-2026-05-04.md',
    date: '2026-05-04',
    type: 'multi-agent',
    description: '15-agent multi-round drug discovery pipeline consensus',
  },
  {
    id: 'may-03-comprehensive',
    label: 'Drug Repurposing & Ayurvedic Bridge (May 2026)',
    filename: 'oral_mucositis_drug_candidates-2026-05-03.md',
    date: '2026-05-03',
    type: 'individual',
    description: 'Comprehensive analysis with breast cancer intersection and Ayurvedic bridge',
  },
  {
    id: 'jan-29-candidates',
    label: 'Molecular Property Profiling (Jan 2026)',
    filename: 'oral_mucositis_drug_candidates-2026-01-29.md',
    date: '2026-01-29',
    type: 'individual',
    description: 'Initial ChemBL-based repurposing candidates',
  },
];

export function getAnalysisById(id: string): AnalysisEntry | undefined {
  return ANALYSIS_REGISTRY.find((entry) => entry.id === id);
}
