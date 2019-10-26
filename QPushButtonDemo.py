#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@datatime:2019/10/26
@Author:Mr.hu

QPushButton
AToolButton
QRadioButton
QCheckBox
"""
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QPushButton Demo")

        self.button1 = QPushButton('第一个按钮')
        self.button1.setText('First Button1')
        self.button1.setCheckable(True)  # 拥有checkbox的属性，默认为True
        self.button1.toggle()

        # 在文本前面显示图像
        self.button2 = QPushButton('图像按钮')
        self.button2.setIcon(QIcon(QPixmap('./images/python.png')))

        # 使按钮不可用
        self.button3 = QPushButton('按钮不可用')
        self.button3.setEnabled(False)

        # 设置默认按钮,按回车(热键)即可执行
        self.button4 = QPushButton('&MyButton')
        self.button4.setDefault(True)

        # 将按钮控件的信号绑定到槽（或者说是将事件绑定到响应函数）
        self.button1.clicked.connect(lambda: self.whichButton(self.button1))
        self.button1.clicked.connect(self.buttonState)
        self.button2.clicked.connect(lambda: self.whichButton(self.button2))
        self.button4.clicked.connect(lambda: self.whichButton(self.button4))

        # 将控件添加到布局
        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        self.resize(300, 200)
        self.setLayout(layout)

    def whichButton(self, btn):
        print(time.time(), '被单击的按钮是：'+btn.text())

    def buttonState(self, btn):
        print(time.time(), '当前按钮的状态：', btn)
        if self.button1.isChecked():
            print("按钮1被选中")
        else:
            print("按钮1未被选中")
        print('\n')


if __name__ == '__main__':
    import sys, time
    app = QApplication(sys.argv)
    win = QPushButtonDemo()
    win.show()
    sys.exit(app.exec_())

