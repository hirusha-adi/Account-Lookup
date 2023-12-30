# Form implementation generated from reading ui file '.\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # MainWindow setup
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(381, 491)

        # Central Widget setup
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Title Label setup
        self.label_title = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(90, 10, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")

        # Search Group setup
        self.group_search = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.group_search.setGeometry(QtCore.QRect(10, 60, 361, 71))
        self.group_search.setObjectName("group_search")

        # Username Label setup
        self.label_username = QtWidgets.QLabel(parent=self.group_search)
        self.label_username.setGeometry(QtCore.QRect(20, 30, 61, 31))
        self.label_username.setObjectName("label_username")

        # Username TextEdit setup
        self.txt_username = QtWidgets.QTextEdit(parent=self.group_search)
        self.txt_username.setGeometry(QtCore.QRect(80, 30, 131, 31))
        self.txt_username.setObjectName("txt_username")

        # Search Button setup
        self.btn_search = QtWidgets.QPushButton(parent=self.group_search)
        self.btn_search.setGeometry(QtCore.QRect(220, 30, 75, 31))
        self.btn_search.setObjectName("btn_search")

        # Clear Button setup
        self.btn_clear = QtWidgets.QPushButton(parent=self.group_search)
        self.btn_clear.setGeometry(QtCore.QRect(300, 30, 31, 31))
        self.btn_clear.setObjectName("btn_clear")

        # Table Widget setup
        self.table_widget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.table_widget.setGeometry(QtCore.QRect(10, 140, 361, 281))
        self.table_widget.setObjectName("table_widget")
        self.table_widget.setColumnCount(3)
        self.table_widget.setRowCount(0)

        # Table Headers setup
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(2, item)

        # Labels setup
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 430, 71, 16))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 430, 111, 20))
        self.label_4.setObjectName("label_4")

        # Set Central Widget
        MainWindow.setCentralWidget(self.centralwidget)

        # Menu Bar setup
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 381, 21))
        self.menubar.setObjectName("menubar")

        # Menu setup
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuGuide = QtWidgets.QMenu(parent=self.menubar)
        self.menuGuide.setObjectName("menuGuide")
        self.menuAbout = QtWidgets.QMenu(parent=self.menubar)
        self.menuAbout.setObjectName("menuAbout")

        # Set Menu Bar
        MainWindow.setMenuBar(self.menubar)

        # Status Bar setup
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Action setup
        self.actionSearch = QtGui.QAction(parent=MainWindow)
        self.actionSearch.setObjectName("actionSearch")

        self.actionClear = QtGui.QAction(parent=MainWindow)
        self.actionClear.setObjectName("actionClear")

        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(sys.exit)  # Connect Exit action to sys.exit

        self.actionGuide = QtGui.QAction(parent=MainWindow)
        self.actionGuide.setObjectName("actionGuide")

        self.actionHow_it_works = QtGui.QAction(parent=MainWindow)
        self.actionHow_it_works.setObjectName("actionHow_it_works")

        self.actionLicense = QtGui.QAction(parent=MainWindow)
        self.actionLicense.setObjectName("actionLicense")

        self.actionCredits = QtGui.QAction(parent=MainWindow)
        self.actionCredits.setObjectName("actionCredits")

        self.actionContribute = QtGui.QAction(parent=MainWindow)
        self.actionContribute.setObjectName("actionContribute")

        # Add actions to menus
        self.menuFile.addAction(self.actionSearch)
        self.menuFile.addAction(self.actionClear)
        self.menuFile.addAction(self.actionExit)

        self.menuGuide.addAction(self.actionGuide)
        self.menuGuide.addAction(self.actionHow_it_works)
        self.menuGuide.addAction(self.actionLicense)
        self.menuGuide.addAction(self.actionCredits)
        self.menuGuide.addAction(self.actionContribute)

        # Add menus to menubar
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuGuide.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        # Translate UI elements
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        # Set titles and labels
        MainWindow.setWindowTitle(_translate("MainWindow", "Account Lookup"))
        self.label_title.setText(_translate("MainWindow", "Account Lookup"))
        self.group_search.setTitle(_translate("MainWindow", "Search"))
        self.label_username.setText(_translate("MainWindow", "Username:"))
        self.btn_search.setText(_translate("MainWindow", "Search"))
        self.btn_clear.setText(_translate("MainWindow", "X"))
        item = self.table_widget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.table_widget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Platform Name"))
        item = self.table_widget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        self.label_3.setText(_translate("MainWindow", "Exit"))
        self.label_4.setText(_translate("MainWindow", "Made by @hirushaadi"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuGuide.setTitle(_translate("MainWindow", "Help"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionSearch.setText(_translate("MainWindow", "Search"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionGuide.setText(_translate("MainWindow", "Guide"))
        self.actionHow_it_works.setText(_translate("MainWindow", "How it works?"))
        self.actionLicense.setText(_translate("MainWindow", "License"))
        self.actionCredits.setText(_translate("MainWindow", "Credits"))
        self.actionContribute.setText(_translate("MainWindow", "Contribute"))
