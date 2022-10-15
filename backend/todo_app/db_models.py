import enum
from datetime import datetime

from sqlalchemy import Column, Date, ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import relationship

from .database import Base

# from turtle import back


class UserStatus(enum.Enum):
    ACTIVATED = "ACTIVATED"
    DEACTIVATED = "DEACTIVATED"


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)

    tasks = relationship("Task", back_populates="category")


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    duration = Column(SmallInteger, default=5)
    cycle = Column(SmallInteger, default=1)
    category_id = Column(Integer, ForeignKey("category.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="tasks")
    category = relationship("Category", back_populates="tasks")

    completed_instances = relationship("TasksLog", back_populates="task")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    status = Column(String, default=UserStatus.ACTIVATED)
    points = Column(Integer, default=0)
    secret = Column(String, nullable=False)

    tasks = relationship("Task", back_populates="owner")
    completed_tasks = relationship("TasksLog", back_populates="executor")


class TasksLog(Base):
    __tablename__ = "tasks_log"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, default=datetime.now())
    completion_time = Column(Integer, nullable=True)
    executor_id = Column(Integer, ForeignKey("users.id"))
    task_id = Column(Integer, ForeignKey("tasks.id"))

    executor = relationship("User", back_populates="completed_tasks")
    task = relationship("Task", back_populates="completed_instances")
