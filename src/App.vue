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
      if (window.localStorage.length === 0) window.localStorage.setItem('todoList', JSON.stringify([]))
    }
  }
</script>

<template>
  <Create 
  :todos=todos />
  <ul id="todo-list">
    <li v-for = "todo in todos">
      <Todo
      @toggleCheck="toggleDoneState"
      :todos = todos
      :todo = todo />
    </li>
  </ul>
  <button @click="deleteDone" type="button">delete done tasks</button>
</template>