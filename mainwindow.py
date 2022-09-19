# -*- coding: utf-8 -*-

import sys
import logging

from PySide2 import QtCore
from PySide2.QtWidgets import QApplication, QMainWindow, QAction, QHeaderView, QFileDialog, QDialog, QMessageBox
from PySide2.QtCharts import QtCharts

from models.table_model import CustomTableModel

from ui.dialogs import OpenDialog, ChartDialog
from ui.ui_mainwindow import Ui_MainWindow

from core import findpair
from core import utils

__ver__ = '0.92'

logger = logging.getLogger("findpair")
logger.setLevel(logging.DEBUG)
fileHandler = logging.FileHandler('errors.log')
fileHandler.setFormatter(logging.Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
logger.addHandler(fileHandler)


# stream_handler = logging.StreamHandler(stream=sys.stdout)
# stream_handler.setFormatter(logging.Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
# logger.addHandler(stream_handler)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.is_load = False
        self.has_changed = False

        self.settings = {}
        #Fxime:
        self.points = []

        self.model = None

        self.createUi()

        # Connect signal/slot
        self.ui.selectButton.clicked.connect(self.on_open_file)
        self.ui.selectDpButton.clicked.connect(self.on_select_ratio_file)

        self.ui.calculateButton.clicked.connect(self.on_update)
        self.ui.plotButton.clicked.connect(self.on_open_plot)
        self.ui.exitButton.clicked.connect(self.exit)

        self.ui.sourceGainLine.textChanged.connect(self.source_changed)
        self.ui.sourceDpLine.textChanged.connect(self.parameter_changed)
        self.ui.deltaSpin.textChanged.connect(self.parameter_changed)
        self.ui.ratioMSpin.textChanged.connect(self.parameter_changed)
        self.ui.sourceGainLine.textChanged.connect(self.parameter_changed)

    def createUi(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.createMenuBar()
        self.createTableView()

    def createMenuBar(self):
        self.file_menu = self.ui.menubar.addMenu("File")

        open_action = QAction("Open...", self)
        open_action.triggered.connect(self.on_open_file)
        self.file_menu.addAction(open_action)

        save_as_action = QAction("Save as...", self)
        save_as_action.triggered.connect(self.on_save_as)
        self.file_menu.addAction(save_as_action)

        about_action = QAction("About...", self)
        about_action.triggered.connect(
            lambda: QMessageBox().about(self, "About FindPairs", f"Version: {__ver__}")
        )
        self.file_menu.addAction(about_action)

    def createTableView(self):
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.ui.tableView.horizontalHeader().setSectionsMovable(True)
        self.ui.tableView.horizontalHeader().setStretchLastSection(False)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.verticalHeader().setDefaultAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignJustify)

    def on_open_file(self):
        open_dialog = OpenDialog()

        if open_dialog.exec() == QDialog.Accepted:
            stg = open_dialog.settings()

            if stg['filename']:
                self.is_load = True
                self.settings.update(stg)

                self.ui.sourceGainLine.setText(self.settings['filename'])
                self.ui.statusbar.showMessage(
                    f"Success load file {self.settings['filename']}"
                )

    def on_select_ratio_file(self):
        filename, _ = QFileDialog().getOpenFileName(
            dir="./data/"
        )

        if not filename:
            return

        self.points = utils.load_potentiometer_gain(filename)
        self.ui.sourceDpLine.setText(filename)
        self.ui.statusbar.showMessage(f"Load file with potentiometer ratio {filename}") 

    def on_save_as(self):
        path = QFileDialog.getExistingDirectory(
            self, "Open directory", "./data", QFileDialog.ShowDirsOnly
        )
        if not path:
            return

        # Prepare data for saving
        datatable = []
        for r in range(self.model.rowCount()):
            row = []
            for c in range(self.model.columnCount()):
                row.append(self.model.index(r, c).data())
            datatable.append(row)
        utils.to_csv(path + "/output.csv", datatable)

        print(self.chart_dialog)
        self.ui.statusbar.showMessage(f"Save to {path}")


    def on_update(self):
        tolerance = self.ui.deltaSpin.value()
        ratio_m = self.ui.ratioMSpin.value()

        try:
            df, _ = findpair.make_it_beatiful(
                self.settings, tolerance=tolerance, m=ratio_m, points=self.points)
        except Exception as e:
            logger.exception("Error in function update")
            df = None
            self.ui.statusbar.showMessage("Error handle data")

        if not df:
            return

        self.model = CustomTableModel(df)
        self.ui.tableView.setModel(self.model)

        self.ui.calculateButton.setEnabled(False)
        self.ui.statusbar.showMessage("Success handle data")

        self.has_changed = False

    def on_open_plot(self):
        self.chart_dialog = ChartDialog(model=self.model)
        self.chart_dialog.exec()

    @staticmethod
    def exit(self):
        QtCore.QCoreApplication.exit(0)

    def source_changed(self):
        self.ui.calculateButton.setEnabled(True)

    def parameter_changed(self):
        self.has_changed = True
        if self.is_load:
            self.ui.calculateButton.setEnabled(True)


if __name__ == "__main__":
    app = QApplication([])
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
