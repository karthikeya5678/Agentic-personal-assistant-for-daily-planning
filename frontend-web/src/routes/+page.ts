// src/routes/+page.ts
import type { PageLoad } from './$types';

export const load: PageLoad = async ({ fetch }) => {
  console.log('Fetching user profile for dashboard...');
  try {
    const response = await fetch('http://127.0.0.1:8000/api/v1/profile');
    
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