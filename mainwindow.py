# This Python file uses the following encoding: utf-8
from fileinput import filename
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

__ver__ = '0.9'

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
        self.file_settings = None

        self.model = None

        self.createUI()

        # Connect signal/slot
        self.ui.calculateButton.clicked.connect(self.on_update)
        self.ui.plotButton.clicked.connect(self.on_open_plot)
        self.ui.exitButton.clicked.connect(self.exit)

        self.ui.deltaSpin.textChanged.connect(self.on_changed_parameters)
        self.ui.ratioMSpin.textChanged.connect(self.on_changed_parameters)
        self.ui.pathLine.textChanged.connect(self.on_changed_parameters)

    def createUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle(f"Find Pair")

        # Menubar
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

        # Table View
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.ui.tableView.horizontalHeader().setSectionsMovable(True)
        self.ui.tableView.horizontalHeader().setStretchLastSection(False)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.verticalHeader().setDefaultAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignJustify)

    def on_open_file(self):
        open_dialog = OpenDialog()
        open_dialog.open()

        if open_dialog.exec() == QDialog.Accepted:
            stg = open_dialog.settings()

            if stg['filename']:
                self.is_load = True
                self.ui.pathLine.setText(stg['filename'])
                self.file_settings = stg
                self.ui.statusbar.showMessage("Success load file")
            else:
                self.file_settings = None
                self.is_load = False

    def on_save_as(self):
        path = QFileDialog.getExistingDirectory(
            self, "Open directory", "./data", QFileDialog.ShowDirsOnly
        )
        if not path:
            return

        k1 = []
        k2 = []
        for x in range(self.model.rowCount()):
            k1.append(self.model.index(x, 5).data())
            k2.append(self.model.index(x, 6).data())
        utils.save_as(path, (k1, k2), fmt='hex')

        self.ui.statusbar.showMessage(f"Save to {path}")

    def on_update(self):
        tolerance = self.ui.deltaSpin.value()
        ratio_m = self.ui.ratioMSpin.value()

        try:
            df, sigma = findpair.make_it_beatiful(
                self.file_settings, tolerance=tolerance, m=ratio_m)
        except Exception as e:
            logger.exception("Error in function update")
            df = None
            self.ui.statusbar.showMessage("Error handle data")

        if not df:
            return

        self.model = CustomTableModel(df)
        self.ui.tableView.setModel(self.model)

        self.ui.msdLabel.setText(f"{sigma:.2F}")

        self.ui.calculateButton.setEnabled(False)
        self.has_changed = False
        self.ui.statusbar.showMessage("Success handle data")

    def on_open_plot(self):
        chart_dialog = ChartDialog(model=self.model)
        chart_dialog.open()
        chart_dialog.exec()

    @staticmethod
    def exit(self):
        QtCore.QCoreApplication.exit(0)

    def on_changed_parameters(self):
        self.has_changed = True
        if self.is_load:
            self.ui.calculateButton.setEnabled(True)


if __name__ == "__main__":
    app = QApplication([])
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
