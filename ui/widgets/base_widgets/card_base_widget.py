from PyQt6.QtWidgets import (
    QBoxLayout,
    QLayout,
    QWidget,
)
from qfluentwidgets import CardWidget
from config import UI_CONFIG
HEIGHT = UI_CONFIG["card_height"]


class CardBaseWidget(CardWidget):
    """Base widget for creating UI cards."""
    def __init__(self):
        super().__init__()

        self.setFixedHeight(self.cardHeight())

        self.main_layout = self.createDefaultLayout(self)
        self.main_layout.setSpacing(12)
        self.main_layout.setContentsMargins(12, 8, 12, 8)

    def cardHeight(self) -> int:
        return HEIGHT

    def createDefaultLayout(self, parent: QWidget) -> QBoxLayout:
        """Return the card's default layout."""
        raise NotImplementedError(
            f"{type(self).__name__} must implement createDefaultLayout()"
        )

    def setContentsMargin(
        self,
        left: int = 12,
        top: int = 8,
        right: int = 12,
        bottom: int = 8,
    ) -> None:
        self.main_layout.setContentsMargins(left, top, right, bottom)

    def addWidget(self, widget: QWidget) -> None:
        self.main_layout.addWidget(widget)

    def addLayout(self, layout: QLayout) -> None:
        self.main_layout.addLayout(layout)