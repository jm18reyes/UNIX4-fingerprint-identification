from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os, time
from datetime import datetime

import ui_home

import rootlog

import handler

class Main(QtWidgets.QMainWindow, ui_home.Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.Timer()
        self.broot.clicked.connect(self.Root)

    def Root(self):
        self.dialog = rootlog.Main()
        self.dialog.show()

    def Timer(self):
        _translate = QtCore.QCoreApplication.translate
        d = datetime.now()
        time = d.strftime("%I:%M %p")
        date = d.strftime("%B %d, %Y")
        pos = self.pos
        result = handler.Name(pos)
        #if result is not None:
         #   name = result[0]
        #self.label_4.setText(_translate("MainWindow", name))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:15pt; font-weight:400;\">"+time+"</span></p>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:15pt; font-weight:400;\">"+date+"</span></p>"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())