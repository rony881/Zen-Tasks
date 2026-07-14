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

from core.data_loader import load_schedule, save_schedule
from ui.theme import ADD_BTN_STYLE, TAB_WIDG_STYLE
from ui.widgets.add_task_dialog import AddTaskDialog
from ui.widgets.title_bar import TitleBar
from config import DAYS, TABLE_ROW_HEIGHT, TIME_COL, TASK_COL, PRIORITY_COL
from core.utils.logger import logger

class WeeklyPage(QWidget):
    """Weekly page showing schedule in tabbed table format."""

    def __init__(self, parent: "QWidget|None") -> None:
        """Initialize weekly page with schedule data."""
        super().__init__(parent)
        logger.info("Weekly Page Initialized Successfully")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 1, 24, 24)
        layout.setSpacing(0)

        self._schedule = load_schedule()
        self.title_bar = TitleBar(self,"Weekly Schedule",btn= "Add Task")

        layout.addWidget(self.title_bar)
        layout.addWidget(self._build_tab_widget())

    def _build_tab_widget(self) -> QTabWidget:
        """Build the tab widget containing schedule tables for each day."""
        self.tab_widget = QTabWidget(self)
        self.tab_widget.setDocumentMode(True)
        self.tab_widget.setStyleSheet(TAB_WIDG_STYLE)

        for day, entries in self._schedule.items():
            table = PlannerTable(self.tab_widget)
            table.load_data(entries)
            self.tab_widget.addTab(table, day)

        return self.tab_widget

    def show_input_dialog(self):
        """Show the add task dialog for the current tab."""
        dialog = AddTaskDialog(self,self.tab_widget.currentIndex())
        dialog.task_created.connect(self._on_task_created)
        dialog.exec()
    
    def _on_task_created(self, day_index: int, time: str, task: str, priority: str):
        """Handle task creation from dialog."""
        planner_table: PlannerTable = self.tab_widget.widget(day_index)
        planner_table.add_task(time, task, priority)
        self.tab_widget.setCurrentIndex(day_index)
        self._save_task()

    def _save_task(self):
        """Save all tasks from all tabs to the schedule file."""
        data = {}
        for i in range(self.tab_widget.count()):
            day = self.tab_widget.tabText(i)
            table: PlannerTable = self.tab_widget.widget(i)
            data[day] = table.get_entries()
        save_schedule(data)
        
    def select_day(self, day: str) -> None:
        """Select the tab for the specified day."""
        if day in DAYS:
            self.tab_widget.setCurrentIndex(DAYS.index(day))

class PlannerTable(QWidget):
    """Table widget for displaying and managing schedule entries."""

    def __init__(self, parent):
        """Initialize planner table with table widget."""
        
        super().__init__(parent)
        layout = QVBoxLayout(self)

        self.table = self.create_table()
        layout.addWidget(self.table)

    def create_table(self):
        """Create and configure the table widget."""
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
        table.setShowGrid(False)

        return table

    def add_task(self, time: str, task: str, shift: str) -> int:
        """Add a task row to the table."""
        
        row = self.table.rowCount()
        self.table.insertRow(row)

        time_column = QTableWidgetItem(time)
        self.table.setItem(row, TIME_COL, time_column)

        task_column = QTableWidgetItem(task)
        self.table.setItem(row, TASK_COL, task_column)

        priority_column = QTableWidgetItem(shift)
        priority_column.setForeground(QColor("#ca2851"))
        self.table.setItem(row, PRIORITY_COL, priority_column)

        self.table.setRowHeight(row, TABLE_ROW_HEIGHT)
        return row

    def load_data(self, entries: list[list]) -> None:
        """Load schedule entries into the table."""
        self.table.setRowCount(0)
        for time, task, priority in entries:
            self.add_task(time, task, priority)

    def create_btn(self):
        """Create an add task button."""
        add_button = QPushButton("+ Add Task")
        add_button.setFixedHeight(60)
        add_button.setStyleSheet(ADD_BTN_STYLE)

        return add_button

    def get_entries(self) -> list[list]:
        """Get all entries from the table."""
        entries = []
        for row in range(self.table.rowCount()):
            time = self.table.item(row, TIME_COL).text()
            task = self.table.item(row, TASK_COL).text()
            priority = self.table.item(row, PRIORITY_COL).text()
            entries.append([time, task, priority])
        return entries