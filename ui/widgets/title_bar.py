from PyQt6.QtWidgets import QFrame,QHBoxLayout
from qfluentwidgets import TitleLabel

class TitleBar(QFrame):
    def __init__(self,parent):
        super().__init__(parent)
        
        layout = QHBoxLayout(self)
        title = TitleLabel("📅 Weekly Schedule")
        layout.addWidget(title)
        layout.addStretch()