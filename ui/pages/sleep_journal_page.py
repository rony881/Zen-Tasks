from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QVBoxLayout, QWidget,QHBoxLayout,QTableWidgetItem
from qfluentwidgets import CaptionLabel, CardWidget, FluentIcon, PrimaryPushButton, TableWidget, TitleLabel
from core.data_loader import load_sleep_logs
from core.utils.logger import logger
from ui.theme import TABLE_STYLE
from ui.widgets.stats_card import StatsCard
from ui.widgets.title_bar import TitleBar


class SleepJournal(QWidget):
    """Sleep Journal Page"""
    def __init__(self, parent) -> None:
        super().__init__(parent)
        logger.info("Sleep Journal Page Initialized Successfully")
        SLEEP_LOGS = load_sleep_logs()
        self.setStyleSheet(
            """
            CaptionLabel{
            background: transparent;
            }
            """
        )

        self.table = SleepHistory(self,SLEEP_LOGS)

        self._build_ui()
        
    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 1, 24, 24)
        layout.setSpacing(16)

        title = TitleBar(self,"Sleep Tacking", btn= "Add Log")
        
        layout.addWidget(title)
        layout.addWidget(CaptionLabel("Track tonight's sleep and see how you're trending."))
        
        layout.addLayout(self.statistics())
        layout.addWidget(self.table)
        
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

    def show_input_dialog(self):
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
        self.setStyleSheet(TABLE_STYLE)
        self.verticalHeader().hide()

        header = self.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(header.ResizeMode.Stretch)
        header.setDefaultAlignment(Qt.AlignmentFlag.AlignLeft)

        self.setAlternatingRowColors(True)
        self.setBorderVisible(False)
        self.setShowGrid(False)
        self.setMouseTracking(False)
        self.setWordWrap(False)
        self.setBorderVisible(True)

        # Adds all existing logs
        for log in sleep_logs:
            self.add_sleep_log(log)

        logger.info("Sleep History Loaded Successfully")
    
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

        logger.info("New Sleep Log Added Successfully")
