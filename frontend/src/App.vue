<template>
  <main role="main" class="container">
    <h1 class="mt-2 mb-3 text-center">Sprzątamy!</h1>
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
      class="row flex-nowrap mt-4"
      v-for="task in tasks"
      :key="task.id"
      @onclick="toggleTaskCompleted"
      :class="task.bgClass"
    >
      <div class="col-md-3 col-3 pr-0">{{ task.category }}</div>
      <div class="col-md-5 col-5 pr-0">{{ task.title }}</div>
      <div class="col-md-2 col-2 pr-0">{{ task.duration }}min</div>
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
import { getTasks, setTaskCompleted } from './APIOperations';
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
  async created() {
    await this.setAuthCookie();
    this.refreshTasks();
  },
  methods: {
    async setAuthCookie() {
      const secretKey = 'secret';
      if ((await window.cookieStore.get(secretKey)) == null) {
        let password = '';
        let counter = 0;
        while (counter < 5 && password.length < 5) {
          password = window.prompt('Daj hasło', ''); // eslint-disable-line no-alert
          counter += 1;
        }
        await window.cookieStore.set(secretKey, password);
      }
    },
    refreshTasks() {
      this.selectedItem = { code: '', label: '' };
      this.tasks = [];
      getTasks().then((tasks) => {
        this.tasks = tasks;
        this.tasks.forEach((task, index) => {
          if (task.overdue_hours > 15) {
            this.tasks[index].bgClass = 'late';
          }
          if (task.overdue_hours > 24) {
            this.tasks[index].bgClass = 'super-late';
          }
        });
        this.taskSelectOptions = this.tasks.map((task) => ({
          code: task.id,
          label: `${task.category} - ${task.title}`,
        }));
      });
    },
    completeTask(taskId) {
      setTaskCompleted(taskId);
      this.refreshTasks();
    },
    toggleTaskCompletedFromSelect() {
      if (this.selectedItem.code) {
        this.completeTask(this.selectedItem.code).then(() => {
          this.selectedItem.code = '';
          this.selectedItem.label = '';
        });
      }
    },
  },
  components: {
    'v-select': vSelect,
  },
};
</script>

<style>
.super-late {
  background-color: rgb(184, 116, 116);
}
.late {
  background-color: rgb(239, 198, 198);
}
</style>
