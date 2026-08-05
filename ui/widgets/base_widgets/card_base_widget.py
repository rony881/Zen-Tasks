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

        self.setStyleSheet(
            """
            CardWidget{
                border: 1px solid #999999;
                border-radius: 6px;
            }
            """
        )

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

    def add(self, item) -> None:
        """Add a widget or layout to the Card."""
        if isinstance(item, QWidget):
            self.main_layout.addWidget(item)
        elif isinstance(item, QLayout):
            self.main_layout.addLayout(item)
        else:
            raise TypeError(
                f"Expected QWidget or QLayout, got {type(item).__name__}"
            )