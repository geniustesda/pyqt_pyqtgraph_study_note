#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@datatime:2019/10/27
@Author:Mr.hu
QTableView
每一个Cell（单元格）是一个QTableWidget
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class TableWidgetDemo(QWidget):
    def __init__(self):
        super(TableWidgetDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget演示")
        self.resize(500, 300)
        layout = QHBoxLayout()

        tablewidget = QTableWidget()
        tablewidget.setRowCount(4)
        tablewidget.setColumnCount(3)
        # 设置表头
        tablewidget.setHorizontalHeaderLabels(['姓名', '年龄', '籍贯'])
        # 设置禁止编辑
        tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 整行选中
        tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # # 根据字体自适应列和行
        # tablewidget.resizeColumnsToContents()
        # tablewidget.resizeRowsToContents()

        # # 设置垂直索引
        # tablewidget.verticalHeader().setVisible(False)   # 关闭索引
        # # 设置水平索引
        # tablewidget.horizontalHeader().setVisible(False) # 关闭水平字段显示，如果未定义字段才有效

        # # 隐藏表格线
        # tablewidget.setShowGrid(False)

        item1 = QTableWidgetItem('小明')
        item2 = QTableWidgetItem('20')
        item3 = QTableWidgetItem('上海')

        tablewidget.setItem(0, 0, item1)
        tablewidget.setItem(0, 1, item2)
        tablewidget.setItem(0, 2, item3)

        layout.addWidget(tablewidget)
        self.setLayout(layout)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = TableWidgetDemo()
    win.show()
    sys.exit(app.exec_())

