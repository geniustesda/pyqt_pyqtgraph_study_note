#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@datatime:2019/10/27
@Author:Mr.hu

在单元格中放置控件
setCellWidget
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class PlaceControllerCell(QWidget):
    def __init__(self):
        super(PlaceControllerCell, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("在单元格中放置控件")
        self.resize(430, 300)
        layout = QHBoxLayout()

        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重(kg)'])
        textItem = QTableWidgetItem('小明')

        combox = QComboBox()
        combox.addItem('男')
        combox.addItem('女')
        # QSS
        combox.setStyleSheet('QComboBox(margin:3px)')

        modifyButton = QPushButton('修改')
        modifyButton.setDown(True)
        modifyButton.setStyleSheet('QPushButton{margin:3px};')

        tableWidget.setItem(0, 0, textItem)
        tableWidget.setCellWidget(0, 1, combox)
        tableWidget.setCellWidget(0, 2, modifyButton)

        layout.addWidget(tableWidget)
        self.setLayout(layout)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    win = PlaceControllerCell()
    win.show()
    sys.exit(app.exec_())
