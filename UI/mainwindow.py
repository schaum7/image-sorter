# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ImageSorter(object):
    def setupUi(self, ImageSorter):
        ImageSorter.setObjectName("ImageSorter")
        ImageSorter.resize(800, 166)
        self.centralwidget = QtWidgets.QWidget(ImageSorter)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_path_source = QtWidgets.QLabel(self.centralwidget)
        self.lbl_path_source.setObjectName("lbl_path_source")
        self.gridLayout.addWidget(self.lbl_path_source, 0, 1, 1, 1)
        self.le_path_target = QtWidgets.QLineEdit(self.centralwidget)
        self.le_path_target.setObjectName("le_path_target")
        self.gridLayout.addWidget(self.le_path_target, 3, 1, 1, 1)
        self.lbl_path_target = QtWidgets.QLabel(self.centralwidget)
        self.lbl_path_target.setObjectName("lbl_path_target")
        self.gridLayout.addWidget(self.lbl_path_target, 2, 1, 1, 1)
        self.le_path_source = QtWidgets.QLineEdit(self.centralwidget)
        self.le_path_source.setObjectName("le_path_source")
        self.gridLayout.addWidget(self.le_path_source, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_sortieren_starten = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sortieren_starten.setObjectName("btn_sortieren_starten")
        self.horizontalLayout.addWidget(self.btn_sortieren_starten)
        self.lbl_result = QtWidgets.QLabel(self.centralwidget)
        self.lbl_result.setText("")
        self.lbl_result.setObjectName("lbl_result")
        self.horizontalLayout.addWidget(self.lbl_result)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        ImageSorter.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ImageSorter)
        self.statusbar.setObjectName("statusbar")
        ImageSorter.setStatusBar(self.statusbar)

        self.retranslateUi(ImageSorter)
        QtCore.QMetaObject.connectSlotsByName(ImageSorter)

    def retranslateUi(self, ImageSorter):
        _translate = QtCore.QCoreApplication.translate
        ImageSorter.setWindowTitle(_translate("ImageSorter", "MainWindow"))
        self.lbl_path_source.setText(_translate("ImageSorter", "Quellpfad:"))
        self.lbl_path_target.setText(_translate("ImageSorter", "Zielpfad:"))
        self.btn_sortieren_starten.setText(_translate("ImageSorter", "Bilder sortieren"))
