import sys
from PyQt6 import QtWidgets
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.uic import loadUi
import sqlite3
from load_QRfinal_vol import LoadQR_vol
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class VolunteeringWindow(QMainWindow):
    showSuccessDialog = pyqtSignal()

    def __init__(self):
        super(VolunteeringWindow, self).__init__()
        self.emailId = ""
        self.event = ""
        try:
            loadUi("ui/volunteering_register.ui", self)
            print("UI file loaded successfully")
            print(self)  # Print the contents of MainWindow
        except Exception as e:
            print("Error loading UI file:", e)
        self.conn = sqlite3.connect("karyakram.db")
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT event_name FROM calendar")
        results = self.cur.fetchall()
        print(results)
        self.eventfield.clear()
        self.default_event = "Events"  # Set your default event name here
        self.eventfield.addItem(self.default_event)  # Add the default event to the combo box
        for row in results:
            self.eventfield.addItem(row[0])  # Add other events from the database to the combo box
        self.v_butt.clicked.connect(self.volun_confirm)

    def validate_email(self, email):
        # Using a regular expression to validate email format
        pattern = r'^[a-zA-Z0-9_.+-]+@student\.sfit\.ac\.in$'
        return re.match(pattern, email)

    def volun_confirm(self):
        name = self.namefield.text()
        contact = self.contactfield.text()
        self.emailId = self.emailIdfield.text()
        pid = self.pidfield.text()
        dept = self.deptfield.currentText()
        year = self.yearfield.currentText()
        self.event = self.eventfield.currentText()
        domain = self.domainfield.currentText()
        if len(name) == 0 or len(contact) == 0 or len(self.emailId) == 0 or len(pid) == 0 or len(dept) == 0 or len(
                year) == 0 or len(self.event) == 0 or len(domain) == 0:
            self.error.setText("Please input all fields!")
        elif not self.validate_email(self.emailId):
            self.error.setText("Use sfit emailId only!")
        elif not len(contact) == 10:
            self.error.setText("Enter vaild contact no!")
        elif not len(pid) == 6:
            self.error.setText("Enter vaild PID!")
        else:
            try:
                query = f"SELECT pid FROM volunteering ORDER BY ROWID DESC LIMIT 1"
                self.cur.execute(query)
                latest_entry = self.cur.fetchone()[0]
                print(latest_entry)
            except Exception as e:
                print("issue with pid:", e)
            query_check_user = "SELECT COUNT(*) FROM volunteering WHERE pid=?"
            self.cur.execute(query_check_user, (pid,))
            result_count = self.cur.fetchone()[0]

            if result_count > 0:
                self.error.setText("You have already registered for this event!")
            else:
                try:
                    query_insert_user = "INSERT INTO volunteering (name,contact,emailId,pid,dept,year,event,domain) VALUES (?,?,?,?,?,?,?,?)"
                    self.cur.execute(query_insert_user, (name, contact, self.emailId, pid, dept, year, self.event, domain))
                    print("registered successfully!")
                    self.error.setText("")
                    self.conn.commit()
                    self.showSuccessDialog.emit()
                    self.conn.close()
                except Exception as e:
                    print("error with database:", e)

    def send_notification_email(self):

        # Set up email parameters
        sender_email = "8karyakram@gmail.com"
        receiver_email = self.emailId  # Your Gmail address
        password = "abhq ropz lmss horh"
        subject = "Notification: Registered For An Event"
        body = f"Hello! You have registered for volunteering in the event {self.event}. This is a reminder. Download the QR for the attendance."

        # Generate the QR code and obtain its file path
        load_qr = LoadQR_vol()
        qr_file_path = load_qr.generate_qr_code()

        # Create the email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Add attachment (QR code)
        with open(qr_file_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename= {qr_file_path}")
        message.attach(part)

        # Connect to the SMTP server and send the email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.send_message(message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    mainwindow = VolunteeringWindow()
    widget.addWidget(mainwindow)
    widget.show()
    mainwindow.show()
    sys.exit(app.exec())
