from PyQt6.QtWidgets import (
    QHBoxLayout,
    QLabel,
)
from qfluentwidgets import CardWidget, CheckBox, TransparentToolButton, FluentIcon as FI
from qfluentwidgets.components.date_time.calendar_view import QVBoxLayout


class TaskCard(CardWidget):
    def __init__(self, time:str, task:str, prio:str):
        super().__init__()
        self.setFixedHeight(56)
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
        layout.addWidget(self.checkbox)

        time_lbl = QLabel(time)
        time_lbl.setStyleSheet("color: #333333")
        layout.addWidget(time_lbl)

        task_lbl = QLabel(task)
        task_lbl.setStyleSheet("color: #333333")
        layout.addWidget(task_lbl)
        layout.addStretch()
        
        prio_lbl = QLabel(prio)
        prio_lbl.setStyleSheet("border:1px solid #4dabf7;color: #4dabf7;border-radius: 6px;")
        layout.addWidget(prio_lbl)

        edit_btn = TransparentToolButton(FI.EDIT)
        layout.addWidget(edit_btn)
        
        delete_btn = TransparentToolButton(FI.DELETE)
        layout.addWidget(delete_btn)

class SimpleCard(CardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.card_layout = QVBoxLayout(self)
        self.card_layout.setContentsMargins(20, 16, 20, 16)
        self.card_layout.setSpacing(16)
        
    def setWidget(self,widget):
        self.card_layout.addWidget(widget)