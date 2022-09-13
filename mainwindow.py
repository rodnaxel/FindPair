# This Python file uses the following encoding: utf-8
import sys

import logging

from PySide2 import QtCore
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QAction, QHeaderView, QDialog

from dialogs import OpenDialog
from table_model import CustomTableModel

from ui_mainwindow import Ui_MainWindow

from utils import k_pot, get_nearest_value, load_gain_from_excel, table

logger = logging.getLogger("findpair")
logger.setLevel(logging.DEBUG)
fileHandler = logging.FileHandler('errors.log')
fileHandler.setFormatter(logging.Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
logger.addHandler(fileHandler)

#stream_handler = logging.StreamHandler(stream=sys.stdout)
#stream_handler.setFormatter(logging.Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
# logger.addHandler(stream_handler)


def find_pair(gain, table, delta):
    a = [i for i in table if i[2] <= delta]
    b = [i[1] for i in a]
    near = get_nearest_value(b, gain)
    index = b.index(near)
    res = a[index]
    return res[0], res[3]

def get_amplifier_pairs(gains, deltas, table):
    result = []
    for gain in gains:
        (k1, k2), (s1,s2) = find_pair(gain, table, deltas)
        delta = gain - k1 * k2
        result.append((k1, k2, k1 * k2, gain - k1 * k2, s1, s2))
    return result



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.is_load = False

        self.createUI()

        # Connect signal/slot
        self.ui.calculateButton.clicked.connect(self.calculate)
        self.ui.plotButton.clicked.connect(self.openPlot)
        self.ui.exitButton.clicked.connect(self.exit)

    def createUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Find Pair")

        # Create menubar
        self.file_menu = self.ui.menubar.addMenu("File")

        open_action = QAction("Open...", self)
        self.file_menu.addAction(open_action)
        open_action.triggered.connect(self.openAction)

        save_as_action = QAction("Save as...", self)
        self.file_menu.addAction(save_as_action)
        #save_as_action.triggered.connect(self.report)

        # Create table view
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.ui.tableView.horizontalHeader().setStretchLastSection(False)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.verticalHeader().setDefaultAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignJustify)

    def calculate(self):
        delta = self.ui.deltaSpin.value()
        ratio_m = self.ui.ratioMSpin.value()

        gains = [x / ratio_m for x in self.gains]

        result = get_amplifier_pairs(gains, delta, table)

        self._data = [
            gains,
            [x[2] for x in result],
            [x[0] for x in result],
            [x[1] for x in result],
            [x[3] for x in result],
            [x[4] for x in result],
            [x[5] for x in result]
        ]
        self.model = CustomTableModel(self._data)
        self.ui.tableView.setModel(self.model)

    def openAction(self):
        open_dialog = OpenDialog()
        open_dialog.open()

        if (open_dialog.exec() == QDialog.Accepted):
            stg = open_dialog.settings() 

            self.gains = load_gain_from_excel(
                stg['filename'],
                stg["sheet"],
                stg["column"] + stg["min_row"],
                stg["column"] + stg["max_row"]
            )
            self.ui.pathLine.setText(stg['filename'])
            self.ui.statusbar.showMessage("Success load file")
            self.is_load = True
            self.enable_widget()

    def enable_widget(self):
        self.ui.calculateButton.setEnabled(self.is_load)
        self.ui.plotButton.setEnabled(self.is_load)

    def openPlot(self):
        print("open plot")

    def exit(self):
        QtCore.QCoreApplication.exit(0)



if __name__ == "__main__":
    app = QApplication([])
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
