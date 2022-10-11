export class APIOperations {
    constructor() {
        this.refreshLocalStorage();
        //API URL
        //API KEY
    }
    refreshLocalStorage() {
        this.todos = JSON.parse({ ...localStorage }['todoList'])
        this.id = JSON.parse({ ...localStorage }['latestID'])
    }
    reorderTask(todoIdx1, todoIdx2) {
        const task1 = this.todos[todoIdx1]
        const task2 = this.todos[todoIdx2]

        this.todos[todoIdx1] = task2
        this.todos[todoIdx2] = task1

        window.localStorage.setItem('todoList', JSON.stringify(this.todos))
        this.refreshLocalStorage()
    }
    createTask(title) {
        const todo = {id: this.id, title: title, done: false, date: new Date()}
        this.todos.push(todo)
        window.localStorage.setItem('todoList', JSON.stringify(this.todos))
        window.localStorage.setItem('latestID', JSON.stringify(this.id+1))
        this.refreshLocalStorage()
    }
    deleteTask(todoIdx) {
        this.todos.splice(todoIdx, 1)
        window.localStorage.setItem('todoList' , JSON.stringify(this.todos))
        this.refreshLocalStorage()
     }
    toggleTaskCompleted(todo) {
        todo.done = !todo.done
        const todoIdx = this.todos.indexOf(todo)
        this.todos[todoIdx].done = todo.done
        window.localStorage.setItem('todoList', JSON.stringify(this.todos))
        this.refreshLocalStorage()

    }
    deleteCompletedTasks() {
        this.todos = this.todos.filter(element => element.done == false)
        window.localStorage.setItem('todoList', JSON.stringify(this.todos))
        this.refreshLocalStorage()
    }
};