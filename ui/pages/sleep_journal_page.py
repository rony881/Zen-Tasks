from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QVBoxLayout, QWidget,QHBoxLayout,QTableWidgetItem
from qfluentwidgets import CaptionLabel, CardWidget, FluentIcon, PrimaryPushButton, TableWidget, TitleLabel
from core.data_loader import load_sleep_logs
from core.utils.logger import logger
from ui.widgets.stats_card import StatsCard

HEIGHT = 67

class SleepJournal(QWidget):
    """Sleep Journal Page"""
    def __init__(self, parent) -> None:
        super().__init__(parent)
        logger.info("Sleep Journal Page Initialized Successfully")
        SLEEP_LOGS = load_sleep_logs()

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
            "Avg. sleep"
        )
        self.Consistency = StatsCard(
            self,
            FluentIcon.CALENDAR,
            "Consistency",
        )
        self.sleep_dbt = StatsCard(
            self,
            FluentIcon.STOP_WATCH,
            "Sleep debt"
        )
        self.streak = StatsCard(
            self,
            FluentIcon.CERTIFICATE,
            "Current streak"
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
