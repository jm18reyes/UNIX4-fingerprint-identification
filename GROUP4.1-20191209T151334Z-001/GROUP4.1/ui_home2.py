# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home2.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(520, 420)
        MainWindow.setMinimumSize(QtCore.QSize(520, 420))
        MainWindow.setMaximumSize(QtCore.QSize(520, 420))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 121, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 471, 51))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 160, 121, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 240, 121, 71))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(230, 240, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(230, 280, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.benroll = QtWidgets.QPushButton(self.centralwidget)
        self.benroll.setGeometry(QtCore.QRect(10, 350, 161, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.benroll.setFont(font)
        self.benroll.setObjectName("benroll")
        self.bmuser = QtWidgets.QPushButton(self.centralwidget)
        self.bmuser.setGeometry(QtCore.QRect(180, 350, 161, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bmuser.setFont(font)
        self.bmuser.setObjectName("bmuser")
        self.bmsched = QtWidgets.QPushButton(self.centralwidget)
        self.bmsched.setGeometry(QtCore.QRect(350, 350, 161, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bmsched.setFont(font)
        self.bmsched.setObjectName("bmsched")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MAPUA UNIVERSITY"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600;\">CCESC</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">CENTER for CONTINUING EDUCATION and SPECIAL COMPETENCIES</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">WELCOME</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">TIME:</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">DATE:</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.benroll.setText(_translate("MainWindow", "ENROLL USER"))
        self.bmuser.setText(_translate("MainWindow", "MANAGE USERS"))
        self.bmsched.setText(_translate("MainWindow", "MANAGE SCHEDULES"))
