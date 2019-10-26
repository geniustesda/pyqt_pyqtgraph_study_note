#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@datatime:2019/10/26
@Author:Mr.hu
QLineEdit综合案例
"""
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class QLineEditDemo(QWidget):
    def __init__(self):
        super(QLineEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        edit1 = QLineEdit()
        # int校验器
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(4)   # 最大高度
        edit1.setAlignment(Qt.AlignRight)
        edit1.setFont(QFont('Arial', 20))

        # 浮点数校验器
        edit2 = QLineEdit()
        edit2.setValidator(QDoubleValidator(0.99, 99.99, 2))  # 保留两位小数

        edit3 = QLineEdit()
        edit3.setInputMask('00_9999_999999;#')  # 模型输入，并只能输入数字

        edit4 = QLineEdit()
        edit4.textChanged.connect(self.textChanged)

        edit5 = QLineEdit()
        edit5.setEchoMode(QLineEdit.Password)
        edit5.editingFinished.connect(self.enterPress)

        edit6 = QLineEdit('Hello PyQt5')
        edit6.setReadOnly(True)

        formlayout = QFormLayout()
        formlayout.addRow('整数校验', edit1)
        formlayout.addRow('浮点数校验', edit2)
        formlayout.addRow('Input Mask', edit3)  # 模型输入
        formlayout.addRow('文本变化', edit4)
        formlayout.addRow('密码', edit5)
        formlayout.addRow('只读', edit6)

        self.setLayout(formlayout)
        self.setWindowTitle('QlineEdit综合案例')

    def textChanged(self, text):
        print('输入的内容：'+text)

    def enterPress(self):
        print('已输入值')


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = QLineEditDemo()
    win.show()
    sys.exit(app.exec_())

