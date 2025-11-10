<script lang="ts">
  // This 'data' prop is loaded from our new +page.ts file
  export let data;
</script>

<h1 class="welcome-title">Welcome, {data.profileName}!</h1>
<p>This is your personal dashboard. What would you like to do?</p>

<div class="dashboard-grid">
  <a href="/schedule" class="card schedule">
    <div class="card-icon">🗓️</div>
    <div class="card-title">My Schedule</div>
    <div class="card-desc">View and manage your daily tasks.</div>
  </a>

  <a href="/exams" class="card exams">
    <div class="card-icon">🎓</div>
    <div class="card-title">My Exams</div>
    <div class="card-desc">Add exam dates for proactive reminders.</div>
  </a>

  <a href="/study" class="card study">
    <div class="card-icon">🤖</div>
    <div class="card-title">Study Buddy</div>
    <div class="card-desc">Get AI-powered study materials on demand.</div>
  </a>

  <a href="/travel" class="card travel">
    <div class="card-icon">✈️</div>
    <div class="card-title">Travel Planner</div>
    <div class="card-desc">Let the AI plan your next trip.</div>
  </a>

  <a href="/bus" class="card bus">
    <div class="card-icon">🚌</div>
    <div class="card-title">Bus Tracker</div>
    <div class="card-desc">Track your APSRTC bus in real-time.</div>
  </a>

  <a href="/recommend" class="card recommend">
    <div class="card-icon">🍿</div>
    <div class="card-title">Recommender</div>
    <div class="card-desc">Get movie or learning suggestions.</div>
  </a>
</div>

<style>
  .welcome-title {
    font-size: 2.5rem; /* Make the welcome message bigger */
  }
  h1, p {
    text-align: center;
  }
  .dashboard-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
  }
  .card {
    background-color: var(--card-bg);
    border-radius: 8px;
    box-shadow: var(--card-shadow);
    padding: 1.5rem;
    text-decoration: none;
    color: var(--color-text);
    transition: all 0.2s ease-in-out;
    border: 2px solid transparent;
  }
  .card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  }
  .card-icon {
    font-size: 2.5rem;
  }
  .card-title {
    font-size: 1.25rem;
    font-weight: bold;
    margin: 1rem 0 0.5rem 0;
  }
  .card-desc {
    font-size: 0.9rem;
    line-height: 1.4;
  }

  /* Fun hover colors */
  .schedule:hover { border-color: #3f51b5; }
  .exams:hover { border-color: #f44336; }
  .study:hover { border-color: #9c27b0; }
  .travel:hover { border-color: #ff9800; }
  .bus:hover { border-color: #e91e63; }
  .recommend:hover { border-color: #4caf50; }
</style>