from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QGroupBox, QTextEdit, QPushButton, QTableWidget, QMenuBar, QMenu, QTextBrowser, QVBoxLayout
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QStatusBar

from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from PyQt6.QtWidgets import QProgressDialog
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox

import requests
import json
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse

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
        self.btn_search.clicked.connect(lambda: check_username(ui.txt_username.toPlainText()))

        self.btn_clear = QPushButton(self.group_search)
        self.btn_clear.setGeometry(320, 30, 31, 31)
        self.btn_clear.setText("X")

        # Table widget setup
        self.table_widget = QTableWidget(self.centralwidget)
        self.table_widget.setGeometry(10, 140, 361, 221)
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Platform Name", "URL", "Status"])

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
        
    def update_table(self, found_accounts):
        self.table_widget.setRowCount(0)  # clear table

        for account_info in found_accounts:
            row_position = self.table_widget.rowCount()
            self.table_widget.insertRow(row_position)

            # populate
            self.table_widget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(account_info["name"])))
            self.table_widget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(account_info["url_user"]))
            self.table_widget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(account_info["http_status"]))

found_accounts = []

def extract_main_url(input_url):
    try:
        parsed_url = urlparse(input_url)
        main_url = f"{parsed_url.scheme}://{parsed_url.netloc}/"
        return main_url
    except:
        return input_url 

def check_username_on_site(site, username, session):
    uri = site.get("uri_check")
    method = site.get("method", "GET")
    payload = site.get("post_body", {})
    headers = site.get("headers", {})

    try:
        if method == "GET":
            final_url = uri.format(account=username)
            response = session.get(final_url, headers=headers, timeout=10)
        elif method == "POST":
            final_url = uri
            response = session.post(final_url, data=payload, headers=headers, timeout=10)

        response.raise_for_status()

        if response.status_code == site["e_code"] and site["e_string"] in response.text:
            account_info = {
                "id": len(found_accounts) + 1,
                "username": username,
                "name": site.get("name"),
                "url_main": extract_main_url(final_url),
                "url_user": final_url,
                "exists": "Claimed",
                "http_status": response.status_code,
                "response_time_s": f"{response.elapsed.total_seconds():.3f}",
            }
            found_accounts.append(account_info)
            return True
        elif response.status_code == site["m_code"] and site["m_string"] in response.text:
            return False

    except requests.exceptions.RequestException as req_err:
        print(f"Error occurred for {site['name']} - {req_err}")

    return False

def check_username(username):
    if str(username).strip() == '':
        error_message = QMessageBox()
        error_message.setIcon(QMessageBox.Icon.Critical)
        error_message.setWindowTitle("Error")
        error_message.setText("Please enter a username")
        error_message.exec()
        return
    
    global found_accounts
    found_accounts = []

    with open('wmn-data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    total_sites = len(data["sites"])
    progress_dialog = QProgressDialog(f"Searching for {username}...", "Cancel", 0, total_sites)
    progress_dialog.setWindowModality(Qt.WindowModality.WindowModal)
    progress_dialog.setWindowTitle("Searching")

    def update_progress(i):
        progress_dialog.setValue(i)
        app.processEvents()

    with ThreadPoolExecutor() as executor, requests.Session() as session:
        futures = [executor.submit(check_username_on_site, site, username, session) for site in data["sites"]]
        for i, future in enumerate(futures):
            if progress_dialog.wasCanceled():
                break
            result = future.result()
            update_progress(i + 1)

            if result:
                ui.update_table(found_accounts)

    progress_dialog.setValue(total_sites)
    progress_dialog.close()

    if not any(found_accounts):
        error_message = QMessageBox()
        error_message.setIcon(QMessageBox.Icon.Critical)
        error_message.setWindowTitle("Not Found")
        error_message.setText(f"Username {username} not found on any site.")
        error_message.exec()
        return


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
