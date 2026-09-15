import sys

from PyQt6.QtWidgets import QApplication

from zen.main_window import MainWindow
from zen.core.utils.logger import logger

# ==============================================
# Run Application
# ==============================================
if __name__ == "__main__":
    logger.info("Starting Application")
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    logger.info("Application Window Displayed")
    sys.exit(app.exec())