export function preprocessMarkdown(markdown: string): string {
  let result = markdown;
  result = convertBoxDrawing(result);
  result = convertScoreBars(result);
  result = convertCoverageBlocks(result);
  result = wrapSafetyVerdicts(result);
  return result;
}

function convertBoxDrawing(text: string): string {
  return text
    .replace(/^[═]{5,}$/gm, '<hr class="border-t-2 border-primary/30 my-4" />')
    .replace(/^[━]{5,}$/gm, '<hr class="border-t border-border my-3" />')
    .replace(/^[─]{5,}$/gm, '<hr class="border-t border-border my-2" />');
}

function convertScoreBars(text: string): string {
  return text.replace(
    /^(\s*[\w\s/&-]+?)\s+(█+)(░+)\s+(\d+)\/(\d+)$/gm,
    (_match, label: string, _filled: string, _empty: string, score: string, max: string) => {
      const pct = (parseInt(score) / parseInt(max)) * 100;
      let color = 'bg-emerald-500';
      if (pct < 40) color = 'bg-red-500';
      else if (pct < 70) color = 'bg-amber-500';
      return `<div class="flex items-center gap-3 my-1"><span class="w-44 text-sm text-muted-foreground truncate">${label.trim()}</span><div class="flex-1 h-3 bg-muted rounded-full overflow-hidden"><div class="${color} h-full rounded-full" style="width: ${pct}%"></div></div><span class="text-sm font-mono font-semibold w-12 text-right">${score}/${max}</span></div>`;
    },
  );
}

function convertCoverageBlocks(text: string): string {
  return text
    .replace(
      /████/g,
      '<span class="inline-block w-4 h-4 bg-primary rounded-sm align-middle" title="Covered"></span>',
    )
    .replace(
      /██/g,
      '<span class="inline-block w-3 h-3 bg-primary/70 rounded-sm align-middle" title="Partial"></span>',
    )
    .replace(
      /░░░░/g,
      '<span class="inline-block w-4 h-4 bg-muted rounded-sm align-middle" title="Gap"></span>',
    )
    .replace(
      /░░/g,
      '<span class="inline-block w-3 h-3 bg-muted rounded-sm align-middle" title="Gap"></span>',
    );
}

function wrapSafetyVerdicts(text: string): string {
  const verdictColors: Record<string, string> = {
    GREEN: 'bg-emerald-100 text-emerald-800 border-emerald-300',
    YELLOW: 'bg-amber-100 text-amber-800 border-amber-300',
    ORANGE: 'bg-orange-100 text-orange-800 border-orange-300',
    RED: 'bg-red-100 text-red-800 border-red-300',
  };

  for (const [verdict, classes] of Object.entries(verdictColors)) {
    const regex = new RegExp(`\\b(${verdict})\\b(?![^<]*>)`, 'g');
    text = text.replace(
      regex,
      `<span class="inline-block px-1.5 py-0.5 text-xs font-semibold rounded border ${classes}">${verdict}</span>`,
    );
  }

  return text;
}
