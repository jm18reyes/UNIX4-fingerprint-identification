from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os

import ui_success2

import enroll

class Main(QtWidgets.QMainWindow, ui_success2.Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.bok.clicked.connect(self.CloseAll)

    def CloseAll(self):
        app = QtWidgets.QApplication.instance()
        app.closeAllWindows()
        self.dialog = enroll.Main()
        self.dialog.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())