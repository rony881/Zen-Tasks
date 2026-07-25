from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QHBoxLayout, QLabel, QPushButton, QTextEdit, QVBoxLayout, QWidget

from ui.theme import CLOSE_BTN_STYLE, DIALOG_CARD_STYLE


class DialogBaseWidget(QDialog):
    """Base Widget For Making Dialogs for the Application."""

    def __init__(self, parent: QWidget | None):
        super().__init__(parent)
        """Initialize the Dialog."""
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.Dialog)
        
        self.outer = QVBoxLayout(self)
        self.outer.setContentsMargins(24, 24, 24, 24)

        self.container = self.makeContainer("container", DIALOG_CARD_STYLE)
        self.container_layout = self.makeVLayout(self.container)

        self.header = QHBoxLayout()
        self.header.setContentsMargins(0,0,0,0)
        self.addLayout(self.header)

        self.title = QLabel()
        self.title.setStyleSheet("color:#666666;font-size:17px;")
        self.header.addWidget(self.title)

        self.close_btn = self.makeButton("✕", 28, 28, CLOSE_BTN_STYLE)
        self.header.addWidget(self.close_btn)
        
        
    def _setup_ui(self):
        ...

    def setDialogTitle(self, title: str):
        """Set Dialog Window Title"""
        self.setWindowTitle(title)

    def setDialogSize(self, width: int= 600, height: int= 300):
        """Set Dialog Window size"""
        self.resize(width, height)

    def makeContainer(self, object_name: str, stylesheet):
        container = QWidget()
        container.setObjectName(object_name)
        container.setStyleSheet(stylesheet)
        return container
        
    def makeVLayout(self, widget: QWidget):
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(24, 5, 24, 18)
        layout.setSpacing(0)
        return layout

    def addLayout(self, layout: QVBoxLayout | QHBoxLayout) -> None:
        """Add a Layout to Dialog."""
        self.container_layout.addLayout(layout)
    
    def makeButton(
        self,
        text: str,
        w: int,
        h: int,
        stylesheet
    ) -> QPushButton:
        button = QPushButton(text)
        button.setFixedSize(w,h)
        button.setCursor(Qt.CursorShape.PointingHandCursor)
        button.setStyleSheet(stylesheet)

        return button

    def makeTextArea(self, placeholderText: str, height: int, stylesheet):
        text_area = QTextEdit()
        text_area.setPlaceholderText(placeholderText)
        text_area.setFixedHeight(height)
        text_area.setStyleSheet(stylesheet)
        