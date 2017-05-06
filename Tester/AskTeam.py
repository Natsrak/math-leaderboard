from PySide import QtGui
from Ui_AskTeam import Ui_AskTeam
import test_question
import csv
import random


class AskTeam(QtGui.QDialog, Ui_AskTeam):
   def __init__(self):
      super(AskTeam, self).__init__()
      self.setupUi(self)
      #self.assignWidgets()
      self.show()

   #def assignWidgets(self):
    #self.buttonBox.Ok.clicked.connect(self.goOK)

   # def accepted(self):
   #     # This opens up the file with our questions
   #     with open('Questions.txt') as questionsFile:
   #         reader = csv.reader(questionsFile, delimiter="\t")
   #         lines = list(reader)
   #         tqs = []
   #         for line in lines:
   #             tqs.append(test_question.TestQuestion(line))
   #
   #     team = self.teamsComboBox.value
   #     demQuestions = self.questionCountComboBox.value
   #     totRes = 0
   #     random.shuffle(tqs)
   #     for x in range(int(demQuestions)):
   #         totRes += self.ask_question(tqs[x])
   #     print("Your " + team + " team score: " + str(totRes))
   #
   #     with open('scores.txt') as scoresFile:
   #         reader = csv.reader(scoresFile, delimiter="\t", quotechar='^')
   #         lines = list(reader)
   #
   #     # python 3 - with open('scores.txt', 'w', newline='') as csvfile:
   #     with open('scores.txt', 'w') as csvfile:
   #         writer = csv.writer(csvfile, delimiter='\t',
   #                             quotechar='^', quoting=csv.QUOTE_MINIMAL)
   #         for line in lines:
   #             writer.writerow(line)
   #         writer.writerow([team, totRes, demQuestions])

