// src/routes/profile/+page.ts
import type { PageLoad } from './$types';

export const load: PageLoad = async ({ fetch }) => {
  console.log('Fetching user profile...');
  try {
    const response = await fetch('http://127.0.0.1:8000/api/v1/profile');
    const profile = await response.json();
    return { profile };
  } catch (error) {
    return { profile: { name: "", goal: "", interests: "" } };
  }
};