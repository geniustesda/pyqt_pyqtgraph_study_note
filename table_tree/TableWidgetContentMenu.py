#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@datatime:2019/10/27
@Author:Mr.hu
在表格中显示上下文菜单
1.如何弹出菜单
2.如何在满足条件的情况下弹出菜单
QMenu.exec_()  # 弹出菜单
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class TableWidgetContextMenu(QWidget):
    def __init__(self):
        super(TableWidgetContextMenu, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("在表格中显示上下文菜单")
        self.resize(500, 300)
        # 初始化表格参数
        self.tableWidget = QTableWidget()
        self.table_shape = (5, 3)
        self.tableWidget.setRowCount(self.table_shape[0])
        self.tableWidget.setColumnCount(self.table_shape[1])
        self.tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重'])
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)    # 设置上下文菜单
        self.tableWidget.customContextMenuRequested.connect(self.generateMenu)  # 触发上下文菜单,连接到槽

        # 向表格添加数据
        newItem = QTableWidgetItem('张三')
        self.tableWidget.setItem(0, 0, newItem)
        newItem = QTableWidgetItem('男')
        self.tableWidget.setItem(0, 1, newItem)
        newItem = QTableWidgetItem('130')
        self.tableWidget.setItem(0, 2, newItem)
        # 将表格添加到布局
        layout = QHBoxLayout()
        layout.addWidget(self.tableWidget)
        # 设置布局
        self.setLayout(layout)

    def outSelet(self, item):
        if item == None:
            return
        return item.text()

    def generateMenu(self, pos):
        print(pos)  # 坐标值
        allRow = self.tableWidget.rowCount()  # 获取当前表格有多少行
        for i in self.tableWidget.selectionModel().selection().indexes():
            rowNum = i.row()
            if rowNum < allRow:  # 表格内右键即有菜单栏
                screenPos = self.tableWidget.mapToGlobal(pos)  # 将坐标转换成全局
                print(screenPos)
                menu = QMenu()
                item1 = menu.addAction('菜单项1')
                item2 = menu.addAction('菜单项2')
                item3 = menu.addAction('菜单项3')
                # 根据鼠标的坐标生成菜单，被阻塞
                action = menu.exec(screenPos)
                if action == item1:
                    print('选择了第1个菜单项', self.tableWidget.item(rowNum, 0).text(),
                                            self.tableWidget.item(rowNum, 1).text(),
                                            self.tableWidget.item(rowNum, 2).text(),)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = TableWidgetContextMenu()
    win.show()
    sys.exit(app.exec_())


