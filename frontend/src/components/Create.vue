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
        }
    },
    methods: {
        addTodo() {
            if (this.title.trim().length === 0) { 
                console.warn('Title required.')   
            } else {
                this.api.createTask(this.title)
            }
            this.title = ""
        }
    },
    props: ['api']
}
</script>