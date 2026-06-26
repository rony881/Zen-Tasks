from qfluentwidgets import FluentWindow, FluentIcon as FI,FluentStyleSheet
from ui.pages.weekly_page import WeeklyPage

class MainWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        self.resize(1200,900)
        self.navigationInterface.setExpandWidth(240)

        self.weekly_page = WeeklyPage(self)
        self.weekly_page.setObjectName("weekly_page")

        self._setup_main_panel()

    def _setup_main_panel(self):
        self.addSubInterface(self.weekly_page,FI.DOCUMENT,"Weekly Page")
