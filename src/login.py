import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit
from PyQt6.uic import loadUi
import sqlite3
from PyQt6 import uic



class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        try:
            uic.loadUi("ui/login.ui", self)
            print("UI file loaded successfully")
            print(self)  # Print the contents of MainWindow
        except Exception as e:
            print("Error loading UI file:", e)
        self.passwordfield.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordfield_2.setEchoMode(QLineEdit.EchoMode.Password)
        tab_widget=self.tabWidget
        login_butt=tab_widget.widget(0).findChild(QPushButton,"login_butt")
        login_butt_2=tab_widget.widget(1).findChild(QPushButton,"login_butt_2")



    def authenticate_user(username, password):
        conn = sqlite3.connect("karyakram.db")
        cur = conn.cursor()
        query = 'SELECT Password FROM signupinfo WHERE Username= ?'
        cur.execute(query, (username,))
        result_pass = cur.fetchone()
        conn.close()

        if result_pass and result_pass[0] == password:
            return True
        else:
            return False

    def authenticate_admin(username,password):
        conn = sqlite3.connect("karyakram.db")
        cur = conn.cursor()
        query = 'SELECT Password FROM admin_signup WHERE Username= ?'
        cur.execute(query, (username,))
        result_pass = cur.fetchone()
        conn.close()

        if result_pass and result_pass[0] == password:
            return True
        else:
            return False




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    mainwindow = LoginWindow()
    widget.addWidget(mainwindow)
    widget.show()
    mainwindow.show()
    sys.exit(app.exec())