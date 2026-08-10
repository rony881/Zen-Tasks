"""
Database acces for the application.
"""

import sqlite3
from config import DB_FILE

def get_connection() -> sqlite3.Connection:
    """Open a connection to the database and make sure the tables exist."""
    DB_FILE.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    create_tables(conn)
    return conn

def create_tables(conn: sqlite3.Connection) -> None:
    """Create all tables the app needs, if they don't already exist."""
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS schedule (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            day TEXT NOT NULL,
            time TEXT NOT NULL,
            task TEXT NOT NULL,
            priority TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS todays_tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            time TEXT NOT NULL,
            task TEXT NOT NULL,
            priority TEXT NOT NULL,
            done INTEGER NOT NULL DEFAULT 0
        );

        CREATE TABLE IF NOT EXISTS sleep_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            bedtime TEXT NOT NULL,
            wakeup TEXT NOT NULL,
            duration TEXT NOT NULL,
            quality TEXT NOT NULL,
            awakenings INTEGER NOT NULL DEFAULT 0,
            mood TEXT
        );
    """)
    conn.commit() 