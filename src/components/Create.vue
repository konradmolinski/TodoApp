<script>
    export default {
    data() {
        return {
            title: ''
        }
    },
    methods: {
        addTodo() {
            if (this.title.trim().length === 0) { 
                console.warn('Title required.')   
            } else {
                const todo = {title: this.title, done: false, date: new Date()}
                this.todos.push(todo)
                window.localStorage.setItem('todoList' , JSON.stringify(this.todos))
            }
        }
    },
    props: ['todos']
}
</script>

<template>
    <h1>Create Todo:</h1>
    <input v-model="title" type="text">
    <button @click="addTodo" type="button">Add</button>
</template>