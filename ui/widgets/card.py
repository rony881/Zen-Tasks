from PyQt6.QtWidgets import (
    QFrame, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QWidget, QSizePolicy
)
from PyQt6.QtCore import Qt


class TaskCard(QFrame):
    def __init__(self, task_name, time):
        super().__init__()

        self.setFixedSize(230, 140)   # fixed width and height
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.setStyleSheet("""
            QFrame {
                background-color: #121212;
                border-radius: 8px;
            }
            QLabel {
                color: white;
            }
            QPushButton {
                background-color: #2a2a2a;
                color: white;
                border: none;
                padding: 6px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #3a3a3a;
            }
        """)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(8)

        # Top row
        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(0, 0, 0, 0)

        time_label = QLabel(time)
        time_label.setStyleSheet("""
            color: gray;
            background: #1e1e1e;
            padding: 4px 8px;
            border-radius: 4px;
        """)

        menu_button = QPushButton("⋮")
        menu_button.setFixedSize(28, 28)

        top_layout.addWidget(time_label)
        top_layout.addStretch()
        top_layout.addWidget(menu_button)

        main_layout.addLayout(top_layout)

        # Title
        self.title = QLabel(task_name)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setWordWrap(True)
        self.title.setStyleSheet("""
            font-size: 15px;
            font-weight: bold;
        """)
        main_layout.addWidget(self.title, 1)

        # Separator
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setStyleSheet("background:#333; max-height:1px;")
        main_layout.addWidget(separator)

        # Bottom button
        mark_button = QPushButton("Mark Done")
        mark_button.setFixedHeight(32)
        main_layout.addWidget(mark_button)