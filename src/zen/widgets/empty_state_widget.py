from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QSizePolicy
from qfluentwidgets import (
    BodyLabel,
    CaptionLabel,
    FluentIcon,
    IconWidget,
    PrimaryPushButton,
    StrongBodyLabel,
)

from zen.theme import ADD_BTN_STYLE


class EmptyStateWidget(QWidget):
    
    add_clicked = pyqtSignal()

    def __init__(
        self,
        title: str = "No tasks for today",
        subtitle: str = "Enjoy the free time, or add something to get done.",
        button_text: str = "Add Task",
        icon: FluentIcon = FluentIcon.CALENDAR,
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(10)

        icon_widget = IconWidget(icon, self)
        icon_widget.setFixedSize(56, 56)

        title_lbl = StrongBodyLabel(title, self)
        title_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        subtitle_lbl = CaptionLabel(subtitle, self)
        subtitle_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle_lbl.setWordWrap(True)
        subtitle_lbl.setStyleSheet("color: #8a8a8a;")

        self.add_btn = PrimaryPushButton(FluentIcon.ADD, "    " + button_text, self)
        self.add_btn.setStyleSheet(ADD_BTN_STYLE)
        self.add_btn.clicked.connect(self.add_clicked.emit)

        layout.addWidget(icon_widget, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(title_lbl)
        layout.addWidget(subtitle_lbl)
        layout.addSpacing(6)
        layout.addWidget(self.add_btn, alignment=Qt.AlignmentFlag.AlignHCenter)