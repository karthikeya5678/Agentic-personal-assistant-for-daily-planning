// src/routes/recommend/+page.server.ts
import type { RequestEvent } from '@sveltejs/kit';

export const actions = {
  // We will have two separate actions, one for movies, one for learning
  movie: async ({ fetch }: RequestEvent) => {
    const response = await fetch('http://127.0.0.1:8000/api/v1/recommendations', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ type: 'movie' })
    });
    const result = await response.json();
    return { success: true, recommendation: result.recommendation };
  },
  learn: async ({ fetch }: RequestEvent) => {
    const response = await fetch('http://127.0.0.1:8000/api/v1/recommendations', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ type: 'learn' })
    });
    const result = await response.json();
    return { success: true, recommendation: result.recommendation };
  }
};