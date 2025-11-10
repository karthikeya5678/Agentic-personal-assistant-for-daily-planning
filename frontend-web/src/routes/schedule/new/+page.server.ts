// src/routes/schedule/new/+page.server.ts

import { redirect } from '@sveltejs/kit';
import { apiUrl } from '$lib/api';

export const actions = {
  // Add `{ fetch }` to the function parameters here
  default: async ({ request, fetch }: import('@sveltejs/kit').RequestEvent) => {
    const formData = await request.formData();
    const data = {
      time: formData.get('time'),
      task_name: formData.get('task_name'),
      day_type: formData.get('day_type')
    };

    // This `fetch` will now be the special SvelteKit version
    await fetch(apiUrl('/api/v1/schedule'), {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });

    throw redirect(303, '/schedule');
  }
};