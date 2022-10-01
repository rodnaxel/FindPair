from PySide2.QtCharts import QtCharts
from PySide2.QtCore import Qt
from PySide2.QtGui import QPainter


class BaseChartView(QtCharts.QChartView):
    def __init__(self, **options):
        super(BaseChartView, self).__init__()

        self.chart = QtCharts.QChart()
        self.chart.setTitle("Gain(K1xK2)")

        self.add_axis_x()
        self.add_axis_y()

        self.setChart(self.chart)
        self.setRenderHint(QPainter.Antialiasing)

    def add_axis_x(self):
        raise NotImplementedError()
    
    def add_axis_y(self):
        raise NotImplementedError()

    def add_series(self):
        raise NotImplementedError()


class LineChart(BaseChartView):
    def __init__(self, model):
        super(LineChart, self).__init__()

        self.model = model

        if self.model:
            self.add_series("Gain", 0)
            self.add_series("K1xK2", 1)


    def add_axis_x(self):
        self.axis_x = QtCharts.QValueAxis()
        self.axis_x.setTitleText("Step")
        self.axis_x.setRange(0, 80)
        self.axis_x.setTickInterval(10)
        self.axis_x.setTickCount(9)
        self.axis_x.setMinorTickCount(4)
        self.axis_x.setLabelFormat("%d")
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)

    def add_axis_y(self):
        self.axis_y = QtCharts.QValueAxis()
        self.axis_y.setTitleText("Gain")
        self.axis_y.setRange(0, 2400)
        self.axis_y.setTickInterval(10)
        self.axis_y.setTickCount(9)
        self.axis_y.setMinorTickCount(4)
        self.axis_y.setLabelFormat("%.2f")
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)

    def add_series(self, name, columns, attachedX=None, attachedY=None):
        series = QtCharts.QLineSeries()
        series.setName(name)

        for x in range(self.model.rowCount()):
            y = float(self.model.index(x, columns).data())
            series.append(x, y)

        self.chart.addSeries(series)

        series.attachAxis(attachedX or self.axis_x)
        series.attachAxis(attachedY or self.axis_y)


class DeviationChart(BaseChartView):
    def __init__(self, model):
        super(DeviationChart, self).__init__()

        self.model = model
      
        if self.model:
            self.add_series("Deviation", 4)

    def add_axis_x(self):
        self.axis_x = QtCharts.QValueAxis()
        self.axis_x.setTitleText("Step")
        self.axis_x.setRange(0, 80)
        self.axis_x.setTickInterval(10)
        self.axis_x.setTickCount(9)
        self.axis_x.setMinorTickCount(4)
        self.axis_x.setLabelFormat("%d")
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)

    def add_axis_y(self):
        self.axis_y = QtCharts.QValueAxis()
        self.axis_y.setTitleText("Deviation")
        self.axis_y.setRange(-60.0, 60.0)
        self.axis_y.setTickInterval(10.0)
        self.axis_y.setTickCount(9)
        self.axis_y.setMinorTickCount(4)
        self.axis_y.setLabelFormat("%.2f")
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)

    def add_series(self, name, columns, attachedX=None, attachedY=None):
        series = QtCharts.QLineSeries()
        series.setName(name)

        for x in range(self.model.rowCount()):
            y = round(float(self.model.index(x, columns).data()),1)
            series.append(x, y)

        self.chart.addSeries(series)

        series.attachAxis(self.axis_x)
        series.attachAxis(self.axis_y)
