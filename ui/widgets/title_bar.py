from PyQt6.QtWidgets import QFrame,QHBoxLayout,QPushButton

from qfluentwidgets import TitleLabel
from ui.widgets.add_task_dialog import AddTaskDialog
from ui.theme import ADD_BTN_STYLE

class TitleBar(QFrame):
    def __init__(self,parent, h1: str):
        super().__init__(parent)
        self.parent = parent
        layout = QHBoxLayout(self)

        title = TitleLabel(h1)
        layout.addWidget(title)
        layout.addStretch()

        add_btn = QPushButton("+ Add Task")
        add_btn.setStyleSheet(ADD_BTN_STYLE)
        add_btn.clicked.connect(self.dummy)
        layout.addWidget(add_btn)
        
    def dummy(self):
        self.dialog = AddTaskDialog(self.parent)
        self.dialog.show()
        