from core.db import connection
from core.utils.logger import logger


def load_schedule() -> dict[str, list[list]]:
    """Load weekly schedule, grouped by day, in insertion order."""
    with connection() as conn:
        rows = conn.execute(
            "SELECT day, time, task, priority FROM schedule ORDER BY id"
        ).fetchall()

    data: dict[str, list[list]] = {}
    for r in rows:
        data.setdefault(r["day"], []).append([r["time"], r["task"], r["priority"]])
    logger.info(f"Loaded {len(rows)} schedule entries")
    return data


def save_schedule(data: dict[str, list[list]]) -> None:
    """Replace the whole schedule with the given data."""
    with connection() as conn:
        conn.execute("DELETE FROM schedule")
        conn.executemany(
            "INSERT INTO schedule (day, time, task, priority) VALUES (?, ?, ?, ?)",
            [(day, t, task, p) for day, entries in data.items()
             for t, task, p in entries],
        )
    logger.info("Schedule saved to database")