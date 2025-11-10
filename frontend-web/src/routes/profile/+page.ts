// src/routes/profile/+page.ts
import type { PageLoad } from './$types';
import { apiUrl } from '$lib/api';

export const load: PageLoad = async ({ fetch }) => {
  console.log('Fetching user profile...');
  try {
    const response = await fetch(apiUrl('/api/v1/profile'));
    const profile = await response.json();
    return { profile };
  } catch (error) {
    return { profile: { name: "", goal: "", interests: "" } };
  }
};