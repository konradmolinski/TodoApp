<script>
  import Create from './components/Create.vue'
  import Todo from './components/Todo.vue'

  export default {
    data() {
      return {
        todos: JSON.parse({ ...localStorage }['todoList'])
      }
    },
    components: {
    Create,
    Todo
    },
    methods: {
      deleteDone() {
        this.todos = this.todos.filter(element => element.done == false)
        window.localStorage.setItem('todoList' , JSON.stringify(this.todos))
      },
      toggleDoneState(todoInstance) {
        todoInstance.done = !todoInstance.done
        const todoIdx = this.todos.indexOf(todoInstance)
        this.todos[todoIdx].done = todoInstance.done
        window.localStorage.setItem('todoList', JSON.stringify(this.todos))
      }
    },
    beforeCreate() {
      if (window.localStorage.length === 0) {
        window.localStorage.setItem('todoList', JSON.stringify([]))
        window.localStorage.setItem('latestID', JSON.stringify(1))
      }
    }
  }
</script>

<template>
  <Create 
  :todos=todos />
  <p v-if="this.todos.length === 0" id="empty-list-info">No tasks yet.</p>
  <ul id="todo-list">
    <li v-for = "todo in todos">
      <Todo
      @toggleCheck="toggleDoneState"
      :todos = todos
      :todo = todo />
    </li>
  </ul>
  <button id="delete-btn" @click="deleteDone" type="button">delete completed</button>
</template>