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

    def get_priority_color(self, priority: str) -> dict:
        return PRIORITY_COLORS.get(priority, {"bg": "#F5F5F5", "text": "#616161"})
    
    def set_priority_color(self, colours: dict) -> None:
        self.setStyleSheet(f"""
            QLabel {{
                color: {colours['text']};
                background-color: {colours['bg']};
                border-radius: 6px;
                padding: 10px 10px;
                font-weight: 600;
                font-size: 11px;
            }}
        """)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)