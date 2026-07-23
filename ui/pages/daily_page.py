from qfluentwidgets import (InfoBar, 
    InfoBarPosition, 
    ProgressRing, 
)
from config import INFO_BAR_DURATION_SHORT, current_day
from core.services.task_service import load_todays_tasks, save_todays_tasks
from core.models.task import Task
from ui.widgets.add_task_dialog import AddTaskDialog
from ui.widgets.edit_task_dialog import EditTaskDialog
from ui.widgets.task_card import SimpleCard, TaskCard
from ui.widgets.page_base_widget import PageBaseWidget
from core.utils.logger import logger

class DailyPage(PageBaseWidget):
    """Daily page showing today's tasks with progress tracking and also many features."""

    def __init__(self, parent) -> None:
        super().__init__(parent)
        logger.info("Initializing DailyPage")
        self.tasks = load_todays_tasks(current_day)

        self.build_ui()

    def build_ui(self):
        self.setPageHeader("Today", "Add Task")
        card_area = self._card_area()
        card_area.addWidget(self.progress_ring())
        self.addWidget(card_area)
        self.addListContainer()

        self._refresh_task_list()

    def _card_area(self):
        card = SimpleCard()
        return card
        
    def progress_ring(self):
        self.progress = ProgressRing()
        self.progress.setFixedSize(48, 48)
        self.progress.setTextVisible(True)

        return self.progress

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
            card.edit_clicked.connect(self.onUpdateButtonClicked)
            card.delete_clicked.connect(self._on_delete_task)
            self.list_layout.addWidget(card)

        self.list_layout.addStretch(1)
        self.update_stats()
        
    def _add_task(self, task: Task):
        """Add a new task to the task list."""
        
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
        
        self.progress.setValue(percent)

    def onAddButtonClicked(self):
        """One Add Button Clicked"""
        dialog = AddTaskDialog(self)
        if dialog.exec():
            data = dialog.get_data()
            self._add_task(data)

    def onUpdateButtonClicked(self, task: Task):
        """Open the edit dialog for an existing task."""
        logger.info(f"Edit task button requested: {task.task}")
        dialog = EditTaskDialog(task, parent=self)
        if dialog.exec():
            updated_task = dialog.get_data()
            self._update_task(updated_task)
            
    def _update_task(self, task: Task):
        """Handle task_updated signal from EditTaskDialog."""
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
