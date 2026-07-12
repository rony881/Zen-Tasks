from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout
from qfluentwidgets import CaptionLabel, CardWidget, IconWidget,StrongBodyLabel


class StatsCard(CardWidget):
    def __init__(self, parent, icon, title: str):
        super().__init__(parent)
        
        layout = QVBoxLayout(self)
        self.setFixedHeight(112)
        layout.setContentsMargins(16, 14, 16, 12)
        layout.setSpacing(4)
        
        # ========= Top Area ========
        top = QHBoxLayout()
        top.setSpacing(6)

        # -------- Icon ---------
        icon_w = IconWidget(icon, self)
        icon_w.setFixedSize(15, 15)
        top.addWidget(icon_w)
        
        # -------- Title --------
        top.addWidget(CaptionLabel(title, self))
        top.addStretch(1)
        layout.addLayout(top)

        # ------- Value Label ------
        self.valueLabel = StrongBodyLabel("_", self)
        self.valueLabel.setStyleSheet("""
            font-size:25px;
            color:#3a3a3a;
            """)
        layout.addWidget(self.valueLabel)
        
        self.subLabel = CaptionLabel("", self)
        self.subLabel.setTextColor("#606060", "#c0c0c0")
        layout.addWidget(self.subLabel)
        layout.addStretch(1)

    def set_Value(self, value: str, sub: str):
        self.valueLabel.setText(value)
        self.subLabel.setText(sub)
                