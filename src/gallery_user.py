import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextBrowser
from PyQt6.uic import loadUi
from PyQt6.QtGui import QPixmap
import sqlite3

from PyQt6.uic.properties import QtGui


class GalleryWindow(QMainWindow):
    def __init__(self):
        super(GalleryWindow, self).__init__()

        try:
            loadUi("ui/gallery_user.ui", self)
            print("UI file loaded successfully")
            self.textBrowser.setStyleSheet("border-radius: 10px;")
            print(self)  # Print the contents of MainWindow
        except Exception as e:
            print("Error loading UI file:", e)

        self.eventcombobox.currentIndexChanged.connect(self.handle_combobox_change)
        self.conn = sqlite3.connect("karyakram.db")
        self.cursor = self.conn.cursor()
        self.populate_data()  # populate initial data

    def populate_data(self):
        pass

    def handle_combobox_change(self, index):
        try:
            # get selected item from dropbox menu
            selected_item = self.eventcombobox.currentText()

            # retrieve data from database
            query = "SELECT info FROM gallery WHERE name=?"
            self.cursor.execute(query, (selected_item,))
            data = self.cursor.fetchone()

            # debug statements
            print("Selected item:", selected_item)
            print("Data from database:", data)

            # updating information field
            if data:
                # Display retrieved info in a QTextEdit widget
                self.textBrowser.setPlainText(data[0])
            else:
                # Clear QTextEdit if no data found
                self.textBrowser.clear()

        except Exception as e:
            print("Error handling combobox change:", e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    mainwindow = GalleryWindow()
    widget.addWidget(mainwindow)
    widget.show()
    mainwindow.show()
    sys.exit(app.exec())