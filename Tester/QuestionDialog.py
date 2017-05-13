from PySide import QtGui
from Ui_QuestionDialog import Ui_QuestionDialog
import csv
import easygui
import random
from AskTeam import AskTeam


class QuestionDialog(QtGui.QDialog, Ui_QuestionDialog):
    def __init__(self):
        super(QuestionDialog, self).__init__()
        self.setupUi(self)
        self.assign_widgets()
        self.result = 0
        self.testQuestions = []
        self.resultLabel.setText("")

    def assign_widgets(self):
        self.possibilty1Button.clicked.connect(self.go_test1)
        self.possibilty2Button.clicked.connect(self.go_test2)
        self.possibilty3Button.clicked.connect(self.go_test3)
        self.possibilty4Button.clicked.connect(self.go_test4)

    def ask_question(self, tq):
        self.testQuestions = tq
        a = tq.possibles
        random.shuffle(a)
        self.fill_question(tq.question, a)

        # return self.result

    def fill_question(self, question, possibilities):
        self.testQuestionLabel.setText(question)
        self.possibilty1Button.setText(possibilities[0])
        self.possibilty2Button.setText(possibilities[1])
        self.possibilty3Button.setText(possibilities[2])
        self.possibilty4Button.setText(possibilities[3])

    def go_test1(self):
        self.check(self.possibilty1Button.text())

    def go_test2(self):
        self.check(self.possibilty2Button.text())

    def go_test3(self):
        self.check(self.possibilty3Button.text())

    def go_test4(self):
        self.check(self.possibilty4Button.text())

    def check(self, guess):
        answer = self.testQuestions.answer
        if guess == answer:
            self.result = 1
            self.resultLabel.setText("Yay!")
        else:
            self.result = 0
            self.resultLabel.setText("So close")
        self.close()
