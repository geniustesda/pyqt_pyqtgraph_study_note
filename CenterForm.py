#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@datatime:2019/10/26
@Author:Mr.hu
"""
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class CenterForm(QMainWindow):
    def __init__(self):
        super(CenterForm, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("窗口居中")
        self.resize(400, 300)
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width())/2
        newTop = (screen.height() - size.height())/2
        self.move(newLeft, newTop)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = CenterForm()
    win.show()
    sys.exit(app.exec_())
