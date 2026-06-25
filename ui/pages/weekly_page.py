from PyQt6.QtWidgets import (
    QStackedWidget,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QHeaderView,
    QTableWidgetItem,
    QFrame,
    QAbstractItemView,
    QPushButton
)
from PyQt6.QtGui import QColor,QFont
from PyQt6.QtCore import Qt

from core.data_loader import load_schedule
from ui.widgets.title_bar import TitleBar
from qfluentwidgets import TableWidget

DAYS = ["Sat","Sun","Mon", "Tue", "Wed", "Thu", "Fri"]

class WeeklyPlanner(QWidget):

    def __init__(self, parent: 'QWidget|None') -> None:
        super().__init__(parent)
        self._current_day = "Mon"
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self._schedule = load_schedule()
        self.title_bar = TitleBar(self)
        self.day_buttons = {}
        
        layout.addWidget(self.title_bar)
        layout.addWidget(self._make_day_bar())
        layout.addWidget(self._weekly_table())

    def _weekly_table(self) -> QStackedWidget:
        self.week_tabs = QStackedWidget(self)
        for day, entries in self._schedule.items():
            table = PlannerTable(self.week_tabs)
            table.load_data(entries)
            self.week_tabs.addWidget(table)
        return self.week_tabs

    def _make_day_bar(self) -> QFrame:
        frame = QFrame()
        frame.setFixedHeight(48)
 
        h = QHBoxLayout(frame)
        h.setContentsMargins(16, 8, 16, 8)
        h.setSpacing(4)

        for day in DAYS:
            btn = QPushButton(day)
            btn.setFixedHeight(30)
            btn.setCheckable(True)
            btn.setStyleSheet("""
            QPushButton {
                background    : transparent;
                color         : #6B6B69;
                border        : 1px solid transparent;
                border-radius : 6px;
                font-size     : 12.5px;
                font-family   : 'Segoe UI', sans-serif;
                padding       : 0 14px;
            }
            QPushButton:hover {
                    background : #F0EFED;
                    color      : #1C1C1C;
            }
            QPushButton:checked {
                background    : #E8F3FE;
                color         : #2383E2;
                border        : 1px solid #B4D1F8;
                border-radius : 6px;
                font-weight   : 600;
                font-size     : 12.5px;
                font-family   : 'Segoe UI', sans-serif;
                padding       : 0 14px;
            }
            """)
            self.day_buttons[day] = btn
            btn.clicked.connect(
                lambda checked, d=day:
                self.select_day(d)
            )
            h.addWidget(btn)
        h.addStretch()
        
        return frame
    def select_day(self, day):
        self.week_tabs.setCurrentIndex(DAYS.index(day))
        for d, btn in self.day_buttons.items():
            btn.setChecked(d == day)
            
class PlannerTable(TableWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_columns()

    def _setup_columns(self):

        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(["Time","Task","Priority"])

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
        

    def add_task(self,time: str, task: str, shift: str) -> int:
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

    def load_data(self, entries: list[list]) -> None:
        self.setRowCount(0)
        for time, task, priority in entries:
            self.add_task(time, task, priority)