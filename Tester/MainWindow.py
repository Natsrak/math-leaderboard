from PySide import QtGui
from Ui_MainWindow import Ui_MainWindow
import csv
import easygui
import test_question
import random
from LeaderBoard import LeaderBoard
from AskTeam import AskTeam

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
   def __init__(self):
      super(MainWindow, self).__init__()
      self.setupUi(self)
      self.assignWidgets()
      self.show()

   def assignWidgets(self):
      self.leaderBoardButton.clicked.connect(self.goLeaderBoard)
      self.playButton.clicked.connect(self.goPlay)

   def goLeaderBoard(self):
      leaderBoard = LeaderBoard()
      leaderBoard.show()

   def ask_question(self, tq):
      a = tq.possibles
      random.shuffle(a)
      q = easygui.buttonbox(tq.question, "?", choices=[a[0], a[1], a[2], a[3]])
      answer = tq.answer
      if q == answer:
         result = 1
         easygui.msgbox("Yay!")
      else:
         result = 0
         easygui.msgbox("Try again!")
      return result

   def goPlay(self):
      askTeams = AskTeam()
      play = askTeams.exec_()
      if play == QtGui.QDialog.Accepted:
         team = askTeams.teamsComboBox.currentText()
         demQuestions = askTeams.questionCountComboBox.currentText()
         self.askQuestions(team, demQuestions)

   def askQuestions(self, team, demQuestions):
      # This opens up the file with our questions
      with open('Questions.txt') as questionsFile:
         reader = csv.reader(questionsFile, delimiter="\t")
         lines = list(reader)
         tqs = []
         for line in lines:
            tqs.append(test_question.TestQuestion(line))

      totRes = 0
      random.shuffle(tqs)
      for x in range(int(demQuestions)):
         totRes += self.ask_question(tqs[x])
      print("Your " + team + " team score: " + str(totRes))

      with open('scores.txt') as scoresFile:
         reader = csv.reader(scoresFile, delimiter="\t", quotechar='^')
         lines = list(reader)

      # python 3 - with open('scores.txt', 'w', newline='') as csvfile:
      with open('scores.txt', 'w') as csvfile:
         writer = csv.writer(csvfile, delimiter='\t',
                             quotechar='^', quoting=csv.QUOTE_MINIMAL)
         for line in lines:
            writer.writerow(line)
         writer.writerow([team, totRes, demQuestions])

      #
      # with open('teams.txt') as teamsFile:
      #    reader = csv.reader(teamsFile, delimiter="\t")
      #    lines = list(reader)
      #    teams = []
      #    for line in lines:
      #       if len(line):
      #          teams.append(line[0])
      #
      # team = easygui.choicebox("Pick your team", "Pick Team", teams)
      # while not team in teams:
      #    team = easygui.choicebox("Pick your team", "Pick Team", teams)
      #
      # posQuestAmount = ("01", "05", "10")
      # demQuestions = easygui.choicebox("How many questions?", "Questions", posQuestAmount)
      # while not demQuestions in posQuestAmount:
      #    demQuestions = easygui.choicebox("How many questions?", "Questions", posQuestAmount)
      #

