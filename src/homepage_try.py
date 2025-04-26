import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QMessageBox, QFileDialog
import sqlite3
from gallery_admin import GadminWindow
class ImageInsertionWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Insertion Example")

        # Create QLabel to display the image
        self.image_label = QLabel("No image selected")

        # Create QPushButton to select image
        self.select_image_button = QPushButton("Select Image")
        self.select_image_button.clicked.connect(self.select_image)

        # Create QPushButton to save image
        self.save_image_button = QPushButton("Save Image")
        self.save_image_button.clicked.connect(self.save_image)

        # Create a layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.select_image_button)
        layout.addWidget(self.save_image_button)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Initialize image data variable
        self.image_data = None

    def select_image(self):
        # Open file dialog to select image file
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Select Image")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("Image Files (*.png *.jpg *.jpeg)")
        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            # Load image data
            with open(file_path, "rb") as file:
                self.image_data = file.read()
            # Display selected image
            pixmap = QPixmap(file_path)
            self.image_label.setPixmap(pixmap)

    def save_image(self):
        if self.image_data:
            try:

                # Connect to SQLite database
                conn = sqlite3.connect("your_database.db")
                cursor = conn.cursor()

                # Insert image data into database
                cursor.execute("INSERT INTO images (image_data) VALUES (?)", (self.image_data,))
                conn.commit()

                conn.close()
                QMessageBox.information(self, "Success", "Image saved to database successfully.")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to save image to database: {e}")
        else:
            QMessageBox.warning(self, "Error", "No image selected.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageInsertionWindow()
    window.show()
    sys.exit(app.exec())
