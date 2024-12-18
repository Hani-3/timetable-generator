

import pandas as pd
from flask import Flask, render_template, send_file, request
import io
import random
from datetime import time, timedelta, datetime
import sys
from src.exception import CustomException
from src.logger import logging

app = Flask(__name__)

import pandas as pd

def load_data_from_excel(file_path):
    # Read each sheet from the Excel file
    courses_df = pd.read_excel(file_path, sheet_name="Courses")
    teachers_df = pd.read_excel(file_path, sheet_name="Teachers")
    credits_df = pd.read_excel(file_path, sheet_name="Credit Points")
    time_slots_df = pd.read_excel(file_path, sheet_name="Time Slots")
    subjects_with_teachers_df = pd.read_excel(file_path, sheet_name="Subjects with Teachers")

    # Convert dataframes to dictionaries
    courses = {}
    for _, row in courses_df.iterrows():
        course_name = row['Course Name']
        semester = row['Semester']
        theory_subject = row['Theory Subjects']
        practical_subject = row['Practical Subjects']

        if course_name not in courses:
            courses[course_name] = {}
        if semester not in courses[course_name]:
            courses[course_name][semester] = {
                'Theory_subjects': [],
                'Practical_subjects': []
            }
        
        # Append subjects to the list
        if pd.notna(theory_subject):  # Check if not NaN
            courses[course_name][semester]['Theory_subjects'].append(theory_subject)
        if pd.notna(practical_subject):  # Check if not NaN
            courses[course_name][semester]['Practical_subjects'].append(practical_subject)

    teachers = {}
    for _, row in teachers_df.iterrows():
        course_name = row['Course Name']
        teacher = row['Teacher Name']
        
        if course_name not in teachers:
            teachers[course_name] = []
        teachers[course_name].append(teacher)

        

    credit_points = credits_df.set_index('Subject')['Credits'].to_dict()

    time_slots = {}
    for _, row in time_slots_df.iterrows():
        course_name = row['Course Name']
        start_time = row['Start Time']
        end_time = row['End Time']
        recess_start = row['Recess Start']
        recess_end = row['Recess End']
        theory_length = row['Theory Session Length']
        practical_length = row['Practical Session Length']
        
        time_slots[course_name] = {
            'start_time': start_time,
            'end_time': end_time,
            'recess_start': recess_start,
            'recess_end': recess_end,
            'theory_length': theory_length,
            'practical_length': practical_length

        }

    subject_with_teacher = {}
    for _, row in subjects_with_teachers_df.iterrows():
        subject = row['Subject']
        teacher1 = row['Teacher 1']
        teacher2 = row['Teacher 2']

        subject_with_teacher[subject] = {
            'teacher1' : teacher1,
            'teacher2' : teacher2
        }

    return courses, teachers, credit_points, time_slots, subject_with_teacher

# Path to your Excel file
file_path = 'C:\\Users\\HANI PATEL\\Desktop\\timetable excel.xlsx'

# Load data from Excel
courses, teachers, credit_points, time_slots, subject_with_teacher = load_data_from_excel(file_path)

# Function to increment time
def increment_time(current_time, delta):
    try:
        new_time = (datetime.combine(datetime.today(), current_time) + delta).time()
        return new_time
    except Exception as e:
        logging.info("Error occurred in increment_time")
        raise CustomException(e, sys)


# Track teacher time slots to avoid conflicts
teacher_schedule = {
    'Monday': {},
    'Tuesday': {},
    'Wednesday': {},
    'Thursday': {},
    'Friday': {},
    'Saturday': {}
}

# Function to check if a teacher is available for a specific time slot
def is_teacher_available(teacher, day, start_time, end_time):
    if teacher not in teacher_schedule[day]:
        teacher_schedule[day][teacher] = []
    for slot in teacher_schedule[day][teacher]:
        if slot['start'] < end_time and start_time < slot['end']:
            return False  # Overlapping time slots
    return True

# Function to book a time slot for a teacher
def book_teacher(teacher, day, start_time, end_time):
    teacher_schedule[day][teacher].append({'start': start_time, 'end': end_time})


from datetime import datetime, timedelta

def time_difference(start_time, end_time):
    """
    Calculate the difference in minutes between two datetime.time objects.
    """
    today = datetime.today()
    start_dt = datetime.combine(today, start_time)
    end_dt = datetime.combine(today, end_time)

    if end_dt < start_dt:  # Handle cases where end_time is past midnight
        end_dt += timedelta(days=1)

    return (end_dt - start_dt).total_seconds() / 60  # Return difference in minutes

# Helper function to create timetable
def create_timetable():
    timetable = {}
    try:
        for course in courses:
            for semester in courses[course]:
                timetable[f"{course}-{semester}"] = {}
                subject_options = courses[course][semester]['Theory_subjects'] + courses[course][semester]['Practical_subjects']
                logging.info(f'Subject options: {subject_options}')
                
                # Weight subjects by credit points for distribution across slots
                weighted_subjects = []
                for subject in subject_options:
                    credits = credit_points.get(subject, 0)
                    weighted_subjects.extend([subject] * credits)
                logging.info(f'weighted_subjects: {weighted_subjects}')

                random.shuffle(weighted_subjects)  # Randomize subject order
                logging.info(f'weighted_subjects: {weighted_subjects}')
                subject_idx = 0  # To track which subject to assign next

                weekly_schedule = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
                
                for day in weekly_schedule:
                    logging.info(f"Creating timetable for {course}-{semester} on {day}")
                    timetable[f"{course}-{semester}"][day] = []
                    current_time = time_slots[course]['start_time']
                    end_time_dt = time_slots[course]['end_time']
                    recess_start_dt = time_slots[course]['recess_start']
                    recess_end_dt = time_slots[course]['recess_end']
                    theory_length = time_slots[course]['theory_length']
                    practical_length = time_slots[course]['practical_length']
                    logging.info(f'st: {current_time}, et: {end_time_dt}, rs: {recess_start_dt}, re: {recess_end_dt}, tl: {theory_length}, pl: {practical_length}')

                    time_slots_list = []
                    while current_time < end_time_dt:
                        try:
                            next_time = increment_time(current_time, timedelta(minutes=theory_length))
                            if current_time == recess_start_dt:
                                time_slots_list.append(f"{recess_start_dt.strftime('%H:%M')} - {recess_end_dt.strftime('%H:%M')}")
                                current_time = recess_end_dt
                            else:
                                time_slots_list.append(f"{current_time.strftime('%H:%M')} - {next_time.strftime('%H:%M')}")
                                current_time = next_time
                        except Exception as e:
                            logging.info(f"Error in creating time slots for {course}-{semester} on {day}")
                            raise CustomException(e, sys)

                    timetable[f"{course}-{semester}"]['time_slots'] = time_slots_list

                    #current_time = datetime.strptime(start_time, '%H:%M').time()
                    current_time = time_slots[course]['start_time']

                    while current_time < end_time_dt:
                        # Handle recess
                        if current_time == recess_start_dt:
                            timetable[f"{course}-{semester}"][day].append("Recess")
                            current_time = recess_end_dt  # Skip to end of recess
                            continue

                        if subject_idx >= len(weighted_subjects):
                            subject_idx = 0  # Reset index if we run out of subjects

                        subject = weighted_subjects[subject_idx]
                        teacher = random.choice([subject_with_teacher[subject]['teacher1'], subject_with_teacher[subject]['teacher2']])
                        subject_length = practical_length if subject in courses[course][semester]['Practical_subjects'] else theory_length

                        # Calculate remaining time until the next boundary
                        if current_time < recess_start_dt:
                            remaining_minutes = time_difference(current_time, recess_start_dt)
                        else:
                            remaining_minutes = time_difference(current_time, end_time_dt)

                        if subject in courses[course][semester]['Practical_subjects'] and remaining_minutes < subject_length:
                            # Not enough time for practical; try swapping with a theory subject
                            logging.info('not enouugh time for practical, if condition applied')
                            swapped = False
                            for swap_idx in range(subject_idx + 1, len(weighted_subjects)):
                                swap_subject = weighted_subjects[swap_idx]
                                if swap_subject in courses[course][semester]['Theory_subjects'] and theory_length <= remaining_minutes:
                                    # Perform the swap
                                    weighted_subjects[subject_idx], weighted_subjects[swap_idx] = weighted_subjects[swap_idx], weighted_subjects[subject_idx]
                                    logging.info(f'weighted_subjects[subject_idx]:{weighted_subjects[subject_idx]}, weighted_subjects[swap_idx]: {weighted_subjects[swap_idx]}, weighted_subjects[swap_idx]: {weighted_subjects[swap_idx]}, weighted_subjects[subject_idx]: {weighted_subjects[subject_idx]}')
                                    swapped = True
                                    break
                            
                            if not swapped:
                                # If no suitable swap is found, break (or handle partial scheduling logic here)
                                break

                        # Re-fetch the (possibly swapped) subject and assign it
                        subject = weighted_subjects[subject_idx]
                        subject_length = practical_length if subject in courses[course][semester]['Practical_subjects'] else theory_length
                        next_time = increment_time(current_time, timedelta(minutes=subject_length))

                        if not is_teacher_available(teacher, day, current_time, increment_time(current_time, timedelta(minutes=subject_length))):
                            logging.info(f"{teacher} is already booked for {current_time} on {day}. Finding a new teacher.")
                            
                            # #Attempt to assign secondary teacher
                            # teacher = subject_with_teacher[subject].get('teacher2')
                            # if teacher and is_teacher_available(teacher, day, current_time, next_time):
                            #     logging.info(f"Assigned {teacher} as the secondary teacher for {subject}.")
                            # else:
                            #     logging.info(f"Both primary and secondary teachers are unavailable for {subject} at {current_time}. Skipping this slot.")
                            #     continue  # Skip this time slot if both teachers are unavailable

                            # Fallback to the other teacher
                            alternate_teacher = (
                                subject_with_teacher[subject]['teacher1']
                                if teacher == subject_with_teacher[subject]['teacher2']
                                else subject_with_teacher[subject]['teacher2']
                            )
                            
                            if not is_teacher_available(alternate_teacher, day, current_time, increment_time(current_time, timedelta(minutes=subject_length))):
                                logging.info(f"Both {teacher} and {alternate_teacher} are unavailable for {current_time} on {day}. Skipping this slot.")
                                continue  # Skip this time slot if both teachers are unavailable
                            
                            # Assign the alternate teacher
                            teacher = alternate_teacher
                            

                        book_teacher(teacher, day, current_time, increment_time(current_time, timedelta(minutes=subject_length)))


                        # If practical subject, allocate additional consecutive slots as required
                        while subject in courses[course][semester]['Practical_subjects'] and subject_length > theory_length:
                            timetable[f"{course}-{semester}"][day].append(f"{subject}\n({teacher})")
                            subject_length -= theory_length
                            current_time = increment_time(current_time, timedelta(minutes=theory_length))
                            if current_time >= end_time_dt or current_time == recess_start_dt:
                                continue
                        else:
                            timetable[f"{course}-{semester}"][day].append(f"{subject}\n({teacher})")
                            current_time = next_time

                        subject_idx += 1


                # Print each day’s schedule
                for day in weekly_schedule:
                    print(f"\n{course}-{semester} {day}:")
                    for slot in timetable[f"{course}-{semester}"][day]:
                        print(slot)

    except Exception as e:
        logging.info("Failed to create timetable")
        raise CustomException(e, sys)

    return timetable

timetable = create_timetable()  
@app.route('/')
def index():
    # List all courses with links to their individual timetables
    course_list = list(timetable.keys())
    return render_template('index.html', course_list=course_list)


@app.route('/course/<course>')
def course_timetable(course):
    try:
        # Extract the timetable for the selected course
        course_schedule = timetable.get(course)
        if not course_schedule:
            return f"No timetable found for {course}", 404
        return render_template('timetable5.html', course=course, schedule=course_schedule)
    except Exception as e:
        logging.info(f"An error occurred while generating the timetable for {course}.")
        raise CustomException(e, sys)
    


from flask import Flask, render_template, request, send_file
import pandas as pd
import io

# Assuming the rest of your app is defined as earlier

@app.route('/export/<course>')
def export_timetable(course):
    try:
        # Get the timetable for the selected course
        course_schedule = timetable.get(course)
        if not course_schedule:
            return f"No timetable found for {course}", 404

        # Prepare data for export
        data = []
        time_slots = course_schedule['time_slots']
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

        for idx, time_slot in enumerate(time_slots):
            row = [time_slot]  # Add the time slot to the row
            for day in days:
                if idx < len(course_schedule[day]):
                    row.append(course_schedule[day][idx])
                else:
                    row.append('')  # Empty cell if no data
            data.append(row)

        # Create a DataFrame
        df = pd.DataFrame(data, columns=['Time Slots'] + days)

        # Write DataFrame to an Excel file in memory
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name=f"{course} Timetable")
        output.seek(0)

        # Serve the file
        return send_file(
            output,
            as_attachment=True,
            download_name=f"{course}_Timetable.xlsx",
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
    except Exception as e:
        logging.info(f"An error occurred while exporting the timetable for {course}.")
        raise CustomException(e, sys)


if __name__ == '__main__':
    app.run(debug=True)
