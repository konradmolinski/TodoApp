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
    db_categories = {}
    for category in categories:
        db_categories[category] = DBCategory(title=category)
    for db_category in db_categories.values():
        session.add(db_category)

    session.add(wojtek)
    session.add(konrad)
    session.commit()
    session.refresh(wojtek)
    session.refresh(konrad)
    for db_category in db_categories.values():
        session.refresh(db_category)
    tasks = {
        "Łazienka": [
            {"title": "zamiatanie na korytarz przed 17", "duration": 2, "cycle": 1, "owner_id": None},
            {"title": "umycie WC", "duration": 5, "cycle": 2, "owner_id": None},
            {"title": "umycie przysznica", "duration": 5, "cycle": 14, "owner_id": None},
            {"title": "zlewu + lustra", "duration": 5, "cycle": 7, "owner_id": None},
            {"title": "umycie podłogi", "duration": 10, "cycle": 7, "owner_id": None},
            {"title": "umycie kuwet", "duration": 15, "cycle": 7, "owner_id": wojtek.id},
            {"title": "umycie okna", "duration": 15, "cycle": 90, "owner_id": None},
            {"title": "wyprawnie fianek", "duration": 15, "cycle": 30, "owner_id": None},
        ],
        "Kuchnia": [
            {"title": "zastrzyk Frankowi", "duration": 2, "cycle": 1, "owner_id": wojtek.id},
            {"title": "wyniesienie śmieci spod zlewu", "duration": 5, "cycle": 1, "owner_id": None},
            {"title": "wyniesienie śmieci sortowanych", "duration": 5, "cycle": 2, "owner_id": None},
            {"title": "umycie zbiornika od plastików", "duration": 5, "cycle": 7, "owner_id": None},
            {"title": "sprzątanie zlewu", "duration": 5, "cycle": 1, "owner_id": None},
            {"title": "mycie blatów i układanie rzeczy", "duration": 5, "cycle": 1, "owner_id": None},
            {"title": "porządkowanie lodówki", "duration": 5, "cycle": 7, "owner_id": None},
            {"title": "umycie lodówki", "duration": 20, "cycle": 30, "owner_id": None},
            {"title": "umycie kuchenki", "duration": 5, "cycle": 7, "owner_id": None},
            {"title": "włączenie zmywarki", "duration": 3, "cycle": 1, "owner_id": None},
            {"title": "opróźnienie zmywarki", "duration": 3, "cycle": 1, "owner_id": None},
            {"title": "umycie okna", "duration": 15, "cycle": 90, "owner_id": None},
            {"title": "Opróźnienie Adama", "duration": 3, "cycle": 1, "owner_id": None},
        ],
        "Salon": [
            {"title": "Sprzątanie po nasiadówie", "duration": 10, "cycle": 0, "owner_id": None},
            {"title": "Fotele czyste od futra", "duration": 10, "cycle": 0, "owner_id": wojtek.id},
            {"title": "Odkurzanie pokoju", "duration": 7, "cycle": 0, "owner_id": None},
            {"title": "Uprzątnięcie pokoju", "duration": 10, "cycle": 0, "owner_id": None},
            {"title": "Sprzątnięcie balkonu", "duration": 10, "cycle": 0, "owner_id": wojtek.id},
            {"title": "", "duration": 10, "cycle": 0, "owner_id": None},
            {"title": "umycie okien", "duration": 30, "cycle": 90, "owner_id": None},
        ],
    }
    for task_category in tasks.keys():
        for task in tasks[task_category]:
            session.add(
                DBTask(
                    title=task["title"],
                    duration=task["duration"],
                    cycle=task["cycle"],
                    category_id=db_categories[task_category].id,
                    owner_id=task["owner_id"],
                )
            )
    session.commit()


if __name__ == "__main__":
    create_seed_data()
