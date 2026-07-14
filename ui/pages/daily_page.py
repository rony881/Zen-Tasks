from PyQt6.QtWidgets import QHBoxLayout, QScrollArea, QVBoxLayout, QWidget, QFrame
from qfluentwidgets import (InfoBar, 
    InfoBarPosition, 
    PrimaryPushButton,
    ProgressRing, 
    TransparentPushButton,
    FluentIcon as FI
)
from config import INFO_BAR_DURATION_SHORT, current_day
from core.data_loader import load_todays_tasks, save_todays_tasks
from core.models.task import Task
from ui.widgets.add_task_dialog import AddTaskDialog
from ui.widgets.edit_task_dialog import EditTaskDialog
from ui.widgets.card import SimpleCard, TaskCard
from ui.widgets.title_bar import TitleBar
from core.utils.logger import logger

class DailyPage(QWidget):
    """Daily page showing today's tasks with progress tracking and also many features."""
    
    def __init__(self, parent) -> None:
        super().__init__(parent)
        logger.info("Initializing DailyPage")
        # main Layout of this page
        self.page_layout = QVBoxLayout(self)
        self.page_layout.setContentsMargins(24, 1, 24, 24)
        self.tasks = load_todays_tasks(current_day)
        
        self._build_ui()
        logger.info(f"DailyPage initialized with {len(self.tasks)} tasks")

    def _build_ui(self):
        """Build the UI components for the daily page."""
        # ======= Header =========
        # title shown on top of the page
        self.title = TitleBar(self,"My Task",btn="Add Task")
        self.page_layout.addWidget(self.title)

        # ======= Header Area ========
        self.progress_ring = ProgressRing()
        self.progress_ring.setFixedSize(48, 48)
        self.progress_ring.setTextVisible(True)
        progress_card = SimpleCard()
        progress_card.setWidget(self.progress_ring)
        self.page_layout.addWidget(progress_card)

        # ======= Main Content ======
        # Scroll Area for the Tasks List
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setStyleSheet("QScrollArea{background: transparent; border: none;}")

        # main container for Tasks List
        self.list_container = QWidget()
        self.list_container.setStyleSheet("background: transparent;")
        self.list_layout = QVBoxLayout(self.list_container)
        self.list_layout.setContentsMargins(6, 4, 6, 4)
        self.list_layout.setSpacing(8)

        self.scroll_area.setWidget(self.list_container)
        self.page_layout.addWidget(self.scroll_area)

        self._refresh_task_list()

    def _add_task(self, time,task_name, priority):
        """Add a new task to the task list."""
        
        task = Task(
            time = time,
            task = task_name,
            priority = priority,
            done = False,
        )
        self.tasks.append(task)
        save_todays_tasks(self.tasks)
        self._refresh_task_list()
        
        InfoBar.success(
            title="Task added",
            content=task.task,
            duration=INFO_BAR_DURATION_SHORT,
            position=InfoBarPosition.TOP,
            parent=self,
        )
        
    def update_stats(self, checked=None):
        """Update progress ring based on completed tasks."""
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t.done)
        percent = int(completed / total * 100) if total else 0
        
        self.progress_ring.setValue(percent)

    def show_input_dialog(self):
        """Open the dialog for creating a new task."""
        dialog = AddTaskDialog(parent=self)
        dialog.task_created.connect(self._on_task_created)
        dialog.exec()

    def _on_task_created(self, day_index, time, task_text, priority):
        """Handle task_created signal from AddTaskDialog."""
        self._add_task(time, task_text, priority)

    def _on_edit_task(self, task: Task):
        """Open the edit dialog for an existing task."""
        logger.info(f"Edit task button requested: {task.task}")
        dialog = EditTaskDialog(task, parent=self)
        dialog.task_updated.connect(self._on_task_updated)
        dialog.exec()

    def _on_task_updated(self, task: Task, time, task_text, priority):
        """Handle task_updated signal from EditTaskDialog."""
        task.time = time
        task.task = task_text
        task.priority = priority
        save_todays_tasks(self.tasks)
        self._refresh_task_list()

        InfoBar.success(
            title="Task updated",
            content=task.task,
            duration=INFO_BAR_DURATION_SHORT,
            position=InfoBarPosition.TOP,
            parent=self,
        )

    def _on_delete_task(self, task: Task):
        """Remove a task from the list and persist the change."""
        if task in self.tasks:
            self.tasks.remove(task)
            save_todays_tasks(self.tasks)
            self._refresh_task_list()

            InfoBar.success(
                title="Task deleted",
                content=task.task,
                duration=INFO_BAR_DURATION_SHORT,
                position=InfoBarPosition.TOP,
                parent=self,
            )

    def _on_clear_completed(self):
        """Remove all completed tasks from the list."""
        remaining = [t for t in self.tasks if not t.done]
        if len(remaining) == len(self.tasks):
            return
        self.tasks = remaining
        save_todays_tasks(self.tasks)
        self._refresh_task_list()

    def _refresh_task_list(self):
        """Clear and rebuild the task card list from self.tasks."""
        while self.list_layout.count():
            item = self.list_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        for task in self.tasks:
            card = TaskCard(task)
            card.checkbox_changed.connect(self.update_stats)
            card.edit_clicked.connect(self._on_edit_task)
            card.delete_clicked.connect(self._on_delete_task)
            self.list_layout.addWidget(card)

        self.list_layout.addStretch(1)
        self.update_stats()