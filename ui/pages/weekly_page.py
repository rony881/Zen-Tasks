from sched import scheduler

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QFrame, QGridLayout, QInputDialog,QTabWidget
)
from PyQt6.QtCore import Qt
from ui.widgets.card import TaskCard
from qfluentwidgets import SimpleCardWidget,TitleLabel, TabBar

schedule = {
    "Morning" : ["Reading", "Drawing", "Meditation"],
    "AfterNoon" : ["Exercise", "Drawing", "Meditation"],
    "Knight" : ["Reading", "Leg Day", "Meditation"]
}

week = ["Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"]

class WeeklyTab(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        # ================
        # Header / Title
        # ================
        title = TitleLabel("Weekly Schedule")
        self.layout.addWidget(title)

        # ================
        # Tabbar
        #================
        tabs = QTabWidget()
        for day in week:
            tabs.addTab(DayWidget(schedule),day)

        self.layout.addWidget(tabs)

class DayWidget(QWidget):
    def __init__(self, routine):
        super().__init__()

        self.layout = QVBoxLayout(self)

        for time, tasks in routine.items():
            for task in tasks:
                card = TaskCard(task, time)
                self.layout.addWidget(card)


        

