# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainbwMhkZ.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)
from . import source_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(836, 539)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	background-color: transparent;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QFrame {\n"
"	color: #b5a4d4;\n"
"}\n"
"\n"
"#centralwidget {\n"
"	background-color: #121212;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #5e559e;\n"
"	color: #ffffff;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	padding: 12px;\n"
"	font-size: 15px\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled {\n"
"	color: #cccbd4;\n"
"	background-color: #413b6e;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #ae99d1;\n"
"}\n"
"\n"
"QTextEdit, QScrollArea {\n"
"	border: 1px solid #5e559e;\n"
"	border-radius: 5px;\n"
"	padding: 8px;\n"
"}\n"
"\n"
"QStackedWidget {\n"
"	background-color: #19181a;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: transparent;\n"
"    width: 15px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgba(255, 255, 255, 0.1);\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #4e4a4f;\n"
"}\n"
"\n"
"QScrollBar::a"
                        "dd-line:vertical {\n"
"    border: none;\n"
"    background: transparent;\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: transparent;\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar:left-arrow:vertical, QScrollBar::right-arrow:vertical {\n"
"    border: none;\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: transparent;\n"
"}\n"
"\n"
"DiskInfo {\n"
"	border-bottom: 1px solid #5e559e;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-position: top left;\n"
"	left: 15px;\n"
"}\n"
"\n"
"QGroupBox {\n"
"	color: #b5a4d4;\n"
"	border: 1px solid #5e559e;\n"
"	border-radius: 6px;\n"
"	margin-top: 3ex;\n"
"	font-weight: bold;\n"
""
                        "	padding-top: 12px;\n"
"}\n"
"\n"
"QCheckBox {\n"
"	color: #b5a4d4;\n"
"	padding-bottom: 8px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	width: 30px;\n"
"	height: 30px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	width: 18px;\n"
"	height: 18px;\n"
"	padding: 6px;\n"
"	image: url(:/icons/cil-task.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"	image: url(:/icons/cil-media-stop.png);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: 1px solid #5e559e;\n"
"	border-radius: 5px;\n"
"	padding: 8px 5px 8px 5px;\n"
"	color: #b5a4d4;\n"
"}\n"
"\n"
"#btn_browse {\n"
"	width: 32px;\n"
"	height: 28px;\n"
"	font-weight: bold;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"#btn_start_clean {\n"
"	font-weight: bold;\n"
"	font-size: 20px\n"
"}\n"
"\n"
"#btn_refresh {\n"
"	padding-top: 5px;\n"
"	padding-bottom: 5px;\n"
"}\n"
"\n"
"#label_title {\n"
"	padding: 0px;\n"
"	font-size: 20px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"#btn_exit, #btn_max, #btn_min {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	border-radius: no"
                        "ne;\n"
"	width: 30px;\n"
"	height: 20px;\n"
"	padding: 0.2em 0.5em 0.2em 0.5em;\n"
"}\n"
"\n"
"#btn_max:hover, #btn_min:hover {\n"
"	background-color: #292929;\n"
"}\n"
"\n"
"#btn_exit:hover {\n"
"	background-color: #d4443c;\n"
"}\n"
"\n"
"#btn_min {\n"
"    image: url(:/icons/cil-window-minimize.png);\n"
"}\n"
"\n"
"#btn_max:!checked {\n"
"    image: url(:/icons/cil-window-maximize.png);\n"
"}\n"
"\n"
"#btn_max:checked {\n"
"    image: url(:/icons/cil-window-restore.png);\n"
"}\n"
"\n"
"#btn_exit {\n"
"    image: url(:/icons/cil-x.png);\n"
"}\n"
"\n"
"#label_version {\n"
"	font-size: 13px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title = QFrame(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setFrameShape(QFrame.Shape.StyledPanel)
        self.title.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.title)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.title)
        self.frame_title.setObjectName(u"frame_title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_title.sizePolicy().hasHeightForWidth())
        self.frame_title.setSizePolicy(sizePolicy)
        self.frame_title.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_title)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_up_left = QFrame(self.frame_title)
        self.frame_up_left.setObjectName(u"frame_up_left")
        self.frame_up_left.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_up_left.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_up_left)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.size_up_left = QFrame(self.frame_up_left)
        self.size_up_left.setObjectName(u"size_up_left")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.size_up_left.sizePolicy().hasHeightForWidth())
        self.size_up_left.setSizePolicy(sizePolicy1)
        self.size_up_left.setMinimumSize(QSize(5, 5))
        self.size_up_left.setMaximumSize(QSize(5, 5))
        self.size_up_left.setFrameShape(QFrame.Shape.StyledPanel)
        self.size_up_left.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_9.addWidget(self.size_up_left)

        self.size_up = QFrame(self.frame_up_left)
        self.size_up.setObjectName(u"size_up")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.size_up.sizePolicy().hasHeightForWidth())
        self.size_up.setSizePolicy(sizePolicy2)
        self.size_up.setMinimumSize(QSize(5, 5))
        self.size_up.setMaximumSize(QSize(16777215, 5))
        self.size_up.setFrameShape(QFrame.Shape.StyledPanel)
        self.size_up.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_9.addWidget(self.size_up)


        self.verticalLayout_9.addWidget(self.frame_up_left)

        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")

        self.verticalLayout_9.addWidget(self.label_title)


        self.horizontalLayout_6.addWidget(self.frame_title)

        self.frame_btn = QFrame(self.title)
        self.frame_btn.setObjectName(u"frame_btn")
        self.frame_btn.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_btn.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_btn)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_min = QPushButton(self.frame_btn)
        self.btn_min.setObjectName(u"btn_min")

        self.horizontalLayout_7.addWidget(self.btn_min)

        self.btn_max = QPushButton(self.frame_btn)
        self.btn_max.setObjectName(u"btn_max")

        self.horizontalLayout_7.addWidget(self.btn_max)

        self.btn_exit = QPushButton(self.frame_btn)
        self.btn_exit.setObjectName(u"btn_exit")

        self.horizontalLayout_7.addWidget(self.btn_exit)


        self.horizontalLayout_6.addWidget(self.frame_btn, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout.addWidget(self.title)

        self.size_left_right = QFrame(self.centralwidget)
        self.size_left_right.setObjectName(u"size_left_right")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.size_left_right.sizePolicy().hasHeightForWidth())
        self.size_left_right.setSizePolicy(sizePolicy3)
        self.size_left_right.setFrameShape(QFrame.Shape.StyledPanel)
        self.size_left_right.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.size_left_right)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.size_left = QFrame(self.size_left_right)
        self.size_left.setObjectName(u"size_left")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.size_left.sizePolicy().hasHeightForWidth())
        self.size_left.setSizePolicy(sizePolicy4)
        self.size_left.setMinimumSize(QSize(5, 5))
        self.size_left.setMaximumSize(QSize(5, 16777215))
        self.size_left.setFrameShape(QFrame.Shape.StyledPanel)
        self.size_left.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_4.addWidget(self.size_left)

        self.frame_7 = QFrame(self.size_left_right)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy3.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy3)
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_7)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.body = QFrame(self.frame_7)
        self.body.setObjectName(u"body")
        self.body.setFrameShape(QFrame.Shape.StyledPanel)
        self.body.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.body)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.body)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_10 = QFrame(self.frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_clean = QPushButton(self.frame_10)
        self.btn_clean.setObjectName(u"btn_clean")

        self.verticalLayout_14.addWidget(self.btn_clean)

        self.btn_check = QPushButton(self.frame_10)
        self.btn_check.setObjectName(u"btn_check")

        self.verticalLayout_14.addWidget(self.btn_check)

        self.btn_upgrade = QPushButton(self.frame_10)
        self.btn_upgrade.setObjectName(u"btn_upgrade")

        self.verticalLayout_14.addWidget(self.btn_upgrade)


        self.verticalLayout_2.addWidget(self.frame_10, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.btn_setting = QPushButton(self.frame_2)
        self.btn_setting.setObjectName(u"btn_setting")

        self.verticalLayout_13.addWidget(self.btn_setting)

        self.label_version = QLabel(self.frame_2)
        self.label_version.setObjectName(u"label_version")

        self.verticalLayout_13.addWidget(self.label_version)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame)

        self.stackedWidget = QStackedWidget(self.body)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.clean = QWidget()
        self.clean.setObjectName(u"clean")
        self.verticalLayout_3 = QVBoxLayout(self.clean)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_3 = QFrame(self.clean)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.btn_start_clean = QPushButton(self.frame_8)
        self.btn_start_clean.setObjectName(u"btn_start_clean")
        self.btn_start_clean.setEnabled(True)
        self.btn_start_clean.setCheckable(False)
        self.btn_start_clean.setAutoDefault(False)

        self.verticalLayout_8.addWidget(self.btn_start_clean)


        self.horizontalLayout.addWidget(self.frame_8)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.clean)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.text_output = QTextEdit(self.frame_6)
        self.text_output.setObjectName(u"text_output")
        self.text_output.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.text_output)


        self.verticalLayout_4.addWidget(self.frame_6)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.clean)
        self.upgrade = QWidget()
        self.upgrade.setObjectName(u"upgrade")
        self.verticalLayout_7 = QVBoxLayout(self.upgrade)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.upgrade)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.upgrade)
        self.setting = QWidget()
        self.setting.setObjectName(u"setting")
        self.verticalLayout_15 = QVBoxLayout(self.setting)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_13 = QFrame(self.setting)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_13)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_11 = QFrame(self.frame_13)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lineEdit = QLineEdit(self.frame_11)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_8.addWidget(self.lineEdit)

        self.btn_browse = QPushButton(self.frame_11)
        self.btn_browse.setObjectName(u"btn_browse")

        self.horizontalLayout_8.addWidget(self.btn_browse)


        self.verticalLayout_17.addWidget(self.frame_11)

        self.groupBox = QGroupBox(self.frame_13)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_16 = QVBoxLayout(self.groupBox)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.checkBox_temp = QCheckBox(self.groupBox)
        self.checkBox_temp.setObjectName(u"checkBox_temp")
        self.checkBox_temp.setChecked(True)

        self.verticalLayout_16.addWidget(self.checkBox_temp)

        self.checkBox_prefetch = QCheckBox(self.groupBox)
        self.checkBox_prefetch.setObjectName(u"checkBox_prefetch")
        self.checkBox_prefetch.setChecked(True)

        self.verticalLayout_16.addWidget(self.checkBox_prefetch)

        self.checkBox_recent = QCheckBox(self.groupBox)
        self.checkBox_recent.setObjectName(u"checkBox_recent")
        self.checkBox_recent.setChecked(True)

        self.verticalLayout_16.addWidget(self.checkBox_recent)

        self.checkBox_backup = QCheckBox(self.groupBox)
        self.checkBox_backup.setObjectName(u"checkBox_backup")
        self.checkBox_backup.setChecked(True)

        self.verticalLayout_16.addWidget(self.checkBox_backup)


        self.verticalLayout_17.addWidget(self.groupBox)


        self.verticalLayout_15.addWidget(self.frame_13, 0, Qt.AlignmentFlag.AlignTop)

        self.stackedWidget.addWidget(self.setting)
        self.disk_status = QWidget()
        self.disk_status.setObjectName(u"disk_status")
        self.verticalLayout_10 = QVBoxLayout(self.disk_status)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_9 = QFrame(self.disk_status)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_refresh = QPushButton(self.frame_9)
        self.btn_refresh.setObjectName(u"btn_refresh")

        self.horizontalLayout_3.addWidget(self.btn_refresh)


        self.verticalLayout_10.addWidget(self.frame_9, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)

        self.scrollArea = QScrollArea(self.disk_status)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 67, 38))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.disk_info_area = QFrame(self.scrollAreaWidgetContents)
        self.disk_info_area.setObjectName(u"disk_info_area")
        self.disk_info_area.setFrameShape(QFrame.Shape.StyledPanel)
        self.disk_info_area.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_area = QVBoxLayout(self.disk_info_area)
        self.verticalLayout_area.setObjectName(u"verticalLayout_area")

        self.verticalLayout_11.addWidget(self.disk_info_area, 0, Qt.AlignmentFlag.AlignTop)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_10.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.disk_status)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout_12.addWidget(self.body)


        self.horizontalLayout_4.addWidget(self.frame_7)

        self.size_right = QFrame(self.size_left_right)
        self.size_right.setObjectName(u"size_right")
        sizePolicy4.setHeightForWidth(self.size_right.sizePolicy().hasHeightForWidth())
        self.size_right.setSizePolicy(sizePolicy4)
        self.size_right.setMinimumSize(QSize(5, 5))
        self.size_right.setMaximumSize(QSize(5, 16777215))
        self.size_right.setFrameShape(QFrame.Shape.StyledPanel)
        self.size_right.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_4.addWidget(self.size_right)


        self.verticalLayout.addWidget(self.size_left_right)

        self.size_bottom = QFrame(self.centralwidget)
        self.size_bottom.setObjectName(u"size_bottom")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.size_bottom.sizePolicy().hasHeightForWidth())
        self.size_bottom.setSizePolicy(sizePolicy5)
        self.size_bottom.setFrameShape(QFrame.Shape.StyledPanel)
        self.size_bottom.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.size_bottom)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.size_left_down = QFrame(self.size_bottom)
        self.size_left_down.setObjectName(u"size_left_down")
        sizePolicy1.setHeightForWidth(self.size_left_down.sizePolicy().hasHeightForWidth())
        self.size_left_down.setSizePolicy(sizePolicy1)
        self.size_left_down.setMinimumSize(QSize(5, 5))
        self.size_left_down.setMaximumSize(QSize(5, 5))
        self.size_left_down.setFrameShape(QFrame.Shape.StyledPanel)
        self.size_left_down.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_5.addWidget(self.size_left_down)

        self.size_down = QFrame(self.size_bottom)
        self.size_down.setObjectName(u"size_down")
        sizePolicy2.setHeightForWidth(self.size_down.sizePolicy().hasHeightForWidth())
        self.size_down.setSizePolicy(sizePolicy2)
        self.size_down.setMinimumSize(QSize(5, 5))
        self.size_down.setMaximumSize(QSize(16777215, 5))
        self.size_down.setFrameShape(QFrame.Shape.StyledPanel)
        self.size_down.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_5.addWidget(self.size_down)

        self.size_right_down = QFrame(self.size_bottom)
        self.size_right_down.setObjectName(u"size_right_down")
        sizePolicy1.setHeightForWidth(self.size_right_down.sizePolicy().hasHeightForWidth())
        self.size_right_down.setSizePolicy(sizePolicy1)
        self.size_right_down.setMinimumSize(QSize(5, 5))
        self.size_right_down.setMaximumSize(QSize(5, 5))
        self.size_right_down.setFrameShape(QFrame.Shape.StyledPanel)
        self.size_right_down.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_5.addWidget(self.size_right_down)


        self.verticalLayout.addWidget(self.size_bottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"   Ph\u1ea7n m\u1ec1m b\u1ea3o tr\u00ec", None))
        self.btn_min.setText("")
        self.btn_max.setText("")
        self.btn_exit.setText("")
        self.btn_clean.setText(QCoreApplication.translate("MainWindow", u"D\u1ecdn r\u00e1c", None))
        self.btn_check.setText(QCoreApplication.translate("MainWindow", u"Ki\u1ec3m tra \u1ed5 c\u1ee9ng", None))
        self.btn_upgrade.setText(QCoreApplication.translate("MainWindow", u"N\u00e2ng c\u1ea5p ph\u1ea7n m\u1ec1m", None))
        self.btn_setting.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"Version 0.0.1", None))
        self.btn_start_clean.setText(QCoreApplication.translate("MainWindow", u"B\u1eaft \u0110\u1ea7u D\u1ecdn R\u00e1c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ea7u ra", None))
        self.text_output.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:16px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Coming soon", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0110\u01b0\u1eddng d\u1eabn t\u1edbi th\u01b0 m\u1ee5c ph\u1ea7n m\u1ec1m CarParking", None))
        self.btn_browse.setText(QCoreApplication.translate("MainWindow", u". . .", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"C\u00e1ch d\u1ecdn r\u00e1c", None))
        self.checkBox_temp.setText(QCoreApplication.translate("MainWindow", u"D\u1ecdn th\u01b0 m\u1ee5c Temp", None))
        self.checkBox_prefetch.setText(QCoreApplication.translate("MainWindow", u"D\u1ecdn th\u01b0 m\u1ee5c Prefetch", None))
        self.checkBox_recent.setText(QCoreApplication.translate("MainWindow", u"D\u1ecdn th\u01b0 m\u1ee5c Recent", None))
        self.checkBox_backup.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ec9 gi\u1eef 1 file backup database", None))
        self.btn_refresh.setText(QCoreApplication.translate("MainWindow", u"L\u00e0m m\u1edbi", None))
    # retranslateUi

