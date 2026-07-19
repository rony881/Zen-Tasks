from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QAbstractItemView, QHeaderView, QTableWidgetItem, QTabWidget, QVBoxLayout, QWidget
from qfluentwidgets import InfoBar, InfoBarPosition

from config import DAYS, INFO_BAR_DURATION_SHORT, TABLE_ROW_HEIGHT, TIME_COL, TASK_COL, PRIORITY_COL
from core.data_loader import load_schedule, save_schedule
from core.models.task import Task
from ui.theme import TAB_WIDG_STYLE
from ui.widgets.add_task_dialog import AddTaskDialog
from ui.widgets.page_base_widget import PageBaseWidget
from core.utils.logger import logger


class WeeklyPage(PageBaseWidget):
    """Weekly page showing schedule in tabbed table format."""

    def __init__(self, parent) -> None:
        """Initialize weekly page with schedule data."""
        super().__init__(parent)
        logger.info("Weekly Page Initialized Successfully")

        self._schedule = load_schedule()
        self.build_ui()

    def build_ui(self):
        """Build the page header and tab widget."""
        self.setPageHeader("Weekly Schedule", "Add Task")
        self.tab_widget = self._build_tab_widget()
        self.addWidget(self.tab_widget)

    def _build_tab_widget(self) -> QTabWidget:
        """Build the tab widget containing schedule tables for each day."""
        tab_widget = self.buildTabWidget()

        for day, entries in self._schedule.items():
            table = PlannerTable(self, tab_widget)
            table.load_data(entries)
            tab_widget.addTab(table, day)

        return tab_widget

    def onAddButtonClicked(self) -> None:
        """Show the add task dialog for the current tab."""
        day_index = self.tab_widget.currentIndex()
        dialog = AddTaskDialog(self, day_index)
        if dialog.exec():
            task = dialog.get_data()
            self._add_task(day_index, task)

    def _add_task(self, day_index: int, task: Task):
        """Add a new task to the given day's table and persist it."""
        planner_table: PlannerTable = self.tab_widget.widget(day_index)
        planner_table.add_task(task.time, task.task, task.priority)
        self._save_schedule()

        InfoBar.success(
            title="Task added",
            content=task.task,
            duration=INFO_BAR_DURATION_SHORT,
            position=InfoBarPosition.TOP,
            parent=self,
        )

    def _save_schedule(self):
        """Save all tasks from all tabs to the schedule file."""
        data = {}
        for i in range(self.tab_widget.count()):
            day = self.tab_widget.tabText(i)
            table: PlannerTable = self.tab_widget.widget(i)
            data[day] = table.get_entries()
        save_schedule(data)


class PlannerTable(QWidget):
    """Table widget for displaying and managing schedule entries for one day."""

    def __init__(self, page_base: PageBaseWidget, parent):
        """Initialize planner table with table widget."""
        super().__init__(parent)
        layout = QVBoxLayout(self)

        self.table = page_base.buildTableWidget(["Time", "Task", "Priority"])
        self._configure_table()
        layout.addWidget(self.table)

    def _configure_table(self):
        """Configure column resize behavior and widths."""
        hdr = self.table.horizontalHeader()
        hdr.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        hdr.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        hdr.setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)

        self.table.setColumnWidth(0, 130)
        self.table.setColumnWidth(2, 150)
        self.table.verticalHeader().hide()
        self.table.setBorderRadius(8)
        self.table.setBorderVisible(True)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setAlternatingRowColors(False)

    def add_task(self, time: str, task: str, priority: str) -> int:
        """Add a task row to the table."""
        row = self.table.rowCount()
        self.table.insertRow(row)

        self.table.setItem(row, TIME_COL, QTableWidgetItem(time))
        self.table.setItem(row, TASK_COL, QTableWidgetItem(task))

        priority_column = QTableWidgetItem(priority)
        priority_column.setForeground(QColor("#ca2851"))
        self.table.setItem(row, PRIORITY_COL, priority_column)

        self.table.setRowHeight(row, TABLE_ROW_HEIGHT)
        return row

    def load_data(self, entries: list[list]) -> None:
        """Load schedule entries into the table."""
        self.table.setRowCount(0)
        for time, task, priority in entries:
            self.add_task(time, task, priority)

    def get_entries(self) -> list[list]:
        """Get all entries from the table."""
        entries = []
        for row in range(self.table.rowCount()):
            time = self.table.item(row, TIME_COL).text()
            task = self.table.item(row, TASK_COL).text()
            priority = self.table.item(row, PRIORITY_COL).text()
            entries.append([time, task, priority])
        return entries