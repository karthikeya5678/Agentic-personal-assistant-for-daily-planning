// src/routes/exams/+page.ts

import type { Load as PageLoad } from '@sveltejs/kit';
import { apiUrl } from '$lib/api';

export const load: PageLoad = async ({ fetch }) => {
  console.log('Fetching exams from backend...');
  try {
    const response = await fetch(apiUrl('/api/v1/exams'));
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    const exams = await response.json();
    return { exams: exams };
  } catch (error) {
    console.error('Failed to load exams:', error);
    return { exams: [], error: 'Could not connect to the backend.' };
  }
};