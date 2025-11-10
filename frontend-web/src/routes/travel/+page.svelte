<script lang="ts">
  export let form;
</script>

<h1>AI Travel Planner</h1>
<p>Plan your next trip. The AI will find the best options for you.</p>

<form method="POST">
  <input type="text" name="origin" placeholder="From (e.g., Hyderabad)" required />
  <input type="text" name="destination" placeholder="To (e.g., Warangal)" required />
  <input type="date" name="date" required />
  <button type="submit">Plan My Trip</button>
</form>

{#if form?.success}
  <div class="results">
    <h2>Your Travel Plan:</h2>
    <pre>{form.plan}</pre>
  </div>
{/if}

<style>
  form {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    margin-top: 2rem;
    align-items: end;
  }
  input {
    padding: 0.8rem;
    border-radius: 5px;
    border: 1px solid #ccc;
    font-size: 1rem;
  }
  button {
    grid-column: 1 / -1; /* Span across both columns */
    background-color: var(--color-primary);
    color: white;
    border: none;
    cursor: pointer;
    padding: 0.8rem 1.5rem;
    border-radius: 5px;
    font-weight: bold;
    font-size: 1rem;
  }
  .results {
    margin-top: 2rem;
    text-align: left;
    background-color: var(--card-bg);
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: var(--card-shadow);
  }
  pre {
    white-space: pre-wrap;
    word-wrap: break-word;
    font-family: var(--font-body);
    font-size: 1rem;
    line-height: 1.6;
  }
</style>