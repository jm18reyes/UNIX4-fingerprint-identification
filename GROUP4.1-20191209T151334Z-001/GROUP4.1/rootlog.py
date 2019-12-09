from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os

import ui_rootlog

import home2

class Main(QtWidgets.QMainWindow, ui_rootlog.Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.blogin.clicked.connect(self.rootAuth)
    
    def rootAuth(self):
        input = self.lineEdit.text()
        if input == "Unix09":                             #PALITAN NALANG NG PASS
            app = QtWidgets.QApplication.instance()
            app.closeAllWindows()
            self.dialog = home2.Main()
            self.dialog.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())