from datetime import datetime
import math
import re

from PyQt6.QtWidgets import QAbstractItemView, QGridLayout,QTableWidgetItem
from qfluentwidgets import FluentIcon as FI, TableWidget

from zen.core.services.sleep_services import load_sleep_logs, save_sleep_logs
from zen.core.utils.logger import logger
from zen.widgets.base_widgets.page_base_widget import PageBaseWidget
from zen.widgets.card_widgets.stats_card import StatsCard
from zen.widgets.dialogs.add_sleep_entry_dialog import AddSleepEntryDialog

TARGET_MINUTES = 8 * 60

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
        self.update_statistics()
        
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
    
    @staticmethod
    def _duration_to_minutes(duration: str) -> int:
        duration = duration.strip()
        if ":" in duration:
            h, m = duration.split(":")
            return int(h) * 60 + int(m)
        match = re.match(r"(?:(\d+)h)?\s*(?:(\d+)m)?", duration)
        h = int(match.group(1) or 0)
        m = int(match.group(2) or 0)
        return h * 60 + m

    @staticmethod
    def _time_to_minutes(time_str: str) -> int:
        t = datetime.strptime(time_str.strip(), "%I:%M %p")
        return t.hour * 60 + t.minute

    @staticmethod
    def _parse_log_date(date_str: str):
        date_str = date_str.strip()
        for fmt in ("%Y-%m-%d", "%a, %b %d"):
            try:
                dt = datetime.strptime(date_str, fmt)
                if fmt == "%a, %b %d":
                    dt = dt.replace(year=datetime.now().year)
                return dt.date()
            except ValueError:
                continue
        logger.warning(f"Unrecognized date format: {date_str}")
        return None

    def compute_statistics(self, logs: list[dict]) -> dict:
        if not logs:
            return {"avg_sleep": "--", "consistency": "--",
                     "sleep_debt": "--", "streak": "0"}

        durations = [self._duration_to_minutes(l["duration"]) for l in logs]

        avg_minutes = round(sum(durations) / len(durations))
        avg_h, avg_m = divmod(avg_minutes, 60)

        angles = [(self._time_to_minutes(l["bedtime"]) / 1440) * 2 * math.pi for l in logs]
        sin_sum = sum(math.sin(a) for a in angles)
        cos_sum = sum(math.cos(a) for a in angles)
        r_length = math.hypot(sin_sum, cos_sum) / len(angles)
        consistency_pct = round(r_length * 100)

        debt_minutes = max(0, TARGET_MINUTES * len(durations) - sum(durations))
        debt_h, debt_m = divmod(debt_minutes, 60)

        # Use the tolerant date parser, and drop any unparseable rows
        dates = sorted({d for l in logs if (d := self._parse_log_date(l["date"])) is not None})
        streak = 1
        for i in range(len(dates) - 1, 0, -1):
            if (dates[i] - dates[i - 1]).days == 1:
                streak += 1
            else:
                break

        return {
            "avg_sleep": f"{avg_h}h {avg_m}m",
            "consistency": f"{consistency_pct}%",
            "sleep_debt": f"{debt_h}h {debt_m}m",
            "streak": str(streak),
        }

    def update_statistics(self):
        stats = self.compute_statistics(self.sleep_logs)
        self.avg_sleep.set_value(stats["avg_sleep"], "avg per night")
        self.consistency.set_value(stats["consistency"], "bedtime regularity")
        self.sleep_dbt.set_value(stats["sleep_debt"], "vs 8h target")
        self.streak.set_value(stats["streak"], "days in a row")

    def onAddButtonClicked(self):
        dialog = AddSleepEntryDialog(self)
        if dialog.exec():
            log = dialog.get_data()
            self.sleep_logs.append(log)
            save_sleep_logs(self.sleep_logs)
            self.history.reload(self.sleep_logs)
            self.update_statistics()

            
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
