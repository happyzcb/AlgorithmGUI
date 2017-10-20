from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.uic import loadUi
import sys
from mainwindow import Ui_MainWindow

# class MyMainWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(MyMainWindow, self).__init__()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    base = QtWidgets.QMainWindow()
    ui.setupUi(base)
    base.show()
    sys.exit(app.exec_())
