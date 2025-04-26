import sys
from PyQt6.QtWidgets import QApplication, QStackedWidget, QMessageBox
from signup import SignupWindow
from login import LoginWindow
from registeration import RegisterationWindow
from Participation_register import ParticipationWindow
from hompage_user import HomepageWindow
from gallery_user import GalleryWindow
from volunteering_register import VolunteeringWindow
from homepage_admin import AdHomepageWindow
from qr1 import ScannerWindow
from gallery_admin import GadminWindow
from calendar_admin import CalendarWindow
from load_QRfinal import LoadQR
from load_QRfinal_vol import LoadQR_vol
from homepage_try import ImageInsertionWindow


class ConnectionManager:
    def __init__(self):
        self.login_window = LoginWindow()
        self.homepage_window = HomepageWindow()
        self.gallery_window = GalleryWindow()
        self.registeration_window = RegisterationWindow()
        self.volunteering_window = VolunteeringWindow()
        self.participation_window = ParticipationWindow()
        self.adminhomepage_window = AdHomepageWindow()
        self.image_window=ImageInsertionWindow()
        self.qr_window = LoadQR()
        self.qr_window_vol = LoadQR_vol()
        self.calendar_window = None
        self.galleryadmin_window = None
        self.scanner_window = None
        self.signup_window=SignupWindow()
        #self.galleryadmin_window.image_butt.clicked.connect(self.image_window)
        self.login_window.signup_butt.clicked.connect(self.goto_signup)
        self.signup_window.signupCompleted.connect(self.goto_login)
        self.adminhomepage_window.gallery_butt.clicked.connect(self.goto_galleryadmin)
        self.homepage_window.admin_log.clicked.connect(self.logout)
        self.adminhomepage_window.admin_log.clicked.connect(self.logout)
        self.qr_window.back6_butt.clicked.connect(self.goto_registeration)
        self.qr_window_vol.back6_butt.clicked.connect(self.goto_registeration)
        self.volunteering_window.showSuccessDialog.connect(self.open_qr_volun)
        self.participation_window.showSuccessDialog.connect(self.open_qr)
        self.adminhomepage_window.cal_butt.clicked.connect(self.goto_calendar)
        #self.adminhomepage_window.gallery_butt.clicked.connect(self.goto_galleryadmin)
        self.adminhomepage_window.scanner_butt.clicked.connect(self.goto_scanner)
        self.login_window.login_butt_2.clicked.connect(self.login_function_admin)
        self.login_window.login_butt.clicked.connect(self.login_function)
        self.homepage_window.gallery_butt.clicked.connect(self.galleryfunction)
        self.homepage_window.participation_butt.clicked.connect(self.goto_registeration)
        self.registeration_window.parti_butt.clicked.connect(self.goto_participation)
        self.registeration_window.volun_butt.clicked.connect(self.goto_volunteering)
        self.adminhomepage_window.contact_butt.clicked.connect(self.goto_message)
        self.homepage_window.contact_butt.clicked.connect(self.goto_message)
        self.participation_window.back2_butt.clicked.connect(self.back_registeration)
        self.volunteering_window.back3_butt.clicked.connect(self.back_registeration)
        self.gallery_window.back3_butt.clicked.connect(self.back_homepage)
        self.registeration_window.back4_butt.clicked.connect(self.back_homepage)

    def goto_message(self):
        QMessageBox.information(None, "Under_Construction", "Function coming soon.")

    def goto_login(self):
        widget.addWidget(self.login_window)
        widget.setCurrentWidget(self.login_window)
    def goto_signup(self):
        widget.addWidget(self.signup_window)
        widget.setCurrentWidget(self.signup_window)

    def goto_galleryadmin(self):
        if self.galleryadmin_window is None:
            print("Creating new instance of CalendarWindow")
            self.galleryadmin_window= GadminWindow()
            self.galleryadmin_window.showSuccessDialog.connect(self.goto_galleryadmin)
            widget.addWidget(self.galleryadmin_window)
            self.galleryadmin_window.back8_butt.clicked.connect(self.goto_adminhomepage)
        widget.setCurrentWidget(self.galleryadmin_window)

    def choice(self):
        widget.addWidget(self.image_window)
        widget.setCurrentWidget(self.image_window)
    def logout(self):
        widget.addWidget(self.login_window)
        widget.setCurrentWidget(self.login_window)
    def open_qr_volun(self):
        try:
            self.volunteering_window.send_notification_email()
            widget.addWidget(self.qr_window_vol)
            widget.setCurrentWidget(self.qr_window_vol)
        except Exception as e:
            print("Error:", e)

    def open_qr(self):
        try:
            self.participation_window.send_notification_email()
            widget.addWidget(self.qr_window)
            widget.setCurrentWidget(self.qr_window)
        except Exception as e:
            print("Error:", e)

    def login_function(self):
        username = self.login_window.userfield.text()
        password = self.login_window.passwordfield.text()

        if LoginWindow.authenticate_user(username, password):
            print("Successfully logged in.")
            self.login_window.error.setText("")
            widget.addWidget(self.homepage_window)
            widget.setCurrentWidget(self.homepage_window)
            print("starting:", widget.currentIndex())
        else:
            self.login_window.error.setText("Invalid username or password.")

    def goto_calendar(self):
        if self.calendar_window is None:
            print("Creating new instance of CalendarWindow")
            self.calendar_window = CalendarWindow()
            self.calendar_window.showSuccessDialog.connect(self.goto_calendar)
            widget.addWidget(self.calendar_window)
            self.calendar_window.back7_butt.clicked.connect(self.goto_adminhomepage)
        widget.setCurrentWidget(self.calendar_window)

    def goto_adminhomepage(self):
        if self.adminhomepage_window is None:
            print("Creating new instance of AdHomepageWindow")
            self.adminhomepage_window = AdHomepageWindow()
            widget.addWidget(self.adminhomepage_window)
            self.adminhomepage_window.show()
        else:
            # Reload the table data
            self.adminhomepage_window.load_tabel()

        widget.setCurrentWidget(self.adminhomepage_window)
    def login_function_admin(self):
        username = self.login_window.userfield_2.text()
        password = self.login_window.passwordfield_2.text()

        if LoginWindow.authenticate_admin(username, password):
            print("Admin successfully logged in.")
            widget.addWidget(self.adminhomepage_window)  # Assuming you have an admin homepage window
            widget.setCurrentWidget(self.adminhomepage_window)
        else:
            self.login_window.error.setText("Invalid admin username or password.")

    def goto_registeration(self):
        widget.addWidget(self.registeration_window)
        widget.setCurrentWidget(self.registeration_window)
        print("regisr:", widget.currentIndex())

    def goto_participation(self):
        widget.addWidget(self.participation_window)
        widget.setCurrentWidget(self.participation_window)
        print("parti:", widget.currentIndex())

    def back_registeration(self):
        widget.setCurrentWidget(self.registeration_window)


    def galleryfunction(self):
        # self.homepage_window.gallery_butt.clicked.disconnect(self.galleryfunction)
        widget.addWidget(self.gallery_window)
        widget.setCurrentWidget(self.gallery_window)
        print("gallery:", widget.currentIndex())

    def goto_volunteering(self):
        widget.addWidget(self.volunteering_window)
        widget.setCurrentWidget(self.volunteering_window)

    def back_homepage(self):
        widget.setCurrentWidget(self.homepage_window)
        print("backtohome:", widget.currentIndex())

    def goto_scanner(self):
        if self.scanner_window is None:
            self.scanner_window = ScannerWindow()
            widget.addWidget(self.scanner_window)
            widget.setCurrentWidget(self.scanner_window)

        else:
            widget.setCurrentWidget(self.scanner_window)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    mainwindow = ConnectionManager()
    widget.addWidget(mainwindow.login_window)
    widget.show()
    mainwindow.login_window.show()
    sys.exit(app.exec())
