#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@datatime:2019/10/26
@Author:Mr.hu
对话框：QDialog:
    QMessageDialog
    QColorDialog
    QFileDialog
    QInputDialog
三种窗口：
    QMainWindow
    QWidget
    QDialog
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DialogDemo(QMainWindow):
    def __init__(self):
        super(DialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("对话框：QDialog示例")
        self.resize(400, 300)

        self.button = QPushButton(self)
        self.button.setText('弹出对话框')
        self.button.move(50, 50)
        self.button.clicked.connect(self.showDialog)

    def showDialog(self):
        dialog = QDialog()
        button = QPushButton('确定', dialog)
        button.clicked.connect(dialog.close)
        button.move(50, 50)
        dialog.setWindowTitle('对话框')
        dialog.setWindowModality(Qt.ApplicationModal)

        dialog.exec_()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = DialogDemo()
    win.show()
    sys.exit(app.exec_())

