from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os

import ui_users

import home2, edit

import handler

class Main(QtWidgets.QMainWindow, ui_users.Ui_MainWindow):
    global _translate
    _translate = QtCore.QCoreApplication.translate
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.userList()
        self.bback.clicked.connect(self.Back)
        self.comboBox.currentIndexChanged.connect(self.updateInfo)
        self.ename.clicked.connect(self.editName)
        self.esn.clicked.connect(self.editSN)
        self.eprog.clicked.connect(self.editProg)
        self.eemail.clicked.connect(self.editEmail)
        self.epn.clicked.connect(self.editPhone)
        
    def Back(self):
        self.close()
        self.dialog = home2.Main()
        self.dialog.show()

    def userList(self):
        self.comboBox.clear()
        results = handler.UserList()
        lists = [row[0] for row in results]
        lists.insert(0,"---Select---")
        self.comboBox.addItems(lists)

    def updateInfo(self):
        # text = str(self.comboBox.currentText())
        index = self.comboBox.currentIndex()
        global pos, name, sn, prog, email, cn
        if index == 0:
            (pos, name, sn, prog, email, cn) = (" ", " ", " ", " ", " ", " ")
        else:
            result = handler.Info(index)
            pos = str(result[0])
            name = result[1]
            sn = result[2]
            prog = result[3]
            email = result[4]
            cn = result[5]
            edit.Main.pos = result[0]        
        self.changeText()

    def changeText(self):
        self.name.setText(_translate("MainWindow", name))
        self.inum.setText(_translate("MainWindow", pos))
        self.snum.setText(_translate("MainWindow", sn))
        self.prog.setText(_translate("MainWindow", prog))
        self.email.setText(_translate("MainWindow", email))
        self.pnum.setText(_translate("MainWindow", cn))

    def showEdit(self):
        self.dialog = edit.Main()
        self.dialog.show()

    def editName(self):
        edit.Main.table = "name"
        self.showEdit()

    def editSN(self):
        edit.Main.table = "sNum"
        self.showEdit()
    
    def editProg(self):
        edit.Main.table = "program"
        self.showEdit()
    
    def editEmail(self):
        edit.Main.table = "email"
        self.showEdit()

    def editPhone(self):
        edit.Main.table = "phone"
        self.showEdit()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())