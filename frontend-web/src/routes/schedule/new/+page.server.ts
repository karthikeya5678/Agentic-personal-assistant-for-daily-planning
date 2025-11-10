// src/routes/schedule/new/+page.server.ts

import { redirect } from '@sveltejs/kit';

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
    await fetch('http://127.0.0.1:8000/api/v1/schedule', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });

    throw redirect(303, '/schedule');
  }
};