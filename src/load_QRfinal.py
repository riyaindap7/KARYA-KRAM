import sys
from PyQt6 import QtWidgets
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QFileDialog
from PyQt6.uic import loadUi
import sqlite3
import qrcode
from PyQt6.QtGui import QPixmap
# from Participation_register import ParticipationWindow

# from gallery import GalleryWindow
#import re

conn = None
class LoadQR(QMainWindow):
    showSuccessDialog = pyqtSignal()

    def __init__(self):
        super(LoadQR, self).__init__()
        try:
            loadUi("ui/QRfinal.ui", self)
            print("UI file loaded successfully")
            print(self)  # Print the contents of MainWindow
        except Exception as e:
            print("Error loading UI file:", e)
        self.generateQR.clicked.connect(self.generate_qr_code)
        self.downloadQR_2.clicked.connect(self.download_qr_code)

    def handle_success(self):

        self.show()

    def generate_qr_code(self):
        global conn
        conn = sqlite3.connect('karyakram.db')
        cursor = conn.cursor()

        # Query the database to retrieve the latest entry from the specified column
        cursor.execute(
            "SELECT pid FROM participation ORDER BY ROWID DESC LIMIT 1"
        )
        result = cursor.fetchone()

        if result:
            data_to_encode = result[0]
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(data_to_encode)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            img.save("qrcode.png")

            pixmap = QPixmap("qrcode.png")
            self.qr_qr.setPixmap(pixmap)
            return "qrcode.png"
        else:
            QMessageBox.warning(self, "Warning", "error in loading QR.", QMessageBox.Ok)

    def download_qr_code(self):
        filepath, _ = QFileDialog.getSaveFileName(self, "Save QR Code", "", "Images (*.png *.jpg)")
        if filepath:
            pixmap = self.qr_qr.pixmap()
            if pixmap:
                pixmap.save(filepath)
                QMessageBox.information(self, "Success", "QR code saved successfully.", QMessageBox.Ok)
            else:
                QMessageBox.warning(self, "Warning", "No QR code generated yet.", QMessageBox.Ok)

def cleanup():
    global conn
    if conn:
        conn.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    mainwindow = LoadQR()
    widget.addWidget(mainwindow)
    widget.show()
    app.aboutToQuit.connect(lambda: conn.close() if conn else None)  # Close the SQLite connection on application exit
    sys.exit(app.exec())
