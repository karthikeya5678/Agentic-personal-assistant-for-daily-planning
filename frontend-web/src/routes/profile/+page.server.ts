// src/routes/profile/+page.server.ts
import type { RequestEvent } from '@sveltejs/kit';
import { apiUrl } from '$lib/api';

export const actions = {
  default: async ({ request, fetch }: RequestEvent) => {
    const formData = await request.formData();
    const data = {
      name: formData.get('name'),
      goal: formData.get('goal'),
      interests: formData.get('interests')
    };

    await fetch(apiUrl('/api/v1/profile'), {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });

    return { success: true };
  }
};