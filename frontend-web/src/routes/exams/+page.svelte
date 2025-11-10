<script lang="ts">
  // We get 'data' from our +page.ts load function
  // We get 'form' from our +page.server.ts action
  export let data;
  export let form;

  // The problematic code that caused the crash has been removed.
  // SvelteKit will automatically reload the 'data' prop for us
  // after the 'form' action completes.
</script>

<h1>My Exams</h1>
<p>Add your upcoming exams here. The assistant will send you a WhatsApp reminder 3 days before.</p>

<form method="POST">
  <input type="text" name="subject" placeholder="Subject Name (e.g., Physics)" required />
  <input type="date" name="date" required />
  <button type="submit">Add Exam</button>
</form>

<h2>Upcoming Exams</h2>
<div class="exam-list">
  {#each data.exams as exam (exam._id)}
    <div class="exam-card">
      <span class="exam-subject">{exam.subject}</span>
      <span class="exam-date">
        {new Date(exam.date + 'T00:00:00').toLocaleDateString('en-US', {
          year: 'numeric',
          month: 'long',
          day: 'numeric'
        })}
      </span>
    </div>
  {:else}
    <p>You have no exams scheduled.</p>
  {/each}
</div>

<style>
  form {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr;
    gap: 1rem;
    margin: 2rem 0;
    align-items: center;
  }
  input,
  button {
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
    font-weight: bold;
  }
  .exam-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    text-align: left;
  }
  .exam-card {
    background-color: var(--card-bg);
    border-radius: 8px;
    box-shadow: var(--card-shadow);
    padding: 1rem 1.5rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .exam-subject {
    font-size: 1.1rem;
    font-weight: bold;
  }
  .exam-date {
    font-family: var(--font-mono);
    color: var(--color-primary);
  }
</style>