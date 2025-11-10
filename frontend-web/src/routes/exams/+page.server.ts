// src/routes/exams/+page.server.ts
import type { Actions } from '@sveltejs/kit';
import { apiUrl } from '$lib/api';

// We don't use 'redirect' so we need to tell SvelteKit to reload the page data
export const actions: Actions = {
  default: async ({ request, fetch }) => {
    const formData = await request.formData();
    const data = {
      subject: formData.get('subject'),
      date: formData.get('date')
    };

    await fetch(apiUrl('/api/v1/exams'), {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });

    // We don't redirect, so just return success.
    // The page will reload its data.
    return { success: true };
  }
};