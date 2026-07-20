import json
from config import SLEEP_LOGS_FILE
from core.utils.logger import logger


def load_sleep_logs() -> list[dict]:
    """Loads Sleep Logs History From JSON File """

    if not SLEEP_LOGS_FILE.exists():
        logger.error(f"File not found: {SLEEP_LOGS_FILE}")
        raise FileNotFoundError(f"File not found: {SLEEP_LOGS_FILE}")

    try:
        with open(SLEEP_LOGS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            logger.info(f"Successfully Loaded {SLEEP_LOGS_FILE}")

            return data
            
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in Logs file: {e}")
        raise

    except OSError as e:
        logger.error(f"Failed to read Logs file: {e}")
        raise

def save_sleep_logs(logs: list[dict]):
    """ Save Sleep Logs to JSON file. """

    try:
        SLEEP_LOGS_FILE.parent.mkdir(parents=True, exist_ok=True)
        
        with open(SLEEP_LOGS_FILE, "w", encoding="utf-8") as f:
            json.dump(logs, f, indent=4, ensure_ascii=False)
        logger.info(f"Successfully saved {len(logs)} sleep logs to {SLEEP_LOGS_FILE}")
        
    except OSError as e:
        logger.error(f"Failed to save Logs file: {e}")
        raise