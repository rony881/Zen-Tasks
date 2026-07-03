"""
Logging configuration for the application.
Provides tracking of application behavior
"""

import logging
import sys

def setup_logger(name: str = "Zen", level: int = logging.INFO):
    """this set up and return a configure logger

    Args:
        name: Name of the logger
        level: Logging level
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.handlers:
        return logger

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%H:%M:%S'
    )
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger

logger = setup_logger()