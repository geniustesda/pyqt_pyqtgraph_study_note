#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@datatime:2019/10/22
@Author:Mr.hu
"""
import sys
import cv2
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import *


class UiMainWindow(QWidget):
    def __init__(self, parent=None):
        super(UiMainWindow, self).__init__(parent)

        self.timer_camera = QtCore.QTimer()
        self.cap = cv2.VideoCapture()
        self.CAM_NUM = 0
        self.set_ui()
        self.slot_init()
        self.__flag_work = 0
        self.x = 0
        self.count = 0

    def set_ui(self):
        self.__layout_main = QHBoxLayout()
        self.__layout_fun_button = QVBoxLayout()
        self.__layout_data_show = QVBoxLayout()

        self.button_open_camera = QPushButton('打开相机')
        self.button_close = QPushButton('退出')

        # button color changed
        buttons_color = [self.button_open_camera, self.button_close]
        for one_button in buttons_color:
            one_button.setStyleSheet("QPushButton{color:black}"
                                     "QPushButton:hover{color:red}"
                                     "QPushButton{background-color:rgb(78,255,255)}"
                                     "QPushButton{border:2px}"
                                     "QPushButton{border-radius:10px}"
                                     "QPushButton{padding:2px 4px}")
        self.button_open_camera.setMinimumHeight(50)
        self.button_close.setMinimumHeight(50)

        # 设置默认窗口位置
        self.move(500, 500)

        # 信息显示
        self.label_show_camera = QLabel()
        self.label_move = QLabel()
        self.label_move.setFixedSize(100, 100)

        self.label_show_camera.setFixedSize(641, 481)
        self.label_show_camera.setAutoFillBackground(False)

        self.__layout_fun_button.addWidget(self.button_open_camera)
        self.__layout_fun_button.addWidget(self.button_close)
        self.__layout_fun_button.addWidget(self.label_move)

        self.__layout_main.addLayout(self.__layout_fun_button)
        self.__layout_main.addWidget(self.label_show_camera)

        self.setLayout(self.__layout_main)
        self.label_move.raise_()
        self.setWindowTitle('调用摄像头')

    def slot_init(self):
        self.button_open_camera.clicked.connect(self.button_open_camera_click)
        self.timer_camera.timeout.connect(self.show_camera)
        self.button_close.clicked.connect(self.close)

    def button_open_camera_click(self):
        if self.timer_camera.isActive() == False:
            flag = self.cap.open(self.CAM_NUM)
            if flag == False:
                msg = QtWidgets.QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确",
                                                    buttons=QtWidgets.QMessageBox.Ok,
                                                    defaultButton=QtWidgets.QMessageBox.Ok)
            else:
                self.timer_camera.start(10)
                self.button_open_camera.setText('关闭相机')

        else:
            self.timer_camera.stop()
            self.cap.release()
            self.label_show_camera.clear()
            self.button_open_camera.setText('打开相机')

    def show_camera(self):
        flag, self.image = self.cap.read()
        show = cv2.resize(self.image, (640, 480))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.label_show_camera.setPixmap(QtGui.QPixmap.fromImage(showImage))

    def closeEvent(self, event):
        ok = QtWidgets.QPushButton()
        cancel = QtWidgets.QPushButton()

        msg = QMessageBox(QMessageBox.Warning, '关闭', '是否关闭')

        msg.addButton(ok, QMessageBox.ActionRole)
        msg.addButton(cancel, QMessageBox.RejectRole)
        ok.setText('确定')
        cancel.setText('取消')

        if msg.exec_() == QMessageBox.RejectRole:
            event.ignore()
        else:
            if self.cap.isOpened():
                self.cap.release()
            if self.timer_camera.isActive():
                self.timer_camera.stop()
            event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = UiMainWindow()
    win.show()
    sys.exit(app.exec_())
