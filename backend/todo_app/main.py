import string
from typing import List
from sqlalchemy.orm import Session
from datetime import datetime
from . import crud, models, schemas
from .database import SessionLocal, engine
from fastapi import FastAPI, Depends, status, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

class ReorderParams(BaseModel):
    first_id: int
    second_id: int

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/todos", response_model=List[schemas.Todo])
def read_todos(db: Session = Depends(get_db)):
    todos = crud.get_todos(db)
    return todos

@app.post("/todos", response_model = schemas.Todo)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db=db, todo=todo)

@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    crud.delete_todo(db, todo_id=todo_id)

@app.delete("/todos", status_code=status.HTTP_204_NO_CONTENT)
def delete_completed_todos(db: Session = Depends(get_db)):
    crud.delete_completed_todos(db)

@app.put("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def update_todo_state(todo_id: int, db: Session = Depends(get_db)):
    crud.update_todo_state(db, todo_id=todo_id)

@app.put("/todos-reorder", status_code=status.HTTP_204_NO_CONTENT)
def reorder_todos(reorder_params: ReorderParams, db: Session = Depends(get_db)):
    crud.reorder_todos(db, reorder_params=reorder_params)

@app.get("/todos/{todo_id}", response_model=schemas.Todo)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_todo(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo