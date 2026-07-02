# core/data_loader.py
import json
from pathlib import Path

_DATA_FILE = Path(__file__).parent.parent / "data" / "weekly_schedule.json"

_TODAYS_TASK_FILE = Path(__file__).parent.parent / "data" / "todays_tasks.json"

def load_schedule() -> dict[str, list[list]]:
    """Load weekly schedule from JSON file."""
    if not _DATA_FILE.exists():
        raise FileNotFoundError(f"Schedule file not found: {_DATA_FILE}")
    with open(_DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_schedule(data: dict) -> None:
    with open(_DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def load_todays_tasks(day:str) -> list[dict]:
    daily_task = []
    schedule = load_schedule()

    for time,task,prio in schedule[day]:
        daily_task.append({
            "time" : time,
            "task" : task,
            "priority" : prio,
            "done" : False
        })
        save_todays_tasks(daily_task)

    try:
        with open(_TODAYS_TASK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []

def save_todays_tasks(tasks: list[dict]) -> None:
    with open(_TODAYS_TASK_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)
