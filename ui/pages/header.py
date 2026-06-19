from PyQt6.QtWidgets import (
 QWidget, QLabel, QVBoxLayout,
)
from PyQt6.QtCore import Qt

class Page_Header(QWidget):
    def __init__(self,h1:str, h2:str = None):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setStyleSheet(
            """
                background: #111111;
            """
            )

        if h1:
            self.title = QLabel(f" {h1}")
            self.title.setContentsMargins(4,4,0,4)
            self.title.setStyleSheet(
                """
                background: #111111;
                border-top-left-radius: 5px;
                border-top-right-radius: 5px;
                font-size: 22px;
                font-weight: bold;
                """
            )
            layout.addWidget(self.title)

        if h2:
            subtitle = QLabel(f" {h2}")
            subtitle.setStyleSheet("color: gray;")
            layout.addWidget(subtitle)


