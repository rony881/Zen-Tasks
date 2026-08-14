"""
This File is Centralized Configuration for the Appllication.
This File Contains all constants and settings used throughout the Application
"""

from pathlib import Path
from datetime import datetime

# ======== Apllication Data ================
PRIORITIES = ["Low", "Medium", "High", "Critical"]

# ============ Directory Paths ============
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"

# ============ Data Files ============
DB_FILE = DATA_DIR / "Zen.db"


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

# ============ UI Styling Constants ============
INFO_BAR_DURATION_SHORT = 1800
TABLE_ROW_HEIGHT = 46


# ==== Current Day ======
current_day = datetime.now().strftime("%a")
