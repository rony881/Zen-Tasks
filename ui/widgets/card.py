from asyncio import tasks

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QLabel,
)
from qfluentwidgets import CardWidget, CheckBox, TransparentToolButton, FluentIcon as FI
from qfluentwidgets.components.date_time.calendar_view import QVBoxLayout


class TaskCard(CardWidget):
    checkbox_changed = pyqtSignal(bool)
    def __init__(self, task: dict):
        super().__init__()
        self.setFixedHeight(56)
        self.task = task
        self.setStyleSheet(
            """
            CardWidget{
                border: 1px solid #999999;
                border-radius: 6px;
            }
            """
        )

        layout = QHBoxLayout(self)
        layout.setContentsMargins(12,8,12,8)
        layout.setSpacing(12)

        self.checkbox = CheckBox()
        self.checkbox.setChecked(task["done"])
        self.checkbox.toggled.connect(self.on_checked)
        layout.addWidget(self.checkbox)

        time_lbl = QLabel(task["time"])
        time_lbl.setStyleSheet("color: #333333")
        layout.addWidget(time_lbl)

        self.task_lbl = QLabel(task["task"])
        self.task_lbl.setStyleSheet("color: #333333")
        layout.addWidget(self.task_lbl)
        layout.addStretch()
        
        prio_lbl = QLabel(task["priority"])
        prio_lbl.setStyleSheet("color: #4dabf7;")
        layout.addWidget(prio_lbl)

        edit_btn = TransparentToolButton(FI.EDIT)
        layout.addWidget(edit_btn)
        
        delete_btn = TransparentToolButton(FI.DELETE)
        layout.addWidget(delete_btn)

    def on_checked(self, checked):
        self.task["done"] = checked
        self.checkbox_changed.emit(checked)
        
class SimpleCard(CardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.card_layout = QVBoxLayout(self)
        self.card_layout.setContentsMargins(20, 16, 20, 16)
        self.card_layout.setSpacing(16)
        
    def setWidget(self,widget):
        self.card_layout.addWidget(widget)