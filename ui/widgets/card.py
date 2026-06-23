from PyQt6.QtWidgets import (
    QVBoxLayout,QHBoxLayout
)
from qfluentwidgets import CardWidget,SubtitleLabel,BodyLabel


class TaskCard(CardWidget):
    def __init__(self, task, time):
        super().__init__()

        self.setFixedHeight(100)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)

        self.time_label = SubtitleLabel(time)
        self.task_label = BodyLabel(task)

        main_layout.addWidget(self.time_label)
        main_layout.addWidget(self.task_label)

        main_layout.addStretch()

        buttom_layout = QHBoxLayout()
        buttom_layout.addStretch()

        main_layout.addLayout(buttom_layout)
