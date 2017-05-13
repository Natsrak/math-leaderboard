from PySide import QtGui
from Ui_MainWindow import Ui_MainWindow
import csv
import easygui
import test_question
import random
from AskTeam import AskTeam


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.assign_widgets()
        self.show_scores()
        self.show()
        self.showFullScreen()

    def assign_widgets(self):
        self.playButton.clicked.connect(self.go_play)
        self.quitButton.clicked.connect(self.destroy)

    def show_scores(self):
        with open('scores.txt') as scoresFile:
            reader = csv.reader(scoresFile, delimiter="\t", quotechar='^')
            lines = list(reader)
            scores = []
            scoring = dict()
            for line in lines:
                scoring.setdefault(line[0], 0)
                scoring[line[0]] += (float(line[1]) - (float(line[2]) / 2))
            self.leaderBoardWidget.setRowCount(scoring.__len__())
            for n, team in enumerate(sorted(scoring, key = scoring.get, reverse = True)):
                self.leaderBoardWidget.setItem(n, 0, QtGui.QTableWidgetItem(team))
                score = "{0:.0f}".format(round(scoring[team] * 10, 0))
                self.leaderBoardWidget.setItem(n, 1, QtGui.QTableWidgetItem(score))
        return scores

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

    def go_play(self):
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
