from datetime import datetime
from sqlite3 import Date
from typing import List, Any

from pydantic import BaseModel, validator


class CategoryBase(BaseModel):
    title: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    tasks: "Task"

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    status: str
    points: int


class UserCreate(UserBase):
    secret: str


class User(UserBase):
    tasks: "Task"
    completed_tasks: "TasksLog"

    class Config:
        orm_mode = True


class TaskBase(BaseModel):
    title: str
    duration: int
    cycle: int
    owner_id: int | None = None
    category: str


class TaskCreate(TaskBase):
    pass


class TasksLogBase(BaseModel):
    completion_time: int | None = None
    task_id: int


class TasksLogCreate(TasksLogBase):
    pass


class TasksLog(TasksLogBase):
    date: datetime

    class Config:
        orm_mode = True


class MinimalTaskBase(BaseModel):
    title: str
    category: str | None = None
    duration: int | None = None
    overdue_hours: int


class MinimalTask(BaseModel):
    id: int


class MinimalTaskCreate(MinimalTaskBase):
    duration: int | None = None
    cycle: int | None = None
    owner_id: int | None = None
    category_id: int | None = None
    category: str | None = None

    @validator("category_id", always=True)
    def mutually_exclusive(cls, v, values) -> Any:  # type: ignore
        if values["category"] is not None and v:
            raise ValueError("'category' and 'category_id' are mutually exclusive.")
        return v


class Task(TaskBase):
    completed_instances: TasksLog

    class Config:
        orm_mode = True
