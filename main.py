from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QGroupBox, QTextEdit, QPushButton, QTableWidget, QMenuBar, QMenu, QTextBrowser, QVBoxLayout
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QStatusBar

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Main window setup
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(381, 525)

        # Central widget setup
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Title label setup
        self.label_title = QLabel(self.centralwidget)
        self.label_title.setGeometry(90, 10, 191, 41)
        font = self.label_title.font()
        font.setPointSize(20)
        self.label_title.setFont(font)
        self.label_title.setText("Account Lookup")

        # Search group box setup
        self.group_search = QGroupBox(self.centralwidget)
        self.group_search.setGeometry(10, 60, 361, 71)
        self.group_search.setTitle("Search")

        # Username label setup
        self.label_username = QLabel(self.group_search)
        self.label_username.setGeometry(10, 30, 61, 31)
        self.label_username.setText("Username:")

        # Username text edit setup
        self.txt_username = QTextEdit(self.group_search)
        self.txt_username.setGeometry(70, 30, 161, 31)

        # Search and clear buttons setup
        self.btn_search = QPushButton(self.group_search)
        self.btn_search.setGeometry(240, 30, 75, 31)
        self.btn_search.setText("Search")
        self.btn_clear = QPushButton(self.group_search)
        self.btn_clear.setGeometry(320, 30, 31, 31)
        self.btn_clear.setText("X")

        # Table widget setup
        self.table_widget = QTableWidget(self.centralwidget)
        self.table_widget.setGeometry(10, 140, 361, 221)
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["ID", "Platform Name", "Status"])

        # Log group box setup
        self.group_log = QGroupBox(self.centralwidget)
        self.group_log.setGeometry(10, 370, 361, 111)
        self.group_log.setTitle("Log")

        # Text browser setup
        self.textBrowser = QTextBrowser(self.group_log)
        self.textBrowser.setGeometry(10, 30, 341, 71)

        # Set central widget
        MainWindow.setCentralWidget(self.centralwidget)

        # Menu bar setup
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(0, 0, 381, 21)

        # File menu setup
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setTitle("File")

        # Help menu setup
        self.menuGuide = QMenu(self.menubar)
        self.menuGuide.setTitle("Help")

        # About menu setup
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setTitle("About")

        # Set menu bar
        MainWindow.setMenuBar(self.menubar)

        # Status bar setup
        self.statusbar = QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        # Action setup
        self.actionSearch = QAction(MainWindow)
        self.actionSearch.setText("Search")
        self.actionClear = QAction(MainWindow)
        self.actionClear.setText("Clear")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setText("Exit")
        self.actionGuide = QAction(MainWindow)
        self.actionGuide.setText("Guide")
        self.actionHow_it_works = QAction(MainWindow)
        self.actionHow_it_works.setText("How it works?")
        self.actionLicense = QAction(MainWindow)
        self.actionLicense.setText("License")
        self.actionCredits = QAction(MainWindow)
        self.actionCredits.setText("Credits")
        self.actionContribute = QAction(MainWindow)
        self.actionContribute.setText("Contribute")

        # Add actions to menus
        self.menuFile.addAction(self.actionSearch)
        self.menuFile.addAction(self.actionClear)
        self.menuFile.addAction(self.actionExit)
        self.menuGuide.addAction(self.actionGuide)
        self.menuGuide.addAction(self.actionHow_it_works)
        self.menuGuide.addAction(self.actionLicense)
        self.menuGuide.addAction(self.actionCredits)
        self.menuGuide.addAction(self.actionContribute)

        # Add menus to menu bar
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuGuide.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
