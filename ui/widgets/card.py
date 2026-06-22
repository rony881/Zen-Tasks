from PyQt6.QtWidgets import (
    QFrame, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QWidget, QSizePolicy
)
from PyQt6.QtCore import Qt
from qfluentwidgets import CardWidget,SubtitleLabel,PushButton,BodyLabel

class TaskCard(CardWidget):
    def __init__(self, task, time):
        super().__init__()

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(8)

        # Title Label
        time_label = SubtitleLabel(time)
        # Task
        task_name = BodyLabel(task)
        # Menu Button ⋮
        menu_button = PushButton("Complete")

        # # Top Area
        # top_area = QLabel()
        # top_layout = QHBoxLayout(top_area)

        # top_layout.addWidget

        main_layout.addWidget(time_label)
        main_layout.addWidget(task_name)
        main_layout.addWidget(menu_button)