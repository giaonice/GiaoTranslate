# from Qt import __binding__
#
# print(__binding__)
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
from PyQt5.QtGui import QBitmap, QPainter, QPen, QBrush
from PyQt5.QtCore import Qt, QPoint, QRect, pyqtSignal
from qfluentwidgets import ToolButton
import qrc_rc
'''
# Qt 中无法导入 QScreen 类
try:
    from PySide2.QtGui import QScreen
except:
    from PyQt5.QtGui import QScreen
'''
import sys

class WScreenShot(QWidget):
    creenshothide = pyqtSignal(bool)

    def __init__(self, parent = None):
        super(WScreenShot, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint |Qt.WindowStaysOnTopHint)  # Qt.FramelessWindowHint |

        self.setStyleSheet('''background-color:black; ''')
        # self.setStyleSheet("border: 2px solid black; border-radius: 10px;")
        self.setWindowOpacity(0.5)
        self.desktopRect = QDesktopWidget().screenGeometry()
        self.setGeometry(self.desktopRect)
        self.setCursor(Qt.CrossCursor)
        self.blackMask = QBitmap(self.desktopRect.size())
        self.blackMask.fill(Qt.black)
        self.mask = self.blackMask.copy()
        self.isDrawing = False
        self.startPoint = QPoint()
        self.endPoint = QPoint()

        self.yes = ToolButton(self.window())
        self.yes.setObjectName("yes")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/static/static/对勾.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.yes.setIcon(icon4)

        self.no = ToolButton(self.window())
        self.no.setObjectName("no")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/static/static/退出.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.no.setIcon(icon4)

        self.reload = ToolButton(self.window())
        self.reload.setObjectName("reload")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/static/static/刷新.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reload.setIcon(icon4)

        self.x = self.desktopRect.width()
        self.y = self.desktopRect.height()

        self.botton_to_right()

        self.no.clicked.connect(lambda: self.no_())
        self.yes.clicked.connect(lambda: self.yes_())
        self.reload.clicked.connect(lambda: self.reload_())

    def reload_(self):
        self.setMask(QBitmap(self.blackMask.copy()))
        self.botton_to_right()

    def no_(self):
        # print(1)
        self.setMask(QBitmap(self.blackMask.copy()))
        self.botton_to_right()
        # self.creenshothide.emit(False)
        self.hide()

    def yes_(self):
        # print(2)
        self.hide()
        screenshot = QApplication.primaryScreen().grabWindow(QApplication.desktop().winId())
        rect = QRect(self.startPoint, self.endPoint)
        outputRegion = screenshot.copy(rect)
        outputRegion.save('img.png', format = 'PNG', quality = 100)
        self.setMask(QBitmap(self.blackMask.copy()))
        self.botton_to_right()
        self.creenshothide.emit(True)
        # self.hide()

    def botton_to_right(self):
        self.yes.setGeometry(self.x - 50, self.y - 100, 50, 50)
        self.no.setGeometry(self.x - 100, self.y - 100, 50, 50)
        self.reload.setGeometry(self.x - 150, self.y - 100, 50, 50)

    def paintEvent(self, event):
        # print(3)
        if self.isDrawing:
            self.mask = self.blackMask.copy()
            pp = QPainter(self.mask)
            pen = QPen()
            pen.setStyle(Qt.NoPen)
            pp.setPen(pen)
            brush = QBrush(Qt.white)
            pp.setBrush(brush)
            pp.drawRect(QRect(self.startPoint, self.endPoint))
            self.setMask(QBitmap(self.mask))
            self.botton_to_right()

    def mousePressEvent(self, event):
        # print(4)
        if event.button() == Qt.LeftButton:
            self.startPoint = event.pos()
            self.endPoint = self.startPoint
            self.isDrawing = True
            # self.botton_to_right()

    def mouseMoveEvent(self, event):
        # print(5)
        if self.isDrawing:
            self.endPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        # print(6)
        if event.button() == Qt.LeftButton:
            self.isDrawing = False
            self.endPoint = event.pos()
            self.yes.setGeometry(self.endPoint.x() - 40,  self.endPoint.y(), 40, 40)
            self.yes.showNormal()
            self.no.setGeometry(self.endPoint.x() - 80, self.endPoint.y(), 40, 40)
            self.no.showNormal()
            self.reload.setGeometry(self.endPoint.x() - 120, self.endPoint.y(), 40, 40)
            self.reload.showNormal()
            # self.hide()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = WScreenShot()
    win.show()
    app.exec_()
