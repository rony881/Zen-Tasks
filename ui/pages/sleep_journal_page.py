from PyQt6.QtWidgets import QAbstractItemView, QGridLayout,QTableWidgetItem
from qfluentwidgets import FluentIcon as FI, TableWidget
from core.data_loader import load_sleep_logs
from core.utils.logger import logger
from ui.widgets.page_base_widget import PageBaseWidget
from ui.widgets.stats_card import StatsCard


class SleepJournal(PageBaseWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.build_ui()

    def build_ui(self):
        self.setPageHeader("Sleep Tracker", "Add Entry")
        self.addLayout(self.statistics())
        self.addTitle("Sleep History")
        self.addWidget(SleepHistory(self))
        
    def statistics(self):
        # ---- Stat cards ----
        statsGrid = QGridLayout()
        statsGrid.setSpacing(12)
        
        self.avg_sleep = StatsCard(
            self,
            FI.QUIET_HOURS,
            "Avg. sleep"
        )
        self.consistency = StatsCard(
            self,
            FI.CALENDAR,
            "Consistency",
        )
        self.sleep_dbt = StatsCard(
            self,
            FI.STOP_WATCH,
            "Sleep debt"
        )
        self.streak = StatsCard(
            self,
            FI.CERTIFICATE,
            "Current streak"
        )

        statsGrid.addWidget(self.avg_sleep,0,0)
        statsGrid.addWidget(self.consistency ,0,1)
        statsGrid.addWidget(self.sleep_dbt,0,2)
        statsGrid.addWidget(self.streak,0,3)
        
        return statsGrid

    def onAddButtonClicked(self):
        self.avg_sleep.set_Value(7,"Hours")
        self.consistency.set_Value(4,"Nights")
        self.sleep_dbt.set_Value(2,"Hours")
        self.streak.set_Value(4,"Nights")
    
class SleepHistory(TableWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.sleep_logs = load_sleep_logs()

        self.setColumnCount(7)
        self.setHorizontalHeaderLabels([
            "Date",
            "Bedtime",
            "Wake",
            "Duration",
            "Quality",
            "Awakenings",
            "Mood"
        ])
        self.verticalHeader().hide()
        self.setBorderRadius(8)
        self.setBorderVisible(True)
        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setAlternatingRowColors(False)
        self.setShowGrid(False)
        self.setMouseTracking(False)
        
        header = self.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(header.ResizeMode.Stretch)

        # Adds all existing logs
        for log in self.sleep_logs:
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
            log["quality"],
            log["awakenings"],
            log["mood"]
        ]

        for column, value in enumerate(values):
            self.setItem(
                row,
                column,
                QTableWidgetItem(str(value))
            )

        logger.info("New Sleep Log Added Successfully")