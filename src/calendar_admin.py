import sys
from PyQt6 import QtWidgets
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.uic import loadUi
import sqlite3
from PyQt6.QtCore import QDate

class CalendarWindow(QMainWindow):
    showSuccessDialog = pyqtSignal()
    def __init__(self):
        super(CalendarWindow, self).__init__()
        try:
            loadUi("ui/calendar_admin.ui", self)
            print("UI file loaded successfully")
            print(self)# Print the contents of MainWindow
            self.calendarWidget1.selectionChanged.connect(self.calendarDateChanged)
            # self.upadteTaskList()
            self.Venue.setPlaceholderText("Enter venue")

            # Connect editingFinished signal to handle the disappearance of placeholder text
            self.Venue.editingFinished.connect(self.handleVenueEditingFinished)
            self.CreateEvent.clicked.connect(self.handleCreateEventClicked)
            self.show()
        except Exception as e:
            print("Error loading UI file:", e)

    def calendarDateChanged(self):
        print("the calendar date was changed")
        dateSelected = self.calendarWidget1.selectedDate().toPyDate()
        self.show_date.setText(str(dateSelected))
        print("Date selected: ", dateSelected)

    def handleVenueEditingFinished(self):
        # Check if the text in the venue QLineEdit is empty and set placeholder text again
        if not self.Venue.text():
            self.Venue.setPlaceholderText("Enter venue")

    def handleCreateEventClicked(self):
        # Check if necessary fields are filled
        date_str = self.show_date.text()
        event_name = self.comboBox.currentText()
        venue = self.Venue.text()
        timefr = self.timeEdit.time().toString()
        timeto = self.timeEdit_2.time().toString()

        # Convert date string to a QDate object
        date = QDate.fromString(date_str, "yyyy-MM-dd")  # Adjust the format as per your data

        current_date = QDate.currentDate()

        if date < current_date:
            QMessageBox.warning(self, "Warning", "The selected date has already passed.")
        elif not self.calendarWidget1.selectedDate().isValid() or not self.Venue.text():
            QMessageBox.warning(self, "Warning", "Please fill in all fields.")
        else:
            conn = sqlite3.connect("karyakram.db")
            cur = conn.cursor()
            query_insert_event = "INSERT INTO calendar (date, event_name, venue, timefr, timeto) VALUES (?, ?, ?, ?, ?)"

            # Convert QDate to string representation
            date_str = date.toString("yyyy-MM-dd")  # Adjust the format as per your data

            # Execute the query
            cur.execute(query_insert_event, (date_str, event_name, venue, timefr, timeto))
            conn.commit()
            self.showSuccessDialog.emit()
            QMessageBox.information(self, "Success", "Event added successfully.")
            conn.close()

    def show_success_dialog(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Event_add Activity")
        msg_box.setText("Event Added Successfully!")
        msg_box.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    mainwindow = CalendarWindow()
    widget.addWidget(mainwindow)
    widget.show()
    mainwindow.show()
    sys.exit(app.exec())