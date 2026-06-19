from PyQt6.QtWidgets import  QLabel, QVBoxLayout, QFrame
from PyQt6.QtCore import Qt


class TaskCard(QFrame):
    def __init__(self, task_name):
        super().__init__()

        self.setStyleSheet("background-color: #121212;border-radius:6px;")

        layout = QVBoxLayout()
        layout.setSpacing(0)
        self.setLayout(layout)

        # Title Area
        self.title = QLabel(task_name)
        self.title.setStyleSheet(
            """
            font-size:18px;
            """
            )
        # Add to layout
        layout.addWidget(self.title)