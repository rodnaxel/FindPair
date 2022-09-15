
from PySide2.QtCore import Qt
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import QWidget, QFileDialog, QDialog, QVBoxLayout
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
        self.ui.browseButton.clicked.connect(self.browse)

    def browse(self):
        self.filename, _ = QFileDialog.getOpenFileName(
            self, "Open file", ".", "Data Files (*.xlsx)"
        )
        if not self.filename:
            return

        self.ui.filenameBox.setText(self.filename)
        
        wb = load_workbook(self.filename, data_only=True)
        
        self.ui.sheetBox.addItems(wb.sheetnames)
        self.ui.sheetBox.setCurrentIndex(len(wb.sheetnames) - 1)

    def settings(self):    
        return {
            "filename": self.filename,
            "sheet": self.ui.sheetBox.currentText(),
            "column": self.ui.columnBox.text(),
            "min_row": self.ui.rangeMinBox.text(),
            "max_row": self.ui.rangeMaxBox.text()
        }    


class ChartDialog(QDialog):
    def __init__(self, model=None) -> None:
        super(ChartDialog, self).__init__()

        self.setModal(True)
        self.setSizeGripEnabled(True)
        self.model = model

        self.createUI()

    def createUI(self):
        self.resize(400, 400)
        self.setWindowTitle("Graph")

        self.chart = QtCharts.QChart()
        self.chart.setTitle("Dependencies gain at k1 * k2")
        self.chart.legend().hide()
        #self.chart.createDefaultAxes()

        if self.model:
            self.add_series("gain", 0)
            self.add_series("gain", 1)

            # Setting X-axis
            self.axis_x = QtCharts.QValueAxis()
            self.axis_x.setTickCount(10)
            self.axis_x.setTitleText("Step")
            self.chart.addAxis(self.axis_x, Qt.AlignBottom)
            self.series.attachAxis(self.axis_x)

            # Setting Y-axis
            self.axis_y = QtCharts.QValueAxis()
            self.axis_y.setMin(0)
            self.axis_y.setMin(100)
            self.axis_y.setTickCount(10)
            self.axis_y.setTickType(QtCharts.QValueAxis.TicksFixed)
            self.axis_y.setLabelFormat("%.2f")
            self.axis_y.setTitleText("Gain")
            self.chart.addAxis(self.axis_y, Qt.AlignLeft)
            self.series.attachAxis(self.axis_y)
        
        self._chart_view = QtCharts.QChartView(self.chart)
        self._chart_view.setRenderHint(QPainter.Antialiasing)

        layout = QVBoxLayout(self)
        layout.addWidget(self._chart_view)

    def add_series(self, name, columns):
        self.series = QtCharts.QLineSeries()
        self.series.setName(name)

        for x in range(self.model.rowCount()):
            y = float(self.model.index(x, columns).data())
            self.series.append(x, y)

        self.chart.addSeries(self.series)



        # # Getting the color from the QChart to use it on the QTableView
        # color_name = self.series.pen().color().name()
        # self.model.color = f"{color_name}"




        