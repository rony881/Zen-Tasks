from qfluentwidgets import (
    MessageBoxBase,
    LineEdit,
    TextEdit,
    ComboBox,
    PrimaryPushButton
)

class AddTaskDialog(MessageBoxBase):
    def __init__(self, parent):
        super().__init__(parent)

        self.titleEdit = LineEdit()
        self.titleEdit.setPlaceholderText("Task title")
        self.resize(400,500)

        self.descriptionEdit = TextEdit()

        self.priority = ComboBox()
        self.priority.addItems([
            "Low",
            "Medium",
            "High"
        ])

        self.viewLayout.addWidget(self.titleEdit)
        self.viewLayout.addWidget(self.descriptionEdit)
        self.viewLayout.addWidget(self.priority)

        self.yesButton.setText("Add Task")
        self.cancelButton.setText("Cancel")