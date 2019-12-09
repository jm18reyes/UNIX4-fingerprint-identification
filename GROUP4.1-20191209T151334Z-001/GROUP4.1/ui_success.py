# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'success.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 200)
        MainWindow.setMinimumSize(QtCore.QSize(390, 200))
        MainWindow.setMaximumSize(QtCore.QSize(390, 200))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 341, 51))
        self.label.setObjectName("label")
        self.bok = QtWidgets.QPushButton(self.centralwidget)
        self.bok.setGeometry(QtCore.QRect(130, 130, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.bok.setFont(font)
        self.bok.setStyleSheet("")
        self.bok.setObjectName("bok")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MESSAGE"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Authentication Successful</span></p></body></html>"))
        self.bok.setText(_translate("MainWindow", "OK"))
