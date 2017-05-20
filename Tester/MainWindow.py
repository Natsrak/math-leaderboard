from PySide import QtGui
from Ui_MainWindow import Ui_MainWindow
import csv
import easygui
import test_question
import random
from AskTeam import AskTeam
from QuestionDialog import QuestionDialog


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

    def calc_score(self, correct, total):
        return (float(correct) - (float(total) / 2))

    def format_score(self, score):
        return "{0:.0f}".format(round(score * 10, 0))

    def show_scores(self):
        with open('scores.txt') as scoresFile:
            reader = csv.reader(scoresFile, delimiter="\t", quotechar='^')
            lines = list(reader)
            scores = []
            scoring = dict()
            for line in lines:
                scoring.setdefault(line[0], 0)
                scoring[line[0]] += self.calc_score(line[1], line[2])
            self.leaderBoardWidget.setRowCount(scoring.__len__())
            for n, team in enumerate(sorted(scoring, key = scoring.get, reverse = True)):
                self.leaderBoardWidget.setItem(n, 0, QtGui.QTableWidgetItem(team))
                score = self.format_score(scoring[team])
                self.leaderBoardWidget.setItem(n, 1, QtGui.QTableWidgetItem(score))
        return scores

    def go_play(self):
        askTeams = AskTeam()
        play = askTeams.exec_()
        if play == QtGui.QDialog.Accepted:
            team = askTeams.teamsComboBox.currentText()
            demQuestions = askTeams.questionCountComboBox.currentText()
            self.loop_questions(team, demQuestions)
            self.show_scores()

    def loop_questions(self, team, demQuestions):
        total_questions = 0
        total_correct = 0
        level = 1

        round_questions = int(demQuestions)
        quiz = True
        while quiz:
            round_correct = self.ask_questions(team, round_questions, level)
            total_correct += round_correct
            total_questions += round_questions

            quiz = False
            if round_correct == round_questions:
                level += 1
                if level <= 4:
                    quiz = easygui.ynbox('Level ' + str(level) + '!\n\nDo you wish to continue?', 'Congratulations', ('Yes', 'No'))

            if not quiz:
                easygui.msgbox("Your score was " + self.format_score(self.calc_score(total_correct, total_questions)))

    def ask_questions(self, team, total_questions, level):
        total_correct = 0
        questions_filename = 'Math_' + str(level) + '.txt'
        # This opens up the file with our questions
        with open(questions_filename) as questionsFile:
            reader = csv.reader(questionsFile, delimiter="\t")
            lines = list(reader)
            tqs = []
            for line in lines:
                if len(line) != 5:
                    continue
                tqs.append(test_question.TestQuestion(line))
        question_dialog = QuestionDialog()
        random.shuffle(tqs)
        for x in range(total_questions):
            question_dialog.ask_question(tqs[x])
            question_dialog.exec_()
            total_correct += question_dialog.result
        print("Your " + team + " team score: " + str(total_correct))
        with open('scores.txt') as scoresFile:
            reader = csv.reader(scoresFile, delimiter="\t", quotechar='^')
            lines = list(reader)

        # python 3 - with open('scores.txt', 'w', newline='') as csvfile:
        with open('scores.txt', 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter='\t',
                                quotechar='^', quoting=csv.QUOTE_MINIMAL)
            for line in lines:
                writer.writerow(line)
            writer.writerow([team, total_correct, total_questions])
        return total_correct
