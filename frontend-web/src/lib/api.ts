// src/lib/api.ts
export const API_BASE = import.meta.env.VITE_API_BASE || 'http://127.0.0.1:8000';

export function apiUrl(path: string) {
  if (!path.startsWith('/')) path = '/' + path;
  return `${API_BASE}${path}`;
}
