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
        self.sourceGroup = QGroupBox(self.centralwidget)
        self.sourceGroup.setObjectName(u"sourceGroup")
        self.verticalLayout_4 = QVBoxLayout(self.sourceGroup)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.selectPathLayout = QHBoxLayout()
        self.selectPathLayout.setObjectName(u"selectPathLayout")
        self.label = QLabel(self.sourceGroup)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(80, 0))

        self.selectPathLayout.addWidget(self.label)

        self.pathLine = QLineEdit(self.sourceGroup)
        self.pathLine.setObjectName(u"pathLine")
        self.pathLine.setAutoFillBackground(False)
        self.pathLine.setFrame(True)
        self.pathLine.setReadOnly(True)

        self.selectPathLayout.addWidget(self.pathLine)


        self.verticalLayout_4.addLayout(self.selectPathLayout)

        self.selectPathLayout_3 = QHBoxLayout()
        self.selectPathLayout_3.setObjectName(u"selectPathLayout_3")
        self.label_6 = QLabel(self.sourceGroup)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(80, 0))

        self.selectPathLayout_3.addWidget(self.label_6)

        self.pathLine_3 = QLineEdit(self.sourceGroup)
        self.pathLine_3.setObjectName(u"pathLine_3")
        self.pathLine_3.setAutoFillBackground(False)
        self.pathLine_3.setFrame(True)
        self.pathLine_3.setReadOnly(True)

        self.selectPathLayout_3.addWidget(self.pathLine_3)


        self.verticalLayout_4.addLayout(self.selectPathLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.selectButton = QPushButton(self.sourceGroup)
        self.selectButton.setObjectName(u"selectButton")

        self.horizontalLayout.addWidget(self.selectButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.sourceGroup)

        self.parameterBox = QGroupBox(self.centralwidget)
        self.parameterBox.setObjectName(u"parameterBox")
        self.horizontalLayout_2 = QHBoxLayout(self.parameterBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
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


        self.horizontalLayout_2.addLayout(self.ratioMLayout)

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
        self.deltaSpin.setValue(10)

        self.deltaLayout.addWidget(self.deltaSpin)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.deltaLayout.addItem(self.horizontalSpacer)


        self.horizontalLayout_2.addLayout(self.deltaLayout)


        self.verticalLayout_2.addWidget(self.parameterBox)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setFrameShadow(QFrame.Plain)

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
        self.sourceGroup.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Gain File:", None))
        self.pathLine.setPlaceholderText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Gain DP File:", None))
        self.pathLine_3.setPlaceholderText("")
        self.selectButton.setText(QCoreApplication.translate("MainWindow", u"Select...", None))
        self.parameterBox.setTitle(QCoreApplication.translate("MainWindow", u"Parameters:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"M:", None))
        self.ratioMSpin.setSpecialValueText("")
        self.ratioMSpin.setPrefix("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"|S1 - S2|:", None))
        self.calculateButton.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.plotButton.setText(QCoreApplication.translate("MainWindow", u"Chart", None))
        self.exitButton.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

