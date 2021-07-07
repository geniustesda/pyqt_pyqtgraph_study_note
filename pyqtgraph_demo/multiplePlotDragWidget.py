from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtWidgets
from pyqtgraph.Qt import QtCore, QtGui
from pyqtgraph import LinearRegionItem
import sys
import pyqtgraph as pg
import numpy as np
from pyqtgraph import GraphicsObject
import pyqtgraph.functions as fn


class MyInfiniteLine(pg.InfiniteLine):
    rightButtonDrag = QtCore.Signal(object)

    def mouseDragEvent(self, ev):
        if self.movable and ev.button() == QtCore.Qt.LeftButton:
            if ev.isStart():
                self.moving = True
                self.cursorOffset = self.pos() - self.mapToParent(ev.buttonDownPos())
                self.startPosition = self.pos()
            ev.accept()

            if not self.moving:
                return

            self.setPos(self.cursorOffset + self.mapToParent(ev.pos()))
            self.sigDragged.emit(self)
            if ev.isFinish():
                self.moving = False
                self.sigPositionChangeFinished.emit(self)

        elif self.movable and ev.button() == QtCore.Qt.RightButton:
            if ev.isStart():
                self.moving = True
                self.cursorOffset = self.pos() - self.mapToParent(ev.buttonDownPos())
                self.startPosition = self.pos()
            ev.accept()

            if not self.moving:
                return

            self.setPos(self.cursorOffset + self.mapToParent(ev.pos()))
            self.rightButtonDrag.emit((self.cursorOffset + self.mapToParent(ev.pos())))
            # self.sigDragged.emit(self)
            if ev.isFinish():
                self.moving = False
                self.sigPositionChangeFinished.emit(self)


class MyLinearRegionItem(pg.LinearRegionItem):
    def __init__(self, values=(0, 1), orientation='vertical', brush=None, pen=None,
                 hoverBrush=None, hoverPen=None, movable=True, bounds=None,
                 span=(0, 1), swapMode='sort'):
        GraphicsObject.__init__(self)
        self.orientation = orientation
        self.bounds = QtCore.QRectF()
        self.blockLineSignal = False
        self.moving = False
        self.mouseHovering = False
        self.span = span
        self.swapMode = swapMode
        self._bounds = None

        # note LinearRegionItem.Horizontal and LinearRegionItem.Vertical
        # are kept for backward compatibility.
        lineKwds = dict(
            movable=movable,
            bounds=bounds,
            span=span,
            pen=pen,
            hoverPen=hoverPen,
        )

        if orientation in ('horizontal', LinearRegionItem.Horizontal):
            self.lines = [
                MyInfiniteLine(QtCore.QPointF(0, values[0]), angle=0, **lineKwds),
                MyInfiniteLine(QtCore.QPointF(0, values[1]), angle=0, **lineKwds)]
            tr = QtGui.QTransform.fromScale(1, -1)
            self.lines[0].setTransform(tr, True)
            self.lines[1].setTransform(tr, True)
        elif orientation in ('vertical', LinearRegionItem.Vertical):
            self.lines = [
                MyInfiniteLine(QtCore.QPointF(values[0], 0), angle=90, **lineKwds),
                MyInfiniteLine(QtCore.QPointF(values[1], 0), angle=90, **lineKwds)]
        else:
            raise Exception("Orientation must be 'vertical' or 'horizontal'.")

        for l in self.lines:
            l.setParentItem(self)
            l.sigPositionChangeFinished.connect(self.lineMoveFinished)
        self.lines[0].sigPositionChanged.connect(self._line0Moved)
        self.lines[1].sigPositionChanged.connect(self._line1Moved)

        if brush is None:
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 255, 50))
        self.setBrush(brush)

        if hoverBrush is None:
            c = self.brush.color()
            c.setAlpha(min(c.alpha() * 2, 255))
            hoverBrush = fn.mkBrush(c)
        self.setHoverBrush(hoverBrush)

        self.setMovable(movable)

    def mouseClickEvent(self, ev):
        self.sigClicked.emit(ev)
        print(ev._button)
        # print(self.lines[0].value())
        # print(self.lines[1].value())
        if self.moving and ev.button() == QtCore.Qt.RightButton:
            for i, l in enumerate(self.lines):
                l.setPos(self.startPositions[i])
            self.moving = False
            self.sigRegionChanged.emit(self)
            self.sigRegionChangeFinished.emit(self)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(800, 700)
        pg.setConfigOption('foreground', 'k')  # 设置前景色
        pg.setConfigOption('background', 'w')  # 设置pg的背景色

        self.plot_list = []  # 绘图列表
        self.ragionLine_list = []  # 垂线列表
        self.grid_layout = QtWidgets.QGridLayout(self)  # 将QWidget作为绘制的对象
        self.init_plot_group()
        # self.init_plot()
        self.vLine0_val = 0
        self.vLine1_val = 10

    def axis_changed(self, event):
        viewRange = event.state.get('viewRange')
        x_range = viewRange[0]
        print(x_range)

        for plot in self.plot_list[:-1]:
            plot.setXRange(x_range[0], x_range[1])

    def InifiniteRightButtonDrag0(self, point_val):
        current_val, _ = point_val
        print("line0", current_val)
        for ragionLine in self.ragionLine_list:
            ragionLine[0].setPos(current_val)

    def InifiniteRightButtonDrag1(self, point_val):
        current_val, _ = point_val
        print("line1", current_val)
        for ragionLine in self.ragionLine_list:
            ragionLine[1].setPos(current_val)

    def init_plot_group(self):
        for _ in range(4):
            pw = pg.PlotWidget(self)  # 创建一个绘图控件
            # pw = pg.GraphicsLayoutWidget(self)
            self.plot_list.append(pw)
            data = np.random.random(size=50)
            pw.plot(data)  # 在绘图控件中绘制图形
            pw.showAxis('left', False)  # 关闭y轴的显示
            # pw.showAxis('bottom', False)  # 关闭x轴的显示
            self.grid_layout.addWidget(pw, _, 0, 1, 1)

            # 添加垂线
            # vLine = pg.InfiniteLine(angle=90, movable=True)

            # 添加双垂线和填充
            # ragionLine = pg.LinearRegionItem(values=(0, 20))
            ragionLine = MyLinearRegionItem(values=(0, 20))

            ragionLine.lines[0].rightButtonDrag.connect(self.InifiniteRightButtonDrag0)
            ragionLine.lines[1].rightButtonDrag.connect(self.InifiniteRightButtonDrag1)

            pw.addItem(ragionLine)
            self.ragionLine_list.append(ragionLine.lines)
        pw.sigXRangeChanged.connect(self.axis_changed)

    def init_plot(self):
        # if self._channels_list is not None:
        pw = pg.GraphicsLayoutWidget(self)
        self.grid_layout.addWidget(pw)
        curves = []
        self._channels_list = list(range(4))
        for i, ch in enumerate(self._channels_list):
            curve = pw.addPlot(name=str(ch))
            curve.setLabel('left', text=ch)
            curve.disableAutoRange('y')  # 限制滚轮改变Y轴
            if i + 1 < len(self._channels_list):
                curve.showAxis('bottom', False)
                curve.setMouseEnabled(x=False, y=False)  # 只让鼠标动X轴
            curve.showAxis('left', False)
            data = np.random.random(size=50)
            curve.plot(data)
            curves.append(curve)
            pw.nextRow()
        curves[-1].sigXRangeChanged.connect(self.axis_changed)
        self.plot_list = curves


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
