import csv
import easygui

class LeaderBoard:
    def __init__(self):
        pass

    def get_scores(self):
        with open('scores.txt') as scoresFile:
            reader = csv.reader(scoresFile, delimiter="\t", quotechar='^')
            lines = list(reader)
            scores = []
            scoring = dict()
            for line in lines:
                scoring.setdefault(line[0], 0)
                scoring[line[0]] += (float(line[1]) - (float(line[2]) / 2))
            for team in sorted(scoring, key = scoring.get, reverse = True):
                scores.append("{0:.0f}\t{1}".format(round(scoring[team] * 10, 0), team))
        return scores

    def show(self):
        scores = self.get_scores()
        board = '\n'.join([str(x) for x in scores])
        easygui.textbox('Scores        Teams', 'Leader Board', board)
