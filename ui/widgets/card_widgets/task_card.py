from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
)
from qfluentwidgets import CardWidget, CheckBox, TransparentToolButton, FluentIcon as FI
from core.models.task import Task

from config import UI_CONFIG
from ui.widgets.base_widgets.card_base_widget import CardBaseWidget
from .priority_label import PriorityLabel 
HEIGHT = UI_CONFIG["card_height"]

class TaskCard(CardBaseWidget):
    """Card widget displaying a single task with checkbox, edit, and delete buttons."""
    checkbox_changed = pyqtSignal(bool)
    edit_clicked = pyqtSignal(Task)
    delete_clicked = pyqtSignal(Task)
    
    def __init__(self, task: Task):
        """Initialize task card with task data."""
        super().__init__()
        self.task = task

        self.checkbox = CheckBox()
        self.checkbox.setChecked(task.done)
        self.checkbox.toggled.connect(self.on_checked)
        self.main_layout.addWidget(self.checkbox)

        time_lbl = QLabel(task.time)
        time_lbl.setStyleSheet("color: #333333")
        self.main_layout.addWidget(time_lbl)

        self.task_lbl = QLabel(task.task)
        self.task_lbl.setStyleSheet("color: #333333")
        self.main_layout.addWidget(self.task_lbl)
        self.main_layout.addStretch()
        
        prio_lbl = PriorityLabel(task.priority)
        self.main_layout.addWidget(prio_lbl)

        edit_btn = TransparentToolButton(FI.EDIT)
        edit_btn.clicked.connect(lambda: self.edit_clicked.emit(self.task))
        self.main_layout.addWidget(edit_btn)
        
        delete_btn = TransparentToolButton(FI.DELETE)
        delete_btn.clicked.connect(lambda: self.delete_clicked.emit(self.task))
        self.main_layout.addWidget(delete_btn)

    def on_checked(self, checked):
        """Handle checkbox state change."""
        self.task.done = checked
        self.checkbox_changed.emit(checked)

    def createDefaultLayout(self, parent) -> QHBoxLayout:
        return QHBoxLayout(parent)
        
class SimpleCard(CardWidget):
    """Simple card widget for containing other widgets."""
    
    def __init__(self, parent=None):
        """Initialize simple card with vertical layout."""
        super().__init__(parent)
        self.card_layout = QVBoxLayout(self)
        self.card_layout.setContentsMargins(20, 16, 20, 16)
        self.card_layout.setSpacing(16)
        
    def addWidget(self,widget):
        """Set the widget to be contained in this card."""
        self.card_layout.addWidget(widget)