#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@datatime:2019/10/27
@Author:Mr.hu
文件对话框：QFileDialogDemo
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QFileDialogDemo(QWidget):
    def __init__(self):
        super(QFileDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("文件对话框：QFileDialog")
        self.button1 = QPushButton('加载图片')
        self.imageLabel = QLabel()  # 图片标签，用于后面显示图片
        self.button2 = QPushButton('加载文本')

        self.contents = QTextEdit()  # 用于显示文本文件内容

        self.button1.clicked.connect(self.loadImage)
        self.button2.clicked.connect(self.loadText)

        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.imageLabel)
        layout.addWidget(self.contents)

        self.setLayout(layout)

    def loadImage(self):
        fname, _ = QFileDialog.getOpenFileName(self, '打开文件', '.', '图像文件(*.jpg *.png)')
        # fname = QFileDialog.getOpenFileNames(self, '打开文件', '.', '图像文件(*.jpg *.png)')
        self.imageLabel.setPixmap(QPixmap(fname))  # 显示文件到图像label上

    def loadText(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec():
            filenames = dialog.selectedFiles()
            print(filenames)
            with open(filenames[0], 'r', encoding='utf-8')as fp:
                content = fp.read()
            self.contents.setText(content)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = QFileDialogDemo()
    win.show()
    sys.exit(app.exec())



