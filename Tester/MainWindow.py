from PySide import QtGui
from Ui_MainWindow import Ui_MainWindow
from LeaderBoard import LeaderBoard


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
   def __init__(self):
      super(MainWindow, self).__init__()
      self.setupUi(self)
      self.assignWidgets()
      self.show()

   def assignWidgets(self):
      self.leaderBoardButton.clicked.connect(self.goLeaderBoard)

   def goLeaderBoard(self):
      leaderBoard = LeaderBoard()
      leaderBoard.show()
