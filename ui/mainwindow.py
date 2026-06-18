from PyQt6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QListWidget,
    QSplitter
)
from ui.pages.weekly_page import Weekly_Tab

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(1200,900)
        self.splitter = QSplitter()
        self.splitter.setStyleSheet(
            """
            background-color: #0a0a0a;
            """)       
        self.setCentralWidget(self.splitter)

        self.weekly_page = Weekly_Tab(self)

        # Setup
        self._setup_main_panel()
        self._setup_side_panel()
        self._setup_splitter()

    def _setup_side_panel(self):
        self.side_panel = QWidget()
        self.side_panel.setFixedWidth
        self.side_menu = QListWidget()
        # Side Layout
        self.side_layout = QVBoxLayout(self.side_panel)
        self.side_layout.setContentsMargins(5, 5, 0, 5)
        self.side_layout.addWidget(self.side_menu)

    def _setup_main_panel(self):
        self.main_panel = QWidget()

        # Main Panel Layout
        self.main_panel_layout = QVBoxLayout(self.main_panel)
        self.main_panel_layout.setContentsMargins(0, 5, 5, 5)
        self.main_panel_layout.addWidget(self.weekly_page)

    def _setup_splitter(self):
        self.splitter.addWidget(self.side_panel)
        self.splitter.addWidget(self.main_panel)

        self.splitter.setSizes([200,1000])
