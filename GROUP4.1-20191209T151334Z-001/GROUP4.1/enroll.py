from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os

import ui_enroll

import home2

import handler

class Main(QtWidgets.QMainWindow, ui_enroll.Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.init()
        self.bsave.clicked.connect(self.Save)
        self.bcancel.clicked.connect(self.Cancel)

    def init(self):
        pos = self.pos
        self.inum.setText(str(pos))

    def Save(self):
        name = self.name.text()
        pos = self.pos
        sn = self.snum.text()
        prog = self.prog.text()
        email = self.email.text()
        pn = self.pnum.text()
        hr = self.total.text()
        handler.AddUser(pos, name, sn, prog, email, pn, hr)

    def Cancel(self):
        self.close()
        self.dialog = home2.Main()
        self.dialog.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())