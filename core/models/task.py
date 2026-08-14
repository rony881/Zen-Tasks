"""
Data models for the application.
"""
from dataclasses import dataclass
from typing import Literal


@dataclass
class Task:
    
    time: str
    task: str
    priority: Literal["Low", "Medium", "High", "Critical"]
    done: bool = False
    
