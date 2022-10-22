from collections.abc import Generator
from todo_app.database import SessionLocal
from typing import Any
from todo_app.db_models import DBCategory, DBUser, DBTask


def get_db() -> Generator[Any, Any, Any]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


session = next(get_db())


def create_seed_data() -> None:
    # users
    wojtek = DBUser(name="Wojtek", status="ACTIVATED", secret="bardzotrudnehaslo")
    konrad = DBUser(name="Konrad", status="ACTIVATED", secret="kondziowehaslo")
    # categories
    categories = [
        "Koty",
        "Łazienka",
        "Kuchnia",
        "Korytarz",
        "Salon",
        "Balkon",
        "Wojtka",
        "Konrada",
    ]
    db_categories = []
    for category in categories:
        db_categories.append(DBCategory(title=category))
    for db_category in db_categories:
        session.add(db_category)

    session.add(wojtek)
    session.add(konrad)
    session.commit()
    session.refresh(wojtek)
    session.refresh(konrad)
    for db_category in db_categories:
        session.refresh(db_category)
    task_1 = DBTask(
        title="Czyszczenie prysznica",
        duration=5,
        cycle=14,
        category_id=db_categories[3].id,
    )
    session.add(task_1)
    session.commit()


if __name__ == "__main__":
    create_seed_data()
