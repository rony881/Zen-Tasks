from qfluentwidgets import FluentWindow, FluentIcon as FI
from ui.pages.weekly_page import WeeklyPage

class Mainwindow(FluentWindow):
    def __init__(self):
        super().__init__()

        self.resize(1200,900)

        # Weekly Page
        self.weekly_page = WeeklyPage(self)
        self.weekly_page.setObjectName("WeeklyTab")
        # Setup
        self._setup_main_panel()

    def _setup_main_panel(self):
        self.addSubInterface(self.weekly_page,FI.TAG,"Weekly Page")
