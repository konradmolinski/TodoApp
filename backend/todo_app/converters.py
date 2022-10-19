from datetime import datetime, timedelta

from .db_models import DBTask
from .schemas import MinimalTask


def db_task_to_minimal_task(db_task: DBTask) -> MinimalTask:
    if not len(db_task.completed_instances):
        overdue_hours = 24 * 10
    else:
        overdue_hours = (
            datetime.now() - db_task.completed_instances[0].date
        ).seconds / 3600
    return MinimalTask(
        id=db_task.id,
        title=db_task.title,
        category=db_task.category.title,
        duration=db_task.duration,
        overdue_hours=overdue_hours,
    )
