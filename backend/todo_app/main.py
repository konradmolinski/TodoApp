import string
import logging

from typing import List
from sqlalchemy.orm import Session
from datetime import datetime
from . import crud, models, schemas
from .database import SessionLocal, engine
from fastapi import FastAPI, Depends, status, HTTPException, Response
from pydantic import BaseModel

app = FastAPI()

logger = logging.getLogger()
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
fh = logging.FileHandler(filename='./server.log')
formatter_stream = logging.Formatter(
    "%(module)s - %(funcName)s - line:%(lineno)d - %(levelname)s - %(message)s"
)

formatter_file = logging.Formatter(
    "%(asctime)s - %(module)s - %(funcName)s - line:%(lineno)d - %(levelname)s - %(message)s"
)
ch.setFormatter(formatter_stream)
fh.setFormatter(formatter_file)
logger.addHandler(ch)
logger.addHandler(fh)
 
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
    # try:
    return crud.get_todos(db)
    # except:
    #     return status.HTTP_404_NOT_FOUND

@app.post("/todos", response_model = schemas.Todo)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db), response = Response):
    logger.info(f"Creating todo with parameters {todo}")
    try:
        return crud.create_todo(db=db, todo=todo)
    except Exception as ex:
        logger.error(ex)
        raise HTTPException(status_code=400, detail="Couldn't add new todo")
    

@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    try:
        crud.delete_todo(db, todo_id=todo_id)
    except:
        return status.HTTP_400_BAD_REQUEST

@app.delete("/todos", status_code=status.HTTP_204_NO_CONTENT)
def delete_completed_todos(db: Session = Depends(get_db)):
    try:
        crud.delete_completed_todos(db)
    except:
        return status.HTTP_400_BAD_REQUEST

@app.put("/todos/{todo_id}")
def update_todo_state(todo_id: int, db: Session = Depends(get_db)):
    try:
        return crud.update_todo_state(db, todo_id=todo_id)
    except:
        return status.HTTP_400_BAD_REQUEST

@app.put("/todos-reorder")
def reorder_todos(reorder_params: ReorderParams, db: Session = Depends(get_db)):
    try:
        return crud.reorder_todos(db, reorder_params=(reorder_params['first_id'], reorder_params['second_id']))
    except:
        return status.HTTP_400_BAD_REQUEST

@app.get("/todos/{todo_id}", response_model=schemas.Todo)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_todo(db, todo_id=todo_id)
    except:
        return status.HTTP_404_NOT_FOUND