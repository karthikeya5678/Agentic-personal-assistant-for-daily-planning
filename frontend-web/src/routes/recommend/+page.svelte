<script lang="ts">
  export let form;
</script>

<h1>Sunday Recommender</h1>
<p>What are you in the mood for?</p>

<div classs="button-row">
  <form action="?/movie" method="POST">
    <button type="submit">Suggest a Movie 🎬</button>
  </form>

  <form action="?/learn" method="POST">
    <button type="submit" class="learn-button">Suggest a Skill 💡</button>
  </form>
</div>

{#if form?.success}
  <div class="results">
    <h2>Here are some ideas:</h2>
    <pre>{form.recommendation}</pre>
  </div>
{/if}

<style>
  .button-row {
    display: flex;
    gap: 1.5rem;
    justify-content: center;
    margin-top: 2rem;
  }
  button {
    background-color: var(--color-primary);
    color: white;
    border: none;
    cursor: pointer;
    padding: 1rem 2rem;
    border-radius: 8px;
    font-weight: bold;
    font-size: 1.1rem;
    transition: transform 0.2s;
  }
  button:hover {
    transform: scale(1.05);
  }
  .learn-button {
    background-color: #4caf50; /* Green */
  }
  .results {
    margin-top: 2.5rem;
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