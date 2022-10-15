from datetime import datetime
from sqlite3 import Date
from typing import List, Union

from pydantic import BaseModel


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
    category_id: int


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    completed_instances: "TasksLog"

    class Config:
        orm_mode = True


class TasksLogBase(BaseModel):
    completion_time: int | None = None
    executor_id: int
    task_id: int


class TasksLogCreate(TasksLogBase):
    pass


class TasksLog(TasksLogBase):
    date: datetime

    class Config:
        orm_mode = True
