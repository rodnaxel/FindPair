# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.selectPathLayout = QHBoxLayout()
        self.selectPathLayout.setObjectName(u"selectPathLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.selectPathLayout.addWidget(self.label)

        self.pathLine = QLineEdit(self.centralwidget)
        self.pathLine.setObjectName(u"pathLine")
        self.pathLine.setAutoFillBackground(False)
        self.pathLine.setFrame(True)
        self.pathLine.setReadOnly(True)

        self.selectPathLayout.addWidget(self.pathLine)


        self.verticalLayout_2.addLayout(self.selectPathLayout)

        self.parameterBox = QGroupBox(self.centralwidget)
        self.parameterBox.setObjectName(u"parameterBox")
        self.verticalLayout = QVBoxLayout(self.parameterBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.deltaLayout = QHBoxLayout()
        self.deltaLayout.setObjectName(u"deltaLayout")
        self.label_2 = QLabel(self.parameterBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 0))

        self.deltaLayout.addWidget(self.label_2)

        self.deltaSpin = QSpinBox(self.parameterBox)
        self.deltaSpin.setObjectName(u"deltaSpin")
        self.deltaSpin.setMinimumSize(QSize(60, 0))
        self.deltaSpin.setMaximum(255)
        self.deltaSpin.setValue(1)

        self.deltaLayout.addWidget(self.deltaSpin)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.deltaLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.deltaLayout)

        self.ratioMLayout = QHBoxLayout()
        self.ratioMLayout.setObjectName(u"ratioMLayout")
        self.label_3 = QLabel(self.parameterBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(50, 0))

        self.ratioMLayout.addWidget(self.label_3)

        self.ratioMSpin = QDoubleSpinBox(self.parameterBox)
        self.ratioMSpin.setObjectName(u"ratioMSpin")
        self.ratioMSpin.setMinimumSize(QSize(60, 0))
        self.ratioMSpin.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.ratioMSpin.setMinimum(0.100000000000000)
        self.ratioMSpin.setMaximum(10.000000000000000)
        self.ratioMSpin.setSingleStep(0.010000000000000)
        self.ratioMSpin.setValue(2.160000000000000)

        self.ratioMLayout.addWidget(self.ratioMSpin)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.ratioMLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.ratioMLayout)


        self.verticalLayout_2.addWidget(self.parameterBox)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.layout = QHBoxLayout()
        self.layout.setObjectName(u"layout")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(50, 0))

        self.layout.addWidget(self.label_4)

        self.msdLabel = QLabel(self.groupBox)
        self.msdLabel.setObjectName(u"msdLabel")
        self.msdLabel.setMinimumSize(QSize(50, 0))
        self.msdLabel.setFrameShape(QFrame.Box)
        self.msdLabel.setFrameShadow(QFrame.Raised)

        self.layout.addWidget(self.msdLabel)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.layout)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_2.addWidget(self.tableView)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.calculateButton = QPushButton(self.centralwidget)
        self.calculateButton.setObjectName(u"calculateButton")
        self.calculateButton.setEnabled(False)

        self.buttonsLayout.addWidget(self.calculateButton)

        self.plotButton = QPushButton(self.centralwidget)
        self.plotButton.setObjectName(u"plotButton")
        self.plotButton.setEnabled(True)

        self.buttonsLayout.addWidget(self.plotButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.buttonsLayout.addItem(self.horizontalSpacer_3)

        self.exitButton = QPushButton(self.centralwidget)
        self.exitButton.setObjectName(u"exitButton")

        self.buttonsLayout.addWidget(self.exitButton)


        self.verticalLayout_2.addLayout(self.buttonsLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Source:", None))
        self.pathLine.setPlaceholderText("")
        self.parameterBox.setTitle(QCoreApplication.translate("MainWindow", u"Parameters:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"|S1 - S2|:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"M:", None))
        self.ratioMSpin.setSpecialValueText("")
        self.ratioMSpin.setPrefix("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Result:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Sigma:", None))
        self.msdLabel.setText("")
        self.calculateButton.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.plotButton.setText(QCoreApplication.translate("MainWindow", u"Chart", None))
        self.exitButton.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

