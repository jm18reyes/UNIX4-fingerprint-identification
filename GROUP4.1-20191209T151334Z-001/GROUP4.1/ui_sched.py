# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sched.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(270, 370)
        MainWindow.setMinimumSize(QtCore.QSize(270, 370))
        MainWindow.setMaximumSize(QtCore.QSize(270, 370))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(60, 90, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 10), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 60, 81, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 251, 31))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 170, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 140, 81, 31))
        self.label_3.setObjectName("label_3")
        self.rbprimary = QtWidgets.QRadioButton(self.centralwidget)
        self.rbprimary.setGeometry(QtCore.QRect(50, 250, 71, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rbprimary.setFont(font)
        self.rbprimary.setChecked(True)
        self.rbprimary.setObjectName("rbprimary")
        self.rbbackup = QtWidgets.QRadioButton(self.centralwidget)
        self.rbbackup.setGeometry(QtCore.QRect(150, 250, 71, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rbbackup.setFont(font)
        self.rbbackup.setObjectName("rbbackup")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 210, 81, 31))
        self.label_4.setObjectName("label_4")
        self.bsave = QtWidgets.QPushButton(self.centralwidget)
        self.bsave.setGeometry(QtCore.QRect(20, 310, 101, 31))
        self.bsave.setObjectName("bsave")
        self.bcancel = QtWidgets.QPushButton(self.centralwidget)
        self.bcancel.setGeometry(QtCore.QRect(140, 310, 101, 31))
        self.bcancel.setObjectName("bcancel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MANAGE SCHEDULE"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">DATE</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">SCHEDULE</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">TIME</span></p></body></html>"))
        self.rbprimary.setText(_translate("MainWindow", "Primary"))
        self.rbbackup.setText(_translate("MainWindow", "Backup"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">TYPE</span></p></body></html>"))
        self.bsave.setText(_translate("MainWindow", "SAVE"))
        self.bcancel.setText(_translate("MainWindow", "CANCEL"))
