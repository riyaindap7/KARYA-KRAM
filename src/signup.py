import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
Import images_rc.py
from PyQt6.uic import loadUi
import sqlite3
#from subprocess import Popen
import re
from PyQt6.QtCore import pyqtSignal

class SignupWindow(QMainWindow):
    signupCompleted=pyqtSignal()
    def __init__(self):
        super(SignupWindow, self).__init__()
        try:
            loadUi("ui/signup_new.ui", self)
            print("UI file loaded successfully")
            print(self)  # Print the contents of MainWindow
        except Exception as e:
            print("Error loading UI file:", e)
        self.passwordfield.setEchoMode(QLineEdit.EchoMode.Password)
        self.conpassword.setEchoMode(QLineEdit.EchoMode.Password)
        self.signup_butt.clicked.connect(self.signupfunction)

    def validate_email(self,email):
        # Using a regular expression to validate email format
        pattern = r'^[a-zA-Z0-9_.+-]+@student\.sfit\.ac\.in$'
        return re.match(pattern, email)
    def signupfunction(self):
        emailId = self.emailfield.text()
        user = self.userfield.text()
        password = self.passwordfield.text()
        conpass=self.conpassword.text()
        if len(emailId) == 0 or len(user) == 0 or len(password) == 0:
            self.error.setText("Please input all fields.")
        elif password!=conpass:
            self.error.setText("Password Mismatched.")
        elif not self.validate_email(emailId):
            self.error.setText("Use sfit emailId only.")
        else:
            conn = sqlite3.connect("karyakram.db")
            cur = conn.cursor()
            query_check_user = "SELECT COUNT(*) FROM signupinfo WHERE Username = ?"
            cur.execute(query_check_user, (user,))
            result_count = cur.fetchone()[0]

            if result_count > 0:
                    # check if user already exist
                self.error.setText("Username already exists.")
            else:
                query_insert_user = "INSERT INTO signupinfo (emailId, Username, Password) VALUES (?, ?, ?)"
                cur.execute(query_insert_user, (emailId, user, password))
                conn.commit()
                self.error.setText("User Registered Successfully! ")
                print("User successfully registered.")
                QMessageBox.information(self, "Success", "User Successfully Registered.")
                try:
                    self.close()
                    self.signupCompleted.emit()
                    #self.showSuccessDialog.emit()
                    """login_window = LoginWindow()
                    widget.addWidget(login_window)
                    widget.setCurrentIndex(widget.currentIndex() + 1)"""
                    self.close()
                except Exception as e:
                    print("Error loading login file:", e)

                conn.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    mainwindow = SignupWindow()
    widget.addWidget(mainwindow)
    widget.show()
    mainwindow.show()
    sys.exit(app.exec())