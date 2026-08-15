from datetime import datetime

from PyQt6.QtCore import QTime
from PyQt6.QtWidgets import QSpinBox
from qfluentwidgets import InfoBar, InfoBarPosition

from config import INFO_BAR_DURATION_SHORT
from ui.theme import PRIORITY_STYLE, TASK_INPUT_STYLE, ADD_BTN_STYLE
from ui.widgets.base_widgets.dialog_base_widget import DialogBaseWidget


QUALITY_OPTIONS = ["Good", "Fair", "Poor"]

INPUT_STYLE = """
QComboBox, QSpinBox {
    color: #444444;
    background: transparent;
    border: 1px solid #cccccc;
    border-radius: 6px;
    padding: 4px 10px;
    min-width: 100px;
}
"""


class AddSleepEntryDialog(DialogBaseWidget):
    """Dialog for recording a sleep entry."""

    def _setup_ui(self):
        """Set up the dialog UI components."""
        self.setDialogTitle("Add Sleep Entry")

        # Bedtime
        self.add(self.makeLabel("Bedtime"))
        self.bedtime_picker = self.makeTimePicker()
        self.add(self.bedtime_picker)

        # Wake time
        self.add(self.makeLabel("Wake Time"))
        self.wakeup_picker = self.makeTimePicker()
        self.add(self.wakeup_picker)

        # Sleep quality
        self.add(self.makeLabel("Sleep Quality"))
        self.quality = self.makeComboBox(
            items=QUALITY_OPTIONS,
            object_name="quality",
            stylesheet=PRIORITY_STYLE,
            placeholder="Quality",
        )
        self.add(self.quality)

        # Awakenings
        self.add(self.makeLabel("Awakenings"))
        self.awakenings = QSpinBox()
        self.awakenings.setRange(0, 20)
        self.awakenings.setValue(0)
        self.awakenings.setStyleSheet(INPUT_STYLE)
        self.add(self.awakenings)

        # Note
        self.add(self.makeLabel("Note (optional)"))
        self.note_input = self.makeTextArea(
            "Dreams, caffeine, stress, anything worth remembering...",
            70,
            TASK_INPUT_STYLE,
        )
        self.add(self.note_input)

        self.setSubmitButtonText(
            "Add Entry",
            object_name="add_entry_button",
            stylesheet=ADD_BTN_STYLE,
        )

    def validate(self) -> bool:
        """Validate the sleep entry before submitting."""
        if not self.quality.currentText():
            InfoBar.error(
                title="Entry not added",
                content="Quality cannot be empty",
                duration=INFO_BAR_DURATION_SHORT,
                position=InfoBarPosition.TOP,
                parent=self,
            )
            return False

        return True

    def get_data(self) -> dict:
        """Return the sleep entry as a dictionary."""
        bedtime = self.bedtime_picker.getTime()
        wakeup = self.wakeup_picker.getTime()

        return {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "bedtime": bedtime.toString("hh:mm AP"),
            "wakeup": wakeup.toString("hh:mm AP"),
            "duration": self._compute_duration(bedtime, wakeup),
            "quality": self.quality.currentText(),
            "awakenings": self.awakenings.value(),
            "mood": self.note_input.toPlainText().strip(),
        }

    @staticmethod
    def _compute_duration(start: QTime, end: QTime) -> str:
        """Return duration between two times, handling overnight sleep."""
        seconds = start.secsTo(end)

        if seconds <= 0:
            seconds += 24 * 60 * 60

        hours, remainder = divmod(seconds, 3600)
        minutes = remainder // 60

        return f"{hours:02d}:{minutes:02d}"