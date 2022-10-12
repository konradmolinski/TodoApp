from calendar import monthrange
from datetime import datetime, timedelta
from turtle import st

from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.orm import Session

from . import logger, schemas
from .crud import TodoDB
from .database import get_db

app = FastAPI()


@app.get("/todos", response_model=list[schemas.Todo], status_code=status.HTTP_200_OK)
def get_todos(db: Session = Depends(get_db)) -> list[schemas.Todo]:
    with TodoDB.from_db(db) as db_operations:
        return db_operations.get_todos()


@app.get(
    "/todos/{todo_id}", response_model=schemas.Todo, status_code=status.HTTP_200_OK
)
def get_todo(todo_id: int, db: Session = Depends(get_db)) -> schemas.Todo:
    with TodoDB.from_db(db) as db_operations:
        # TODO add some stats
        return schemas.Todo.from_orm(db_operations.get_todo(todo_id))  # type: ignore


@app.post("/todos", response_model=schemas.Todo)
def create_todo(
    todo: schemas.TodoCreate, db: Session = Depends(get_db), response=Response
) -> schemas.Todo:
    logger.info(f"Creating todo with parameters {todo}")
    with TodoDB.from_db(db) as db_operations:
        # try:
        db_todo = db_operations.create_todo(todo)
        return schemas.Todo.from_orm(db_todo)  # type: ignore
        # except Exception as ex:
        # logger.error(ex)
        # raise HTTPException(status_code=400, detail="Couldn't add new todo")


@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)) -> None:
    with TodoDB.from_db(db) as db_operations:
        try:
            db_operations.delete_todo(todo_id)
        except:
            # TODO check if exception is really not found
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.get("/todos/{todo_id}/stats", response_model=schemas.TodoStats)
def read_todo_stats(
    todo_id: int,
    date_min: datetime | None = None,
    date_max: datetime | None = None,
    db: Session = Depends(get_db),
) -> schemas.Todo:
    # TODO get statistics of one task
    # try:
    #     return crud.get_todo(db, todo_id=todo_id)
    # except:
    #     return status.HTTP_404_NOT_FOUND
    raise NotImplementedError()


@app.get("/users", response_model=list[schemas.User])
def get_users(db: Session = Depends(get_db)) -> list[schemas.User]:
    with TodoDB.from_db(db) as db_operations:
        return db_operations.get_users()


@app.get("/tasks", response_model=schemas.Todo)
def get_user_tasks(user_id: str, db: Session = Depends(get_db)) -> schemas.Todo:
    pass


@app.get("/todos/{todo_id}/complete", response_model=schemas.TodoLog)
def complete_user_task(
    todo_id: int, user_id: str, db: Session = Depends(get_db)
) -> schemas.TodoLog:
    # try:
    #     crud.read
    pass


@app.get("/users/stats", response_model=list[schemas.UserStats])
def get_users_stats(
    date_min: datetime | None = None,
    date_max: datetime | None = None,
    db: Session = Depends(get_db),
) -> list[schemas.UserStats]:
    now = datetime.now()
    if not date_min and not date_max:
        # Set current month for stats
        date_min = datetime(
            year=now.year, month=now.month, day=1, hour=0, minute=0, second=0
        )
        date_max = date_min + timedelta(
            days=monthrange(year=now.year, month=now.month)[1]
        )
    with TodoDB.from_db(db) as db_operations:
        return db_operations.get_users_stats(date_min=date_min, date_max=date_max)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
