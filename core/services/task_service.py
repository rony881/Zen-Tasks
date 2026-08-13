from config import current_day
from core.db import connection
from core.models.task import Task
from core.utils.logger import logger

_DAY_KEY = "last_loaded_day"


def load_todays_tasks(day: str = current_day) -> list[Task]:
    """Return today's tasks, rebuilding the snapshot from the schedule if needed."""
    with connection() as conn:
        row = conn.execute(
            "SELECT value FROM app_state WHERE key = ?", (_DAY_KEY,)
        ).fetchone()
        loaded_day = row["value"] if row else None

        if loaded_day != day:
            conn.execute("DELETE FROM todays_tasks WHERE day = ?", (day,))
            entries = conn.execute(
                "SELECT time, task, priority FROM schedule WHERE day = ? ORDER BY id",
                (day,),
            ).fetchall()
            conn.executemany(
                """INSERT INTO todays_tasks (day, schedule_id, time, task, priority, done)
                   VALUES (?, NULL, ?, ?, ?, 0)""",
                [(day, r["time"], r["task"], r["priority"]) for r in entries],
            )
            conn.execute(
                """INSERT INTO app_state (key, value) VALUES (?, ?)
                   ON CONFLICT(key) DO UPDATE SET value = excluded.value""",
                (_DAY_KEY, day),
            )
            logger.info(f"Rebuilt today's snapshot for {day}")

        rows = conn.execute(
            """SELECT time, task, priority, done FROM todays_tasks
               WHERE day = ? ORDER BY id""",
            (day,),
        ).fetchall()

    tasks = [Task(r["time"], r["task"], r["priority"], done=bool(r["done"]))
             for r in rows]
    logger.info(f"Loaded {len(tasks)} tasks for {day}")
    return tasks


def save_todays_tasks(tasks: list[Task], day: str = current_day) -> None:
    """Persist today's tasks. 'done' state is preserved per task."""
    with connection() as conn:
        conn.execute("DELETE FROM todays_tasks WHERE day = ?", (day,))
        conn.executemany(
            """INSERT INTO todays_tasks (day, time, task, priority, done)
               VALUES (?, ?, ?, ?, ?)""",
            [(day, t.time, t.task, t.priority, int(t.done)) for t in tasks],
        )
    logger.info(f"Saved {len(tasks)} tasks for {day}")