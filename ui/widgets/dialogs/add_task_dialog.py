from qfluentwidgets import InfoBar, InfoBarPosition
from config import INFO_BAR_DURATION_SHORT, PRIORITIES,UI_CONFIG
from core.models.task import Task
from ui.theme import ADD_BTN_STYLE, PRIORITY_STYLE, TASK_INPUT_STYLE
from ui.widgets.base_widgets.dialog_base_widget import DialogBaseWidget
DIALOG_WIDTH = UI_CONFIG["dialog_width"]
DIALOG_HEIGHT = UI_CONFIG["dialog_height"]

class AddTaskDialog(DialogBaseWidget):
    """Dialog for creating new tasks with time, description, and priority."""
        
    def _setup_ui(self):
        """Set up the dialog UI components."""
        self.setDialogTitle("Add New Task")
        
        # Task input
        self.task_input = self.makeTextArea(
            "write task discription...",
            110,
            TASK_INPUT_STYLE
        )
        self.add(self.makeLabel("Task Name"))
        self.add(self.task_input)

        # Time picker
        time_picker_layout = self.makeHLayout()
        self.timePicker = self.makeTimePicker()
        time_picker_layout.addWidget(self.makeLabel("Time :"))
        time_picker_layout.addWidget(self.timePicker)
        self.add(time_picker_layout)

        # Priority
        priority_layout = self.makeHLayout()
        self.priority = self.makeComboBox(PRIORITIES, "priority", PRIORITY_STYLE)
        priority_layout.addWidget(self.makeLabel("Priority :"))
        priority_layout.addWidget(self.priority)
        self.add(priority_layout)
        
        self.setSubmitButtonText(
            "Add Task",
            object_name="add_task_button",
            stylesheet=ADD_BTN_STYLE
        )
        
    def validate(self) -> bool:
        """Validate the sleep entry before submitting."""
        task = self.task_input.toPlainText().strip()
        priority = self.priority.currentText()
    
        if not task or not priority:
            InfoBar.error(
                title="Task not added",
                content="Task and Priority cannot be empty",
                duration=INFO_BAR_DURATION_SHORT,
                position=InfoBarPosition.TOP,
                parent=self,
            )
            return False
        return True

    def get_data(self):
        time = self.timePicker.getTime().toString("hh:mm AP")
        task = self.task_input.toPlainText().strip()
        priority = self.priority.currentText()

        return Task(
            time,
            task,
            priority
        )
        