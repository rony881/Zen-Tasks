from PyQt6.QtWidgets import (
 QWidget, QLabel, QVBoxLayout,
)
from PyQt6.QtCore import Qt

class Page_Header(QWidget):
    def __init__(self,h1:str, h2:str = None):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(4, 0, 0, 0)

        if h1:
            self.title = QLabel(h1)
            self.title.setStyleSheet(
                """
                font-size: 22px;
                font-weight: bold;
                """
            )
            layout.addWidget(self.title)

        if h2:
            subtitle = QLabel(h2)
            subtitle.setStyleSheet("color: gray;")
            layout.addWidget(subtitle)


