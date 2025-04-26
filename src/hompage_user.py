import sys
from PyQt6 import QtWidgets
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QFrame, QPushButton
from PyQt6.uic import loadUi
import sqlite3
from gallery_user import GalleryWindow
from registeration import RegisterationWindow


class HomepageWindow(QMainWindow):
    def __init__(self):
        super(HomepageWindow, self).__init__()
        try:
            loadUi("ui/Homepage_pyqt.ui", self)
            print("UI file loaded successfully")
            print(self)  # Print the contents of MainWindow
            self.upcoming_events()
        except Exception as e:
            print("Error loading UI file:", e)

        #self.gallery_butt.clicked.connect(self.galleryfunction)
        #self.participation_butt.clicked.connect(self.participationfunction)

    def upcoming_events(self):
        conn=sqlite3.connect('karyakram.db')
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM calendar WHERE date >= date('now') ORDER BY date")
        events=cursor.fetchall()
        for event in events:
            print(event)
        cursor.execute("SELECT COUNT(*) FROM calendar WHERE date >= date('now') ORDER BY date")
        count=cursor.fetchone()
        if count:
            count_row = count[0]
            print("count is", count_row)
        else:
            print("No row satisfying condition")
        conn.close()
        try:
            if count_row>=3:
                first_row=events[0]
                for row1 in first_row:
                    self.label_10.setText(first_row[0])
                    self.label_11.setText(first_row[1])
                    self.label_12.setText(first_row[2])
                    self.label_13.setText(first_row[3])
                    self.label_14.setText(first_row[4])
                second_row=events[1]
                for row2 in second_row:
                    self.label_21.setText(second_row[0])
                    self.label_22.setText(second_row[1])
                    self.label_23.setText(second_row[2])
                    self.label_24.setText(second_row[3])
                    self.label_25.setText(second_row[4])
                third_row = events[2]
                for row2 in third_row:
                    self.label_32.setText(third_row[0])
                    self.label_33.setText(third_row[1])
                    self.label_34.setText(third_row[2])
                    self.label_35.setText(third_row[3])
                    self.label_36.setText(third_row[4])
            elif count_row==2:
                first_row = events[0]
                for row1 in first_row:
                    self.label_10.setText(first_row[0])
                    self.label_11.setText(first_row[1])
                    self.label_12.setText(first_row[2])
                    self.label_13.setText(first_row[3])
                    self.label_14.setText(first_row[4])
                second_row = events[1]
                for row2 in second_row:
                    self.label_21.setText(second_row[0])
                    self.label_22.setText(second_row[1])
                    self.label_23.setText(second_row[2])
                    self.label_24.setText(second_row[3])
                    self.label_25.setText(second_row[4])
                self.hidden=False
                self.frame1 = self.findChild(QFrame, "Mosaic")
                if not self.hidden:
                    self.frame1.hide()
            elif count_row==1:
                first_row = events[0]
                for row1 in first_row:
                    self.label_10.setText(first_row[0])
                    self.label_11.setText(first_row[1])
                    self.label_12.setText(first_row[2])
                    self.label_13.setText(first_row[3])
                    self.label_14.setText(first_row[4])
                self.hidden = False
                self.frame1 = self.findChild(QFrame, "Mosaic")
                if not self.hidden:
                    self.frame1.hide()
                self.hidden = False
                self.frame2 = self.findChild(QFrame, "Iris")
                if not self.hidden:
                    self.frame2.hide()
            else:
                self.hidden = False
                self.frame1 = self.findChild(QFrame, "Mosaic")
                if not self.hidden:
                    self.frame1.hide()
                self.hidden = False
                self.frame2 = self.findChild(QFrame, "Iris")
                if not self.hidden:
                    self.frame2.hide()
                #removing existing widgets
                self.ignitra_frame=self.findChild(QFrame,"Ignitra")
                if self.ignitra_frame is None:
                    print("Ignitra not found")
                    return
                for widget in self.ignitra_frame.children():
                    if isinstance(widget,(QLabel,QPushButton)):
                        widget.deleteLater()
                #creating a brand new label
                new_label=QLabel("NO UPCOMING EVENTS SOON",self.ignitra_frame)
                new_label.setStyleSheet(("color:black;font-size:22px; font-weight: bold;"))
                new_label.setFont(QFont("Comic Sans Ms",35))
                new_label.setFixedHeight(40)
                self.ignitra_frame.layout().addWidget(new_label)
        except Exception as e:
            print("error loading data:",e)

    """def galleryfunction(self):
        try:
            mainwindow1 = GalleryWindow()
            widget.addWidget(mainwindow1)
            widget.setCurrentIndex((widget.currentIndex() + 1))
        except Exception as e:
            print("Error loading UI file:", e)

    def participationfunction(self):
        mainwindow1 = RegisterationWindow()
        widget.addWidget(mainwindow1)
        widget.setCurrentIndex((widget.currentIndex() + 1))"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    mainwindow = HomepageWindow()
    widget.addWidget(mainwindow)
    #mainwindow.set_widget(widget)
    widget.show()
    mainwindow.show()
    sys.exit(app.exec())
