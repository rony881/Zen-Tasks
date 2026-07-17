from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget
from qfluentwidgets import FluentIcon, PrimaryPushButton, TitleLabel
from ui.theme import ADD_BTN_STYLE, TITLE_STYLE


class PageBaseWidget(QWidget):
    """Page Base Widget for making Pages"""

    def __init__(self,parent):
        super().__init__(parent)
        self.page_layout = QVBoxLayout(self)
        self.page_layout.setContentsMargins(24, 1, 24, 24)

    def setPageType(self,type):
        self.page_type = type
        
    def setPageHeader(self,header: str, button: str | None = None): 
        self.page_layout.addLayout(self.headerFrame(header, button))

    def headerFrame(self,header: str, button: str | None = None):
        header_lout = QHBoxLayout(self)
        
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
        self.page_layout.addWidget(widget)
        
    def addLayout(self,layout):
        self.page_layout.addLayout(layout)

    def onAddButtonClicked(self):
        """
        Override this method to decide what happen 
        if add button is clicked
        """
        ...