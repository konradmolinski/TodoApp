<template>
    <div id="todo-div" :class="{'todo-done': this.todo.done}">
        <div id="text-div" @click="toggleTaskCompleted">
            <p v-if="!this.todo.done">{{ todo.title }}</p>
            <p v-else id="todo-title-done">{{ todo.title }}</p>
        </div>
    <span v-if="!isFirst()" @click="moveUp" class="up-btn">&uarr;</span>
    <span v-if="isLast()" class="no-btn"> </span>
    <span v-if="!isLast()" @click="moveDown" class="down-btn">&darr;</span>
    
    <span  @click="deleteTodo" class="close-btn">&#215</span>
    </div>
</template>

<script>
    export default {
    data () {
        return {
            todoIdx: this.api.todos.indexOf(this.todo)
        }
    },
    props: ['todo', 'api'],
    methods: {
        toggleTaskCompleted() {
            this.api.toggleTaskCompleted(this.todo)
        },
        deleteTodo() {
            this.api.deleteTask(this.todoIdx)
        },
        isLast() {
            return this.todoIdx === this.api.todos.length-1
        },
        isFirst() {
            return this.todoIdx === 0
        },
        moveUp() {
            this.api.reorderTask(this.todoIdx, this.todoIdx -1)
        },
        moveDown() {
            this.api.reorderTask(this.todoIdx, this.todoIdx +1)
        },
    },
}
</script>