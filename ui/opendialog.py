# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'opendialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 180)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.h_layout_1 = QHBoxLayout()
        self.h_layout_1.setObjectName(u"h_layout_1")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 0))

        self.h_layout_1.addWidget(self.label)

        self.filenameBox = QLineEdit(Dialog)
        self.filenameBox.setObjectName(u"filenameBox")
        self.filenameBox.setReadOnly(True)

        self.h_layout_1.addWidget(self.filenameBox)

        self.browseButton = QPushButton(Dialog)
        self.browseButton.setObjectName(u"browseButton")

        self.h_layout_1.addWidget(self.browseButton)


        self.verticalLayout.addLayout(self.h_layout_1)

        self.h_layout_2 = QHBoxLayout()
        self.h_layout_2.setObjectName(u"h_layout_2")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(60, 0))

        self.h_layout_2.addWidget(self.label_2)

        self.sheetBox = QComboBox(Dialog)
        self.sheetBox.setObjectName(u"sheetBox")
        self.sheetBox.setEnabled(True)
        self.sheetBox.setMinimumSize(QSize(150, 0))

        self.h_layout_2.addWidget(self.sheetBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.h_layout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.h_layout_2)

        self.h_layout_3 = QHBoxLayout()
        self.h_layout_3.setObjectName(u"h_layout_3")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(60, 0))

        self.h_layout_3.addWidget(self.label_3)

        self.columnBox = QLineEdit(Dialog)
        self.columnBox.setObjectName(u"columnBox")
        self.columnBox.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.columnBox.sizePolicy().hasHeightForWidth())
        self.columnBox.setSizePolicy(sizePolicy)
        self.columnBox.setMinimumSize(QSize(40, 0))
        self.columnBox.setMaximumSize(QSize(40, 16777215))
        self.columnBox.setBaseSize(QSize(40, 0))

        self.h_layout_3.addWidget(self.columnBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.h_layout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.h_layout_3)

        self.h_layout_4 = QHBoxLayout()
        self.h_layout_4.setObjectName(u"h_layout_4")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(60, 0))

        self.h_layout_4.addWidget(self.label_4)

        self.rangeMinBox = QLineEdit(Dialog)
        self.rangeMinBox.setObjectName(u"rangeMinBox")
        self.rangeMinBox.setEnabled(True)
        sizePolicy.setHeightForWidth(self.rangeMinBox.sizePolicy().hasHeightForWidth())
        self.rangeMinBox.setSizePolicy(sizePolicy)
        self.rangeMinBox.setMinimumSize(QSize(40, 0))
        self.rangeMinBox.setMaximumSize(QSize(40, 16777215))
        self.rangeMinBox.setBaseSize(QSize(40, 0))

        self.h_layout_4.addWidget(self.rangeMinBox)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.h_layout_4.addWidget(self.label_5)

        self.rangeMaxBox = QLineEdit(Dialog)
        self.rangeMaxBox.setObjectName(u"rangeMaxBox")
        self.rangeMaxBox.setEnabled(True)
        sizePolicy.setHeightForWidth(self.rangeMaxBox.sizePolicy().hasHeightForWidth())
        self.rangeMaxBox.setSizePolicy(sizePolicy)
        self.rangeMaxBox.setMinimumSize(QSize(40, 0))
        self.rangeMaxBox.setMaximumSize(QSize(40, 16777215))
        self.rangeMaxBox.setBaseSize(QSize(40, 0))

        self.h_layout_4.addWidget(self.rangeMaxBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.h_layout_4.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.h_layout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Open file", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Filename:", None))
        self.filenameBox.setPlaceholderText(QCoreApplication.translate("Dialog", u"Select path to source file", None))
        self.browseButton.setText(QCoreApplication.translate("Dialog", u"Browse...", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Sheet:", None))
        self.sheetBox.setPlaceholderText(QCoreApplication.translate("Dialog", u"Select sheet", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Column:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Range:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u":", None))
    # retranslateUi

