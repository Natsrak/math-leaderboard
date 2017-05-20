# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AskTeam.ui'
#
# Created: Sat May 20 14:54:20 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AskTeam(object):
    def setupUi(self, AskTeam):
        AskTeam.setObjectName("AskTeam")
        AskTeam.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(AskTeam)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtGui.QWidget(AskTeam)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 251, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.teamsComboBox = QtGui.QComboBox(self.layoutWidget)
        self.teamsComboBox.setObjectName("teamsComboBox")
        self.teamsComboBox.addItem("")
        self.teamsComboBox.addItem("")
        self.teamsComboBox.addItem("")
        self.teamsComboBox.addItem("")
        self.teamsComboBox.addItem("")
        self.teamsComboBox.addItem("")
        self.teamsComboBox.addItem("")
        self.teamsComboBox.addItem("")
        self.verticalLayout.addWidget(self.teamsComboBox)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setEnabled(False)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.questionCountComboBox = QtGui.QComboBox(self.layoutWidget)
        self.questionCountComboBox.setEnabled(False)
        self.questionCountComboBox.setObjectName("questionCountComboBox")
        self.questionCountComboBox.addItem("")
        self.questionCountComboBox.addItem("")
        self.questionCountComboBox.addItem("")
        self.verticalLayout.addWidget(self.questionCountComboBox)

        self.retranslateUi(AskTeam)
        self.questionCountComboBox.setCurrentIndex(1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), AskTeam.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), AskTeam.reject)
        QtCore.QMetaObject.connectSlotsByName(AskTeam)

    def retranslateUi(self, AskTeam):
        AskTeam.setWindowTitle(QtGui.QApplication.translate("AskTeam", "Ask Team", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AskTeam", "Pick your team", None, QtGui.QApplication.UnicodeUTF8))
        self.teamsComboBox.setItemText(0, QtGui.QApplication.translate("AskTeam", "Bay Lynxes", None, QtGui.QApplication.UnicodeUTF8))
        self.teamsComboBox.setItemText(1, QtGui.QApplication.translate("AskTeam", "Bears", None, QtGui.QApplication.UnicodeUTF8))
        self.teamsComboBox.setItemText(2, QtGui.QApplication.translate("AskTeam", "Dolphins", None, QtGui.QApplication.UnicodeUTF8))
        self.teamsComboBox.setItemText(3, QtGui.QApplication.translate("AskTeam", "Foxes", None, QtGui.QApplication.UnicodeUTF8))
        self.teamsComboBox.setItemText(4, QtGui.QApplication.translate("AskTeam", "Kingfishers", None, QtGui.QApplication.UnicodeUTF8))
        self.teamsComboBox.setItemText(5, QtGui.QApplication.translate("AskTeam", "Marlins", None, QtGui.QApplication.UnicodeUTF8))
        self.teamsComboBox.setItemText(6, QtGui.QApplication.translate("AskTeam", "Ospreys", None, QtGui.QApplication.UnicodeUTF8))
        self.teamsComboBox.setItemText(7, QtGui.QApplication.translate("AskTeam", "Stingrays", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AskTeam", "Pick the amount of questions you wish to answer", None, QtGui.QApplication.UnicodeUTF8))
        self.questionCountComboBox.setItemText(0, QtGui.QApplication.translate("AskTeam", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.questionCountComboBox.setItemText(1, QtGui.QApplication.translate("AskTeam", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.questionCountComboBox.setItemText(2, QtGui.QApplication.translate("AskTeam", "10", None, QtGui.QApplication.UnicodeUTF8))

