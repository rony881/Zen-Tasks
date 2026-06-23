from PyQt6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QListWidget,
    QSplitter
)
from qfluentwidgets import FluentWindow, FluentIcon as FI
from ui.pages.weekly_page import WeeklyPlanner

class Mainwindow(FluentWindow):
    def __init__(self):
        super().__init__()

        self.resize(1200,900)

        # Weekly Page
        self.weekly_page = WeeklyPlanner(self)
        self.weekly_page.setObjectName("WeeklyTab")
        # Setup
        self._setup_main_panel()

    def _setup_main_panel(self):
        self.addSubInterface(self.weekly_page,FI.HOME,"Weekly Page")
