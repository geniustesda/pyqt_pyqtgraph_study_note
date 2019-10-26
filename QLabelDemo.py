#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@datatime:2019/10/26
@Author:Mr.hu
"""
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QLabelDemo(QWidget):
    def __init__(self, parent=None):
        super(QLabelDemo, self).__init__(parent)

        self.initUi()

    def initUi(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color='yellow'>这是一个文本标签</font>")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)  # 居中对齐

        label2.setText("<a href='#'>欢迎使用python</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap("./images/python.jpg"))  # 设置ico图标

        label4.setText("<a href='https://www.baidu.com'>百度</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超链')
        label4.setOpenExternalLinks(True)  # 增加链接响应事件,会覆盖其它信号

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)

        self.setLayout(layout)

        # 如果是主窗口，就需要这样写
        # mainform = QWidget()
        # mainform.setLayout(layout)
        # self.setCentralWidget(mainform)

        label2.linkHovered.connect(self.label_hovered)
        label4.linkActivated.connect(self.label_licked)

    def label_hovered(self):
        print("当鼠标滑过label2", time.time())

    def label_licked(self):
        print("当鼠标单击label4", time.time())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QLabelDemo()
    win.show()
    sys.exit(app.exec_())
