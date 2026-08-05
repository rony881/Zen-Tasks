from qfluentwidgets import InfoBar, InfoBarPosition
from config import INFO_BAR_DURATION_SHORT, PRIORITIES,UI_CONFIG
from core.models.task import Task
from ui.theme import PRIORITY_STYLE, TASK_INPUT_STYLE
from ui.widgets.base_widgets.dialog_base_widget import DialogBaseWidget
DIALOG_WIDTH = UI_CONFIG["dialog_width"]
DIALOG_HEIGHT = UI_CONFIG["dialog_height"]

class AddTaskDialog(DialogBaseWidget):
    """Dialog for creating new tasks with time, description, and priority."""
        
    def _setup_ui(self):
        """Set up the dialog UI components."""
        self.setDialogTitle("Add New Task")
        self.setDialogSize()
        
        self.task_input = self.makeTextArea(
            "write task discription...",
            110,
            TASK_INPUT_STYLE
        )
        self.addWidget(self.task_input)
        
        self.timePicker = self.makeTimePicker()
        self.priority = self.makeComboBox(PRIORITIES, "priority", PRIORITY_STYLE)

        footer = self.makeFooter(
                self.timePicker,
                self.priority,
                submitBtnText= "Add Task"
            )
        self.add(footer)
        
    def onSubmit(self) -> None:
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
            return
    
        self.accept()

    def get_data(self):
        time = self.timePicker.getTime().toString("hh:mm AP")
        task = self.task_input.toPlainText().strip()
        priority = self.priority.currentText()

        return Task(
            time,
            task,
            priority
        )
        