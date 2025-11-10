<h1>Add a New Task</h1>

<form method="POST">
  <div class="form-group">
    <label for="task_name">Task Name</label>
    <input type="text" id="task_name" name="task_name" required />
  </div>

  <div class="form-group">
    <label for="time">Time (HH:MM)</label>
    <input type="time" id="time" name="time" required />
  </div>

  <div class="form-group">
    <label for="day_type">Day Type</label>
    <select id="day_type" name="day_type">
      <option value="weekday">Weekday</option>
      <option value="sunday">Sunday</option>
    </select>
  </div>

  <button type="submit">Add Task</button>
</form>

<style>
  form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    max-width: 400px;
    margin-top: 2rem;
  }
  .form-group {
    display: flex;
    flex-direction: column;
  }
  label {
    margin-bottom: 0.5rem;
    font-weight: bold;
  }
  input, select, button {
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
</style>