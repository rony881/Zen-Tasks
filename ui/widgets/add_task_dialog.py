from PyQt6.QtWidgets import QDialog, QVBoxLayout,QComboBox,QGraphicsDropShadowEffect,QHBoxLayout,QPushButton,QTextEdit,QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor

class AddTaskDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Task")
        self.resize(600,300)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.Dialog)
        
        self._setup_ui()
        self._add_shadow()
        
    def _setup_ui(self):
        outer = QVBoxLayout(self)
        outer.setContentsMargins(24, 24, 24, 24)

        self.card = QWidget()
        self.card.setObjectName("card")
        self.card.setStyleSheet("""
            QWidget#card {
                background: #FFFFFF;
                border-radius: 16px;
                border: 1px solid #e8e8e8;
            }
            """)
        card_layout = QVBoxLayout(self.card)
        card_layout.setContentsMargins(24, 18, 24, 18)
        card_layout.setSpacing(0)

        header = QHBoxLayout()
        header.setSpacing(6)

        close_btn = QPushButton("✕")
        close_btn.setFixedSize(28, 28)
        close_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        close_btn.clicked.connect(self.reject)
        close_btn.setStyleSheet("""
            QPushButton {
                border: none; border-radius: 14px;
                color: #888; font-size: 14px; background: transparent;
            }
            QPushButton:hover { background: #F0F0F0; color: #111111; }
        """)
        header.addStretch()
        header.addWidget(close_btn)

        self.task_disc = QTextEdit()
        self.task_disc.setPlaceholderText("Add Description....")
        self.task_disc.setFixedHeight(110)
        self.task_disc.setFrameShape(QTextEdit.Shape.NoFrame)
        self.task_disc.setStyleSheet("""
            QTextEdit {
                border: none;
                font-size: 14px;
                color: #555555;
                background: transparent;
            }
        """)
        footer = QHBoxLayout()
        footer.setSpacing(8)
        footer.setContentsMargins(0, 12, 0, 0)
        footer.addStretch()
        
        create_btn = QPushButton("Create Task")
        create_btn.setFixedHeight(40)
        create_btn.setCursor(Qt.CursorShape.PointingHandCursor)

        create_btn.clicked.connect(self._on_create)
        create_btn.setStyleSheet("""
            QPushButton {
                background: #00a86b;
                color: white;
                border: none;
                border-radius: 20px;
                padding: 0 24px;
                font-size: 14px;
                font-weight: 700;
            }
            QPushButton:hover   { background: #009960; }
            QPushButton:pressed { background: #008855; }
        """)
        footer.addWidget(create_btn)
        
        card_layout.addLayout(header)
        card_layout.addWidget(self.task_disc)
        card_layout.addLayout(footer)

        outer.addWidget(self.card)

        
    def _on_create(self):
        ...

    def _add_shadow(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(48)
        shadow.setXOffset(0)
        shadow.setYOffset(10)
        shadow.setColor(QColor(0, 0, 0, 45))
        self.card.setGraphicsEffect(shadow)