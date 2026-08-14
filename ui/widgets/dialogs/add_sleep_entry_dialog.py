from datetime import datetime
from PyQt6.QtCore import QTime
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QSpinBox
from qfluentwidgets import InfoBar, InfoBarPosition
from config import INFO_BAR_DURATION_SHORT
from ui.theme import TASK_INPUT_STYLE
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
        self.setDialogSize()

        self.bedtime_picker = self.makeTimePicker()
        self.wakeup_picker = self.makeTimePicker()

        times_row = self._make_field_row(
            ("Bedtime", self.bedtime_picker),
            ("Wake", self.wakeup_picker),
        )
        self.add(times_row)

        self.quality = self.makeComboBox(
            QUALITY_OPTIONS, "quality", INPUT_STYLE, placeholder="Quality"
        )
        self.awakenings = QSpinBox()
        self.awakenings.setRange(0, 20)
        self.awakenings.setValue(0)
        self.awakenings.setStyleSheet(INPUT_STYLE)

        details_row = self._make_field_row(
            ("Quality", self.quality),
            ("Awakenings", self.awakenings),
        )
        self.add(details_row)

        self.mood_input = self.makeTextArea(
            "How was your mood? (optional)",
            70,
            TASK_INPUT_STYLE,
        )
        self.add(self.mood_input)

        footer = self.makeFooter(submitBtnText="Add Entry")
        self.add(footer)

    def _make_field_row(self, *fields) -> QHBoxLayout:
        """Build a horizontal row of labelled input widgets."""
        row = QHBoxLayout()
        row.setSpacing(8)
        for label_text, widget in fields:
            label = QLabel(label_text)
            label.setStyleSheet(FIELD_LABEL_STYLE)
            row.addWidget(label)
            row.addWidget(widget)
        row.addStretch(1)
        return row

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
            "mood": self.mood_input.toPlainText().strip(),
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
