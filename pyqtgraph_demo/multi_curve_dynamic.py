#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@datatime:2019/10/18
@Author:Mr.hu
多曲线动态显示
"""
import pyqtgraph as pg
import numpy as np
import array
import time

app = pg.mkQApp()

time_line = array.array('d')
data1 = array.array('d')
data2 = array.array('d')
all_data = array.array('d')

N = 200
win = pg.GraphicsWindow()
win.setWindowTitle("sin和cos绘图")
win.resize(800, 500)

p = win.addPlot(row=1, col=0)
p2 = win.addPlot(row=2, col=0)
p.showGrid(x=True, y=True)
# p.setRange(xRange=[0, N - 1], yRange=[-1.2, 1.2], padding=0)
p.setLabels(left='y/v', bottom='x/seconds', title='y=sin(x) y=cos(x)')

curve1 = p.plot(pen='y')
curve2 = p.plot(pen='y')
curve3 = p2.plot(pen='b')
start_time = time.time()
idx = 0


def plotData():
    global idx
    tmp1 = np.sin(np.pi / 50 * idx)
    tmp2 = np.cos(np.pi / 50 * idx)
    spend_time = time.time()-start_time
    time_line.append(spend_time)
    all_data.append(tmp1)
    if len(data1) < N:
        data1.append(tmp1)
        data2.append(tmp2)
    else:
        data1[:-1] = data1[1:]
        data1[-1] = tmp1
        data2[:-1] = data2[1:]
        data2[-1] = tmp2
    curve1.setData(time_line[-N:], data1, pen='y')
    curve2.setData(time_line[-N:], data2, pen='b')
    curve3.setData(time_line, all_data, pen='y')
    p.setRange(xRange=[spend_time-2, spend_time + 0.5], yRange=[-1.2, 1.2], padding=0)
    idx += 1


timer = pg.QtCore.QTimer()
timer.timeout.connect(plotData)
timer.start(10)
app.exec_()
