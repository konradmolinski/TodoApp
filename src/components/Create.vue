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
                this.api.createTask(this.latestID, this.title)
                this.latestID = JSON.parse({ ...localStorage }['latestID'])
            }
            this.title = ""
        }
    },
    props: ['api']
}
</script>