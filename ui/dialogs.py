# -*- coding: utf-8 -*-

import os
from datetime import datetime

from openpyxl import load_workbook

from PySide2.QtCore import Qt
from PySide2.QtGui import QPainter, QPixmap
from PySide2.QtWidgets import *
from PySide2.QtCharts import QtCharts

from ui.opendialog import Ui_Dialog

from core import utils


class OpenDialog(QDialog):
    def __init__(self, stg=None) -> None:
        super(OpenDialog, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.columnBox.setText("N")
        self.ui.rangeMinBox.setText("4")
        self.ui.rangeMaxBox.setText("75")

    # Connect signal/slot
        self.ui.browseButton.clicked.connect(self.on_browse)

    def on_browse(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, "Open file", "./data", "Data Files (*.xlsx)"
        )
        if not filename:
            return

        self.ui.filenameBox.setText(filename)
        
        wb = load_workbook(filename, data_only=True)
        self.ui.sheetBox.addItems(wb.sheetnames)

        # FIXME: только для отладки
        self.ui.sheetBox.setCurrentIndex(len(wb.sheetnames) - 1)

    def settings(self):    
        return {
            "filename": self.ui.filenameBox.text(),
            "sheet": self.ui.sheetBox.currentText(),
            "column": self.ui.columnBox.text(),
            "min_row": self.ui.rangeMinBox.text(),
            "max_row": self.ui.rangeMaxBox.text(),
        }



class LineChart(QtCharts.QChartView):
    def __init__(self, model):
        super(LineChart, self).__init__()

        self.model = model

        self.chart = QtCharts.QChart()
        self.chart.setTitle("Gain(K1xK2)")

        # Setting X-axis
        self.axis_x = QtCharts.QValueAxis()
        self.axis_x.setTitleText("Step")
        self.axis_x.setRange(0, 80)
        self.axis_x.setTickInterval(10)
        self.axis_x.setTickCount(9)
        self.axis_x.setMinorTickCount(4)
        self.axis_x.setLabelFormat("%d")
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)

        # Setting Y-axis
        self.axis_y = QtCharts.QValueAxis()
        self.axis_y.setTitleText("Gain")
        self.axis_y.setRange(0, 4000)
        self.axis_y.setTickInterval(10)
        self.axis_y.setTickCount(9)
        self.axis_y.setMinorTickCount(4)
        self.axis_y.setLabelFormat("%.2f")
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)

        if self.model:
            self.add_series("Gain", 0)
            self.add_series("K1xK2", 1)

        self.setChart(self.chart)
        self.setRenderHint(QPainter.Antialiasing)

    def add_series(self, name, columns, attachedX=None, attachedY=None):
        series = QtCharts.QLineSeries()
        series.setName(name)

        series.attachAxis(attachedX or self.axis_x)
        series.attachAxis(attachedY or self.axis_y)

        for x in range(self.model.rowCount()):
            y = float(self.model.index(x, columns).data())
            series.append(x, y)

        self.chart.addSeries(series)


class OtherChart(QtCharts.QChartView):
    def __init__(self, model):
        super(OtherChart, self).__init__()

        self.model = model

        self.chart = QtCharts.QChart()
        self.chart.setTitle("Gain(K1xK2)")

        # Setting X-axis
        self.axis_x = QtCharts.QValueAxis()
        self.axis_x.setTitleText("Step")
        self.axis_x.setRange(0, 80)
        self.axis_x.setTickInterval(10)
        self.axis_x.setTickCount(9)
        self.axis_x.setMinorTickCount(4)
        self.axis_x.setLabelFormat("%d")
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)

        # Setting Y2-axis
        self.axis_y = QtCharts.QValueAxis()
        self.axis_y.setTitleText("Deviation")
        self.axis_y.setRange(-50.0, 50.0)
        self.axis_y.setTickInterval(10.0)
        self.axis_y.setTickCount(9)
        self.axis_y.setMinorTickCount(4)
        self.axis_y.setLabelFormat("%.2f")
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)

        if self.model:
            self.add_series("Deviation", 4)

        self.setChart(self.chart)
        self.setRenderHint(QPainter.Antialiasing)

    def add_series(self, name, columns, attachedX=None, attachedY=None):
        series = QtCharts.QLineSeries()
        series.setName(name)

        series.attachAxis(self.axis_x)
        series.attachAxis(self.axis_y)

        for x in range(self.model.rowCount()):
            y = float(self.model.index(x, columns).data())
            series.append(x, y)

        self.chart.addSeries(series)



class ChartDialog(QDialog):
    def __init__(self, model=None) -> None:
        super(ChartDialog, self).__init__()

        self.model = model

        self.setModal(True)
        self.setSizeGripEnabled(True)
        self.resize(800, 800)

        self.setupUI()

        self.saveButton.clicked.connect(self.on_save)


    def setupUI(self):
        self._chart_view = LineChart(self.model)
        self._chart_view.setWindowTitle("gains")


        self._chart_view2 = OtherChart(self.model)
        self._chart_view2.setWindowTitle("deviation")
        self._chart_view2.setMaximumHeight(self.height() / 3)

        layout = QVBoxLayout(self)
        hbox = QHBoxLayout()

        self.saveButton = QPushButton("Save")
        hbox.addWidget(self.saveButton)

        self.clearButton = QPushButton("Clear")
        hbox.addWidget(self.clearButton)

        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hbox.addSpacerItem(spacer)

        layout.addLayout(hbox)
        layout.addWidget(self._chart_view)
        layout.addWidget(self._chart_view2)

    def on_save(self):    
        output = "./output"
        utils.make_directory(output)
        for chart in (w for w in self.children() if isinstance(w, QtCharts.QChartView)): 
            pixmap = QPixmap(chart.size())
            chart.render(pixmap)
            filename = datetime.now().strftime("%Y%m%d")  + "_" + chart.windowTitle()
            path = os.path.join(output, filename + ".png")
            print(path)
            pixmap.save(path, "PNG")







        