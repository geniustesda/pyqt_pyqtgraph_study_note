#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@datatime:2019/10/27
@Author:Mr.hu
让控件支持拖拽

可被拖拽的控件
A.setDragEnable(True)

可接受其它控件：
B.setAcceptDrop(True)

B需要两个事件：
1、dragEnterEvent   将A拖到B时触发
2、dropEvent        在B区域放下A时触发
"""
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MyComBoxDemo(QComboBox):
    def __init__(self):
        super(MyComBoxDemo, self).__init__()
        self.setAcceptDrops(True)   # 使其能够接收控件

    def dragEnterEvent(self, e):    # 拖拽到的事件
        if e.mimeData().hasText():  # 只接收文本
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):         # 放下事件
        self.addItem(e.mimeData().text())  # 添加新控件的文本到类目


class DrapDropDemo(QWidget):
    def __init__(self):
        super(DrapDropDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("拖拽Demo")
        # 设置被拖拽控件和拖拽区域控件
        line_edit = QLineEdit()          # 被拖拽的控件
        line_edit.setDragEnabled(True)   # 让QLineEdit控件可拖
        combo = MyComBoxDemo()           # 拖拽到的区域

        # 布局
        formLayout = QFormLayout()
        formLayout.addRow(QLabel("将左边的文本拖拽到右边的下拉列表中"))
        formLayout.addRow(line_edit, combo)
        self.setLayout(formLayout)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = DrapDropDemo()
    win.show()
    sys.exit(app.exec_())