# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferencesdialog.ui'
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
        Dialog.resize(500, 400)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
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


        self.verticalLayout_3.addLayout(self.h_layout_1)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFlat(False)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.h_layout_2 = QHBoxLayout()
        self.h_layout_2.setObjectName(u"h_layout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(60, 0))

        self.h_layout_2.addWidget(self.label_2)

        self.gainSheetBox = QComboBox(self.groupBox)
        self.gainSheetBox.setObjectName(u"gainSheetBox")
        self.gainSheetBox.setEnabled(True)
        self.gainSheetBox.setMinimumSize(QSize(150, 0))

        self.h_layout_2.addWidget(self.gainSheetBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.h_layout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.h_layout_2)

        self.h_layout_3 = QHBoxLayout()
        self.h_layout_3.setObjectName(u"h_layout_3")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(60, 0))

        self.h_layout_3.addWidget(self.label_3)

        self.gainColumnBox = QLineEdit(self.groupBox)
        self.gainColumnBox.setObjectName(u"gainColumnBox")
        self.gainColumnBox.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gainColumnBox.sizePolicy().hasHeightForWidth())
        self.gainColumnBox.setSizePolicy(sizePolicy)
        self.gainColumnBox.setMinimumSize(QSize(40, 0))
        self.gainColumnBox.setMaximumSize(QSize(40, 16777215))
        self.gainColumnBox.setBaseSize(QSize(40, 0))

        self.h_layout_3.addWidget(self.gainColumnBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.h_layout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.h_layout_3)

        self.h_layout_4 = QHBoxLayout()
        self.h_layout_4.setObjectName(u"h_layout_4")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(60, 0))

        self.h_layout_4.addWidget(self.label_4)

        self.gainRangeMinBox = QLineEdit(self.groupBox)
        self.gainRangeMinBox.setObjectName(u"gainRangeMinBox")
        self.gainRangeMinBox.setEnabled(True)
        sizePolicy.setHeightForWidth(self.gainRangeMinBox.sizePolicy().hasHeightForWidth())
        self.gainRangeMinBox.setSizePolicy(sizePolicy)
        self.gainRangeMinBox.setMinimumSize(QSize(40, 0))
        self.gainRangeMinBox.setMaximumSize(QSize(40, 16777215))
        self.gainRangeMinBox.setBaseSize(QSize(40, 0))

        self.h_layout_4.addWidget(self.gainRangeMinBox)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.h_layout_4.addWidget(self.label_5)

        self.gainRangeMaxBox = QLineEdit(self.groupBox)
        self.gainRangeMaxBox.setObjectName(u"gainRangeMaxBox")
        self.gainRangeMaxBox.setEnabled(True)
        sizePolicy.setHeightForWidth(self.gainRangeMaxBox.sizePolicy().hasHeightForWidth())
        self.gainRangeMaxBox.setSizePolicy(sizePolicy)
        self.gainRangeMaxBox.setMinimumSize(QSize(40, 0))
        self.gainRangeMaxBox.setMaximumSize(QSize(40, 16777215))
        self.gainRangeMaxBox.setBaseSize(QSize(40, 0))

        self.h_layout_4.addWidget(self.gainRangeMaxBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.h_layout_4.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.h_layout_4)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(True)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.h_layout_5 = QHBoxLayout()
        self.h_layout_5.setObjectName(u"h_layout_5")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(60, 0))

        self.h_layout_5.addWidget(self.label_6)

        self.ratioSheetBox = QComboBox(self.groupBox_2)
        self.ratioSheetBox.setObjectName(u"ratioSheetBox")
        self.ratioSheetBox.setEnabled(True)
        self.ratioSheetBox.setMinimumSize(QSize(150, 0))

        self.h_layout_5.addWidget(self.ratioSheetBox)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.h_layout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.h_layout_5)

        self.h_layout_6 = QHBoxLayout()
        self.h_layout_6.setObjectName(u"h_layout_6")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(60, 0))

        self.h_layout_6.addWidget(self.label_7)

        self.ratioColumnBox = QLineEdit(self.groupBox_2)
        self.ratioColumnBox.setObjectName(u"ratioColumnBox")
        self.ratioColumnBox.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ratioColumnBox.sizePolicy().hasHeightForWidth())
        self.ratioColumnBox.setSizePolicy(sizePolicy)
        self.ratioColumnBox.setMinimumSize(QSize(40, 0))
        self.ratioColumnBox.setMaximumSize(QSize(40, 16777215))
        self.ratioColumnBox.setBaseSize(QSize(40, 0))

        self.h_layout_6.addWidget(self.ratioColumnBox)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.h_layout_6.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.h_layout_6)

        self.h_layout_7 = QHBoxLayout()
        self.h_layout_7.setObjectName(u"h_layout_7")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(60, 0))

        self.h_layout_7.addWidget(self.label_8)

        self.ratioRangeMinBox = QLineEdit(self.groupBox_2)
        self.ratioRangeMinBox.setObjectName(u"ratioRangeMinBox")
        self.ratioRangeMinBox.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ratioRangeMinBox.sizePolicy().hasHeightForWidth())
        self.ratioRangeMinBox.setSizePolicy(sizePolicy)
        self.ratioRangeMinBox.setMinimumSize(QSize(40, 0))
        self.ratioRangeMinBox.setMaximumSize(QSize(40, 16777215))
        self.ratioRangeMinBox.setBaseSize(QSize(40, 0))

        self.h_layout_7.addWidget(self.ratioRangeMinBox)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.h_layout_7.addWidget(self.label_9)

        self.ratioRangeMaxBox = QLineEdit(self.groupBox_2)
        self.ratioRangeMaxBox.setObjectName(u"ratioRangeMaxBox")
        self.ratioRangeMaxBox.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ratioRangeMaxBox.sizePolicy().hasHeightForWidth())
        self.ratioRangeMaxBox.setSizePolicy(sizePolicy)
        self.ratioRangeMaxBox.setMinimumSize(QSize(40, 0))
        self.ratioRangeMaxBox.setMaximumSize(QSize(40, 16777215))
        self.ratioRangeMaxBox.setBaseSize(QSize(40, 0))

        self.h_layout_7.addWidget(self.ratioRangeMaxBox)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.h_layout_7.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.h_layout_7)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.loadAndUpdateCheck_2 = QCheckBox(Dialog)
        self.loadAndUpdateCheck_2.setObjectName(u"loadAndUpdateCheck_2")
        self.loadAndUpdateCheck_2.setChecked(True)

        self.verticalLayout_3.addWidget(self.loadAndUpdateCheck_2)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_3.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Open file", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Filename:", None))
        self.filenameBox.setPlaceholderText(QCoreApplication.translate("Dialog", u"Select source data file", None))
        self.browseButton.setText(QCoreApplication.translate("Dialog", u"Browse...", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Gain data:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Sheet:", None))
        self.gainSheetBox.setPlaceholderText(QCoreApplication.translate("Dialog", u"Select sheet", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Column:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Range:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u":", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Potentiometer data:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Sheet:", None))
        self.ratioSheetBox.setPlaceholderText(QCoreApplication.translate("Dialog", u"Select sheet", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Column:", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Range:", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u":", None))
        self.loadAndUpdateCheck_2.setText(QCoreApplication.translate("Dialog", u"Load and update", None))
    # retranslateUi

