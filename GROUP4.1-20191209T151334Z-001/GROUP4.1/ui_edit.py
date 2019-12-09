# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(355, 230)
        MainWindow.setMinimumSize(QtCore.QSize(355, 230))
        MainWindow.setMaximumSize(QtCore.QSize(355, 230))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.box = QtWidgets.QLineEdit(self.centralwidget)
        self.box.setGeometry(QtCore.QRect(40, 90, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.box.setFont(font)
        self.box.setAlignment(QtCore.Qt.AlignCenter)
        self.box.setReadOnly(False)
        self.box.setObjectName("box")
        self.bok = QtWidgets.QPushButton(self.centralwidget)
        self.bok.setGeometry(QtCore.QRect(120, 160, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bok.setFont(font)
        self.bok.setObjectName("bok")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 40, 91, 21))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EDIT"))
        self.bok.setText(_translate("MainWindow", "SAVE"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">EDIT INFO</span></p></body></html>"))
