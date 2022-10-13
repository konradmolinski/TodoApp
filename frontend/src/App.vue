<template>
  <p v-if="this.tasks.length === 0" id="empty-list-info">All done!</p>
  <ul id="todo-list">
    <li v-for="task in tasks" :key="task.id">
      <div id="todo-div" @click="completeTask(task)">
        <div id="text-div" @click="toggleTaskCompleted">
          <p> {{task.category}}  -> {{ task.name }}</p>
        </div>
      </div>
    </li>
  </ul>
</template>

<script>
import APIOperations from './APIOperations';

export default {
  data() {
    return {
      api: null,
      tasks: [],
    };
  },
  mounted() {
    this.api = new APIOperations();
    this.tasks = this.api.getTasks();
  },
  methods: {
    completeTask(task) {
      this.api.setTaskCompleted(task.id);
    },
  },
};
</script>
