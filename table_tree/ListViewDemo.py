#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@datatime:2019/10/27
@Author:Mr.hu

显示列表数据（QListView控件）
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ListViewDemo(QWidget):
    def __init__(self):
        super(ListViewDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QListView 示例")
        self.resize(300, 270)

        listview = QListView()
        list_model = QStringListModel()
        self.list_data = ['列表项1', '列表项2', '列表项3']

        list_model.setStringList(self.list_data)
        listview.setModel(list_model)
        listview.clicked.connect(self.clicked_list)

        layout = QVBoxLayout()
        layout.addWidget(listview)
        self.setLayout(layout)

    def clicked_list(self, item):
        print(item.row())
        QMessageBox.information(self, 'QListView', '您选择了:' + self.list_data[item.row()])


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = ListViewDemo()
    win.show()
    sys.exit(app.exec_())
