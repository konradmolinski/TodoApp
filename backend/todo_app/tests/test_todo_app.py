from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest
from ..database import Base
from ..main import app, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread" : False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def test_warmup_cleanup():
    from ..crud import delete_todo, get_todos
    db = next(override_get_db())
    
    todos = get_todos(db=db)
    for todo in todos:
        delete_todo(db, todo.id)
    db.commit()
    db.close()

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_todo():
    response = client.post(
        "/todos",
        json={"title": "przemekhuj"})
    assert response.status_code == 200

def test_get_todo():
    response = client.get("/todos/1")
    assert response.status_code == 200
    assert response.json()['title'] == "przemekhuj"

def test_get_todos():
    response = client.get("/todos")
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_update_todo_state():
    response = client.put(
        "/todos/1",
        json={"id": "1"})
    assert response.status_code == 204

    response = client.get("/todos/1")
    assert response.status_code == 200
    assert response.json()['done'] == True

def test_delete_todo():
    response = client.delete("/todos/1")
    assert response.status_code == 204

def test_delete_completed_todos():
    response = client.delete("/todos")
    assert response.status_code == 204


# def update_todoŔ