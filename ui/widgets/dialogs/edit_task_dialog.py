from PyQt6.QtCore import QTime
from core.models.task import Task
from core.utils.logger import logger
from ui.theme import ADD_BTN_STYLE
from ui.widgets.dialogs.add_task_dialog import AddTaskDialog


class EditTaskDialog(AddTaskDialog):
    """Dialog for editing an existing task's time, description, and priority."""

    def __init__(self, task: Task, parent=None):
        """Initialize edit task dialog, pre-filled with the given task's data."""
        self.task = task
        super().__init__(parent)

    def _setup_ui(self):
        super()._setup_ui()
        self.setWindowTitle("Edit Task")
        self.setSubmitButtonText(
            "Save Changes",
            object_name="edit_task_button",
            stylesheet=ADD_BTN_STYLE
        )
        self._fill_up_dialog()

    def _fill_up_dialog(self):
        """Pre-fill the dialog fields with the task's existing data."""
        self.task_input.setPlainText(self.task.task)
        parsed_time = QTime.fromString(self.task.time, "hh:mm AP")
        self.timePicker.setTime(parsed_time)
        index = self.priority.findText(self.task.priority)
        if index >= 0:
            self.priority.setCurrentIndex(index)

    def get_data(self) -> Task:
        """Returns the updated task."""
        self.task.task = self.task_input.toPlainText().strip()
        self.task.time = self.timePicker.getTime().toString("hh:mm AP")
        self.task.priority = self.priority.currentText()
        return self.task