from PyQt6.QtWidgets import QVBoxLayout, QWidget
from qfluentwidgets.components import layout
from core.utils.logger import logger


class SleepJournal(QWidget):
    """Slepp Journal Page"""
    def __init__(self, parent) -> None:
        super().__init__(parent)
        logger.info("Sleep Journal Page Initialized Successfully")
        self.main_layout = QVBoxLayout(self)

        self._build_ui()

    def _build_ui(self):
        ...
        