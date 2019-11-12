#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@datatime:2019/11/12
@Author:Mr.hu
拖动控件之间的边界（QSplitter）
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class SplitterDemo(QWidget):
    def __init__(self):
        super(SplitterDemo, self).__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        self.setWindowTitle("QSplitter 例子")
        self.setGeometry(300, 300, 300, 200)

        topleft = QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        textEdit = QTextEdit()

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(textEdit)
        splitter1.setSizes([200, 100])

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        splitter2.setSizes([200, 100])

        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        self.resize(600, 500)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    demo = SplitterDemo()
    demo.show()
    sys.exit(app.exec_())

