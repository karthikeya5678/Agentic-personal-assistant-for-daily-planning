<script lang="ts">
  export let data;
  export let form;

  let name = data.profile.name || '';
  let goal = data.profile.goal || '';
  let interests = data.profile.interests || '';

  let saved = false;

  // This will update the form fields if the data is reloaded
  $: {
    name = data.profile.name || '';
    goal = data.profile.goal || '';
    interests = data.profile.interests || '';
  }

  // Show a "Saved!" message when the form action completes
  $: if (form?.success) {
    saved = true;
    setTimeout(() => { saved = false; }, 2000);
  }
</script>

<h1>Your Profile</h1>
<p>This information helps the AI make better suggestions for you.</p>

<form method="POST">
  <div class="form-group">
    <label for="name">Your Name</label>
    <input type="text" id="name" name="name" bind:value={name} />
  </div>

  <div class="form-group">
    <label for="goal">Your Main Goal</label>
    <input type="text" id="goal" name="goal" bind:value={goal} placeholder="e.g., Learn AI, Get a job" />
  </div>

  <div class="form-group">
    <label for="interests">Your Interests</label>
    <textarea id="interests" name="interests" bind:value={interests} placeholder="e.g., Python, Sci-fi movies, Cricket" />
  </div>

  <button type="submit">
    {#if saved}
      Saved! ✅
    {:else}
      Save Profile
    {/if}
  </button>
</form>

<style>
  /* You can copy/paste styles from src/routes/schedule/new/+page.svelte */
  form {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    max-width: 600px;
    margin-top: 2rem;
  }
  .form-group { display: flex; flex-direction: column; }
  label { margin-bottom: 0.5rem; font-weight: bold; }
  input, textarea, button {
    padding: 0.8rem; border-radius: 5px; border: 1px solid #ccc; font-size: 1rem;
  }
  textarea {
    min-height: 100px;
    font-family: var(--font-body);
  }
  button {
    background-color: var(--color-primary); color: white; border: none;
    cursor: pointer; font-weight: bold; transition: background-color 0.2s;
  }
  button:hover { background-color: #303f9f; }
</style>