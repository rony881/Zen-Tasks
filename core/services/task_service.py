# core/services/task_service.py
import json
from config import LAST_LOADED_DAY_FILE, TODAYS_TASKS_FILE
from core.utils.logger import logger
from core.models.task import Task


def load_todays_tasks(day: str) -> list[Task]:
    """Load today's tasks for the specified day."""
    try:
        from core.data_loader import load_schedule
        
        schedule = load_schedule()
        if day not in schedule:
            logger.warning(f"Day '{day}' not found in schedule")
            return []
        
        if last_loaded_day() != day or not TODAYS_TASKS_FILE.exists():
            daily_tasks = []
            for time, task, prio in schedule[day]:
                daily_tasks.append(Task(
                    time=time,
                    task=task,
                    priority=prio,
                    done=False
                ))
            save_todays_tasks(daily_tasks)
            save_todays_day(day)
        
        with open(TODAYS_TASKS_FILE, "r", encoding="utf-8") as f:
            tasks_data = json.load(f)
            tasks = [Task.from_dict(t) for t in tasks_data]
            logger.info(f"Successfully loaded {len(tasks)} tasks for {day}")
            return tasks
            
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in tasks file: {e}")
        return []
    except (OSError, KeyError) as e:
        logger.error(f"Failed to load today's tasks: {e}")
        return []


def save_todays_tasks(tasks: list[Task]) -> None:
    """ Save today's tasks to JSON file. """
    
    try:
        TODAYS_TASKS_FILE.parent.mkdir(parents=True, exist_ok=True)
        task_data = [task.to_dict() for task in tasks]
        with open(TODAYS_TASKS_FILE, "w", encoding="utf-8") as f:
            json.dump(task_data, f, indent=4, ensure_ascii=False)
        logger.info(f"Successfully saved {len(tasks)} tasks to {TODAYS_TASKS_FILE}")
        
    except OSError as e:
        logger.error(f"Failed to save tasks file: {e}")
        raise


def last_loaded_day() -> str | None:
    try:
        return LAST_LOADED_DAY_FILE.read_text(encoding="utf-8").strip()
    except OSError :
        return None


def save_todays_day(day: str) -> None:
    try:
        LAST_LOADED_DAY_FILE.parent.mkdir(parents=True, exist_ok=True)
        LAST_LOADED_DAY_FILE.write_text(day, encoding="utf-8")
    except OSError as e:
        logger.error(f"Failed to write last loaded day: {e}")