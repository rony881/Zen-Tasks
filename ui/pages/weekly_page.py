from tkinter import Widget

from PyQt6.QtWidgets import (
    QLabel,
    QPushButton,
    QWidget,
    QFrame,
    QHBoxLayout,
    QVBoxLayout,
    QTabWidget
)

days = ["SAT","SUN","MON","TUE","WED","THU","FRI"]
dummy_tasks = ["Reading","Study","Maditate","Workout","Art"]

class Tab_Panel(QTabWidget):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
    
    def add_tab(self,widget,tab_name):
        self.addTab(widget,tab_name)


class Weekly_Tab(QFrame):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent

        layout = QVBoxLayout(self)
        tab = Tab_Panel(self) 

        for day in days:
            tab.add_tab(Daily_page(dummy_tasks),day)
        
        layout.addWidget(tab)

class Daily_page(QWidget):
    def __init__(self, tasks):
        super().__init__()

        layout = QVBoxLayout(self)

        for task in tasks:
            layout.addWidget(QLabel(task))

        layout.addStretch()

        add_btn = QPushButton("+ New")
        layout.addWidget(add_btn)
