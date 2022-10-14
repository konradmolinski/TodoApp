<template>
  <main role="main" class="container">
    <h1 class="mt-2 mb-3 text-center">Zadania</h1>
    <div class="row flex-nowrap">
      <div class="col-10">
        <v-select
          v-model="selectedItem"
          :options="taskSelectOptions"
        ></v-select>
      </div>
      <div class="col-1 text-right">
        <button
          class="btn btn-success"
          :disabled="selectedItem.code === ''"
          @click="toggleTaskCompletedFromSelect"
        >
          ✓
        </button>
      </div>
    </div>
    <p v-if="this.tasks.length === 0" id="empty-list-info">No tasks!</p>
    <div
      class="row flex-nowrap pt-4"
      v-for="task in tasks"
      :key="task.id"
      @onclick="toggleTaskCompleted"
      :style="bgColor"
    >
      <div class="col-md-3 col-3 pr-0">{{ task.category }}</div>
      <div class="col-md-5 col-5 pr-0">{{ task.name }}</div>
      <div class="col-md-2 col-2 pr-0">{{ task.duration_minutes }}min</div>
      <div class="col-md-1 col-1 text-right">
        <button class="btn btn-success" @click="completeTask(task.id)">
          ✓
        </button>
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
      this.tasks.forEach((task, index) => {
        this.tasks[index].bgColor = task.overdue_hours > 1 ? 'background-color: lightred' : ' background-color: white';
      });
      this.taskSelectOptions = this.tasks.map((task) => ({
        code: task.id,
        label: `${task.category} - ${task.name}`,
      }));
    },
    completeTask(taskId) {
      this.api.setTaskCompleted(taskId);
      this.refreshTasks();
    },
    toggleTaskCompletedFromSelect() {
      if (this.selectedItem.code) {
        this.completeTask(this.selectedItem.code);
        this.selectedItem.code = '';
        this.selectedItem.label = '';
      }
    },
  },
  components: {
    'v-select': vSelect,
  },
};
</script>

<style type="style/scss">
$lateTask: #121212;
</style>
