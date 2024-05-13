from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QTimer, QThread, Signal
from UI.ui_main import Ui_MainWindow
import sys


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.btn_clean.clicked.connect(self._on_btn_clean_clicked)
        self.btn_check.clicked.connect(self._on_btn_check_clicked)

    def _on_btn_clean_clicked(self):
        self.stackedWidget.setCurrentWidget(self.clean)
        pass

    def _on_btn_check_clicked(self):
        self.stackedWidget.setCurrentWidget(self.disk_status)
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())