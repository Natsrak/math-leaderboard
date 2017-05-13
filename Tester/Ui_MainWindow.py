# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Sat May 13 16:55:48 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1083, 663)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 110, 781, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.playButton = QtGui.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(540, 180, 101, 41))
        self.playButton.setObjectName("playButton")
        self.quitButton = QtGui.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(540, 390, 91, 41))
        self.quitButton.setObjectName("quitButton")
        self.leaderBoardWidget = QtGui.QTableWidget(self.centralwidget)
        self.leaderBoardWidget.setGeometry(QtCore.QRect(140, 180, 321, 251))
        self.leaderBoardWidget.setObjectName("leaderBoardWidget")
        self.leaderBoardWidget.setColumnCount(2)
        self.leaderBoardWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.leaderBoardWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.leaderBoardWidget.setHorizontalHeaderItem(1, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1083, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Acolympics", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Welcome!  We are very excited to have you here to play the Acolympics!", None, QtGui.QApplication.UnicodeUTF8))
        self.playButton.setText(QtGui.QApplication.translate("MainWindow", "Play", None, QtGui.QApplication.UnicodeUTF8))
        self.quitButton.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.leaderBoardWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Team", None, QtGui.QApplication.UnicodeUTF8))
        self.leaderBoardWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Score", None, QtGui.QApplication.UnicodeUTF8))

