from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout
from qfluentwidgets import CaptionLabel, CardWidget,StrongBodyLabel


class StatsCard(CardWidget):
    def __init__(self, parent,title,value,subtitle):
        super().__init__(parent)
        # self.setFixedSize(270, 170)
        
        layout = QVBoxLayout(self)
        
        top = QHBoxLayout()
        titleLabel = CaptionLabel(title)
        top.addWidget(titleLabel)
        top.addStretch()

        valueLabel = StrongBodyLabel(value)
        valueLabel.setStyleSheet("font-size:32px;color:#555;")
        
        subtitleLabel = CaptionLabel(subtitle)

        layout.addLayout(top)
        layout.addWidget(valueLabel)
        layout.addWidget(subtitleLabel)
        