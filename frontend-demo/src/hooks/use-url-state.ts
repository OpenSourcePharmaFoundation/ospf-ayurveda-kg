import { useCallback, useSyncExternalStore } from 'react';

type ParamMap = Record<string, string | null>;

function getParams(): URLSearchParams {
  return new URLSearchParams(window.location.search);
}

function setParams(params: URLSearchParams) {
  const qs = params.toString();
  const url = qs ? `${window.location.pathname}?${qs}` : window.location.pathname;
  window.history.pushState(null, '', url);
  notifyListeners();
}

type Listener = () => void;
const listeners = new Set<Listener>();

function subscribe(listener: Listener) {
  listeners.add(listener);
  return () => listeners.delete(listener);
}

function notifyListeners() {
  for (const listener of listeners) listener();
}

if (typeof window !== 'undefined') {
  window.addEventListener('popstate', notifyListeners);
}

export function readParam(key: string): string | null {
  return getParams().get(key);
}

export function useUrlParam(key: string, fallback: string | null = null): string | null {
  const value = useSyncExternalStore(
    subscribe,
    () => getParams().get(key) ?? fallback,
  );
  return value;
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
