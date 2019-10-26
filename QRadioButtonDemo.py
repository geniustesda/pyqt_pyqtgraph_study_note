#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@datatime:2019/10/26
@Author:Mr.hu
单选按钮控件（QRadioButton）
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QRadioButtonDemo(QWidget):
    def __init__(self):
        super(QRadioButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('单选按钮控件(QRadioButton)')

        # 控件
        self.button1 = QRadioButton('单选按钮1')
        self.button1.setCheckable(True)
        self.button2 = QRadioButton('单选按钮2')
        self.button3 = QRadioButton('单选按钮3')

        # 事件
        self.button1.toggled.connect(self.button_state)
        self.button2.toggled.connect(self.button_state)
        self.button3.toggled.connect(self.button_state)

        # 布局
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        self.setLayout(layout)

    def button_state(self):
        radio_button = self.sender()
        if radio_button.isChecked() ==True:
            print(radio_button.text(), "被选中")
        else:
            print(radio_button.text(), "取消选中")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = QRadioButtonDemo()
    win.show()
    sys.exit(app.exec())
