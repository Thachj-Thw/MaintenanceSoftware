# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'disk_infonqDViQ.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_DiskInfo(object):
    def setupUi(self, DiskInfo):
        if not DiskInfo.objectName():
            DiskInfo.setObjectName(u"DiskInfo")
        DiskInfo.resize(575, 152)
        self.horizontalLayout = QHBoxLayout(DiskInfo)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_name = QLabel(DiskInfo)
        self.label_name.setObjectName(u"label_name")

        self.horizontalLayout.addWidget(self.label_name)

        self.label_caption = QLabel(DiskInfo)
        self.label_caption.setObjectName(u"label_caption")

        self.horizontalLayout.addWidget(self.label_caption)

        self.label_status = QLabel(DiskInfo)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_status)


        self.retranslateUi(DiskInfo)

        QMetaObject.connectSlotsByName(DiskInfo)
    # setupUi

    def retranslateUi(self, DiskInfo):
        DiskInfo.setWindowTitle(QCoreApplication.translate("DiskInfo", u"Form", None))
        self.label_name.setText(QCoreApplication.translate("DiskInfo", u"TextLabel", None))
        self.label_caption.setText(QCoreApplication.translate("DiskInfo", u"TextLabel", None))
        self.label_status.setText(QCoreApplication.translate("DiskInfo", u"TextLabel", None))
    # retranslateUi

