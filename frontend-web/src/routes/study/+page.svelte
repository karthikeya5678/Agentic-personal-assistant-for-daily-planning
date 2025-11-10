<script lang="ts">
  // This special prop receives the data returned from the form action
  export let form;
</script>

<h1>AI Study Buddy</h1>
<p>Enter a topic, and the AI will find study resources for you.</p>

<form method="POST">
  <input type="text" name="topic" placeholder="e.g., 'Python decorators'" required />
  <button type="submit">Find Resources</button>
</form>

{#if form?.success}
  <div class="results">
    <h2>Study Materials Found:</h2>
    <pre>{form.materials}</pre>
  </div>
{/if}

<style>
  form {
    display: flex;
    gap: 1rem;
    margin-top: 2rem;
  }
  input {
    flex-grow: 1;
    padding: 0.8rem;
    border-radius: 5px;
    border: 1px solid #ccc;
    font-size: 1rem;
  }
  button {
    background-color: var(--color-primary);
    color: white;
    border: none;
    cursor: pointer;
    padding: 0.8rem 1.5rem;
    border-radius: 5px;
    font-weight: bold;
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
    white-space: pre-wrap; /* Allows text to wrap */
    word-wrap: break-word;
    font-family: var(--font-body);
    font-size: 1rem;
    line-height: 1.6;
  }
</style>