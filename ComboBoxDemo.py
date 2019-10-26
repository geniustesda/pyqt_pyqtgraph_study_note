#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@datatime:2019/10/26
@Author:Mr.hu
下拉列表控件（QComboBox）
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ComboBoxDemo(QWidget):
    def __init__(self):
        super(ComboBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("下拉列表控件演示")
        self.resize(300, 100)

        self.label = QLabel('选择编程语言')
        self.cb = QComboBox()
        self.cb.addItem('C++')
        self.cb.addItem('Python')
        self.cb.addItem('Java')
        self.cb.addItems(['C#', 'Nodejs', 'Ruby'])  # 一次添加多个参数

        self.cb.currentIndexChanged.connect(self.selectionChange)

        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.cb)
        self.setLayout(layout)

    def selectionChange(self, i):
        """
        :param i: 事件默认传参,数字代表下拉列表的索引
        :return: None
        """
        self.label.setText(self.cb.currentText())
        self.label.adjustSize()  # 自动调整大小,这里看不到具体作用

        for count in range(self.cb.count()):
            print(time.time(), count, self.cb.itemText(count))
        print("当前选中：", i, self.cb.currentText())


if __name__ == '__main__':
    import sys, time
    app = QApplication(sys.argv)
    win = ComboBoxDemo()
    win.show()
    sys.exit(app.exec_())