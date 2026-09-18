from qfluentwidgets import (InfoBar, 
    InfoBarPosition, 
    ProgressRing, 
)

from zen.config import INFO_BAR_DURATION_SHORT, current_day
from zen.core.services.task_service import load_todays_tasks, save_todays_tasks
from zen.core.models.task import Task
from zen.widgets.dialogs.add_task_dialog import AddTaskDialog
from zen.widgets.dialogs.edit_task_dialog import EditTaskDialog
from zen.widgets.card_widgets.task_card import TaskCard
from zen.widgets.base_widgets.page_base_widget import PageBaseWidget
from zen.widgets.empty_state_widget import EmptyStateWidget
from zen.core.utils.logger import logger

class DailyPage(PageBaseWidget):
    """Daily page showing today's tasks with progress tracking and also many features."""

    def __init__(self, parent) -> None:
        super().__init__(parent)
        logger.info("Initializing DailyPage")
        self.tasks = load_todays_tasks(current_day)

        self.build_ui()

    def build_ui(self):
        self.setPageHeader("Today", "Add Task")
        self.setListContentMargins(60,4,60,4)
        self.addListContainer()

        self._refresh_task_list()

        
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

        if not self.tasks:
            self._show_empty_task()
            return

        for task in self.tasks:
            card = TaskCard(task)
            card.checkbox_changed.connect(self._on_task_checked)
            card.edit_clicked.connect(self.onUpdateButtonClicked)
            card.delete_clicked.connect(self._on_delete_task)
            self.list_layout.addWidget(card)

        self.list_layout.addStretch(1)

    def _show_empty_task(self):
            empty_state = EmptyStateWidget(
                title="No tasks for today",
                subtitle="Enjoy the free time, or add something to get done.",
                button_text="Add Task",
            )
            empty_state.add_clicked.connect(self.onAddButtonClicked)
            self.list_layout.addWidget(empty_state)
        
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

    def _on_task_checked(self, checked=None):
        """Save the task list after a task is checked/unchecked."""
        save_todays_tasks(self.tasks)
        logger.info(f"Task checked: {checked}")
        
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