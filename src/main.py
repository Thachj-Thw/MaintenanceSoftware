from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QTextCursor
from UI.ui_main import Ui_MainWindow
from UI.ui_disk_info import Ui_DiskInfo
from UI.customs import TitleBar
import sys
import os
from Maintenance import clean, DiskInfoStruct, get_all_disk, auto_format, detect_car_parking_folder
from Config import Config
import module


__version__ = "0.0.1"



class DiskInfo(QWidget, Ui_DiskInfo):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setupUi(self)



class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Maintenance Sofware")
        self.label_version.setText("Version " + __version__)
        TitleBar.setup(self, self.title, self.frame_title, 
                       self.btn_min, self.btn_max, self.btn_exit, self.frame_btn, None,
                       self.size_up, self.size_right, self.size_right_down, self.size_down, self.size_left_down, self.size_left)

        self.btn_clean.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.clean))
        self.btn_check.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.disk_status))
        self.btn_upgrade.clicked.connect(lambda: self.stackedWidget.setCurrentWidget((self.upgrade)))
        self.btn_setting.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.setting))
        self.btn_browse.clicked.connect(self._on_btn_browse_clicked)

        self.btn_start_clean.clicked.connect(self._on_btn_start_clean_clicked)
        self.btn_refresh.clicked.connect(self._show_disk_info)
        self._show_disk_info()
        self._thread = None
        self.clean_size = 0
        self.lineEdit.setText(detect_car_parking_folder())
        self.config = Config("setting")
        self.config.setup(
            ("check_temp", self.checkBox_temp.isChecked, self.checkBox_temp.setChecked, True),
            ("check_prefetch", self.checkBox_prefetch.isChecked, self.checkBox_prefetch.setChecked, True),
            ("check-recent", self.checkBox_recent.isChecked, self.checkBox_recent.setChecked, True),
            ("check-backup", self.checkBox_backup.isChecked, self.checkBox_backup.setChecked, True)
        )
        self.config.load()
        self.checkBox_temp.checkStateChanged.connect(self.config.upgrade)
        self.checkBox_prefetch.checkStateChanged.connect(self.config.upgrade)
        self.checkBox_recent.checkStateChanged.connect(self.config.upgrade)
        self.checkBox_backup.checkStateChanged.connect(self.config.upgrade)
    
    def _on_btn_browse_clicked(self):
        if path := QFileDialog.getExistingDirectory(None, "Chọn thư mục phần mềm CarParking", ""):
            self.lineEdit.setText(path)

    def _show_disk_info(self) -> None:
        for widget in self.disk_info_area.children():
            if isinstance(widget, DiskInfo):
                self.verticalLayout_area.removeWidget(widget)
                widget.deleteLater()
        for disk in get_all_disk():
            self.add_disk_info(disk)

    def _on_btn_start_clean_clicked(self) -> None:
        if not self._thread:
            self.btn_start_clean.setEnabled(False)
            self.clean_size = 0
            self._thread = WorkerClean(
                self.checkBox_temp.isChecked(), self.checkBox_prefetch.isChecked(), 
                self.checkBox_recent.isChecked(), self.checkBox_backup.isChecked(), 
                os.path.join(self.lineEdit.text(), "BackupDatabase")
            )
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

    def _on_clean_end(self) -> None:
        self._log(f"Free {auto_format(self.clean_size)}", "#b5a4d4", True)
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
        widget.label_status.setText("Status\n" + data.status)
        if data.status == "OK":
            widget.label_status.setStyleSheet("color: #27cf57")
        elif data.status == "caution":
            widget.label_status.setStyleSheet("color: #ff8800")
        elif data.status == "bad":
            widget.label_status.setStyleSheet("color: #cf2727")
        self.verticalLayout_area.addWidget(widget)


class WorkerClean(QThread):
    
    one_success = Signal(clean.CleanStruct)
    end = Signal()
    error = Signal(str)
    def __init__(self, temp: bool, prefetch: bool, recent: bool, backup: bool, backup_dir: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.temp = temp
        self.prefetch = prefetch
        self.recent = recent
        self.backup = backup
        self.backup_dir = backup_dir
    
    def run(self) -> None:
        try:
            if self.temp:
                for msg in clean.clean_temp():
                    self.one_success.emit(msg)
        except Exception as e:
            self.error.emit(str(e))
        try:
            if self.prefetch:
                for msg in clean.clean_prefetch():
                    self.one_success.emit(msg)
        except Exception as e:
            self.error.emit(str(e))
        try:
            if self.recent:
                for msg in clean.clean_recent():
                    self.one_success.emit(msg)
        except Exception as e:
            self.error.emit(str(e))
        try:
            if self.backup:
                for msg in clean.clean_backup_database(self.backup_dir):
                    self.one_success.emit(msg)
        except Exception as e:
            self.error.emit(str(e))
        self.end.emit()





if __name__ == "__main__":
    module.hide_console()
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
