import { useState, useEffect, useMemo } from 'react';
import { parseMarkdown } from '@/lib/markdown-parser';
import type { AnalysisDocument } from '@/types/analysis';

interface UseAnalysisDocumentResult {
  document: AnalysisDocument | null;
  loading: boolean;
  error: string | null;
}

const cache = new Map<string, AnalysisDocument>();

export function useAnalysisDocument(filename: string | null): UseAnalysisDocumentResult {
  const [raw, setRaw] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!filename) {
      setRaw(null);
      return;
    }

    if (cache.has(filename)) {
      setRaw('__cached__');
      return;
    }

    setLoading(true);
    setError(null);

    fetch(`/data/analysis/${filename}`)
      .then((res) => {
        if (!res.ok) throw new Error(`Failed to load ${filename}`);
        return res.text();
      })
      .then((text) => {
        setRaw(text);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, [filename]);

  const document = useMemo(() => {
    if (!filename) return null;
    if (cache.has(filename)) return cache.get(filename)!;
    if (!raw || raw === '__cached__') return null;

    const doc = parseMarkdown(raw);
    cache.set(filename, doc);
    return doc;
  }, [filename, raw]);

  return { document, loading, error };
}
