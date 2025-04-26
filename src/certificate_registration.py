import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
import sqlite3
#from gallery import GalleryWindow

class CertificateWindow(QMainWindow):
    def __init__(self):
        super(CertificateWindow, self).__init__()
        try:
            loadUi("ui/certificate_registration.ui", self)
            print("UI file loaded successfully")
            print(self)  # Print the contents of MainWindow
        except Exception as e:
            print("Error loading UI file:", e)
        #self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        #self.signupbtn.clicked.connect(self.goto_setevent)
        #self.loginbtn.clicked.connect(self.loginfunction)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    mainwindow = CertificateWindow()
    widget.addWidget(mainwindow)
    widget.show()
    mainwindow.show()
    sys.exit(app.exec())