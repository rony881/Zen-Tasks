from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QComboBox,
    QLayout,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from qfluentwidgets import (
    AMTimePicker,
    MessageBoxBase,
    StrongBodyLabel,
    SubtitleLabel,
    TextEdit,
)
from core.models.task import Task


class DialogBaseWidget(MessageBoxBase):
    """Base Widget For Making Dialogs for the Application."""

    def __init__(self, parent: QWidget | None):
        """Initialize the Dialog."""
        super().__init__(parent)

        self._titleLabel = SubtitleLabel()
        self._titleLabel.setStyleSheet("color:#666666;font-size:17px;")
        self.viewLayout.addWidget(self._titleLabel)
        self.viewLayout.addSpacing(4)
        
        self._setup_ui()
        
    def _setup_ui(self):
        """
        Override this method to setup the UI for the Dialog.
        """
        ...

    def setDialogTitle(self, title: str):
        """Set Dialog Window Title"""
        self._titleLabel.setText(title)

    def setSubmitButtonText(self, text: str, object_name: str | None = None, stylesheet: str | None = None):
        """
        Set the text and optionally the object name of the submit button.
        submit button is a QPushButton.
        """
        self.yesButton.setText(text)
        if object_name:
            self.yesButton.setObjectName(object_name)
        if stylesheet:
            self.yesButton.setStyleSheet(stylesheet)

    def setCancelButtonText(self, text: str, object_name: str | None = None, stylesheet: str | None = None):
        """
        Set the text and optionally the object name of the cancel button.
        cancel button is a QPushButton.
        """
        self.cancelButton.setText(text)
        if object_name:
            self.cancelButton.setObjectName(object_name)
        if stylesheet:
            self.cancelButton.setStyleSheet(stylesheet)

    def validate(self) -> bool:
        """
        Override this method to validate the dialog's data.
        Returns True if the data is valid, False otherwise.
        """
        raise NotImplementedError

    def add(self, item) -> None:
        """Add a widget or layout to the dialog."""
        if isinstance(item, QWidget):
            self.viewLayout.addWidget(item)
        elif isinstance(item, QLayout):
            self.viewLayout.addLayout(item)
        else:
            raise TypeError(
                f"Expected QWidget or QLayout, got {type(item).__name__}"
            )
        
    def makeVLayout(self, widget: QWidget) -> QVBoxLayout:
        """Make a vertical layout."""
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(24, 5, 24, 18)
        layout.setSpacing(0)
        return layout

    def makeLabel(self, text: str) -> StrongBodyLabel:
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

    def makeComboBox(self,
        items: list[str],
        object_name: str,
        stylesheet,
        placeholder: str | None = None
    ) -> QComboBox:
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

    def get_data(self) -> Task | dict:
        """Override this Method to Get the Dialogs Data """
        raise NotImplementedError
