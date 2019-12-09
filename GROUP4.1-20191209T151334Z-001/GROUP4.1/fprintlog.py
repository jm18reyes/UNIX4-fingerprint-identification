from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os

import ui_fprintlog

import fpsearch, success, sched, home, home2

class Main(QtWidgets.QMainWindow, ui_fprintlog.Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)  
        self.auth()
    def auth(self):
        try:
            posNum = fpsearch.checkFP()
            sched.Main.pos = posNum
            home.Main.pos = posNum
            home2.Main.pos = posNum
            self.dialog = success.Main()
            self.dialog.show()
        except:
            print("error")  #SHOW ERROR PROMPT

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())