<script lang="ts">
  import { page } from '$app/stores';
</script>

<header>
  <div class="logo">
    <a href="/">🚀 My Assistant</a>
  </div>
  <nav>
    <a href="/" class:active={$page.url.pathname === '/'}>Dashboard</a>
    
    <a href="/schedule" class:active={$page.url.pathname.startsWith('/schedule')}>Schedule</a>
    <a href="/study" class:active={$page.url.pathname.startsWith('/study')}>Study Buddy</a>
    <a href="/travel" class:active={$page.url.pathname.startsWith('/travel')}>Travel Planner</a>
    <a href="/bus" class:active={$page.url.pathname.startsWith('/bus')}>Bus Tracker</a>
    <a href="/exams" class:active={$page.url.pathname.startsWith('/exams')}>Exams</a>
    <a href="/recommend" class:active={$page.url.pathname.startsWith('/recommend')}>Recommend</a>
    <a href="/profile" class:active={$page.url.pathname.startsWith('/profile')}>Profile</a>
  </nav>
</header>

<style>
  header {
    background: linear-gradient(90deg, #3f51b5 0%, #303f9f 100%);
    color: white;
    padding: 0 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
  }

  .logo a {
    font-size: 1.5rem;
    font-weight: bold;
    text-decoration: none;
    color: white;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  nav {
    display: flex;
    gap: 0.5rem;
  }

  nav a {
    text-decoration: none;
    color: white;
    font-weight: 500;
    padding: 1.5rem 1rem;
    border-bottom: 3px solid transparent;
    transition: all 0.2s ease-in-out;
  }

  /* This is the style for the active link */
  nav a.active {
    background-color: rgba(255, 255, 255, 0.1);
    border-bottom-color: #ffffff;
  }

  nav a:hover:not(.active) {
    background-color: rgba(255, 255, 255, 0.05);
  }
</style>