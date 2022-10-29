# -*- coding: utf-8 -*-

import sys, os
import logging

from PySide2 import QtCore
from PySide2.QtCore import QTranslator
from PySide2.QtGui import QGuiApplication
from PySide2.QtWidgets import (
    QApplication, QWidget, QMainWindow, QAction, QHeaderView, QFileDialog, QDialog, QMessageBox)

from PySide2.QtCharts import QtCharts

from models.table_model import CustomTableModel

from ui.dialogs import OpenDialog, ChartDialog
from ui.ui_mainwindow import Ui_MainWindow

from core import findpair
from core import utils

__ver__ = '0.96'

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
        # !TODO: Translator
        # self._translator = QTranslator()
        # self._translator.load('./translations/language_ru.qm')
        # QGuiApplication.installTranslator(self._translator)
        # QGuiApplication.removeTranslator(self._translator)
        # self.ui.retranslateUi(self)

        self.is_load = False
        self.has_changed = False

        self.settings = {}
        # Fxime:
        self.points = {}

        self.model = None

        self.createUi()

        # Connect signal/slot
        self.ui.selectButton.clicked.connect(self.on_open_preferences)

        self.ui.calculateButton.clicked.connect(self.on_update)
        self.ui.plotButton.clicked.connect(self.on_open_plot)
        self.ui.reportButton.clicked.connect(self.on_save_as)
        self.ui.exitButton.clicked.connect(self.exit)

        self.ui.sourceGainLine.textChanged.connect(self.source_changed)
        self.ui.deltaSpin.textChanged.connect(self.parameter_changed)
        self.ui.ratioMSpin.textChanged.connect(self.parameter_changed)
        self.ui.sourceGainLine.textChanged.connect(self.parameter_changed)

    def createUi(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.createMenuBar()
        self.createTableView()

    def createMenuBar(self):
        self.ui.actionOpen.triggered.connect(self.on_open_preferences)
        self.ui.actionSave_as.triggered.connect(self.on_save_as)
        self.ui.actionAbout.triggered.connect(
            lambda: QMessageBox().about(self,
                                        self.tr("About FindPairs"),
                                        self.tr(f"Version: {__ver__}"))
        )

    def createTableView(self):
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.ui.tableView.horizontalHeader().setSectionsMovable(True)
        self.ui.tableView.horizontalHeader().setStretchLastSection(False)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.verticalHeader().setDefaultAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignJustify)

    def on_open_preferences(self):
        open_dialog = OpenDialog(self)

        if open_dialog.exec() == QDialog.Accepted:
            stg = open_dialog.read_settings()

            if stg['filename']:
                self.is_load = True
                self.settings.update(stg)

                self.ui.sourceGainLine.setText(self.settings['filename'])
                self.setWindowTitle(
                    "{0} {1}".format(self.windowTitle(), self.settings['filename'])
                )

    def on_save_as(self):
        if not self.model:
            self.ui.statusbar.showMessage("Error: No data for report")
            return

        filename, _ = QFileDialog.getSaveFileName(
            self, "Save as", ".", "Excel (*.xlsx)"
        )

        if not filename:
            return

        # Prepare data for saving
        headers = ["№", "КУ", "К1 x K2", "K1", "K2", "КУ - К1 х К2", "S1 (dec)", "S1 (hex)", "S2 (dec)", "S2 (hex)"]
        rows = []
        for index, r in enumerate(range(self.model.rowCount()), 1):
            row = [index]
            for c in range(self.model.columnCount()):
                value = self.model.index(r, c).data()
                if c in [5, 6]:
                    row.extend((value, hex(value)))
                else:
                    row.append(value)

            rows.append(row)

        tolerance = self.ui.deltaSpin.value()
        ratio_m = self.ui.ratioMSpin.value()

        try:
            utils.to_excel(filename, rows, tolerance, ratio_m, headers=headers)
        except PermissionError:
            QMessageBox().critical(self, "Error", "Сохранение недоступно. Закройте файл и повторите попытку")
            self.ui.statusbar.showMessage(f"Error save report to {filename}")

        self.ui.statusbar.showMessage(f"Save to {filename}")

    def on_update(self):
        tolerance = self.ui.deltaSpin.value()
        ratio_m = self.ui.ratioMSpin.value()

        df = findpair.make_it_beatiful(
            self.settings, tolerance=tolerance, m=ratio_m)

        # try:
        #     df = findpair.make_it_beatiful(
        #         self.settings, tolerance=tolerance, m=ratio_m)
        # except Exception as e:
        #     logger.exception("Error in function update")
        #     df = None
        #     self.ui.statusbar.showMessage("Error update data")

        if not df:
            return

        self.model = CustomTableModel(df)
        self.ui.tableView.setModel(self.model)

        self.ui.calculateButton.setEnabled(False)
        self.ui.statusbar.showMessage("Data updated")

        self.ui.reportButton.setEnabled(True)

        self.has_changed = False

    def on_open_plot(self):
        self.chart_dialog = ChartDialog(model=self.model)
        self.chart_dialog.exec()

    def on_report(self):
        filename = "./data/report.xlsx"
        self.ui.statusbar.showMessage(f"Report data to file {filename}")

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

    # if os.path.exists('./translations/language_ru.qm'):
    #     translator = QTranslator(app)
    #     translator.load('./translations/language_ru.qm')
    #     app.installTranslator(translator)

    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
