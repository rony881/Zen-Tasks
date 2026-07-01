from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget

from ui.widgets.title_bar import TitleBar


class DailyPage(QWidget):
    
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.page_layout = QVBoxLayout(self)
        self.page_layout.setContentsMargins(0,0,0,0)
        self._build_ui()

    def _build_ui(self):
        self.title = TitleBar(self,"My Task")
        self.page_layout.addWidget(self.title)

        content_area = QWidget(self)
        