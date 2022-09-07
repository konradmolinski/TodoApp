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
      :todos = todos
      :todo = todo />
    </li>
  </ul>
</template>