# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainKTTiTL.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(730, 596)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QFrame(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setFrameShape(QFrame.Shape.StyledPanel)
        self.title.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.title)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.title)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.frame_7 = QFrame(self.title)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_4 = QPushButton(self.frame_7)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_7.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_7)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_7.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_7)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_7.addWidget(self.pushButton_6)


        self.horizontalLayout_6.addWidget(self.frame_7)


        self.verticalLayout.addWidget(self.title)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_clean = QPushButton(self.frame)
        self.btn_clean.setObjectName(u"btn_clean")

        self.verticalLayout_2.addWidget(self.btn_clean)

        self.btn_check = QPushButton(self.frame)
        self.btn_check.setObjectName(u"btn_check")

        self.verticalLayout_2.addWidget(self.btn_check)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignTop)

        self.stackedWidget = QStackedWidget(self.frame_2)
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
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.text_output = QTextEdit(self.frame_6)
        self.text_output.setObjectName(u"text_output")

        self.verticalLayout_6.addWidget(self.text_output)


        self.verticalLayout_4.addWidget(self.frame_6)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.clean)
        self.disk_status = QWidget()
        self.disk_status.setObjectName(u"disk_status")
        self.verticalLayout_10 = QVBoxLayout(self.disk_status)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.scrollArea = QScrollArea(self.disk_status)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 554, 468))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_9 = QFrame(self.scrollAreaWidgetContents)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_11.addWidget(self.frame_9)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_10.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.disk_status)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Ph\u1ea7n m\u1ec1m b\u1ea3o tr\u00ec", None))
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.btn_clean.setText(QCoreApplication.translate("MainWindow", u"D\u1ecdn r\u00e1c", None))
        self.btn_check.setText(QCoreApplication.translate("MainWindow", u"Ki\u1ec3m tra \u1ed5 c\u1ee9ng", None))
        self.btn_start_clean.setText(QCoreApplication.translate("MainWindow", u"D\u1ecdn R\u00e1c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ea7u ra", None))
    # retranslateUi

