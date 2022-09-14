# This Python file uses the following encoding: utf-8
import sys
import logging

from PySide2 import QtCore
from PySide2.QtWidgets import QApplication, QMainWindow,  QAction, QHeaderView, QFileDialog, QDialog, QMessageBox
from PySide2.QtCharts import QtCharts

from models.table_model import CustomTableModel

from ui.dialogs import OpenDialog
from ui.ui_mainwindow import Ui_MainWindow

from core import findpair


__ver__ = '0.9'


logger = logging.getLogger("findpair")
logger.setLevel(logging.DEBUG)
fileHandler = logging.FileHandler('errors.log')
fileHandler.setFormatter(logging.Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
logger.addHandler(fileHandler)

#stream_handler = logging.StreamHandler(stream=sys.stdout)
#stream_handler.setFormatter(logging.Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
# logger.addHandler(stream_handler)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.is_load = False
        self.has_changed = False
        self.file_settings = None

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

        if (open_dialog.exec() == QDialog.Accepted):
            stg = open_dialog.settings() 
            
            if (stg['filename']):
                self.is_load = True
                self.ui.pathLine.setText(stg['filename'])
                self.file_settings = stg
                self.ui.statusbar.showMessage("Success load file")
            else:
                self.file_settings = None
                self.is_load = False

    def on_save_as(self):
        filename, _  = QFileDialog.getSaveFileName(
            self, "Save as", "./data", "Output (*.csv, *.txt)"
        )
        if not filename:
            return
      
        self.ui.statusbar.showMessage(f"Save to {filename}")

    def on_update(self):

        tolerance = self.ui.deltaSpin.value()
        ratio_m = self.ui.ratioMSpin.value()

        try:
            df = findpair.make_it_beatiful(
                self.file_settings, tolerance=tolerance, m=ratio_m)
        except Exception as e:
            logger.exception("Error in function update")
            df = None
        finally:
            self.ui.statusbar.showMessage("Error handle data")

        if not df:
            return

        self.model = CustomTableModel(df)
        self.ui.tableView.setModel(self.model)

        self.ui.calculateButton.setEnabled(False)

    def on_open_plot(self):
        QMessageBox.information(self, "Info", "Недоступно в бесплатной версии")

    def exit(self):
        QtCore.QCoreApplication.exit(0)

    def on_changed_parameters(self):
        self.has_changed = True
        self.ui.calculateButton.setEnabled(True)



if __name__ == "__main__":
    app = QApplication([])
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
