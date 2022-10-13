export default class APIOperations {
  constructor() {
    try {
      this.refreshLocalStorage();
    } catch (e) {
      console.log('No tasks found');
    }
    this.generateTasks();

    // API URL
    // API KEY
  }

  getTasks() {
    return this.tasks;
  }

  refreshLocalStorage() {
    try {
      this.tasks = JSON.parse({ ...localStorage }.tasks);
    } catch (e) {
      console.log(e);
    }
  }

  syncTasks() {
    window.localStorage.setItem('tasks', JSON.stringify((this.tasks)));
  }

  generateTasks() {
    if (!this.tasks || this.tasks.length === 0) {
      this.tasks = [];
      for (let i = 0; i < 10; i += 1) {
        this.tasks.push({
          id: i + 1,
          name: 'Sprzątanie kuwety',
          category: 'Łazienka',
          cycle_days: 1,
          duration_min: 3,
        });
      }
      this.syncTasks();
    }
  }

  setTaskCompleted(taskId) {
    for (let i = 0, len = this.tasks.length; i < len; i += 1) {
      if (this.tasks[i].id === taskId) {
        this.tasks.splice(i, 1);
        this.syncTasks();
        return;
      }
    }
    throw Error('Could not find task');
  }
}
