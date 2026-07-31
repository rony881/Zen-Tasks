from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt
from ui.theme import PRIORITY_COLORS


class PriorityLabel(QLabel):
    def __init__(self, priority: str):
        super().__init__()
        self.priority = priority
        self.setText(priority)
        priority_color = self.get_priority_color(self.priority)
        self.set_priority_color(priority_color)

    def get_priority_color(self, priority: str) -> str:
        return PRIORITY_COLORS.get(priority, "#9E9E9E")

    def set_priority_color(self, colour: str) -> None:
        self.setStyleSheet(f"""
            QLabel {{
                color: white;
                background-color: {colour};
                border-radius: 8px;
                padding: 2px 10px;
                font-weight: 600;
                font-size: 11px;
            }}
        """)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)