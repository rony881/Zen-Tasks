from core.db import connection
from core.utils.logger import logger


def load_sleep_logs() -> list[dict]:
    """Load sleep log history."""
    with connection() as conn:
        rows = conn.execute("SELECT * FROM sleep_logs ORDER BY id").fetchall()
    logs = [dict(r) for r in rows]
    logger.info(f"Loaded {len(logs)} sleep logs")
    return logs


def save_sleep_logs(logs: list[dict]) -> None:
    """Replace all sleep logs."""
    with connection() as conn:
        conn.execute("DELETE FROM sleep_logs")
        conn.executemany(
            """INSERT INTO sleep_logs (date, bedtime, wakeup, duration, quality,
                                       awakenings, mood)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            [(l["date"], l["bedtime"], l["wakeup"], l["duration"],
              l["quality"], l["awakenings"], l["mood"]) for l in logs],
        )
    logger.info(f"Saved {len(logs)} sleep logs")