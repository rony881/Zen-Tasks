"""
Data models for the Application.
"""
from dataclasses import dataclass,asdict
from typing import Literal

@dataclass
class Task:
    """Represeant a task with time,description,
    priority, and completation status.
    """

    time: str
    task: str
    priority: Literal["Low", "Medium", "High", "Critical"]
    done: bool = False

    def to_dict(self) -> dict:
        """Convert task to dictonary for JSON"""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """Create Task instance from dictionary."""
        return cls(
            time=data["time"],
            task=data["task"],
            priority=data["priority"],
            done=data.get("done", False)
        )