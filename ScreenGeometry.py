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


def onclick_button():
    print("onclick")
    print("绝对坐标（含标题栏）：", widget.x(), widget.y())
    print("工作区的坐标(不含标题栏)：", widget.geometry().x(), widget.geometry().y())
    print("窗口的尺寸：", widget.geometry().width(), widget.geometry().height())
    print("默认工作区的尺寸：", widget.frameGeometry().x(), widget.frameGeometry().y())


app = QApplication(sys.argv)

widget = QWidget()
btn = QPushButton(widget)
btn.setText("按钮")
btn.clicked.connect(onclick_button)

btn.move(24, 25)

widget.resize(300, 240)  # 窗口尺寸

widget.move(250, 200)    # 窗口的绝对坐标

widget.setWindowTitle('屏幕坐标系')

widget.show()

sys.exit(app.exec_())
