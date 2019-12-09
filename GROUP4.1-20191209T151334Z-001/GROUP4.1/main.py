from fprintlog import *

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  
    form = Main()
    form.show()
    sys.exit(app.exec_())