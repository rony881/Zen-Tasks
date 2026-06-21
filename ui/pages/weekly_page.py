from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QFrame, QGridLayout, QInputDialog
)
from PyQt6.QtCore import Qt
from ui.widgets.card import TaskCard
from qfluentwidgets import SimpleCardWidget,TitleLabel, TabBar

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
        tabs = TabBar()
        tabs.addTab("Home","home")
        self.layout.addWidget(tabs)
