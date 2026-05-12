import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select';
import { ANALYSIS_REGISTRY } from '@/lib/analysis-registry';
import type { Section } from '@/types/analysis';

interface AnalysisToolbarProps {
  selectedAnalysis: string;
  onAnalysisChange: (id: string) => void;
  selectedSection: string | null;
  onSectionChange: (id: string | null) => void;
  sections: Section[];
}

export function AnalysisToolbar({
  selectedAnalysis,
  onAnalysisChange,
  selectedSection,
  onSectionChange,
  sections,
}: AnalysisToolbarProps) {
  const isSectionDisabled =
    selectedAnalysis === 'summary' || selectedAnalysis === 'all-output';

  return (
    <div className="flex flex-col sm:flex-row gap-3 mb-6">
      <div className="flex-1">
        <label className="text-xs font-medium text-muted-foreground mb-1.5 block">
          Analysis
        </label>
        <Select
          value={selectedAnalysis}
          onValueChange={(value) => {
            if (value) onAnalysisChange(value);
          }}
        >
          <SelectTrigger className="w-full">
            <SelectValue placeholder="Select analysis..." />
          </SelectTrigger>
          <SelectContent>
            {ANALYSIS_REGISTRY.map((entry) => (
              <SelectItem key={entry.id} value={entry.id}>
                <span className="flex items-center gap-2">
                  <span>{entry.label}</span>
                  {entry.type === 'multi-agent' && (
                    <span className="text-xs bg-primary/10 text-primary px-1.5 py-0.5 rounded">
                      Multi-Agent
                    </span>
                  )}
                </span>
              </SelectItem>
            ))}
          </SelectContent>
        </Select>
      </div>

      <div className="flex-1">
        <label className="text-xs font-medium text-muted-foreground mb-1.5 block">
          Section
        </label>
        <Select
          value={selectedSection ?? '__all__'}
          onValueChange={(value) => {
            if (value) onSectionChange(value === '__all__' ? null : value);
          }}
          disabled={isSectionDisabled}
        >
          <SelectTrigger className="w-full">
            <SelectValue
              placeholder={isSectionDisabled ? 'N/A for this view' : 'All sections'}
            />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="__all__">All sections</SelectItem>
            {sections.map((section) => (
              <SelectItem key={section.id} value={section.id}>
                {section.title}
              </SelectItem>
            ))}
          </SelectContent>
        </Select>
      </div>
    </div>
  );
}
