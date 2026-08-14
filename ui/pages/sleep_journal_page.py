from PyQt6.QtWidgets import QAbstractItemView, QGridLayout,QTableWidgetItem
from qfluentwidgets import FluentIcon as FI, TableWidget
from core.services.sleep_services import load_sleep_logs, save_sleep_logs
from core.utils.logger import logger
from ui.widgets.base_widgets.page_base_widget import PageBaseWidget
from ui.widgets.card_widgets.stats_card import StatsCard
from ui.widgets.dialogs.add_sleep_entry_dialog import AddSleepEntryDialog


class SleepJournal(PageBaseWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.sleep_logs = load_sleep_logs()

        self.build_ui()

    def build_ui(self):
        self.setPageHeader("Sleep Tracker", "Add Entry")
        self.add(self.statistics())
        self.addTitle("Sleep History")
        self.history = SleepHistory(self, self.sleep_logs)
        self.add(self.history)
        
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
        dialog = AddSleepEntryDialog(self)
        if dialog.exec():
            log = dialog.get_data()
            self.sleep_logs.append(log)
            save_sleep_logs(self.sleep_logs)
            self.history.reload(self.sleep_logs)

            
class SleepHistory(TableWidget):
    def __init__(self, parent, logs=None):
        super().__init__(parent)
        self.sleep_logs = logs if logs is not None else load_sleep_logs()

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

    def reload(self, logs: list[dict]):
        """Clear and rebuild the table with the given logs."""
        self.sleep_logs = logs
        self.setRowCount(0)
        for log in self.sleep_logs:
            self.add_sleep_log(log)