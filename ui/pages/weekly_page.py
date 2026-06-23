from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout,QAbstractItemView,QHeaderView,QTableWidgetItem
)
from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt
from qfluentwidgets import TableWidget,TitleLabel
from qfluentwidgets.components.date_time.picker_base import QFrame
from qframelesswindow.titlebar import QHBoxLayout

DATA: dict[str, list[tuple]] = {
    "Mon": [
        ("9:00 AM",  "Morning Walk",           "Low"),
        ("10:00 AM", "Team Standup",            "High"),
        ("11:00 AM", "Code Review",             "Medium"),
        ("12:30 PM", "Lunch Break",             "Low"),
        ("2:00 PM",  "Feature Development",     "Critical"),
        ("4:00 PM",  "Reply to Emails",         "Medium"),
        ("5:30 PM",  "Gym Session",             "High"),
        ],
    "Tue": [
        ("9:30 AM",  "Project Planning",        "High"),
        ("11:00 AM", "Client Call",             "Critical"),
        ("1:00 PM",  "Lunch",                   "Low"),
        ("3:00 PM",  "UI Design Review",        "Medium"),
        ("5:00 PM",  "Documentation",           "Low"),
        ],
    "Wed": [
        ("9:00 AM",  "Sprint Planning",         "Critical"),
        ("11:00 AM", "Backend Development",     "High"),
        ("1:30 PM",  "Break",                   "Low"),
        ("3:00 PM",  "Testing & QA",            "High"),
        ("4:30 PM",  "Team Sync",               "Medium"),
        ],
    "Thu": [
        ("9:00 AM",  "Weekly Review",           "Medium"),
        ("11:00 AM", "Mentor Session",          "High"),
        ("1:00 PM",  "Lunch Walk",              "Low"),
        ("3:00 PM",  "Reading / Research",      "Low"),
        ],
    "Fri": [
        ("10:00 AM", "Retrospective",           "Medium"),
        ("12:00 PM", "Team Lunch",              "Low"),
        ("3:00 PM",  "Demo Preparation",        "Critical"),
        ("5:00 PM",  "Week Wrap-up",            "Medium"),
        ],
    "Sat": [
        ("10:00 AM", "Personal Projects",       "Medium"),
        ("1:00 PM",  "Grocery Shopping",        "Low"),
        ("4:00 PM",  "Outdoor Activity",        "Low"),
        ],
    "Sun": [
        ("9:00 AM",  "Meal Prep",               "Medium"),
        ("11:00 AM", "Family Time",             "High"),
        ("4:00 PM",  "Next-week Planning",      "High"),
        ],
}


class WeeklyPlanner(QWidget):

    def __init__(self, parent: 'QWidget|None') -> None:
        super().__init__(parent)
        self._current_day = "Mon"
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        layout.addWidget(self._make_title_bar())
        self.table = PlannerTable()
        layout.addWidget(self.table, 1)
        # self._load_data()
        
    def _make_title_bar(self):
        title_bar = QFrame()
        layout = QHBoxLayout(title_bar)
        title = TitleLabel("📅 Weekly Schedule")
        layout.addWidget(title)
        layout.addStretch()

        return title_bar

class PlannerTable(TableWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_columns()

    def _setup_columns(self):

        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(["Time","Task","Shift"])

        hdr = self.horizontalHeader()
        hdr.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        hdr.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        hdr.setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)

        # Column Width
        self.setColumnWidth(0, 110)
        self.setColumnWidth(2, 150)
        self.verticalHeader().setVisible(False)
        self.verticalHeader().setDefaultSectionSize(46)

        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.setShowGrid(True)
        self.setAlternatingRowColors(False)
        self.setEditTriggers(
            QAbstractItemView.EditTrigger.DoubleClicked
            | QAbstractItemView.EditTrigger.SelectedClicked
        )
        self.viewport().setMouseTracking(True)

    def add_task(self,task: str, time: str, shift: str) -> int:
        row = self.rowCount()
        self.insertRow(row)

        body_font = QFont("Segoe UI", 13)

        # Column 0 - Time
        time_column = QTableWidgetItem(time)
        time_column.setFont(body_font)
        # time_item.setForeground(QColor("#6B6B69"))
        time_column.setTextAlignment(
            Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft
        )
        self.setItem(row, 0, time_column)

        # Column 1 - Task
        task_column = QTableWidgetItem(task)
        task_column.setFont(body_font)
        # task_item.setForeground(QColor("#6B6B69"))
        task_column.setTextAlignment(
            Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft
        )
        self.setItem(row, 1, task_column)

        # Column 2 - shift
        shift_column = QTableWidgetItem(shift)
        shift_column.setFont(body_font)
        shift_column.setForeground(QColor("#ca2851"))
        shift_column.setTextAlignment(
            Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft
        )
        self.setItem(row, 2, shift_column)

        self.setRowHeight(row,46)
        return row

    def load_data(self, entries: list[tuple]) -> None:
        self.setRowCount(0)
        for time, task, priority in entries:
            self.add_entry(time, task, priority)
        
        
