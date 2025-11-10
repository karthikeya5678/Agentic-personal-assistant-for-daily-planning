<script lang="ts">
  // This special `export let data` statement receives the data
  // returned from the `load` function in +page.ts
  export let data;
</script>

<h1>My Daily Schedule</h1>

<a href="/schedule/new" class="add-button">+ Add New Task</a>

{#if data.error}
  <p class="error">{data.error}</p>
{:else}
  <div class="schedule-list">
    {#each data.tasks as task (task._id)}
      <div class="task-card">
        <span class="task-time">{task.time}</span>
        <span class="task-name">{task.task_name}</span>
      </div>
    {/each}
  </div>
{/if}

<style>
  .add-button {
      display: inline-block;
      padding: 0.8rem 1.5rem;
      background-color: #4caf50;
      color: white;
      text-decoration: none;
      border-radius: 5px;
      font-weight: bold;
      transition: background-color 0.2s;
      margin-bottom: 2rem;
  }
  .error {
    color: red;
    font-weight: bold;
    margin-top: 2rem;
  }
  .schedule-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    margin-top: 2rem;
    text-align: left;
  }
  .task-card {
    background-color: var(--card-bg);
    border-radius: 8px;
    box-shadow: var(--card-shadow);
    padding: 1rem 1.5rem;
    display: flex;
    align-items: center;
    gap: 1.5rem;
  }
  .task-time {
    font-family: var(--font-mono);
    font-size: 1.2rem;
    font-weight: bold;
    color: var(--color-primary);
  }
  .task-name {
    font-size: 1.1rem;
  }
</style>