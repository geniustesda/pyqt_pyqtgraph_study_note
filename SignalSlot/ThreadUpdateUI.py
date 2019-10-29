#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@datatime:2019/10/29
@Author:Mr.hu
多线程更新UI数据
"""
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import time


class BackendThread(QThread):
    update_data = pyqtSignal(str)

    def run(self):
        while 1:
            data = QDateTime.currentDateTime()
            currentTime = data.toString('yyyy-MM-dd hh:mm:ss')
            self.update_data.emit(str(currentTime))
            time.sleep(0.01)


class ThreadUpdateUI(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        # QDialog.__init__(self)
        self.setWindowTitle("多线程更新UI数据")
        self.resize(400, 100)
        # self.input = QLineEdit(self)
        self.input = QLabel(self)
        self.input.resize(300, 100)
        self.initUI()

    def initUI(self):
        self.backend = BackendThread()
        self.backend.update_data.connect(self.handleDisplay)
        self.backend.start()

    def handleDisplay(self, data):
        self.input.setText(data)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = ThreadUpdateUI()
    win.show()
    sys.exit(app.exec_())


