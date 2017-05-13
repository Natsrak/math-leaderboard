# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QuestionDialog.ui'
#
# Created: Sat May 13 17:10:17 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_QuestionDialog(object):
    def setupUi(self, QuestionDialog):
        QuestionDialog.setObjectName("QuestionDialog")
        QuestionDialog.resize(521, 370)
        self.testQuestionLabel = QtGui.QLabel(QuestionDialog)
        self.testQuestionLabel.setGeometry(QtCore.QRect(40, 10, 441, 41))
        self.testQuestionLabel.setObjectName("testQuestionLabel")
        self.possibilty1Button = QtGui.QPushButton(QuestionDialog)
        self.possibilty1Button.setGeometry(QtCore.QRect(34, 90, 451, 23))
        self.possibilty1Button.setObjectName("possibilty1Button")
        self.possibilty2Button = QtGui.QPushButton(QuestionDialog)
        self.possibilty2Button.setGeometry(QtCore.QRect(34, 140, 451, 23))
        self.possibilty2Button.setObjectName("possibilty2Button")
        self.possibilty3Button = QtGui.QPushButton(QuestionDialog)
        self.possibilty3Button.setGeometry(QtCore.QRect(34, 190, 451, 23))
        self.possibilty3Button.setObjectName("possibilty3Button")
        self.possibilty4Button = QtGui.QPushButton(QuestionDialog)
        self.possibilty4Button.setGeometry(QtCore.QRect(34, 240, 451, 23))
        self.possibilty4Button.setObjectName("possibilty4Button")
        self.resultLabel = QtGui.QLabel(QuestionDialog)
        self.resultLabel.setGeometry(QtCore.QRect(35, 310, 451, 20))
        self.resultLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.resultLabel.setObjectName("resultLabel")

        self.retranslateUi(QuestionDialog)
        QtCore.QMetaObject.connectSlotsByName(QuestionDialog)

    def retranslateUi(self, QuestionDialog):
        QuestionDialog.setWindowTitle(QtGui.QApplication.translate("QuestionDialog", "Questions", None, QtGui.QApplication.UnicodeUTF8))
        self.testQuestionLabel.setText(QtGui.QApplication.translate("QuestionDialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.possibilty1Button.setText(QtGui.QApplication.translate("QuestionDialog", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.possibilty2Button.setText(QtGui.QApplication.translate("QuestionDialog", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.possibilty3Button.setText(QtGui.QApplication.translate("QuestionDialog", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.possibilty4Button.setText(QtGui.QApplication.translate("QuestionDialog", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.resultLabel.setText(QtGui.QApplication.translate("QuestionDialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

