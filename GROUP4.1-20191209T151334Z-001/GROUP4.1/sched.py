from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os

import ui_sched

import home2

import handler

class Main(QtWidgets.QMainWindow, ui_sched.Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.timeList()
        self.bsave.clicked.connect(self.Save)
        self.bcancel.clicked.connect(self.Cancel)

    def Save(self):
        date = self.dateEdit.date()
        dates = date.toPyDate()
        index = self.comboBox.currentIndex()
        time = index + 1
        pos = self.pos
        if self.rbprimary.isChecked():
            back = 0
        elif self.rbbackup.isChecked():
            back = 1
        handler.AddSched(pos, time, dates, back)

    def Cancel(self):
        self.dialog = home2.Main()
        self.dialog.show()
        self.close()

    def timeList(self):
        self.comboBox.clear()
        results = dh.TimeList()
        lists = [row[0] for row in results]
        lists.insert(0,"---Select---")
        self.comboBox.addItems(lists)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())