from http.client import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from . import models, schemas

def get_todo(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()

def get_todos(db: Session):
    q = db.query(models.Todo).order_by(models.Todo.order_id).all()
    return q

def create_todo(db: Session, todo: schemas.TodoCreate):
    highest_order_id = db.query(func.max(models.Todo.order_id)).first()
    if highest_order_id._data[0]: #if there is at least one row/latest order_id is 1
        db_todo = models.Todo(title=todo.title, order_id=highest_order_id._data[0] + 1)
    else: #order_id starts from integer 1
        db_todo = models.Todo(title=todo.title, order_id=1)

    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_completed_todos(db: Session):
    db.query(models.Todo).filter(models.Todo.done == True).delete()
    db.commit()

def delete_todo(db: Session, todo_id: int):
    db.query(models.Todo).filter(models.Todo.id == todo_id).delete()
    db.commit()

def update_todo_state(db: Session, todo_id: int):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail=f"todo item with id {todo_id} not found.")
    todo.done = not todo.done
    db.commit()
    return todo

def reorder_todos(db: Session, reorder_params: tuple[int, int]):
    first_todo = db.query(models.Todo).filter(models.Todo.id == reorder_params[0]).first()
    first_todo.order_id = reorder_params[1]
    second_todo = db.query(models.Todo).filter(models.Todo.id == reorder_params[1]).first()
    second_todo.order_id = reorder_params[0]
    
    db.commit()

    return first_todo, second_todo