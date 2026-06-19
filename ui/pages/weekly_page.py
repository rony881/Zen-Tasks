from PyQt6.QtWidgets import (
    QLabel,
    QPushButton,
    QWidget,
    QFrame,
    QHBoxLayout,
    QVBoxLayout,
    QTabWidget,
)
from PyQt6.QtCore import Qt
from .header import Page_Header
from ui.widgets.card import TaskCard

days = ["SAT", "SUN", "MON", "TUE", "WED", "THU", "FRI"]
tasks = ["Reading\nbooks", "Sleep", "Exercise\n30 min", "Art", "Streching", "Exploring", "Study"]


class TaskColumn(QFrame):
    def __init__(self, title, tasks):
        super().__init__()

        self.setFrameShape(QFrame.Shape.Box)
        self.setStyleSheet("border: none;" \
        "background: #1a1a1a;")

        layout = QVBoxLayout(self)

        # Column Header
        header = QLabel(title)
        header.setAlignment(Qt.AlignmentFlag.AlignLeft)
        header.setStyleSheet(
            """
            font-size: 14px;
            font-weight: bold;
            padding: 6px;
            border-bottom: 1px solid #f77e0d;
            """
        )

        layout.addWidget(header)

        # Tasks
        for task in tasks:
            layout.addWidget(task)

        add_btn = QPushButton("+ New")
        add_btn.setStyleSheet(
            """
            QPushButton{background-color: transparent;
            border: 1px solid #282723;
            font-size:18px;
            color: gray;
            border-radius: 6px;}

            QPushButton::hover{background-color: #111111;}
            """
               )
        layout.addWidget(add_btn)

        layout.addStretch()


class DayPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout(self)

        morning_tasks = [TaskCard(task) for task in tasks]
        day_tasks = [TaskCard(task) for task in tasks]
        night_tasks = [TaskCard(task) for task in tasks]

        layout.addWidget(TaskColumn("Morning", morning_tasks),1)
        layout.addWidget(TaskColumn("Day", day_tasks),1)
        layout.addWidget(TaskColumn("Night", night_tasks),1)


class Weekly_Tab(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background: #111111;")

        title = Page_Header("Weekly Schedule","Build Habits, Build Tommorow")
        main_layout = QVBoxLayout(self)                                
        main_layout.setSpacing(0)
        main_layout.addWidget(title)

        tabs = QTabWidget()
        tabs.setDocumentMode(True)
        tabs.setStyleSheet(
            """
            QTabWidget{
            background: #1a1a1a;
            }
            QTabBar{
                background: #111111;
                border: none;
            }
            QTabBar::tab {
                font-size: 12px;
                padding: 6px 18px;
                background: transparent;
            }
            QTabBar::tab:selected {
                color: white;
                border-bottom: 2px solid #f77e0d;
            }
            """
        )

        for day in days:
            tabs.addTab(DayPage(), day)

        main_layout.addWidget(tabs)
