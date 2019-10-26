#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@datatime:2019/10/27
@Author:Mr.hu
消息对话框：QMessageBox
1、关于对话框
2、错误对话框
3、警告对话框
4、提问会话框
5、消息对话框

有两点差异
1、的对话框图标可能不同
2、的按钮不一样
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QMessageBoxDemo(QWidget):
    def __init__(self):
        super(QMessageBoxDemo, self).__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle("QMessageBox示例")
        self.resize(400, 300)

        self.button1 = QPushButton()
        self.button2 = QPushButton()
        self.button3 = QPushButton()
        self.button4 = QPushButton()
        self.button5 = QPushButton()
        self.button1.setText('关于对话框')
        self.button2.setText('消息对话框')
        self.button3.setText('警告对话框')
        self.button4.setText('错误对话框')
        self.button5.setText('提问对话框')

        self.button1.clicked.connect(self.showDialog)
        self.button2.clicked.connect(self.showDialog)
        self.button3.clicked.connect(self.showDialog)
        self.button4.clicked.connect(self.showDialog)
        self.button5.clicked.connect(self.showDialog)

        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)
        self.setLayout(layout)

    def showDialog(self):
        text = self.sender().text()
        if text == '关于对话框':
            QMessageBox.about(self, '关于', '这是一个关于对话框')
        elif text == '消息对话框':
            reply = QMessageBox.information(self, '消息', '这是一个消息对话框',
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)  # 最后一个参数是默认值
            print(text, reply == QMessageBox.Yes)
        elif text == '警告对话框':
            reply = QMessageBox.warning(self, '警告', '这是一个警告对话框',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            print(text, reply == QMessageBox.Yes)
        elif text == '错误对话框':
            reply = QMessageBox.critical(self, '错误', '这是一个错误对话框',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            print(text, reply == QMessageBox.Yes)
        elif text == '提问对话框':
            reply = QMessageBox.question(self, '关于', '这是一个提问对话框',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            print(text, reply == QMessageBox.Yes)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = QMessageBoxDemo()
    win.show()
    sys.exit(app.exec_())