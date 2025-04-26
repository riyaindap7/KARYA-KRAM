import sys
import cv2
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from pyzbar.pyzbar import decode
import sqlite3

class ScannerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Connect to SQLite database
        self.conn = sqlite3.connect('karyakram.db')
        self.c = self.conn.cursor()

        # Start video capture
        self.video = cv2.VideoCapture(0)

        self.should_close_window = False

        self.scan_qr_code()

    def scan_qr_code(self):
        while not self.should_close_window:
            check, frame = self.video.read()
            d = decode(frame)

            try:
                for obj in d:
                    pid = obj.data.decode()  # Extract PID from QR code
                    print("Scanned PID:", pid)

                    # Check if PID already exists in the attendance table
                    self.c.execute("SELECT * FROM attendance WHERE pid_par=? OR pid_vol=?", (pid, pid))
                    existing_pid = self.c.fetchone()

                    if existing_pid:
                        QMessageBox.information(self, "Attendance Already Registered",
                                                f"Your attendance for PID: {pid} is already registered.")
                    else:
                        # Check if PID already exists in the participation table
                        self.c.execute("SELECT * FROM participation WHERE pid=?", (pid,))
                        existing_pid_participation = self.c.fetchone()

                        # Check if PID already exists in the volunteering table
                        self.c.execute("SELECT * FROM volunteering WHERE pid=?", (pid,))
                        existing_pid_volunteer = self.c.fetchone()

                        if existing_pid_participation and existing_pid_volunteer:
                            # Insert PID into the attendance table's pid_par and pid_vol columns
                            self.c.execute("INSERT INTO attendance (pid_par, pid_vol) VALUES (?, ?)", (pid, pid))
                            self.conn.commit()
                            QMessageBox.information(self, "Attendance Registered",
                                                    f"Attendance for PID: {pid} is successfully registered.")
                            self.should_close_window = True

                        elif existing_pid_participation:
                            # Insert PID into the attendance table's pid_par column
                            self.c.execute("INSERT INTO attendance (pid_par) VALUES (?)", (pid,))
                            self.conn.commit()
                            QMessageBox.information(self, "Attendance Registered",
                                                    f"Attendance for PID: {pid} is successfully registered.")
                            self.should_close_window = True

                        elif existing_pid_volunteer:
                            # Insert PID into the attendance table's pid_vol column
                            self.c.execute("INSERT INTO attendance (pid_vol) VALUES (?)", (pid,))
                            self.conn.commit()
                            QMessageBox.information(self, "Attendance Registered",
                                                    f"Attendance for PID: {pid} is successfully registered.")
                            self.should_close_window = True

                        else:
                            QMessageBox.information(self, "PID Not Registered",
                                                    f"PID: {pid} is not registered for participation or volunteering.")

            except Exception as e:
                print("Error:", e)

            cv2.imshow("Attendance", frame)
            key = cv2.waitKey(1)
            if key == ord("q"):
                break

        # Close video capture and database connection
        self.video.release()
        cv2.destroyAllWindows()
        self.conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScannerWindow()
    window.show()
    sys.exit(app.exec())

