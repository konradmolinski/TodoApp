<template>
    <div id="create-div">
        <h1>Todo App</h1>
        <input id="title-input" v-model="title" type="text">
        <button @click="addTodo" type="button">Add</button>
    </div>
</template>

<script>
    export default {
    data() {
        return {
            title: '',
            latestID: JSON.parse(window.localStorage.getItem('latestID'))
        }
    },
    methods: {
        addTodo() {
            if (this.title.trim().length === 0) { 
                console.warn('Title required.')   
            } else {
                const todo = {id: this.latestID, title: this.title, done: false, date: new Date()}
                this.todos.push(todo)
                window.localStorage.setItem('todoList' , JSON.stringify(this.todos))
                this.latestID ++
                window.localStorage.setItem('latestID', JSON.stringify(this.latestID))
            }
        }
    },
    props: ['todos']
}
</script>