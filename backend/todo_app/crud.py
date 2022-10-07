from http.client import HTTPException
from sqlalchemy.orm import Session

from . import models, schemas

def get_todo(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()

def get_todo_by_title(db: Session, title: str):
    return db.query(models.Todo).filter(models.Todo.title == title).first()

def get_todos(db: Session):
    return db.query(models.Todo).all()

def create_todo(db: Session, todo: schemas.TodoCreate):
    db_todo = models.Todo(title=todo.title)
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

def reorder_todos(db: Session, reorder_params: dict):
    first_id = reorder_params['first_id']
    second_id = reorder_params['second_id']

    first_todo = db.query(models.Todo).filter(models.Todo.id == first_id).first()
    first_todo.order_id = second_id
    second_todo = db.query(models.Todo).filter(models.Todo.id == second_id).first()
    second_todo.order_id = first_id
    
    db.commit()