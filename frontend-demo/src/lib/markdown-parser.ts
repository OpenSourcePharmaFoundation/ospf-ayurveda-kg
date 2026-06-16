import type { AnalysisDocument, Section } from '@/types/analysis';

function slugify(text: string): string {
  return text
    .toLowerCase()
    .replace(/[^\w\s-]/g, '')
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-')
    .trim();
}

function extractTitle(preamble: string): string {
  const lines = preamble.split('\n');
  for (const line of lines) {
    const h1Match = line.match(/^#\s+(.+)/);
    if (h1Match) return h1Match[1].trim();
  }
  return lines.find((l) => l.trim().length > 0)?.trim() ?? 'Untitled Analysis';
}

export function parseMarkdown(raw: string): AnalysisDocument {
  const lines = raw.split('\n');
  const sections: Section[] = [];
  let preambleLines: string[] = [];
  let currentTitle: string | null = null;
  let currentLines: string[] = [];

  for (const line of lines) {
    const h2Match = line.match(/^##\s+(.+)/);

    if (h2Match) {
      if (currentTitle !== null) {
        sections.push({
          id: slugify(currentTitle),
          title: currentTitle,
          content: currentLines.join('\n').trim(),
        });
      } else {
        preambleLines = [...currentLines];
      }
      currentTitle = h2Match[1].trim();
      currentLines = [];
    } else {
      currentLines.push(line);
    }
  }

  if (currentTitle !== null) {
    sections.push({
      id: slugify(currentTitle),
      title: currentTitle,
      content: currentLines.join('\n').trim(),
    });
  } else {
    preambleLines = [...currentLines];
  }

  const preamble = preambleLines.join('\n').trim();

  return {
    title: extractTitle(preamble || raw),
    preamble,
    sections,
  };
}
