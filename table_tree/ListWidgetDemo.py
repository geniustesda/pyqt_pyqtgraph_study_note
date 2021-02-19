#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@datatime:2019/10/27
@Author:Mr.hu

扩展列表控件（QListWidget）
QListView
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ListWidgetDemo(QMainWindow):
    def __init__(self, parent=None):
        super(ListWidgetDemo, self).__init__(parent)
        self.setWindowTitle("QListWidget 例子")
        self.resize(300, 277)
        self.initUI()

    def initUI(self):
        self.listwidget = QListWidget()
        # self.listwidget.resize(300, 120)
        self.listwidget.addItem('item1')
        self.listwidget.addItem('item2')
        self.listwidget.addItem('item3')
        self.listwidget.addItem('item4')
        self.listwidget.addItem('item5')

        self.listwidget.itemClicked.connect(self.clicked_event)

        self.listwidget.setWindowTitle("demo")
        self.setCentralWidget(self.listwidget)

    def clicked_event(self, item):
        print(item)
        QMessageBox.information(self, "QListWidget", "您选择了：" +
                                self.listwidget.item(self.listwidget.row(item)).text())


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = ListWidgetDemo()
    win.show()
    sys.exit(app.exec_())
