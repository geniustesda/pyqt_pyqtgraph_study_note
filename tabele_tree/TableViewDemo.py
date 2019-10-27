#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@datatime:2019/10/27
@Author:Mr.hu

显示二维表数据（QTableView）
数据源
Model

需要创建QTableView实例和一个数据源（Model），然后将两者关联
MVC结构：Model Viewer Controller
MVC的目的是降低前后端的耦合度
"""
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class TableViewDemo(QWidget):
    def __init__(self):
        super(TableViewDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableView表格控件")
        self.resize(500, 300)

        self.model = QStandardItemModel(4, 3)
        self.model.setHorizontalHeaderLabels(['id', '姓名', '年龄'])     # 字段列表
        # self.model.setVerticalHeaderLabels(['qq', 'ww', 'ee', 'rr'])  # 索引列表

        self.tableView = QTableView()
        # 关联QTableView和model
        self.tableView.setModel(self.model)

        layout = QVBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)

        # 添加数据
        self.model.setItem(0, 0, QStandardItem('10'))
        self.model.setItem(0, 1, QStandardItem('雷神'))
        self.model.setItem(0, 2, QStandardItem("2000"))

        self.model.setItem(1, 0, QStandardItem('20'))
        self.model.setItem(1, 1, QStandardItem('死亡女神'))
        self.model.setItem(1, 2, QStandardItem("3000"))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    win = TableViewDemo()
    win.show()
    sys.exit(app.exec_())
