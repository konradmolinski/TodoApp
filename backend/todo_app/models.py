from datetime import datetime
from sqlalchemy import Boolean, Column, Integer, String, Text
from .database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    done = Column(Boolean, default=False)
    date = Column(Text, default=datetime.now())
    order_id = Column(Integer, nullable=False, unique=True)