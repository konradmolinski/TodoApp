<template>
  <Create 
  :api = api />
  <p v-if="this.api.todos.length === 0" id="empty-list-info">No tasks yet.</p>
  <ul id="todo-list">
    <li v-for = "todo in api.todos">
      <Todo
      :todo = todo
      :api = api
       />
    </li>
  </ul>
  <button id="delete-btn" @click="deleteDone" type="button">delete completed</button>
</template>

<script>
  import Create from './components/Create.vue'
  import Todo from './components/Todo.vue'
  import { APIOperations } from './APIOperations.js'

  export default {
    data() {
      return {
        api: new APIOperations()
      }
    },
    components: {
    Create,
    Todo
    },
    methods: {
      deleteDone() {
        this.api.deleteCompletedTasks()
      },
    },
    beforeCreate() {
      if (window.localStorage.length === 0) {
        window.localStorage.setItem('todoList', JSON.stringify([]))
        window.localStorage.setItem('latestID', JSON.stringify(1))
      }
    }
  }
</script>
