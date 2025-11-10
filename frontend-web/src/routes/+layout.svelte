<script lang="ts">
  import '../app.css';
  import Header from '$lib/components/Header.svelte'; // Import the Header
  import { fade } from 'svelte/transition';
  import { page } from '$app/stores';
</script>

<Header />

<main>
  {#key $page.url.pathname}
    <div transition:fade={{ duration: 250 }}>
      <slot />
    </div>
  {/key}
</main>

<style>
  /* This 'main' style provides padding for the content area */
  main {
    max-width: 1100px;
    margin: 2rem auto;
    padding: 1rem 2rem;
  }
</style>