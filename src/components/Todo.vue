<script>
    export default {
    props: ['todo', 'todos'],
    data() {
        return {
            done: this.todo.done
        }
    },
    methods: {
        toggleCheck() {
            this.done = !this.done
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
    <div id="todo-div" @click="toggleCheck">
        <p v-if="!done">{{ todo.title }}</p>
        <p v-else class="todo-done">{{ todo.title }}</p>
        <span @click="deleteTodo" class="close-btn">x</span>
    </div>
</template>