from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QVBoxLayout, QWidget,QHBoxLayout,QTableWidgetItem
from qfluentwidgets import CaptionLabel, CardWidget, FluentIcon, PrimaryPushButton, TableWidget, TitleLabel
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

        self._build_ui()
        
    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(16)
        
        layout.addLayout(self.title_row())
        layout.addWidget(CaptionLabel("Track tonight's sleep and see how you're trending."))
        
        layout.addLayout(self.statistics())
        layout.addWidget(self.table)

    def title_row(self):
        title_row = QHBoxLayout()

        title = TitleLabel("Sleep Journal")
        title_row.addWidget(title)
        title_row.addStretch(1)

        self.add_btn = PrimaryPushButton(FluentIcon.EDIT, "Add Log")
        self.add_btn.clicked.connect(self._on_add_log)
        title_row.addWidget(self.add_btn)

        return title_row
        
    def statistics(self):
        # ---- Stat cards ----
        statsGrid = QGridLayout()
        statsGrid.setSpacing(12)
        
        self.avg_sleep = StatsCard(
            self,
            FluentIcon.QUIET_HOURS,
            "Avg. sleep",
            "7.2 hrs",
            "goal 8.0 h",
        )
        self.Consistency = StatsCard(
            self,
            FluentIcon.CALENDAR,
            "Consistency",
            "87/100",
            "Bed time & Wake regularity",
        )
        self.sleep_dbt = StatsCard(
            self,
            FluentIcon.STOP_WATCH,
            "Sleep debt",
            "2",
            "last 14 days",
        )
        self.streak = StatsCard(
            self,
            FluentIcon.CERTIFICATE,
            "Current streak",
            "6 Nights",
            "Meeting your goal",
        )
        
        statsGrid.addWidget(self.avg_sleep,0,0)
        statsGrid.addWidget(self.Consistency ,0,1)
        statsGrid.addWidget(self.sleep_dbt,0,2)
        statsGrid.addWidget(self.streak,0,3)
        
        return statsGrid

    def _on_add_log(self):
        ...

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
