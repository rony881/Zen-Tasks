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
from PyQt6.QtCore import pyqtSignal,Qt
from PyQt6.QtGui import QColor
from qfluentwidgets import AMTimePicker

class AddTaskDialog(QDialog):
    task_created = pyqtSignal(int, str, str, str)
    
    def __init__(self, parent=None,day_index=None):
        super().__init__(parent)
        self.day_index = day_index
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
        self.task_disc.setPlaceholderText("Write here...")
        self.task_disc.setFixedHeight(110)
        self.task_disc.setStyleSheet("""
            QTextEdit {
                border: none;
                border-radius: 6px;
                font-size: 17px;
                color: #444444;
                background: transparent;
            }
        """)
        footer = QHBoxLayout()
        footer.setSpacing(8)
        footer.setContentsMargins(0, 12, 0, 0)

        self.time = AMTimePicker()
        footer.addWidget(self.time)

        self.priority = QComboBox(self)
        self.priority.addItems(["Low","Medium","High"])
        self.priority.setObjectName("priority")
        self.priority.setStyleSheet("""
        QComboBox#priority {
            color: #6B6B69;
            background: transparent;
            border: 1px solid #cccccc;
            border-bottom: 1px solid #cdcdcd;
            border-top: 1px solid #cccccc;
            border-radius: 6px;
            padding: 4px 10px;
            min-width: 100px;
        }
        
        QComboBox#priority QAbstractItemView {
            background: white;
            border: 1px solid #777777;
            border-radius: 6px;
            outline: none;
        }
        
        QComboBox#priority QAbstractItemView::item {
            color: #6B6B69;
            padding: 6px 10px;
            min-height: 24px;
        }
        
        QComboBox#priority QAbstractItemView::item:selected {
            background: #2383E2;
            color: white;
        }
        
        QComboBox#priority QAbstractItemView::item:hover {
            background: #1A73CE;
            color: #ffffff;
        }
        """)
        self.priority.setCurrentIndex(-1)
        self.priority.setPlaceholderText("Priority")
        footer.addWidget(self.priority)
        
        create_btn = QPushButton("Create Task")
        create_btn.setFixedHeight(40)
        create_btn.setCursor(Qt.CursorShape.PointingHandCursor)

        create_btn.clicked.connect(self._on_create)
        create_btn.setStyleSheet("""
            QPushButton {
                background: #1A73CE;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 0 24px;
                font-size: 14px;
                font-weight: 700;
            }
            QPushButton:hover   { background: #2383E2; }
            QPushButton:pressed { background: #1260B5; }
        """)
        footer.addStretch()
        footer.addWidget(create_btn)
        
        card_layout.addLayout(header)
        card_layout.addWidget(self.task_disc)
        card_layout.addLayout(footer)

        outer.addWidget(self.card)

        
    def _on_create(self):
        task = self.task_disc.toPlainText().strip()
        time = self.time.getTime().toString("hh:mm AP")
        prio = self.priority.currentText()
    
        if not task or not prio:
            return
    
        self.task_created.emit(self.day_index, time, task, prio)
        self.accept()
        
    def _add_shadow(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(48)
        shadow.setXOffset(0)
        shadow.setYOffset(10)
        shadow.setColor(QColor(0, 0, 0, 45))
        self.card.setGraphicsEffect(shadow)