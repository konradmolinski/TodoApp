from xmlrpc.client import boolean
from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str

class TodoCreate(TodoBase): #data that is required while creating Todo, but will not be sent from the API when reading Todo
    pass

class Todo(TodoBase):
    id: int
    done: bool
    date: str
    order_id: int

    class Config:
        orm_mode = True
