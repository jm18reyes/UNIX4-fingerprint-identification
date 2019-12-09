from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os

import ui_edit

import users

import handler

class Main(QtWidgets.QMainWindow, ui_edit.Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.bok.clicked.connect(self.Change)

    def Change(self):
        newval = self.box.text()
        pos = self.pos
        col = self.table
        try:
            handler.UpdateInfo(col, newval, pos)
        except:
            handler.UpdateInfo(col, newval, 0)
        self.dialog = users.Main()
        self.dialog.close()
        self.close()
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())