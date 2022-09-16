export class APIOperations {
    constructor() {
        this.refreshLocalStorage();
        //API URL
        //API KEY
    }
    refreshLocalStorage() {
        this.todos = JSON.parse({ ...localStorage }['todoList'])
    }
    reorderTask(index, direction) { // direction -1 = up 1 = down
        const todo = this.todos[index]
        const higherTodo = this.todos[index + direction]

        this.todos[index + direction] = todo
        this.todos[index] = higherTodo

        window.localStorage.setItem('todoList', JSON.stringify(this.todos))
        this.refreshLocalStorage()
    }
    createTask(id, title) {
        // returns full object 
        // task {
        //     "uuid",
        //     "text",
        //     "created_at",
        //     "order"
        // }
        const todo = {id: id, title: title, done: false, date: new Date()}
        this.todos.push(todo)
        window.localStorage.setItem('todoList', JSON.stringify(this.todos))
        window.localStorage.setItem('latestID', JSON.stringify(id+1))
        this.refreshLocalStorage()
    }
    deleteTask(todoIdx) {
        this.todos.splice(todoIdx, 1)
        window.localStorage.setItem('todoList' , JSON.stringify(this.todos))
        this.refreshLocalStorage()
     }
    toggleTask(todo) {
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