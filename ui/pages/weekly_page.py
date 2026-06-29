from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (
    QHeaderView,
    QPushButton,
    QTableWidgetItem,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)
from qfluentwidgets import TableWidget

from core.data_loader import load_schedule
from ui.theme import ADD_BTN_STYLE, TAB_WIDG_STYLE
from ui.widgets.title_bar import TitleBar
from ui.widgets.add_task_dialog import AddTaskDialog

DAYS = ["Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"]
TIME_COL = 0
TASK_COL = 1
PRIORITY_COL = 2

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
        self.tab_widget.setStyleSheet(TAB_WIDG_STYLE)

        for day, entries in self._schedule.items():
            table = PlannerTable(self.tab_widget)
            table.load_data(entries)
            self.tab_widget.addTab(table, day)

        return self.tab_widget

    def show_add_task_dialog(self):
        dialog = AddTaskDialog(self,self.tab_widget.currentIndex())
        dialog.task_created.connect(self._on_task_created)
        dialog.exec()
    
    def _on_task_created(self, day_index: str, time: str, task: str, priority: str):
        planner_table: PlannerTable = self.tab_widget.widget(day_index)
        planner_table.add_task(time, task, priority)
        self.tab_widget.setCurrentIndex(day_index)
        
    def select_day(self, day: str) -> None:
        if day in DAYS:
            self.tab_widget.setCurrentIndex(DAYS.index(day))

class PlannerTable(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)

        self.table = self.create_table()
        layout.addWidget(self.table)

    def create_table(self):
        table = TableWidget(self)

        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["Time", "Task", "Priority"])

        hdr = table.horizontalHeader()
        hdr.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        hdr.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        hdr.setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)

        table.setColumnWidth(0, 130)
        table.setColumnWidth(2, 150)
        table.setMouseTracking(False)
        table.setShowGrid(True)

        return table

    def add_task(self, time: str, task: str, shift: str) -> int:
        row = self.table.rowCount()
        self.table.insertRow(row)

        time_column = QTableWidgetItem(time)
        self.table.setItem(row, TIME_COL, time_column)

        task_column = QTableWidgetItem(task)
        self.table.setItem(row, TASK_COL, task_column)

        shift_column = QTableWidgetItem(shift)
        shift_column.setForeground(QColor("#ca2851"))
        self.table.setItem(row, PRIORITY_COL, shift_column)

        self.table.setRowHeight(row, 46)
        return row

    def load_data(self, entries: list[list]) -> None:
        self.table.setRowCount(0)
        for time, task, priority in entries:
            self.add_task(time, task, priority)

    def create_btn(self):
        add_button = QPushButton("+ Add Task")
        add_button.setFixedHeight(60)
        add_button.setStyleSheet(ADD_BTN_STYLE)

        return add_button