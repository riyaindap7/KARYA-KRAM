# KARYA-KRAM

**KARYA-KRAM** stands at the forefront of innovation in the realm of college event management, offering a revolutionary web application designed to redefine organization and coordination.

## Project Description

Powered by Python, with a particular emphasis on PyQt6 for GUI design, and SQLite3 for database management, this platform presents a comprehensive solution for every facet of event planning, execution, and preservation.

Central to **KARYA-KRAM** is its intuitive calendar interface, empowering organizers to effortlessly input and manage event details. Featured prominently on the homepage, this interface ensures easy access and facilitates efficient planning and coordination.

Complementing this functionality is the dedicated gallery section, meticulously curated to showcase highlights from past events. By immortalizing memorable moments, this feature fosters a sense of continuity and deepens appreciation for the college's event history.

The integration of QR code functionality streamlines attendance tracking, providing participants with personalized QR codes for seamless registration. Concurrently, organizers benefit from enhanced efficiency in managing attendance records.

Augmenting these capabilities is a robust notification system, meticulously designed to keep participants informed every step of the way. From registration confirmations to real-time event updates delivered via email, participants remain engaged and informed throughout the event lifecycle.

However, **KARYA-KRAM** transcends logistical management; it serves as a catalyst for community engagement. Through its interactive features, students can engage in real-time interactions, sharing experiences, feedback, and insights. This fosters a vibrant ecosystem where the exchange of ideas flourishes, enriching the overall event experience and fostering a profound sense of belonging.

Thus, **KARYA-KRAM** represents a paradigm shift in event management, empowering colleges and organizers to streamline processes, alleviate manual workload, and elevate operational efficiency to unprecedented levels. Its multifaceted approach not only simplifies logistics but also cultivates a vibrant community, laying the groundwork for transformative event experiences and fostering a lasting legacy within the college ecosystem.

---

## Features

- Intuitive calendar interface for event management
- Event gallery showcasing past event highlights
- QR code generation for attendance tracking
- Email notification system for registrations and updates
- Real-time student interaction and feedback
- Robust database management with SQLite3
- User-friendly GUI built with PyQt6

---

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd KaryaKram
   ```

2. Set up a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) Generate Qt resource file if you modify images.qrc:
   ```bash
   pyrcc6 images.qrc -o images_rc.py
   ```

5. Run the application:
   ```bash
   python src/connection_own.py
   ```

---

## Project Structure

- `src/` - Source code for the application
- `ui/` - Qt Designer UI files
- `images.qrc` - Qt resource collection file for images
- `database/karyakram.db` - SQLite3 database file
- `README.md` - Project documentation

---

## Notes

- Ensure all image paths in UI files use Qt resource paths (e.g., `:/prefix/image.png`) for portability.
- The application requires a working SMTP configuration for email notifications.
- For QR code functionality, the `qrcode` Python package is used.

---

## Contact

For any questions or support, please contact @riyaindap7.
