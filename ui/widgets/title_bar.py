from PyQt6.QtWidgets import QFrame, QHBoxLayout, QPushButton

from qfluentwidgets import TitleLabel
from ui.theme import ADD_BTN_STYLE

class TitleBar(QFrame):
    """Title bar widget with optional add task button."""
    def __init__(self, parent, h1: str, btn: bool= False):
        """Initialize title bar with title and optional button."""
        super().__init__(parent)
        self.parent = parent
        layout = QHBoxLayout(self)

        title = TitleLabel(h1)
        layout.addWidget(title)
        layout.addStretch()

        if btn:
            self.add_btn = QPushButton("+ Add Task")
            self.add_btn.setStyleSheet(ADD_BTN_STYLE)
            self.add_btn.clicked.connect(self.parent.show_add_task_dialog)
            layout.addWidget(self.add_btn)
