from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str


class TodoCreate(TodoBase):
    # Data that is required while creating Todo, but will not be sent from the API when reading Todo
    duration: int | None = None


class Todo(TodoBase):
    id: int
    done: bool
    date: str

    duration: int  # minutes

    class Config:
        orm_mode = True


class Stats(BaseModel):
    execution_count: int
    total_time_spent_min: int
    avg_time_spent_min: int


class TodoStats(Todo):
    stats: Stats


class TodoLog(BaseModel):
    todo_id: int


class Category(BaseModel):
    name: str


class User(BaseModel):
    id: int
    name: str


class UserStats(BaseModel):
    user: User
    minutes_worked: int
