// src/routes/recommend/+page.server.ts
import type { RequestEvent } from '@sveltejs/kit';
import { apiUrl } from '$lib/api';

export const actions = {
  // We will have two separate actions, one for movies, one for learning
  movie: async ({ fetch }: RequestEvent) => {
    const response = await fetch(apiUrl('/api/v1/recommendations'), {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ type: 'movie' })
    });
    const result = await response.json();
    return { success: true, recommendation: result.recommendation };
  },
  learn: async ({ fetch }: RequestEvent) => {
    const response = await fetch(apiUrl('/api/v1/recommendations'), {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ type: 'learn' })
    });
    const result = await response.json();
    return { success: true, recommendation: result.recommendation };
  }
};