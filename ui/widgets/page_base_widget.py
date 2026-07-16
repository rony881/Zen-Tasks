from PyQt6.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QWidget
from qfluentwidgets import FluentIcon, PrimaryPushButton, TitleLabel
from ui.theme import ADD_BTN_STYLE, TITLE_STYLE
from ui.widgets.add_task_dialog import AddTaskDialog


class PageBaseWidget(QWidget):
    """Page Base Widget for making Pages"""

    def __init__(self,parent):
        super().__init__(parent)
        self.page_layout = QVBoxLayout(self)
        self.page_layout.setContentsMargins(24, 1, 24, 24)

    def setPageType(self,type):
        self.page_type = type
        
    def setPageHeader(self,header: str, button: str | None = None): 
        h_lout = QHBoxLayout(self)
        h = TitleLabel(self,header)
        h.setStyleSheet(TITLE_STYLE)
        h_lout.addWidget(h)
        h_lout.addStretch(1)
        if button is not None:
            self.add_btn = PrimaryPushButton(FluentIcon.ADD,"    " + button)
            self.add_btn.setStyleSheet(ADD_BTN_STYLE)
            self.add_btn.clicked.connect(self.showInputDialog)
            h_lout.addWidget(self.add_btn)
            
        self.page_layout.addLayout(h_lout)
        
    def AddWidget(self,widget):
        self.page_layout.addWidget(widget)

    def showInputDialog(self):
        match self.page_type:
            case "weekly":
                dialog = AddTaskDialog(self)
                return dialog
            case "today":
                dialog = AddTaskDialog(self)
                return dialog
            case "sleep tracker":
                dialog = AddTaskDialog(self)
                return dialog 