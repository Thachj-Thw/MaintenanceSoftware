from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import QTimer, QThread, Signal
from PySide6.QtGui import QTextCursor
from UI.ui_main import Ui_MainWindow
from UI.ui_disk_info import Ui_DiskInfo
import sys
from Maintenance import clean, DiskInfoStruct, get_all_disk, auto_format
from dataclasses import dataclass



class DiskInfo(QWidget, Ui_DiskInfo):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setupUi(self)



class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.btn_clean.clicked.connect(self._on_btn_clean_clicked)
        self.btn_check.clicked.connect(self._on_btn_check_clicked)
        self.btn_upgrade.clicked.connect(self._on_btn_upgrade_clicked)
        self.btn_start_clean.clicked.connect(self._on_btn_start_clean_clicked)
        self.btn_refresh.clicked.connect(self._show_disk_info)
        self._show_disk_info()
        self._thread = None
        self.clean_size = 0
    

    def _show_disk_info(self) -> None:
        for widget in self.disk_info_area.children():
            if isinstance(widget, DiskInfo):
                self.verticalLayout_area.removeWidget(widget)
                widget.deleteLater()
        for disk in get_all_disk():
            self.add_disk_info(disk)

    def _on_btn_clean_clicked(self) -> None:
        self.stackedWidget.setCurrentWidget(self.clean)

    def _on_btn_check_clicked(self) -> None:
        self.stackedWidget.setCurrentWidget(self.disk_status)

    def _on_btn_upgrade_clicked(self) -> None:
        self.stackedWidget.setCurrentWidget((self.upgrade))

    def _on_btn_start_clean_clicked(self) -> None:
        if not self._thread:
            self.btn_start_clean.setEnabled(False)
            self.clean_size = 0
            self._thread = WorkerClean()
            self._thread.one_success.connect(self._print_output)
            self._thread.error.connect(self._on_clean_error)
            self._thread.end.connect(self._on_clean_end)
            self._thread.start()
        
    def _print_output(self, f: clean.CleanStruct) -> None:
        if f.message:
            self._log(f'[ERROR] {f.filepath} {f.message}', "#cf2727")
        else:
            self._log(f'{f.filename} remove successfully', "#27cf57")
            self.clean_size += f.size

    def _on_clean_error(self, error: str) -> None:
        self._log(error, "#cf2727", True)
        self.btn_start_clean.setEnabled(True)
        self._thread = None
        print(error)

    def _on_clean_end(self) -> None:
        self._log(f"Free {auto_format(self.clean_size)}", "#000000", True)
        self.btn_start_clean.setEnabled(True)
        self._thread = None

    def _log(self, text: str, color: str, bold: bool = False) -> None:
        self.text_output.insertHtml(self.color_html(text, color, bold))
        cursor = self.text_output.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        self.text_output.setTextCursor(cursor)

    @staticmethod
    def color_html(text: str, color: str, bold: bool) -> str:
        return f'<span style="font-size: 13px; font-weight: {str(600) if bold else str(400)}; color: {color}; font-style: normal; white-space: pre-wrap;">{text}\n</span>'


    def add_disk_info(self, data: DiskInfoStruct) -> None:
        widget = DiskInfo(self.disk_info_area)
        widget.label_name.setText(data.name)
        widget.label_caption.setText(data.caption)
        widget.label_status.setText(data.status)
        self.verticalLayout_area.addWidget(widget)



class WorkerClean(QThread):
    
    one_success = Signal(clean.CleanStruct)
    end = Signal()
    error = Signal(str)
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    
    def run(self) -> None:
        try:
            for msg in clean.clean_temp():
                self.one_success.emit(msg)
            for msg in clean.clean_prefetch():
                self.one_success.emit(msg)
            for msg in clean.clean_recent():
                self.one_success.emit(msg)
            self.end.emit()
        except Exception as e:
            self.error.emit(str(e))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())