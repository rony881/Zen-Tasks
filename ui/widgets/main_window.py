from qfluentwidgets import FluentWindow, FluentIcon as FI
from ui.pages.sleep_journal_page import SleepJournal
from ui.pages.weekly_page import WeeklyPage
from ui.pages.daily_page import DailyPage
from config import UI_CONFIG
from core.utils.logger import logger

WINDOW_WIDTH = UI_CONFIG["window_width"]
WINDOW_HEIGHT = UI_CONFIG["window_height"]
NAVI_WIDTH = UI_CONFIG["navigation_width"]

class MainWindow(FluentWindow):
    """ Main application window containing pages."""
    
    def __init__(self):
        """ Initialize the main window """

        super().__init__()
        logger.info("Initializing MainWindow")
        self.resize(WINDOW_WIDTH,WINDOW_HEIGHT)
        self.navigationInterface.setExpandWidth(NAVI_WIDTH)
        self.stackedWidget.setAnimationEnabled(False)
        self.navigationInterface.panel.setStyleSheet("""
            background-color : #e4dad5;
        """)
        self.stackedWidget.setStyleSheet("""
        QStackedWidget {
            border-top-left-radius: 0px;
            background-color: #f6f4f1;
        }
        """)

        # ============ Weekly Page ================
        # self.weekly_page = WeeklyPage(self)
        # self.weekly_page.setObjectName("weekly_page")
        # =========================================

        # ============ Daily Page ================
        self.daily_page = DailyPage(self)
        self.daily_page.setObjectName("daily_page")
        # =========================================
        
        # ============ Sleep Journal ==============
        self.sleep_journal = SleepJournal(self)
        self.sleep_journal.setObjectName("Sleep_Journal")

        self._setup_main_panel()
        logger.info("MainWindow initialized successfully")

    def _setup_main_panel(self):
        """Set up the navigation panel with sub-interfaces."""
        
        # self.addSubInterface(self.weekly_page,FI.DOCUMENT,"Weekly Page")
        self.addSubInterface(self.daily_page,FI.DOCUMENT,"Daily Page")
        self.addSubInterface(self.sleep_journal,FI.LEAF,"Sleep Journal")
