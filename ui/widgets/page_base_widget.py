from PyQt6.QtWidgets import QFrame, QHBoxLayout, QScrollArea, QTabWidget, QVBoxLayout, QWidget
from qfluentwidgets import FluentIcon, PrimaryPushButton, StrongBodyLabel, TableWidget, TitleLabel
from ui.theme import ADD_BTN_STYLE, TAB_WIDG_STYLE, TITLE_STYLE


class PageBaseWidget(QWidget):
    """Page Base Widget for making Pages"""

    def __init__(self,parent):
        super().__init__(parent)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(24, 1, 24, 24)
        self.main_layout.setSpacing(16)

    def setPageType(self,type):
        self.page_type = type
        
    def setPageHeader(self,header: str, button: str | None = None): 
        self.main_layout.addLayout(self.headerFrame(header, button))

    def headerFrame(self,header: str, button: str | None = None):
        header_lout = QHBoxLayout()
        
        hdr = TitleLabel(header)
        hdr.setStyleSheet(TITLE_STYLE)
        header_lout.addWidget(hdr)
        header_lout.addStretch(1)
        
        if button is not None:
            self.add_btn = PrimaryPushButton(FluentIcon.ADD,"    " + button)
            self.add_btn.setStyleSheet(ADD_BTN_STYLE)
            self.add_btn.clicked.connect(self.onAddButtonClicked)
            header_lout.addWidget(self.add_btn)

        return header_lout
        
    def addWidget(self,widget: QWidget):
        self.main_layout.addWidget(widget)
        
    def addLayout(self,layout):
        self.main_layout.addLayout(layout)

    def addStretch(self):
        self.main_layout.addStretch()

    def onAddButtonClicked(self) -> None:
        """
        Override this method to decide what happen 
        if add button is clicked
        """
        ...
        
    def addTitle(self, title: str, *buttons):
        title_layout = QHBoxLayout()
        title_layout.addWidget(self.buildTitle(title))
        title_layout.addStretch(1)

        if buttons:
            for button in buttons:
                title_layout.addWidget(button)

        self.addLayout(title_layout)

    def buildTitle(self, title: str) -> StrongBodyLabel:
        """ Build a Title and return Title as a Label """
        return StrongBodyLabel(title)

    def addListContainer(self):
        list_container = self._buildContainerWidget()
        self.list_layout = QVBoxLayout(list_container)
        self.list_layout.setContentsMargins(6, 4, 6, 4)
        self.list_layout.setSpacing(8)
        scroll_area = self.buildScrollArea(list_container)

        self.addWidget(scroll_area)
        
    def _buildContainerWidget(self) -> QWidget:
        container = QWidget()
        container.setStyleSheet("background: transparent;")
        return container

    def buildScrollArea(self, widget):
        """"Build a QScrollArea, add Widget and return the ScrollArea"""
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        scroll_area.setStyleSheet("QScrollArea{background: transparent; border: none;}")
        scroll_area.setWidget(widget)

        return scroll_area

    def buildTableWidget(self, hdr_lbls: list[str]) -> TableWidget:
        table = TableWidget()
        table.setColumnCount(len(hdr_lbls))
        table.setHorizontalHeaderLabels(hdr_lbls)
        table.setMouseTracking(False)
        table.setShowGrid(False)

        return table

    def buildTabWidget(self) -> QTabWidget:
        tab_widget = QTabWidget()
        tab_widget.setDocumentMode(True)
        tab_widget.setStyleSheet(TAB_WIDG_STYLE)

        return tab_widget