#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@datatime:2020/03/09
@Author:Mr.hu
"""
import sys
import os
import qrcode
import pyzbar
from PIL import Image
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PyQt5 import QtGui
from qrcode_gen_ui import Ui_Form

QR_img_name = "qr_tmp.png"


class QrCodeGen(QWidget, Ui_Form):
    def __init__(self):
        super(QrCodeGen, self).__init__(parent=None)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton.setText("另存为")
        self.lineEdit.textChanged.connect(self.qrcode_gen)
        self.pushButton.clicked.connect(self.save_qrcode)

    def save_qrcode(self):
        img_path, _ = QFileDialog.getSaveFileName(self, 'Save qrcode', '', filter='Qrcode path(*.png)')
        if not img_path:
            return
        self.img.save(img_path)
        QMessageBox.about(self, "Info", "Success save the qrcode!")

    def qrcode_gen(self, content):
        # print(content)
        qr = qrcode.QRCode(version=5,
                           error_correction=qrcode.constants.ERROR_CORRECT_H,
                           box_size=8, border=4)
        qr.add_data(content)
        qr.make(fit=True)
        self.img = qr.make_image()
        self.img.save(QR_img_name)
        self.show_qrcode()

    def show_qrcode(self):
        self.label.setPixmap(QtGui.QPixmap(QR_img_name))

    def decode_qrcode(self, qr_img_path):
        if not os.path.exists(qr_img_path):
            raise FileExistsError(qr_img_path)
        return pyzbar.decode(Image.open(qr_img_path), symbols=[pyzbar.ZBarSymbol.QRCODE])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QrCodeGen()
    win.show()
    sys.exit(app.exec_())
