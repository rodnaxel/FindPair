from PySide2.QtCore import Qt, QAbstractTableModel, QModelIndex
from PySide2.QtGui import QColor


class CustomTableModel(QAbstractTableModel):

    section_names = ("Gain", "K1 x K2", "K1", "K2", "|Gain - K2 x K1|", "Step 1", "Step 2")

    def __init__(self, data=None):
        QAbstractTableModel.__init__(self)

        self.load_data(data)

    def load_data(self, data):
        self._data = data

        self.gains = data[0]
        self.gains_c  = data[1]
        self.k1 = data[2]
        self.k2 = data[3]
        self.diff = data[4]
        self.s1 = data[5]
        self.s2 = data[6] 

        self.modelReset.emit()

    def rowCount(self, parent=QModelIndex()):
        if not self._data:
            return 0
        else:
            return len(self._data[0])

    def columnCount(self, parent=QModelIndex()):
        return len(self.section_names)

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return self.section_names[section]
        else:
            return f"{section}"

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self._data[index.column()][index.row()]
        elif role == Qt.BackgroundRole:
            return QColor(Qt.white)
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignRight

    def reset(self):
        self.beginResetModel()
        self._data = []
        self.endResetModel()