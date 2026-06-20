from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QFrame, QGridLayout, QInputDialog
)
from PyQt6.QtCore import Qt

from ui.widgets.card import TaskCard


class DayPage(QWidget):
    def __init__(self, day_name, initial_tasks=None):
        super().__init__()

        self.day_name = day_name
        self.cards = []

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(10)

        # Top bar
        top_bar = QHBoxLayout()

        self.day_label = QLabel(day_name)
        self.day_label.setStyleSheet("""
            font-size: 14px;
            font-weight: bold;
            color: white;
        """)

        self.add_btn = QPushButton("+ Add")
        self.add_btn.setFixedSize(80, 32)
        self.add_btn.clicked.connect(self.add_task_dialog)

        top_bar.addWidget(self.day_label)
        top_bar.addStretch()
        top_bar.addWidget(self.add_btn)
        self.main_layout.addLayout(top_bar)

        # Scroll area
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.container = QWidget()
        self.grid = QGridLayout(self.container)
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setHorizontalSpacing(12)
        self.grid.setVerticalSpacing(12)
        self.grid.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        self.scroll.setWidget(self.container)
        self.main_layout.addWidget(self.scroll)

        if initial_tasks:
            for task_name, task_time in initial_tasks:
                self.add_task(task_name, task_time)

    def add_task_dialog(self):
        task_name, ok1 = QInputDialog.getText(self, "Add Task", "Task name:")
        if not ok1 or not task_name.strip():
            return

        task_time, ok2 = QInputDialog.getText(self, "Add Task", "Time:")
        if not ok2 or not task_time.strip():
            task_time = "10:00"

        self.add_task(task_name.strip(), task_time.strip())

    def add_task(self, task_name, task_time):
        card = TaskCard(task_name, task_time)
        self.cards.append(card)

        row = len(self.cards) // 3
        col = len(self.cards) % 3

        self.grid.addWidget(card, row, col)

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTabWidget
from .header import Page_Header

days = ["SAT", "SUN", "MON", "TUE", "WED", "THU", "FRI"]


class Weekly_Tab(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background: #111111;")

        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)

        title = Page_Header("Weekly Schedule", "Build Habits, Build Tomorrow")
        main_layout.addWidget(title)

        tabs = QTabWidget()
        tabs.setDocumentMode(True)
        tabs.setStyleSheet("""
            QTabWidget {
                background: #1a1a1a;
            }
            QTabBar {
                background: #111111;
                border: none;
            }
            QTabBar::tab {
                font-size: 12px;
                padding: 6px 18px;
                background: transparent;
                color: gray;
            }
            QTabBar::tab:selected {
                color: white;
                border-bottom: 2px solid #f77e0d;
            }
        """)

        sample_tasks = [
            [("Reading books", "9:30"), ("Sleep", "10:30")],
            [("Exercise 30 min", "8:00")],
            [("Study", "7:00"), ("Art", "5:00"), ("Exploring", "6:00")]
        ]

        for i, day in enumerate(days):
            initial = sample_tasks[i % len(sample_tasks)]
            tabs.addTab(DayPage(day, initial), day)

        main_layout.addWidget(tabs)
