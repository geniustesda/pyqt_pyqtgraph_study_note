#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@datatime:2019/10/26
@Author:Mr.hu
Qlabel 与伙伴关系

mainLayout.addWidget(<控件对象>, rowIndex, ColIndex, Row, Column)
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys


class QLabelBuddy(QDialog):
    def __init__(self):
        super(QLabelBuddy, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("设置Qlabel伙伴关系")
        nameLabel = QLabel("&Name", self)
        nameLineEdit = QLineEdit(self)
        # 设置伙伴控件
        nameLabel.setBuddy(nameLineEdit)

        passwordLabel = QLabel('&Password', self)
        passwordLabelEdit = QLineEdit(self)

        # 设置伙伴关系
        passwordLabel.setBuddy(passwordLabelEdit)

        btnOk = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(nameLineEdit, 0, 1, 1, 2)  # 第一行第二列，占用一行两列

        mainLayout.addWidget(passwordLabel, 1, 0)
        mainLayout.addWidget(passwordLabelEdit, 1, 1, 1, 2)  # 第二行第二列，占用一行两列

        mainLayout.addWidget(btnOk, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QLabelBuddy()
    win.show()
    sys.exit(app.exec_())

