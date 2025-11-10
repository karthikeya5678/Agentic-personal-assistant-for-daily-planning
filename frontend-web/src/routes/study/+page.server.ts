// src/routes/study/+page.server.ts

import { apiUrl } from '$lib/api';

export const actions = {
  default: async ({ request }: { request: Request }) => {
    const formData = await request.formData();
    const topic = formData.get('topic');

    const response = await fetch(apiUrl('/api/v1/study-assistant'), {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ topic })
    });

    const result = await response.json();

    // Return the result to the page
    return {
      success: true,
      materials: result.materials
    };
  }
};