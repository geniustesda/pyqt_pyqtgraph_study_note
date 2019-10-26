#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@datatime:2019/10/27
@Author:Mr.hu

使用剪切板
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ClipBoardDemo(QDialog):
    def __init__(self):
        super(ClipBoardDemo, self).__init__()
        self.initUI()

    def initUI(self):
        textCopyButton = QPushButton('复制文本')
        textPastButton = QPushButton('粘贴文本')

        htmlCopyButton = QPushButton('复制HTML')
        htmlPastButton = QPushButton('粘贴HTML')

        imageCopyButton = QPushButton('复制图像')
        imagePastButton = QPushButton('粘贴图像')

        self.textLabel = QLabel('默认文本')
        self.imagelabel = QLabel()
        self.imagelabel.setPixmap(QPixmap('../images/win.png'))

        layout = QGridLayout()
        # 第一行
        layout.addWidget(textCopyButton, 0, 0)
        layout.addWidget(htmlCopyButton, 0, 1)
        layout.addWidget(imageCopyButton, 0, 2)
        # 第二行
        layout.addWidget(textPastButton, 1, 0)
        layout.addWidget(htmlPastButton, 1, 1)
        layout.addWidget(imagePastButton, 1, 2)

        layout.addWidget(self.textLabel, 2, 0, 1, 2)
        layout.addWidget(self.imagelabel, 2, 2)

        self.setLayout(layout)
        self.setWindowTitle("剪切板演示")

        textCopyButton.clicked.connect(self.copyText)
        textPastButton.clicked.connect(self.pastText)
        htmlCopyButton.clicked.connect(self.copyHtml)
        htmlPastButton.clicked.connect(self.pastHtml)
        imageCopyButton.clicked.connect(self.imageCopy)
        imagePastButton.clicked.connect(self.imagePast)

    def copyText(self):
        clipboard = QApplication.clipboard()
        clipboard.setText('hello world')

    def pastText(self):
        clipboard = QApplication.clipboard()
        self.textLabel.setText(clipboard.text())

    def copyHtml(self):
        mimeData = QMimeData()
        mimeData.setHtml("<b>Bold and <font color='red'>Red</font></b>")
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimeData)

    def pastHtml(self):
        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()
        if mimeData.hasHtml():
            self.textLabel.setText(mimeData.html())

    def imageCopy(self):
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(QPixmap('../images/screen.png'))

    def imagePast(self):
        clipboard = QApplication.clipboard()
        self.imagelabel.setPixmap(clipboard.pixmap())


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = ClipBoardDemo()
    win.show()
    sys.exit(app.exec_())
