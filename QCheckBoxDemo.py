#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@datatime:2019/10/26
@Author:Mr.hu
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QCheckBoxDemo(QWidget):
    def __init__(self):
        super(QCheckBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("复选框控件展示")

        self.checkBox1 = QCheckBox('复选框控件1(默认选中)')
        self.checkBox1.setCheckState(True)
        self.checkBox2 = QCheckBox('复选框控件2(默认未选中)')
        self.checkBox2.setCheckState(False)
        self.checkBox3 = QCheckBox('复选框控件3(默认半选中)')
        self.checkBox3.setTristate(True)  # 会导致默认选中的有三种状态，默认未选中的不变（两种状态）

        self.checkBox1.stateChanged.connect(lambda: self.checkboxState(self.checkBox1))
        self.checkBox2.stateChanged.connect(lambda: self.checkboxState(self.checkBox2))
        self.checkBox3.stateChanged.connect(lambda: self.checkboxState(self.checkBox3))

        layout = QHBoxLayout()
        layout.addWidget(self.checkBox1)
        layout.addWidget(self.checkBox2)
        layout.addWidget(self.checkBox3)
        self.setLayout(layout)
        self.resize(400, 300)

    def checkboxState(self, cb):
        """
        checkstate有三种值: 0/1/2
        isChecked为布尔值: True/False
        """
        # print(self.checkBox1.text(), self.checkBox1.checkState())
        # print(self.checkBox2.text(), self.checkBox2.checkState())
        # print(self.checkBox3.text(), self.checkBox3.checkState())
        print(cb.text(), cb.checkState(), cb.isChecked())


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = QCheckBoxDemo()
    win.show()
    sys.exit(app.exec_())

