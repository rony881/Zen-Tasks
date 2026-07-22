from PyQt6.QtWidgets import (QDialog,
    QVBoxLayout,
    QComboBox,
    QGraphicsDropShadowEffect,
    QHBoxLayout,
    QPushButton,
    QTextEdit,
    QWidget,
    QLabel
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from qfluentwidgets import AMTimePicker, InfoBar, InfoBarPosition
from config import INFO_BAR_DURATION_SHORT, PRIORITIES,UI_CONFIG
from core.models.task import Task
from ui.theme import CLOSE_BTN_STYLE, CREATE_TASK_BTN_STYLE, DIALOG_CARD_STYLE, PRIORITY_STYLE, TASK_INPUT_STYLE
DIALOG_WIDTH = UI_CONFIG["dialog_width"]
DIALOG_HEIGHT = UI_CONFIG["dialog_height"]

class AddTaskDialog(QDialog):
    """Dialog for creating new tasks with time, description, and priority."""
    
    def __init__(
        self,
        parent: QWidget | None = None
    ) -> None:
        
        """Initialize add task dialog."""
        super().__init__(parent)
        self.setWindowTitle("Add Task")
        self.resize(DIALOG_WIDTH,DIALOG_HEIGHT)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.Dialog)

        self._setup_ui()
        self._add_shadow()
        
    def _setup_ui(self):
        """Set up the dialog UI components."""
        outer = QVBoxLayout(self)
        outer.setContentsMargins(24, 24, 24, 24)

        self.card = QWidget()
        self.card.setObjectName("card")
        self.card.setStyleSheet(DIALOG_CARD_STYLE)
        card_layout = QVBoxLayout(self.card)
        card_layout.setContentsMargins(24, 5, 24, 18)
        card_layout.setSpacing(0)

        header = QHBoxLayout()
        header.setContentsMargins(0,0,0,0)

        title = QLabel("Create Task")
        title.setStyleSheet("color:#666666;font-size:17px;")
        header.addWidget(title)

        close_btn = QPushButton("✕")
        close_btn.setFixedSize(28, 28)
        close_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        close_btn.clicked.connect(self.reject)
        close_btn.setStyleSheet(CLOSE_BTN_STYLE)
        
        header.addStretch()
        header.addWidget(close_btn)

        self.task_input = QTextEdit()
        self.task_input.setPlaceholderText("Write here...")
        self.task_input.setFixedHeight(110)
        self.task_input.setStyleSheet(TASK_INPUT_STYLE)
        footer = QHBoxLayout()
        footer.setSpacing(8)
        footer.setContentsMargins(0, 12, 0, 0)

        self.time = AMTimePicker()
        footer.addWidget(self.time)

        self.priority = QComboBox(self)
        self.priority.addItems(PRIORITIES)
        self.priority.setObjectName("priority")
        self.priority.setStyleSheet(PRIORITY_STYLE)
        self.priority.setCurrentIndex(-1)
        self.priority.setPlaceholderText("Priority")
        footer.addWidget(self.priority)
        
        create_btn = QPushButton("Create Task")
        create_btn.setFixedHeight(40)
        create_btn.setCursor(Qt.CursorShape.PointingHandCursor)

        create_btn.clicked.connect(self._accept)
        create_btn.setStyleSheet(CREATE_TASK_BTN_STYLE)
        footer.addStretch()
        footer.addWidget(create_btn)
        
        card_layout.addLayout(header)
        card_layout.addWidget(self.task_input)
        card_layout.addLayout(footer)

        outer.addWidget(self.card)

    def _add_shadow(self):
        """Add drop shadow effect to the dialog card."""
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(48)
        shadow.setXOffset(0)
        shadow.setYOffset(10)
        shadow.setColor(QColor(0, 0, 0, 45))
        self.card.setGraphicsEffect(shadow)
        
    def get_data(self) -> Task:
        """Return The Task Data"""
        task = self.task_input.toPlainText().strip()
        time = self.time.getTime().toString("hh:mm AP")
        prio = (self.priority.currentText())

        return Task(
            time = time,
            task = task,
            priority = prio,
            done = False,
        )
        
    def _accept(self):
        task = self.task_input.toPlainText().strip()
        priority = self.priority.currentText()
    
        if not task or not priority:
            InfoBar.error(
                title="Task not added",
                content="Task and Priority cannot be empty",
                duration=INFO_BAR_DURATION_SHORT,
                position=InfoBarPosition.TOP,
                parent=self,
            )
            return
    
        self.accept()
        