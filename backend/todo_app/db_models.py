import enum
from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import relationship

from .database import Base


class UserStatus(enum.Enum):
    ACTIVATED = "ACTIVATED"
    DEACTIVATED = "DEACTIVATED"


class DBCategory(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, unique=True)

    tasks = relationship("DBTask", back_populates="category")


class DBTask(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    duration = Column(SmallInteger, default=5)
    cycle = Column(SmallInteger, default=1)  # days
    category_id = Column(Integer, ForeignKey("category.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("DBUser", back_populates="tasks")
    category = relationship("DBCategory", back_populates="tasks")

    completed_instances = relationship(
        "DBTasksLog", back_populates="task", order_by="desc(DBTasksLog.completion_time)"
    )


class DBUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    status = Column(String, default=UserStatus.ACTIVATED)
    points = Column(Integer, default=0)
    secret = Column(String, nullable=False, unique=True)

    tasks = relationship("DBTask", back_populates="owner")
    completed_tasks = relationship("DBTasksLog", back_populates="executor")


class DBTasksLog(Base):
    __tablename__ = "tasks_log"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.now())
    completion_time = Column(Integer, nullable=True)
    executor_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)

    executor = relationship("DBUser", back_populates="completed_tasks")
    task = relationship("DBTask", back_populates="completed_instances")
