from PySide6.QtWidgets import QFrame, QPushButton, QLayout, QMainWindow, QGraphicsDropShadowEffect, QSizeGrip
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QColor, QCursor



class TitleBar(QMainWindow):

    def maximize_restore(self):
        if self._max.isChecked():
            self.showMaximized()
            if self._l_shadow:
                self._l_shadow.setContentsMargins(0, 0, 0, 0)
            if self._main:
                self._main.setStyleSheet("QFrame#main{border-radius: 0px;}")
            self._max.setToolTip("Restore Down")
        else:
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            if self._l_shadow:
                self._l_shadow.setContentsMargins(9, 9, 9, 9)
            if self._main:
                self._main.setStyleSheet("")
            self._max.setToolTip("Maximize")

    def update_pos(self, pos):
        self._drag_pos = pos

    def setup(
        self,
        frame_main: QFrame = None,
        frame_move: QFrame = None,
        btn_minimize: QPushButton = None,
        btn_maximize: QPushButton = None,
        btn_close: QPushButton = None,
        frame_btns: QFrame = None,
        layout_shadow: QLayout = None,
        size_top: QFrame = None,
        size_top_left: QFrame = None,
        size_right: QFrame = None,
        size_right_bottom: QFrame = None,
        size_bottom: QFrame = None,
        size_left_bottom: QFrame = None,
        size_left: QFrame = None
    ):
        self._main = frame_main
        self._move = frame_move
        self._min = btn_minimize
        self._max = btn_maximize
        self._close = btn_close
        self._f_btns = frame_btns
        self._l_shadow = layout_shadow
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        if self._main:
            self._main.setGraphicsEffect(
                QGraphicsDropShadowEffect(blurRadius=15, offset=QPoint(3, 3), color=QColor("#000")))

        if self._min:
            self._min.clicked.connect(lambda: self.showMinimized())
            self._min.setToolTip("Minimize")

        if self._max:
            self._max.setCheckable(True)
            self._max.clicked.connect(lambda: TitleBar.maximize_restore(self))
            self._max.setToolTip("Maximize")

        if self._close:
            self._close.clicked.connect(lambda: self.close())
            self._close.setToolTip("Close")

        def move_window(event):
            if event.buttons() == Qt.MouseButton.LeftButton:
                if self._max:
                    if self._max.isChecked():
                        self._max.setChecked(False)
                        ratio = event.x() / self.width()
                        TitleBar.maximize_restore(self)
                        w = self._f_btns.width() if self._f_btns else 0
                        x = min(self.width() - w, ratio * self.width())
                        self.move(event.globalPos() - QPoint(x, event.y() + 9 if self._l_shadow else event.y()))
                if hasattr(self, "_drag_pos"):
                    self.move(self.pos() + event.globalPos() - self._drag_pos)
                    self._drag_pos = event.globalPos()
                    event.accept()
                else:
                    event.ignore()

        def release_window(event):
            if self._max:
                if self.y() + event.y() <= 0 and not self._max.isChecked():
                    self._max.setChecked(True)
                    TitleBar.maximize_restore(self)

        if self._move:
            self._move.mouseMoveEvent = move_window
            self._move.mouseReleaseEvent = release_window
        self.mousePressEvent = lambda event: TitleBar.update_pos(self, event.globalPos())

        def size_move_top(event):
            if event.buttons() == Qt.MouseButton.LeftButton:
                y = event.globalPos().y()
                height = self.y() - y + self.height()
                if height > self.minimumHeight():
                    self.setGeometry(self.x(), y, self.width(), height)
        
        def size_move_right(event):
            if event.buttons() == Qt.MouseButton.LeftButton:
                width = event.globalPos().x() - self.x()
                if width > self.minimumWidth():
                    self.resize(width, self.height())
        
        def size_move_bottom(event):
            if event.buttons() == Qt.MouseButton.LeftButton:
                height = event.globalPos().y() - self.y()
                if height > self.minimumHeight():
                    self.resize(self.width(), height)

        def size_move_left(event):
            if event.buttons() == Qt.MouseButton.LeftButton:
                x = event.globalPos().x()
                width = self.x() - x + self.width()
                if width > self.minimumWidth():
                    self.setGeometry(x, self.y(), width, self.height())

        if size_top:
            size_top.setCursor(Qt.CursorShape.SizeVerCursor)
            size_top.mouseMoveEvent = size_move_top

        if size_right:
            size_right.setCursor(Qt.CursorShape.SizeHorCursor)
            size_right.mouseMoveEvent = size_move_right

        if size_bottom:
            size_bottom.setCursor(Qt.CursorShape.SizeVerCursor)
            size_bottom.mouseMoveEvent = size_move_bottom

        if size_left:
            size_left.setCursor(Qt.CursorShape.SizeHorCursor)
            size_left.mouseMoveEvent = size_move_left

        if size_right_bottom:
            QSizeGrip(size_right_bottom)
        
        if size_left_bottom:
            QSizeGrip(size_left_bottom)
        
        if size_top_left:
            QSizeGrip(size_top_left)