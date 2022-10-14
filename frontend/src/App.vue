<template>
  <main role="main" class="container">
    <h1 class="mt-2 mb-3">Zadania</h1>
    <div class="row">
      <div class="col-md-11 col-xs-11">
        <v-select
          v-model="selectedItem"
          :options="taskSelectOptions"
        ></v-select>
      </div>
      <div class="col-md-1 col-xs-1">
        <button @click="toggleTaskCompleted" >✓</button>
      </div>
    </div>
    <p v-if="this.tasks.length === 0" id="empty-list-info">No tasks!</p>
    <div
      class="row"
      v-for="task in tasks"
      :key="task.id"
      @onclick="toggleTaskCompleted"
    >
      <div class="col-md-4 col-xs-4">{{ task.category }}</div>
      <div class="col-md-4 col-xs-4">{{ task.name }}</div>
      <div class="col-md-2 col-xs-2">{{ task.duration_minutes }}min</div>
      <div class="col-md-1 col-xs-1">
        <button @click="completeTask(task)">✓</button>
      </div>
    </div>
  </main>
</template>

<script>
import vSelect from 'vue-select';
import APIOperations from './APIOperations';
import 'vue-select/dist/vue-select.css';

export default {
  data() {
    return {
      api: null,
      tasks: [],
      taskSelectOptions: [],
      searchText: '',
      selectedItem: {
        code: '',
        label: '',
      },
    };
  },
  created() {
    window.x = this;
    this.api = new APIOperations();
    this.refreshTasks();
  },
  methods: {
    refreshTasks() {
      this.tasks = [];
      this.tasks = this.api.getTasks();
      this.taskSelectOptions = this.tasks.map((task) => ({
        code: task.id,
        label: `${task.category} - ${task.name} - ${task.duration_minutes}min`,
      }));
    },
    completeTask(task) {
      this.api.setTaskCompleted(task.id);
      this.refreshTasks();
    },
    // onSelect(task) {

    // },
  },
  components: {
    'v-select': vSelect,
  },
};
</script>

<style>
</style>
