# Automated Timetable Generation Project

This project aims to automate the generation of timetables for educational institutions based on input data from an Excel file. The system considers various factors such as courses, semesters, teachers, credit points, time slots, and subject-teacher assignments to create a conflict-free timetable.

## Features
1. **User Authentication**
   - Secure login using credentials stored in an Excel file.
     
2. **Excel-based Input**
   - Reads multiple sheets from an Excel file including Courses, Teachers, Credit Points, Time Slots, and Subjects with Teachers.

3. **Dynamic Timetable Creation**
   - Generates timetables for multiple courses and semesters.
   - Assigns teachers to subjects based on predefined ratios while ensuring teacher availability.

4. **Conflict Resolution**
   - Avoids teacher scheduling conflicts using a deterministic teacher-assignment algorithm.
   - Dynamically manages subject-practical durations within available time slots.

5. **Recess and Boundaries**
   - Automatically handles recess periods.
   - Ensures time slots fit within defined daily start and end times.

6. **Credit-based Subject Weighting**
   - Distributes subjects across the timetable proportionally based on credit points.

7. **Teacher Workload Monitoring**
   - Tracks and optimizes teacher workload throughout the week.

8. **Web Interface**
   - Provides a user-friendly interface for viewing timetables and exporting them in Excel format.

9. **Logging and Error Handling**
   - Implements logging for tracking application behavior and error handling for robustness.
     
10. **Export Functionality**
   - Allows users to download the generated timetable as an Excel file.


## Requirements
- Python 3.x
- Flask
- Pandas
- Openpyxl (for handling Excel files)
- Other dependencies specified in `requirements.txt`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Hani-3/timetable-generator.git
   cd timetable-generator
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have an Excel file:
   Example excel sheet link : https://github.com/Hani-3/timetable-generator/blob/main/timetable%20excel.xlsx

5. Run the application:
   ```bash
   python app.py
   ```

6. Access the application in your web browser at `http://127.0.0.1:5000`.

## Usage
1. Navigate to the login page. 
2. Enter your credentials to log in.
3. Upload your Excel file containing course data.
4. After uploading, the system will generate a timetable which can be accessed from the main page.

## File Structure
```
/timetable-management-system
│
├── app.py                   # Main application file
├── requirements.txt         # Python dependencies
├── /uploads                 # Directory for uploaded files
└── /templates               # HTML templates for rendering views
```

## Logging and Error Handling
The application includes logging for tracking events and errors during execution. Any exceptions raised will be logged for debugging purposes.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request for any improvements or features you'd like to add.

---

