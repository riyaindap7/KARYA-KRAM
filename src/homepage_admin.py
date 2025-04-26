import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
import sqlite3

class AdHomepageWindow(QMainWindow):
    def __init__(self):
        super(AdHomepageWindow,self).__init__()
        try:
            loadUi("ui/homepage_admin.ui",self)
            self.load_tabel()
        except Exception as e:
            print("Error loading UI file:", e)

    def load_tabel(self):
        conn=sqlite3.connect("karyakram.db")
        cursor = conn.cursor()
        query = "SELECT * FROM calendar"
        self.table.setRowCount(4)
        # Set column widths
        self.table.setColumnWidth(0, 150)  # Set width of the first column to 200 pixels
        self.table.setColumnWidth(1, 100)  # Set width of the second column to 300 pixels
        self.table.setHorizontalHeaderLabels(["DATE", "EVENT_NAME","LOCATION","TIME_FROM","TIME_TO"])
        tablerow = 0
        for row in cursor.execute(query):
            date_item = QTableWidgetItem(row[0])
            event_item = QTableWidgetItem(row[1])
            loc_item = QTableWidgetItem(row[2])
            timefr_item = QTableWidgetItem(row[3])
            timeto_item = QTableWidgetItem(row[4])
            self.table.setItem(tablerow, 0, date_item)
            self.table.setItem(tablerow, 1, event_item)
            self.table.setItem(tablerow, 2, loc_item)
            self.table.setItem(tablerow, 3, timefr_item)
            self.table.setItem(tablerow, 4, timeto_item)


            # Display multiline text using QTextEdit
            info_text_edit = QTextEdit(row[1])
            info_text_edit.setReadOnly(True)  # Make it read-only
            self.table.setCellWidget(tablerow, 1, info_text_edit)

            tablerow += 1

        """def reload_table(self):
            # Clear existing data and reload the table
            self.table.clearContents()
            self.load_table()"""

if __name__=="__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    mainwindow = AdHomepageWindow()
    widget.addWidget(mainwindow)
    widget.show()
    mainwindow.show()
    sys.exit(app.exec())