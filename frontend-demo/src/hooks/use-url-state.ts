import { useCallback } from 'react';

type ParamMap = Record<string, string | null>;

function getParams(): URLSearchParams {
  return new URLSearchParams(window.location.search);
}

function setParams(params: URLSearchParams) {
  const qs = params.toString();
  const url = qs ? `${window.location.pathname}?${qs}` : window.location.pathname;
  window.history.replaceState(null, '', url);
}

export function readParam(key: string): string | null {
  return getParams().get(key);
}

export function useUrlState() {
  const update = useCallback((changes: ParamMap) => {
    const params = getParams();
    for (const [key, value] of Object.entries(changes)) {
      if (value === null || value === undefined || value === '') {
        params.delete(key);
      } else {
        params.set(key, value);
      }
    }
    setParams(params);
  }, []);

  return { update };
}
