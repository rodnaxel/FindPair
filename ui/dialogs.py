# -*- coding: utf-8 -*-

from PySide2.QtCore import Qt
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import QFileDialog, QDialog, QVBoxLayout
from PySide2.QtCharts import QtCharts

from ui.opendialog import Ui_Dialog

from openpyxl import load_workbook


class OpenDialog(QDialog):
    def __init__(self) -> None:
        super(OpenDialog, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.columnBox.setText("N")
        self.ui.rangeMinBox.setText("4")
        self.ui.rangeMaxBox.setText("75")

    # Connect signal/slot
        self.ui.browseButton.clicked.connect(self.on_browse)

    def on_browse(self):
        self.filename, _ = QFileDialog.getOpenFileName(
            self, "Open file", "./data", "Data Files (*.xlsx)"
        )
        if not self.filename:
            return

        self.ui.filenameBox.setText(self.filename)
        
        wb = load_workbook(self.filename, data_only=True)
        self.ui.sheetBox.addItems(wb.sheetnames)

        # FIXME: только для отладки
        self.ui.sheetBox.setCurrentIndex(len(wb.sheetnames) - 1)

    def settings(self):    
        return {
            "filename": self.filename,
            "sheet": self.ui.sheetBox.currentText(),
            "column": self.ui.columnBox.text(),
            "min_row": self.ui.rangeMinBox.text(),
            "max_row": self.ui.rangeMaxBox.text(),
            "updated": self.ui.loadAndUpdateCheck.isChecked()
        }    


class ChartDialog(QDialog):
    def __init__(self, model=None) -> None:
        super(ChartDialog, self).__init__()

        self.model = model

        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Gain(K1xK2)")
        self.setModal(True)
        self.setSizeGripEnabled(True)
        self.resize(800, 800)

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

        self._chart_view = QtCharts.QChartView(self.chart)
        self._chart_view.setRenderHint(QPainter.Antialiasing)

        layout = QVBoxLayout(self)
        layout.addWidget(self._chart_view)

    def add_series(self, name, columns):
        series = QtCharts.QLineSeries()
        series.setName(name)
        series.attachAxis(self.axis_x)
        series.attachAxis(self.axis_y)

        for x in range(self.model.rowCount()):
            y = float(self.model.index(x, columns).data())
            series.append(x, y)

        self.chart.addSeries(series)

        # # Getting the color from the QChart to use it on the QTableView
        # color_name = self.series.pen().color().name()
        # self.model.color = f"{color_name}"




        