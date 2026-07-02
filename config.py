"""
This File is Centralized Configuration for the Appllication.
This File Contains all constants and settings used throughout the Application
"""

from pathlib import Path

# ======== Apllication Data ================
DAYS = ["Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"]
PRIORITIES = ["Low", "Medium", "High", "Critical"]

# ============ Directory Paths ============
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"

# ============ File Names ============
WEEKLY_SCHEDULE_FILE = DATA_DIR / "weekly_schedule.json"
TODAYS_TASKS_FILE = DATA_DIR / "todays_tasks.json"

# ============ UI Configuration ============
UI_CONFIG = {
    "window_width": 1200,
    "window_height": 720,
    "navigation_width": 240,
    "card_height": 56,
    "dialog_width": 600,
    "dialog_height": 300,
}

# ============ Table Configuration ============
TIME_COL = 0
TASK_COL = 1
PRIORITY_COL = 2
