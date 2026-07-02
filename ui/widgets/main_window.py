from qfluentwidgets import FluentWindow, FluentIcon as FI
from ui.pages.weekly_page import WeeklyPage
from ui.pages.daily_page import DailyPage
from config import UI_CONFIG

WINDOW_WIDTH = UI_CONFIG["window_width"]
WINDOW_HEIGHT = UI_CONFIG["window_height"]
NAVI_WIDTH = UI_CONFIG["navigation_width"]

class MainWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        self.resize(WINDOW_WIDTH,WINDOW_HEIGHT)
        self.navigationInterface.setExpandWidth(NAVI_WIDTH)

        # ============ Weekly Page ================
        self.weekly_page = WeeklyPage(self)
        self.weekly_page.setObjectName("weekly_page")
        # =========================================

        # ============ Daily Page ================
        self.daily_page = DailyPage(self)
        self.daily_page.setObjectName("daily_page")
        # =========================================

        self._setup_main_panel()

    def _setup_main_panel(self):
        self.addSubInterface(self.weekly_page,FI.DOCUMENT,"Weekly Page")
        self.addSubInterface(self.daily_page,FI.DOCUMENT,"Daily Page")
