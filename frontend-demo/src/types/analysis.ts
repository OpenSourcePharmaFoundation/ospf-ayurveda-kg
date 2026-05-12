export interface Section {
  id: string;
  title: string;
  content: string;
}

export interface AnalysisDocument {
  title: string;
  preamble: string;
  sections: Section[];
}

export interface TableData {
  headers: string[];
  rows: Record<string, string>[];
  numericColumns: string[];
  context: string;
}

export interface AnalysisEntry {
  id: string;
  label: string;
  filename: string | null;
  date: string | null;
  type: 'individual' | 'multi-agent' | 'summary' | 'conglomerate';
  description: string;
}
