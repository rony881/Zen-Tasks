# core/data_loader.py
import json
from pathlib import Path

_DATA_FILE = Path(__file__).parent.parent / "data" / "weekly_schedule.json"

def load_schedule() -> dict[str, list[list]]:
    """Load weekly schedule from JSON file."""
    if not _DATA_FILE.exists():
        raise FileNotFoundError(f"Schedule file not found: {_DATA_FILE}")
    with open(_DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)