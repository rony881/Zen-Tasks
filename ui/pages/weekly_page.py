from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout,QAbstractItemView,QHeaderView
)
from PyQt6.QtCore import Qt
from qfluentwidgets import TableWidget

class PlannerTable(TableWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self._setup_columns()

    def _setup_columns(self):

        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(["Time","Task","Shift"])

        hdr = self.horizontalHeader()
        hdr.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        hdr.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        hdr.setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)

        # Column Width
        self.setColumnWidth(0, 110)
        self.setColumnWidth(2, 150)
        self.verticalHeader().setVisible(False)
        self.verticalHeader().setDefaultSectionSize(46)

        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.setShowGrid(True)
        self.setAlternatingRowColors(False)
        self.setEditTriggers(
            QAbstractItemView.EditTrigger.DoubleClicked
            | QAbstractItemView.EditTrigger.SelectedClicked
        )
        self.viewport().setMouseTracking(True)