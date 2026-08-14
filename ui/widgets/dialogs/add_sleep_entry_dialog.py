from datetime import datetime
from PyQt6.QtCore import QTime
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QSpinBox
from qfluentwidgets import InfoBar, InfoBarPosition
from config import INFO_BAR_DURATION_SHORT
from ui.theme import PRIORITY_STYLE, TASK_INPUT_STYLE
from ui.widgets.base_widgets.dialog_base_widget import DialogBaseWidget

FIELD_LABEL_STYLE = "color:#666666;font-size:14px;"
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
        self.setDialogSize(600, 550)

        # Bedtime Label and Picker
        self.bedtime_picker = self.makeTimePicker()
        self.bedtime_lbl = self.makeLabel("Bedtime")
        self.add(self.bedtime_lbl)
        self.add(self.bedtime_picker)

        # Wakeup Label and Picker
        self.wakeup_picker = self.makeTimePicker()
        self.wakeup_lbl = self.makeLabel("Wake Time")
        self.add(self.wakeup_lbl)
        self.add(self.wakeup_picker)

        # Quality Label and Picker
        self.quality = self.makeComboBox(
            items=QUALITY_OPTIONS,
            object_name="quality",
            stylesheet=PRIORITY_STYLE,
            placeholder="Quality"
        )
        self.quality_lbl = self.makeLabel("Sleep Quality")
        self.add(self.quality_lbl)
        self.add(self.quality)

        # Awakenings Label and Picker
        self.awakenings = QSpinBox()
        self.awakenings.setRange(0, 20)
        self.awakenings.setValue(0)
        self.awakenings.setStyleSheet(INPUT_STYLE)
        self.awakenings_lbl = self.makeLabel("Awakenings")
        self.add(self.awakenings_lbl)
        self.add(self.awakenings)

        self.note_input = self.makeTextArea(
            "Dreams, caffeine, stress, anything worth remembering...",
            70,
            TASK_INPUT_STYLE,
        )
        self.note_lbl = self.makeLabel("Note (optional)")
        self.add(self.note_lbl)
        self.add(self.note_input)

        footer = self.makeFooter(submitBtnText="Add Entry")
        self.add(footer)

    def onSubmit(self) -> None:
        """Validate the entry and close the dialog."""
        quality = self.quality.currentText()
        if not quality:
            InfoBar.error(
                title="Entry not added",
                content="Quality cannot be empty",
                duration=INFO_BAR_DURATION_SHORT,
                position=InfoBarPosition.TOP,
                parent=self,
            )
            return
        self.accept()

    def get_data(self) -> dict:
        """Return the sleep entry as a dictionary."""
        return {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "bedtime": self.bedtime_picker.getTime().toString("hh:mm AP"),
            "wakeup": self.wakeup_picker.getTime().toString("hh:mm AP"),
            "duration": self._compute_duration(
                self.bedtime_picker.getTime(),
                self.wakeup_picker.getTime(),
            ),
            "quality": self.quality.currentText(),
            "awakenings": self.awakenings.value(),
            "mood": self.note_input.toPlainText().strip(),
        }

    @staticmethod
    def _compute_duration(start: QTime, end: QTime) -> str:
        """Return duration between two times, handling overnight sleeps."""
        secs = start.secsTo(end)
        if secs <= 0:
            secs += 24 * 3600
        hours, rem = divmod(secs, 3600)
        minutes = rem // 60
        return f"{hours:02d}:{minutes:02d}"
