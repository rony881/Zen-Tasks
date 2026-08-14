from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (
    QComboBox,
    QDialog,
    QGraphicsDropShadowEffect,
    QHBoxLayout,
    QLabel,
    QLayout,
    QPushButton,
    QVBoxLayout,
    QWidget
)
from qfluentwidgets import AMTimePicker, StrongBodyLabel, TextEdit
from core.models.task import Task
from ui.theme import CANCEL_BTN_STYLE, CLOSE_BTN_STYLE, SUBMIT_BTN_STYLE, DIALOG_CARD_STYLE


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
        self.add(self.header)

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
        shadow.setColor(QColor(0, 0, 0, 60))
        self.container.setGraphicsEffect(shadow)
    
    def setDialogTitle(self, title: str):
        """Set Dialog Window Title"""
        self.title.setText(title)

    def setDialogSize(self, width: int= 600, height: int= 300):
        """Set Dialog Window size"""
        self.resize(width, height)

    def add(self, item) -> None:
        """Add a widget or layout to the dialog."""
        if isinstance(item, QWidget):
            self.container_layout.addWidget(item)
        elif isinstance(item, QLayout):
            self.container_layout.addLayout(item)
        else:
            raise TypeError(
                f"Expected QWidget or QLayout, got {type(item).__name__}"
            )
        
    def makeContainer(self, object_name: str, stylesheet) -> QWidget:
        """Make a Contaner Widget."""
        container = QWidget(self)
        container.setObjectName(object_name)
        container.setStyleSheet(stylesheet)
        return container
        
    def makeVLayout(self, widget: QWidget) -> QVBoxLayout:
        """Make a Verticle Layout."""
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(24, 5, 24, 18)
        layout.setSpacing(0)
        return layout

    def makeLabel(self, text: str) -> QLabel:
        title = StrongBodyLabel(text)
        title.setObjectName("title")
        return title

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

    def makeTextArea(self, placeholderText: str, fixedHeight: int, stylesheet) -> TextEdit:
        text_area = TextEdit(self)
        text_area.setPlaceholderText(placeholderText)
        text_area.setFixedHeight(fixedHeight)
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

    def makeTimePicker(self) -> AMTimePicker:
        time_picker = AMTimePicker(self)
        return time_picker

    def makeFooter(
        self,
        *widgets: QPushButton | QComboBox | AMTimePicker,
        submitBtnText: str
    ) -> QHBoxLayout:
        footer = QHBoxLayout()
        footer.setSpacing(8)
        footer.setContentsMargins(0, 12, 0, 0)
    
        for widget in widgets:
            footer.addWidget(widget)
        footer.addStretch()
    
        self.submit_btn = self.makeActionButton(submitBtnText, 40, SUBMIT_BTN_STYLE)
        self.cancel_btn = self.makeActionButton("Cancel", 40, CANCEL_BTN_STYLE)
    
        self.submit_btn.clicked.connect(self.onSubmit)
        self.cancel_btn.clicked.connect(self.onCancel)
    
        footer.addWidget(self.cancel_btn)
        footer.addWidget(self.submit_btn)
    
        return footer

    def get_data(self) -> Task | dict:
        """Override this Method to Get the Dialogs Data """
        ...

    def onSubmit(self) -> None:
        """Override this method for Submit button Action"""
        ...

    def onCancel(self) -> None:
        """Override this method for Cancel button Action"""
        self.reject()
