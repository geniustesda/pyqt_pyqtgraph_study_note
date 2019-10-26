#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@datatime:2019/10/18
@Author:Mr.hu
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon


class FirstMainWin(QMainWindow):
    def __init__(self):
        super(FirstMainWin, self).__init__()

        # 设置主窗口的标题
        self.setWindowTitle('第一个主窗口')

        # 设置窗口的尺寸
        self.resize(400, 300)

        self.status = self.statusBar()

        self.status.showMessage('只存在5秒的消息', 5000)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = FirstMainWin()
    win.show()
    sys.exit(app.exec_())
