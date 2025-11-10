// src/routes/travel/+page.server.ts

import type { Actions } from '@sveltejs/kit';
import { apiUrl } from '$lib/api';

export const actions: Actions = {
  default: async ({ request, fetch }) => {
    const formData = await request.formData();
    const data = {
      origin: formData.get('origin'),
      destination: formData.get('destination'),
      date: formData.get('date')
    };

    const response = await fetch(apiUrl('/api/v1/plan-trip'), {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });

    // CHECK if the response was successful
    if (!response.ok) {
      // If not, log the actual error text and return a friendly error message
      const errorText = await response.text();
      console.error("Error from backend:", errorText);
      return { success: false, plan: "Failed to get a travel plan from the backend." };
    }

    // Only parse JSON if the response was OK
    const result = await response.json();

    return {
      success: true,
      plan: result.plan
    };
  }
};