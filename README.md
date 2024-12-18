# Automated Timetable Generation Project

This project aims to automate the generation of timetables for educational institutions based on input data from an Excel file. The system considers various factors such as courses, semesters, teachers, credit points, time slots, and subject-teacher assignments to create a conflict-free timetable.

## Features

1. **Excel-based Input**
   - Reads multiple sheets from an Excel file including Courses, Teachers, Credit Points, Time Slots, and Subjects with Teachers.

2. **Dynamic Timetable Creation**
   - Generates timetables for multiple courses and semesters.
   - Assigns teachers to subjects based on predefined ratios while ensuring teacher availability.

3. **Conflict Resolution**
   - Avoids teacher scheduling conflicts using a deterministic teacher-assignment algorithm.
   - Dynamically manages subject-practical durations within available time slots.

4. **Recess and Boundaries**
   - Automatically handles recess periods.
   - Ensures time slots fit within defined daily start and end times.

5. **Credit-based Subject Weighting**
   - Distributes subjects across the timetable proportionally based on credit points.

6. **Teacher Workload Monitoring**
   - Tracks and optimizes teacher workload throughout the week.

7. **Web Interface**
   - Provides a user-friendly interface for viewing timetables and exporting them in Excel format.

8. **Logging and Error Handling**
   - Implements logging for tracking application behavior and error handling for robustness.


## Features
- **User Authentication**: Secure login using credentials stored in an Excel file.
- **File Upload**: Users can upload Excel files containing course and scheduling data.
- **Timetable Generation**: Automatically generates a timetable based on courses, teachers, and time slots.
- **Teacher Workload Tracking**: Displays the workload of each teacher based on assigned classes.
- **Export Functionality**: Allows users to download the generated timetable as an Excel file.

## Requirements
- Python 3.x
- Flask
- Pandas
- Openpyxl (for handling Excel files)
- Other dependencies specified in `requirements.txt`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/timetable-management-system.git
   cd timetable-management-system
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have an Excel file with the following sheets:
   - **Login Details**: Contains columns `Email` and `Password`.
   - **Courses**: Contains columns `Course Name`, `Semester`, `Theory Subjects`, and `Practical Subjects`.
   - **Teachers**: Contains columns `Course Name` and `Teacher Name`.
   - **Credit Points**: Contains columns `Subject` and `Credits`.
   - **Time Slots**: Contains columns `Course Name`, `Start Time`, `End Time`, `Recess Start`, `Recess End`, `Theory Session Length`, and `Practical Session Length`.
   - **Subjects with Teachers**: Contains columns for subjects and their respective teachers along with their ratios.

4. Run the application:
   ```bash
   python app.py
   ```

5. Access the application in your web browser at `http://127.0.0.1:5000`.

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

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

Feel free to customize this README template according to your project's specifics or preferences!

