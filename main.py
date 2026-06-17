from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QFrame
)
import sys

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1200,900)
        self.central_widget = QWidget()
        self.central_widget.setStyleSheet(
            """
            background-color: #0a0a0a;
            """
        )
        self.setCentralWidget(self.central_widget)
        self.side_bar = QFrame()
        self.side_bar.setFixedWidth(250)
        self.side_bar.setStyleSheet(
            """
            background-color: #191919;
            """
        )

        self.central_panel = QFrame()
        self.central_panel.setStyleSheet(
            """
            background-color: #191919;
            """
        )

        self._setup_layout()
    def _setup_layout(self):
        self.main_layout = QHBoxLayout(self.central_widget)
        self.side_layout = QVBoxLayout(self.side_bar)

        self.main_layout.addWidget(self.side_bar)
        self.main_layout.addWidget(self.central_panel)




# ==============================================
# Run Application
# ==============================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec())