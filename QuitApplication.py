#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@datatime:2019/10/26
@Author:Mr.hu
"""
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication, self).__init__()
        self.resize(300, 120)
        self.setWindowTitle('退出应用程序')
        self.initUI()

    def initUI(self):
        # 添加Button
        self.button = QPushButton("退出按钮")
        self.button.clicked.connect(self.onClick_Button)

        layout = QHBoxLayout(self)
        layout.addWidget(self.button)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

    # 自动以的槽，相当于事件的方法
    def onClick_Button(self):
        sender = self.sender()
        print(sender.text() + "按钮被按下")
        app = QApplication.instance()
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QuitApplication()
    win.show()
    sys.exit(app.exec_())


