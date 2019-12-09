from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os

import ui_fprintlog

import fpenroll, success2, enroll

class Main(QtWidgets.QMainWindow, ui_fprintlog.Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.auth()

    def auth(self):
        try:
            posNum = fpenroll.checkFP()
            enroll.Main.pos = posNum
            self.dialog = success2.Main()
            self.dialog.show()
        except:
            print("error")  #SHOW ERROR PROMPT


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())