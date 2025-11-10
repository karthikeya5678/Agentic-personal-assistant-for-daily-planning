<script lang="ts">
  export let form;
</script>

<h1>Live Bus Tracker (APSRTC)</h1>
<p>Enter a specific "Service No." (from your ticket) to find its live location.</p>

<form method="POST">
  <input type="text" name="route_number" placeholder="Enter Service No." required />
  <button type="submit">Track Bus</button>
</form>

{#if form?.success}
  <div class="results">
    <h2>Bus Status:</h2>
    <pre>{form.info}</pre>
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
    white-space: pre-wrap;
    word-wrap: break-word;
    font-family: var(--font-body);
    font-size: 1rem;
    line-height: 1.6;
  }
</style>