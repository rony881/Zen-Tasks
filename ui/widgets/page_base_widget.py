from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget
from qfluentwidgets import FluentIcon, PrimaryPushButton, StrongBodyLabel, TitleLabel
from ui.theme import ADD_BTN_STYLE, TITLE_STYLE


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

    def addTitle(self, title: str, *buttons):
        title_layout = QHBoxLayout()
        title_layout.addWidget(self.buildTitle(title))
        title_layout.addStretch(1)

        if buttons:
            for button in buttons:
                title_layout.addWidget(button)

        self.addLayout(title_layout)
 

    def buildTitle(self, title: str) -> StrongBodyLabel:
        return StrongBodyLabel(title)

    def onAddButtonClicked(self):
        """
        Override this method to decide what happen 
        if add button is clicked
        """
        ...