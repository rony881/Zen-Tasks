from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QTableWidget, QVBoxLayout, QWidget,QHBoxLayout,QTableWidgetItem
from qfluentwidgets import CardWidget, FluentIcon, TableWidget
from config import PRIMARAY_FONT, SECONDARY_FONT, UI_CONFIG
from core.utils.logger import logger
from ui.widgets.stats_card import StatsCard

HEIGHT = 67
SLEEP_LOGS = [
    {
        "date": "Mon, Jul 6",
        "bedtime": "11:20 PM",
        "wakeup": "7:10 AM",
        "duration": "7h 50m",
        "score": 91,
        "quality": "😴 Excellent"
    },
    {
        "date": "Tue, Jul 7",
        "bedtime": "12:05 AM",
        "wakeup": "7:45 AM",
        "duration": "7h 40m",
        "score": 88,
        "quality": "🙂 Good"
    },
    {
        "date": "Wed, Jul 8",
        "bedtime": "11:50 PM",
        "wakeup": "6:55 AM",
        "duration": "7h 05m",
        "score": 82,
        "quality": "🙂 Good"
    },
    {
        "date": "Thu, Jul 9",
        "bedtime": "1:10 AM",
        "wakeup": "7:00 AM",
        "duration": "5h 50m",
        "score": 63,
        "quality": "😐 Fair"
    },
    {
        "date": "Fri, Jul 10",
        "bedtime": "10:45 PM",
        "wakeup": "7:15 AM",
        "duration": "8h 30m",
        "score": 96,
        "quality": "🤩 Excellent"
    },
    {
        "date": "Sat, Jul 11",
        "bedtime": "2:00 AM",
        "wakeup": "8:20 AM",
        "duration": "6h 20m",
        "score": 70,
        "quality": "😕 Fair"
    },
    {
        "date": "Sun, Jul 12",
        "bedtime": "11:35 PM",
        "wakeup": "8:00 AM",
        "duration": "8h 25m",
        "score": 94,
        "quality": "😴 Excellent"
    },
    {
        "date": "Mon, Jul 13",
        "bedtime": "12:40 AM",
        "wakeup": "6:30 AM",
        "duration": "5h 50m",
        "score": 61,
        "quality": "😣 Poor"
    },
    {
        "date": "Tue, Jul 14",
        "bedtime": "11:15 PM",
        "wakeup": "7:20 AM",
        "duration": "8h 05m",
        "score": 92,
        "quality": "😊 Excellent"
    },
    {
        "date": "Wed, Jul 15",
        "bedtime": "12:10 AM",
        "wakeup": "7:05 AM",
        "duration": "6h 55m",
        "score": 79,
        "quality": "🙂 Good"
    }
]

class SleepJournal(QWidget):
    """Sleep Journal Page"""
    def __init__(self, parent) -> None:
        super().__init__(parent)
        logger.info("Sleep Journal Page Initialized Successfully")

        self.table = SleepHistory(self,SLEEP_LOGS)
        self.top_widget = TopVisualArea()

        self._build_ui()
        
    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.addWidget(self.top_widget)
        layout.addWidget(self.table)
        

class SleepHistory(TableWidget):
    def __init__(self, parent, sleep_logs):
        super().__init__(parent)

        self.setColumnCount(6)
        self.setHorizontalHeaderLabels([
            "Date",
            "Bedtime",
            "Wake Up",
            "Duration",
            "Score",
            "Quality"
        ])

        self.verticalHeader().hide()

        header = self.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(header.ResizeMode.Stretch)

        self.setAlternatingRowColors(True)
        self.setBorderVisible(False)
        self.setShowGrid(False)
        self.setMouseTracking(False)
        self.setWordWrap(False)
        self.setBorderVisible(True)

        # Adds all existing logs
        for log in sleep_logs:
            self.add_sleep_log(log)

    
    def add_sleep_log(self, log: dict):
        row = self.rowCount()
        self.insertRow(row)

        values = [
            log["date"],
            log["bedtime"],
            log["wakeup"],
            log["duration"],
            log["score"],
            log["quality"]
        ]

        for column, value in enumerate(values):
            self.setItem(
                row,
                column,
                QTableWidgetItem(str(value))
            )

class TopVisualArea(CardWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        logger.info("Sleep Journal Page Initialized Successfully")
        self.setFixedHeight(180)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(2, 2, 2, 2)

        self.setStyleSheet("""CardWidget{
            background: transparent;border: none;
            }""")

        card0 = StatsCard(
            self,
            "Sales",
            "275",
            "+32% this week",
        )
        card1 = StatsCard(
            self,
            "Orders",
            "1,245",
            "+15% this week",
        )
        card2 = StatsCard(
            self,
            "Sats",
            "125",
            "+10% this week",
        )
        card3 = StatsCard(
            self,
            "Active Customer",
            "375",
            "+25% this week",
        )
        layout.addWidget(card0)
        layout.addWidget(card1)
        layout.addWidget(card2)
        layout.addWidget(card3)
        
        