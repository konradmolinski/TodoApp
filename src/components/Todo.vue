<script>
    export default {
    props: ['todo', 'todos'],
    methods: {
        toggleCheck() {
            this.$emit('toggleCheck', this.todo)
        },
        deleteTodo() {
            const todoIdx = this.todos.indexOf(this.todo)
            this.todos.splice(todoIdx, 1)
            window.localStorage.setItem('todoList' , JSON.stringify(this.todos))
        }
    },
}
</script>

<template>
    <div id="todo-div" :class="{'todo-done': this.todo.done}">
        <div id="text-div" @click="toggleCheck">
            <p v-if="!this.todo.done">{{ todo.title }}</p>
            <p v-else style="text-decoration: line-through">{{ todo.title }}</p>
        </div>
    <span @click="deleteTodo" class="close-btn">&#215</span>
    </div>
</template>