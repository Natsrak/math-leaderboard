import sys
from PySide import QtGui
from PySide import QtCore
from Ui_MainWindow import Ui_MainWindow


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
   def __init__(self):
      super(MainWindow, self).__init__()
      self.setupUi(self)
      # self.assignWidgets()
      self.show()


if __name__ == '__main__':
   import sys
   import os
   print("Running in " + os.getcwd() + " .\n")

   app = QtGui.QApplication(sys.argv)

   # msgBox = QtGui.QMessageBox()
   # msgBox.setText("Hello World - using PySide version ")
   # msgBox.exec_()
   win = MainWindow()
   # win  = MyWidget()
   # win  = Ui_MainWindow(QtGui.QMainWindow)

   app.connect(app, QtCore.SIGNAL("lastWindowClosed()"),
               app, QtCore.SLOT("quit()"))
   app.exec_()