// src/routes/+page.ts
import type { PageLoad } from './$types';
import { apiUrl } from '$lib/api';

export const load: PageLoad = async ({ fetch }) => {
  console.log('Fetching user profile for dashboard...');
  try {
    const response = await fetch(apiUrl('/api/v1/profile'));

    if (!response.ok) {
      return { profileName: 'User' }; // Default name if fetch fails
    }

    const profile = await response.json();

    // Send the profile name to the Svelte page
    return {
      profileName: profile.name || 'User' // Use 'User' as fallback
    };

  } catch (error) {
    console.error('Failed to load profile:', error);
    return { profileName: 'User' };
  }
};