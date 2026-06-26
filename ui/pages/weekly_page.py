from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHeaderView,
    QTableWidgetItem,
    QAbstractItemView,
    QTabWidget,
)
from PyQt6.QtGui import QColor, QFont
from PyQt6.QtCore import Qt

from core.data_loader import load_schedule
from ui.widgets.title_bar import TitleBar
from qfluentwidgets import TableWidget

DAYS = ["Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"]


class WeeklyPage(QWidget):

    def __init__(self, parent: "QWidget|None") -> None:
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self._schedule = load_schedule()
        self.title_bar = TitleBar(self,"📅 Weekly Schedule")

        layout.addWidget(self.title_bar)
        layout.addWidget(self._build_tab_widget())

    def _build_tab_widget(self) -> QTabWidget:
        self.tab_widget = QTabWidget(self)
        self.tab_widget.setDocumentMode(True)
        self.tab_widget.setStyleSheet("""
            QTabWidget::pane {
                border          : none;
                background      : transparent;
            }

            QTabBar {
                background      : transparent;
            }

            QTabBar::tab {
                background      : transparent;
                color           : #6B6B69;
                border          : 1px solid transparent;
                border-radius   : 6px;
                font-size       : 12.5px;
                font-family     : 'Segoe UI', sans-serif;
                padding         : 4px 14px;
                margin          : 8px 2px;
                min-height      : 30px;
            }

            QTabBar::tab:hover {
                background      : #F0EFED;
                color           : #1C1C1C;
            }

            QTabBar::tab:selected {
                background      : #E8F3FE;
                color           : #2383E2;
                border          : 1px solid #B4D1F8;
                font-weight     : 600;
            }
        """)

        for day, entries in self._schedule.items():
            table = PlannerTable(self.tab_widget)
            table.load_data(entries)
            self.tab_widget.addTab(table, day)

        return self.tab_widget

    def select_day(self, day: str) -> None:
        """ switch to the given day tab."""
        if day in DAYS:
            self.tab_widget.setCurrentIndex(DAYS.index(day))

class PlannerTable(TableWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_columns()

    def _setup_columns(self):
        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(["Time", "Task", "Priority"])

        hdr = self.horizontalHeader()
        hdr.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        hdr.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        hdr.setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)

        self.setColumnWidth(0, 110)
        self.setColumnWidth(2, 150)

        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.setShowGrid(True)
        self.setAlternatingRowColors(False)
        self.setEditTriggers(
            QAbstractItemView.EditTrigger.DoubleClicked
            | QAbstractItemView.EditTrigger.SelectedClicked
        )
        self.viewport().setMouseTracking(False)

    def add_task(self, time: str, task: str, shift: str) -> int:
        row = self.rowCount()
        self.insertRow(row)

        body_font = QFont("Segoe UI", 13)

        # Column 0 – Time
        time_column = QTableWidgetItem(time)
        time_column.setFont(body_font)
        time_column.setTextAlignment(
            Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft
        )
        self.setItem(row, 0, time_column)

        # Column 1 – Task
        task_column = QTableWidgetItem(task)
        task_column.setFont(body_font)
        task_column.setTextAlignment(
            Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft
        )
        self.setItem(row, 1, task_column)

        # Column 2 – Priority / Shift
        shift_column = QTableWidgetItem(shift)
        shift_column.setFont(body_font)
        shift_column.setForeground(QColor("#ca2851"))
        shift_column.setTextAlignment(
            Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft
        )
        self.setItem(row, 2, shift_column)

        self.setRowHeight(row, 46)
        return row

    def load_data(self, entries: list[list]) -> None:
        self.setRowCount(0)
        for time, task, priority in entries:
            self.add_task(time, task, priority)