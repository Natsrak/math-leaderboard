from PySide import QtGui
from PySide import QtCore
from MainWindow import MainWindow


if __name__ == '__main__':
   import sys
   import os
   print("Running in " + os.getcwd() + " .\n")

   app = QtGui.QApplication(sys.argv)

   win = MainWindow()

   app.connect(app, QtCore.SIGNAL("lastWindowClosed()"),
               app, QtCore.SLOT("quit()"))
   app.exec_()
4