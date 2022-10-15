from collections.abc import Iterator
from contextlib import contextmanager
from typing import TypeVar

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from . import db_models, logger, schemas

SQLALCHEMY_DATABASE_URL = "sqlite:///./todo_app.db"

_T = TypeVar("_T", bound="DBOperations")


class DBOperations:
    """
    Context manager wrapping database operations
    - automatically openning and closing sesion
    """

    def __init__(self, session: Session):
        self.session: Session = session

    @contextmanager
    def __call__(self: _T) -> Iterator[_T]:
        with self.from_db(session=self.session) as dbo:
            yield dbo

    @classmethod
    @contextmanager
    def from_db(cls: type[_T], session: Session) -> Iterator[_T]:
        """
        Create database session.
        """
        try:
            instance = cls(session=session)
            yield instance
        finally:
            instance.session.close()


class TodoDB(DBOperations):
    # def get_tasks(self -> list[db_models.Task]):
    #     return self.session.query(db_models.Task).filter

    def append_task_log(self, task_log: schemas.TasksLogCreate) -> db_models.DBTasksLog:
        completed_task = db_models.DBTasksLog(
            executor_id=task_log.executor_id, task_id=task_log.task_id
        )
        logger.info("ASD")
        self.session.add(completed_task)
        self.session.commit()
        self.session.refresh(completed_task)
        return completed_task


# class TodoDB(DBOperations):
#     def get_todo(self, todo_id: int) -> db_models.Todo | None:
#         return (  # type: ignore
#             self.session.query(db_models.Todo)
#             .filter(db_models.Todo.id == todo_id)
#             .first()
#         )

#     def get_todos(self) -> list[db_models.Todo]:
#         return self.session.query(db_models.Todo).order_by(db_models.Todo.id).all()  # type: ignore

#     def create_todo(self, todo: db_models.Todo) -> db_models.Todo:
#         todo = db_models.Todo(title=todo.title)
#         self.session.add(todo)
#         self.session.commit()
#         self.session.refresh(todo)
#         return todo

#     def delete_todo(self, todo_id: int) -> None:
#         self.session.query(db_models.Todo).filter(db_models.Todo.id == todo_id).delete()
#         self.session.commit()

#     def get_users(self) -> list[db_models.User]:
#         return self.session.query(db_models.User).all()  # type: ignore

#     def get_users_stats(
#         self, date_min: datetime | None = None, date_max: datetime | None = None
#     ) -> list[schemas.UserStats]:
#         pass
# return schemas.UserStats()
