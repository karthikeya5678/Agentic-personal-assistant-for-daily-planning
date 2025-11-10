// src/routes/profile/+page.server.ts
import type { RequestEvent } from '@sveltejs/kit';

export const actions = {
  default: async ({ request, fetch }: RequestEvent) => {
    const formData = await request.formData();
    const data = {
      name: formData.get('name'),
      goal: formData.get('goal'),
      interests: formData.get('interests')
    };

    await fetch('http://127.0.0.1:8000/api/v1/profile', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });

    return { success: true };
  }
};