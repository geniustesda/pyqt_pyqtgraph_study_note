#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@datatime:2019/10/30
@Author:Mr.hu
树控件（QTreeWdiget）的基本用法
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class BasicTreeWidget(QMainWindow):
    def __init__(self):
        super(BasicTreeWidget, self).__init__()
        self.setWindowTitle("树控件（QTreeWdiget）的基本用法")

        self.tree = QTreeWidget()
        self.setCentralWidget(self.tree)

        # 为树指定列数
        self.tree.setColumnCount(2)
        # 指定列标签
        self.tree.setHeaderLabels(['Key', 'Value'])
        root = QTreeWidgetItem(self.tree)
        root.setText(0, 'root')
        root.setIcon(0, QIcon('../images/root.png'))
        self.tree.setColumnWidth(0, 120)

        # 添加子节点1
        child1 = QTreeWidgetItem(root)
        child1.setText(0, '子节点1')
        child1.setText(1, '子节点1的数据')
        child1.setIcon(0, QIcon('../images/bao3.png'))
        # child1.setCheckState(0, Qt.Checked)
        child1.setCheckState(0, 0)

        # 添加子节点1
        child2 = QTreeWidgetItem(root)
        child2.setText(0, '子节点2')
        child2.setText(1, '子节点2的数据')
        child2.setIcon(0, QIcon('../images/bao3.png'))
        # child2.setCheckState(0, Qt.Checked)
        child2.setCheckState(0, 0)
        print(child2.checkState(12))  # 获取状态0、1、2，分别代表未选中、半选中、选中

        # 添加子节点的子节点
        child3 = QTreeWidgetItem(child2)
        child3.setText(0, '子节点的子节点3')
        child3.setText(1, '子节点的子节点3的数据')


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = BasicTreeWidget()
    win.show()
    sys.exit(app.exec_())
