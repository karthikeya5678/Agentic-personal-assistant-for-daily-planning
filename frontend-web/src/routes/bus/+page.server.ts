// src/routes/bus/+page.server.ts
import type { RequestEvent } from '@sveltejs/kit';

export const actions = {
  default: async ({ request, fetch }: RequestEvent) => {
    const formData = await request.formData();
    const route_number = formData.get('route_number');

    const response = await fetch('http://127.0.0.1:8000/api/v1/track-bus', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ route_number })
    });

    if (!response.ok) {
      return { success: false, info: "Failed to connect to the backend." };
    }

    const result = await response.json();
    return { success: true, info: result.info };
  }
};