from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QComboBox, QDialog, QGraphicsDropShadowEffect, QHBoxLayout, QLabel, QPushButton, QTextEdit, QVBoxLayout, QWidget

from ui.theme import CLOSE_BTN_STYLE, DIALOG_CARD_STYLE


class DialogBaseWidget(QDialog):
    """Base Widget For Making Dialogs for the Application."""

    def __init__(self, parent: QWidget | None):
        """Initialize the Dialog."""
        super().__init__(parent)
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
        self.header.addStretch()

        self.close_btn = self.makeIconButton("✕", 28, CLOSE_BTN_STYLE)
        self.close_btn.clicked.connect(self.reject)
        self.header.addWidget(self.close_btn)

        self.outer.addWidget(self.container)

        self._setup_ui()
        self._add_shadow()
        
        
    def _setup_ui(self):
        """Override in subclasses to build the body + footer."""
        ...

    def _add_shadow(self):
        """Add drop shadow effect to the Dialog."""
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(48)
        shadow.setXOffset(0)
        shadow.setYOffset(10)
        shadow.setColor(QColor(0, 0, 0, 45))
        self.container.setGraphicsEffect(shadow)
    
    def setDialogTitle(self, title: str):
        """Set Dialog Window Title"""
        self.title.setText(title)

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

    def addWidget(self, widget: QWidget) -> None:
        """Add a widget directly to the dialog body."""
        self.container_layout.addWidget(widget)
    
    def makeIconButton(self, text: str, size: int, stylesheet) -> QPushButton:
        """Square icon-style button, e.g. the close (✕) button."""
        button = QPushButton(text)
        button.setFixedSize(size, size)
        button.setCursor(Qt.CursorShape.PointingHandCursor)
        button.setStyleSheet(stylesheet)
        return button
    
    def makeActionButton(self, text: str, height: int, stylesheet) -> QPushButton:
        """Text action button, e.g. 'Create Task' / 'Save Changes'."""
        button = QPushButton(text)
        button.setFixedHeight(height)
        button.setCursor(Qt.CursorShape.PointingHandCursor)
        button.setStyleSheet(stylesheet)
        return button

    def makeTextArea(self, placeholderText: str, height: int, stylesheet):
        text_area = QTextEdit()
        text_area.setPlaceholderText(placeholderText)
        text_area.setFixedHeight(height)
        text_area.setStyleSheet(stylesheet)
        return text_area

    def makeComboBox(self, items: list[str], object_name: str, stylesheet, placeholder: str | None = None) -> QComboBox:
        combo = QComboBox(self)
        combo.addItems(items)
        combo.setObjectName(object_name)
        combo.setStyleSheet(stylesheet)
        if placeholder:
            combo.setCurrentIndex(-1)
            combo.setPlaceholderText(placeholder)
        return combo

    def makeFooter(self) -> QHBoxLayout:
        footer = QHBoxLayout()
        footer.setSpacing(8)
        footer.setContentsMargins(0, 12, 0, 0)
        return footer
        