from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, SmallInteger, String, Text

from .database import Base


class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    done = Column(Boolean, default=False)
    date = Column(Text, default=datetime.now())
    duration_min = Column(SmallInteger, default=5)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
