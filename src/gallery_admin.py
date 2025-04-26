import sqlite3
import sys

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QMessageBox, QFileDialog, QStackedWidget
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
from PyQt6 import QtWidgets
#from homepage_try import ImageInsertionWindow
import sqlite3

class GadminWindow(QMainWindow):
    showSuccessDialog = pyqtSignal()
    def __init__(self):
        self.name=""
        super(GadminWindow,self).__init__()
        try:
            loadUi("ui/gallery_admin.ui",self)
            self.para_2.setStyleSheet("background-color: rgb(0,0,0,100); color:  rgb(0,0,0);")
            self.loaddata()
            self.save_butt.clicked.connect(self.saving_event)
            self.loaddata()
        except Exception as e:
            print("Error loading UI file:", e)

    def loaddata(self):
        conn = sqlite3.connect("karyakram.db")
        cursor = conn.cursor()
        query = "SELECT * FROM gallery"
        self.table.setRowCount(4)
        # Set column widths
        self.table.setColumnWidth(0, 200)  # Set width of the first column to 200 pixels
        self.table.setColumnWidth(1, 300)# Set width of the second column to 300 pixels
        self.table.setHorizontalHeaderLabels(["EVENT_NAME","DESCRIPITION"])
        tablerow = 0
        for row in cursor.execute(query):
            name_item = QTableWidgetItem(row[2])
            info_item = QTableWidgetItem(row[1])
            self.table.setItem(tablerow, 0, name_item)
            self.table.setItem(tablerow, 1, info_item)

            # Display multiline text using QTextEdit
            info_text_edit = QTextEdit(row[1])
            info_text_edit.setReadOnly(True)  # Make it read-only
            self.table.setCellWidget(tablerow, 1, info_text_edit)

            tablerow += 1



    def saving_event(self):
        paragraph = self.para_2.toPlainText()
        self.name = self.namefield.text()

        try:
            # Connect to SQLite database
            conn = sqlite3.connect("karyakram.db")
            cursor = conn.cursor()

            # Insert date, info, and image data into database
            cursor.execute("INSERT INTO gallery (info, name) VALUES (?, ?)",
                           (paragraph, self.name))
            self.showSuccessDialog.emit()
            conn.commit()

            # Reload data and update table
            self.loaddata()

            conn.close()
            QMessageBox.information(self, "Success", "Data saved to database successfully.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to save data to database: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    mainwindow = GadminWindow()
    widget.addWidget(mainwindow)
    widget.show()
    mainwindow.show()
    sys.exit(app.exec())

