#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@datatime:2019/10/26
@Author:Mr.hu
QTextEdit例子
"""
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class QTextEditDemo(QWidget):
    def __init__(self, parent=None):
        super(QTextEditDemo, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTextEdit控件演示")
        self.resize(300, 200)

        self.textEdit = QTextEdit()
        # 设置文本
        self.buttonText = QPushButton('显示文本')
        self.buttonHTML = QPushButton('显示HTML')
        # 获取文本
        self.button_to_Text = QPushButton('获取文本')
        self.button_to_HTML = QPushButton('获取html')

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonHTML)
        layout.addWidget(self.button_to_Text)
        layout.addWidget(self.button_to_HTML)

        self.setLayout(layout)

        self.buttonText.clicked.connect(self.onclick_button_text)
        self.buttonHTML.clicked.connect(self.onclick_button_html)
        self.button_to_Text.clicked.connect(self.onclick_button_to_text)
        self.button_to_HTML.clicked.connect(self.onclick_button_to_html)

    def onclick_button_text(self):
        self.textEdit.setPlainText('Hello World')

    def onclick_button_html(self):
        self.textEdit.setHtml("<font color='blue' size='5'>Hello World</font>")

    def onclick_button_to_text(self):
        print(self.textEdit.toPlainText(), '\n')

    def onclick_button_to_html(self):
        print(self.textEdit.toHtml(), '\n')


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = QTextEditDemo()
    win.show()
    sys.exit(app.exec_())

