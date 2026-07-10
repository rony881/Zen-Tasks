from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout
from qfluentwidgets import CaptionLabel, CardWidget, IconWidget,StrongBodyLabel


class StatsCard(CardWidget):
    def __init__(self, parent, icon, title: str, value, subtitle: str):
        super().__init__(parent)
        # self.setFixedSize(270, 170)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 14, 16, 12)
        layout.setSpacing(4)
        
        # ========= Top Area ========
        top = QHBoxLayout()
        top.setSpacing(4)

        # -------- Icon ---------
        icon_w = IconWidget(icon, self)
        icon_w.setFixedSize(15, 15)
        top.addWidget(icon_w)

        # -------- Title --------
        titleLabel = CaptionLabel(title, self)
        top.addWidget(titleLabel)
        top.addStretch(1)

        layout.addLayout(top)

        # ------- Value Label ------
        valueLabel = StrongBodyLabel(value,self)
        valueLabel.setStyleSheet("""
            font-size:25px;
            color:#3a3a3a;
            """)
        layout.addWidget(valueLabel)
        
        subLabel = CaptionLabel(subtitle,self)
        subLabel.setTextColor("#606060", "#c0c0c0")
        layout.addWidget(subLabel)
        layout.addStretch(1)
                