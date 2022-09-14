
from PySide2.QtWidgets import QFileDialog, QDialog
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

