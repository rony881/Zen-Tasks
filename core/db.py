"""
Database access for the application.
"""

import sqlite3
from contextlib import contextmanager
from config import DB_FILE

def get_connection() -> sqlite3.Connection:
    """Open a connection and ensure tables exist."""
    DB_FILE.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode = WAL")
    create_tables(conn)
    return conn

def create_tables(conn: sqlite3.Connection) -> None:
    """Create all tables the app needs, if they don't already exist."""
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS schedule (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            day       TEXT NOT NULL,
            time      TEXT NOT NULL,
            task      TEXT NOT NULL,
            priority  TEXT NOT NULL
        );
        CREATE INDEX IF NOT EXISTS idx_schedule_day ON schedule(day);

        CREATE TABLE IF NOT EXISTS todays_tasks (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            day         TEXT NOT NULL,
            schedule_id INTEGER REFERENCES schedule(id) ON DELETE SET NULL,
            time        TEXT NOT NULL,
            task        TEXT NOT NULL,
            priority    TEXT NOT NULL,
            done        INTEGER NOT NULL DEFAULT 0
        );
        CREATE INDEX IF NOT EXISTS idx_todays_day ON todays_tasks(day);

        CREATE TABLE IF NOT EXISTS sleep_logs (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            date       TEXT NOT NULL,
            bedtime    TEXT NOT NULL,
            wakeup     TEXT NOT NULL,
            duration   TEXT NOT NULL,
            quality    TEXT NOT NULL,
            awakenings INTEGER NOT NULL DEFAULT 0,
            mood       TEXT
        );

        CREATE TABLE IF NOT EXISTS app_state (
            key   TEXT PRIMARY KEY,
            value TEXT NOT NULL
        );
    """)
    conn.commit()


@contextmanager
def connection():
    """Context manager: auto-commit on success, rollback on error."""
    conn = get_connection()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()