from PyQt6.QtWidgets import QFrame,QHBoxLayout,QPushButton
from qfluentwidgets import TitleLabel

class TitleBar(QFrame):
    def __init__(self,parent, h1: str):
        super().__init__(parent)
        layout = QHBoxLayout(self)

        title = TitleLabel(h1)
        layout.addWidget(title)
        layout.addStretch()

        add_btn = QPushButton("+ Add Task")
        add_btn.setStyleSheet(
        """
        QPushButton {
            background    : #2383E2;
            color         : #FFF;
            border        : none;
            border-radius : 6px;
            font-size     : 13px;
            font-weight   : 600;
            font-family   : 'Segoe UI', sans-serif;
            padding       : 7px 20px;
        }
        QPushButton:hover   { background: #1A73CE; }
        QPushButton:pressed { background: #1260B5; }
        """
        )
        layout.addWidget(add_btn)