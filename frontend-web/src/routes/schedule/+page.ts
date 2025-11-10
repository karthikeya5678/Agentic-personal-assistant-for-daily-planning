// src/routes/schedule/+page.ts
import type { PageLoad } from './$types';
import { apiUrl } from '$lib/api';

// The `load` function is SvelteKit's way of fetching data for a page.
export const load: PageLoad = async ({ fetch }) => {
  console.log('Fetching schedule from backend...');

  try {
    const response = await fetch(apiUrl('/api/v1/schedule'));

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const tasks = await response.json();
    console.log('Successfully fetched tasks:', tasks);

    // The data returned here will be available to the +page.svelte component
    return {
      tasks: tasks
    };
  } catch (error) {
    console.error('Failed to load schedule:', error);
    // Return an empty array or an error state if the fetch fails
    return {
      tasks: [],
      error: 'Could not connect to the backend.'
    };
  }
}