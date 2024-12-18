# from flask import Flask, render_template
# import random
# from datetime import time, timedelta, datetime

# import sys
# from src.exception import CustomException
# from src.logger import logging


# app = Flask(__name__)


# # Data setup
# courses = {
#     'MBA': {
#         'Sem-1': {
#             'Theory_subjects': ['PRINCIPLES OF MANAGEMENT', 'QUANTITATIVE TECHNIQUES IN MANAGEMENT', 'MANAGERIAL ECONOMICS', 'MANAGERIAL ACCOUNTING', 'ORGANISATIONAL BEHAVIOUR','MANAGERIAL COMMUNICATION','RESEARCH DESIGN FOR MANAGEMENT'],
#             'Practical_subjects': ['COMMUNICATIVE ENGLISH LABORATORY', 'RESEARCH DESIGN LABORATORY']
#         },
    
#         'Sem-3': {
#             'Theory_subjects': ['STRATEGIC MANAGEMENT', 'FUNDAMENTALS OF ENTERPRISE RESOURCE PLANNING', 'MARKETING','FINANCE','HUMAN RESOURCE','INTERNATIONAL BUSINESS','ENTREPRENEURSHIP','SUPPLY CHAIN MANAGEMENT','SECTOR'],
#             'Practical_subjects': ['PERSONALITY GROWTH LAB',  'MANAGEMENT RESEARCH PROJECT']
#         }
#     },
#     'MCA': {
#         'Sem-1': {
#             'Theory_subjects': ['JAVA PROGRAMMING', 'ALGORITHMS AND LOGIC DEVELOPMENT', 'COMPUTER FUNDAMENTALS AND NETWORKING', 'WEB DESIGNING AND DATABASE', 'PYTHON PROGRAMMING','DATABASE MANAGEMENT SYSTEM','FOUNDATIONS OF MATHEMATICS','LINUX FUNDAMENTAL WITH NETWORKING',],
#             'Practical_subjects': ['PYTHON PROGRAMMING LAB', 'JAVA PROGRAMMING LAB']
#         },

#         'Sem-3': {
#             'Theory_subjects': ['ADVANCED DATABASE MANAGEMENT SYSTEM', 'WEB TECHNOLOGIES DEVELOPMENT USING PHP', 'DEVOPS', 'DESIGN AND ANALYSIS OF ALGORITHMS', 'ENTREPRENEURSHIP','HUMAN VALUES PROFESSIONAL ETHICS','IOS APPLICATION DEVELOPMENT','TESTING AND AUTOMATION REST API','WEB TECHNOLOGIES DEVELOPMENT USING SPRING','BLOCKCHAIN TECHNOLOGY-II','BIG DATA ANALYTICS-II','CLOUD COMPUTING-II','DATA SCIENCE-II','FUNDAMENTAL OF INFORMATION SYSTEMS AUDIT','IOT  ADVANCED','MACHINE LEARNING-II','MOBILE TESTING AUTOMATION'],
#             'Practical_subjects':['SYSTEM DEVELOPMENT PROJECT - I','DATABASE LAB', 'PROGRAMMING LAB']
#         }
#     },
#     'BCA': {
#         'Sem-1': {
#             'Theory_subjects': ['LOGIC DEVELOPMENT WITH PROGRAMMING-I','OFFICE AUTOMATION TOOLS','BASIC WEB PROGRAMMING-I','COMPUTER ORGANIZATION AND ARCHITECTURE','LANGUAGE AND COMMUNICATION SKILLS - I'],
#             'Practical_subjects': ['AUTOMATION TOOLS LAB', 'COMMUNICATION LAB']
#         },
#         'Sem-3': {
#             'Theory_subjects': ['OBJECT ORIENTED CONCEPTS AND PROGRAMMING','ADVANCE DATABASE MANAGEMENT','COMPUTER NETWORK','DATA AND FILE STRUCTURE','DATABASE MANAGEMENT SYSTEM','SOFTWARE ENGINEERING','ENVIRONMENT AND DISASTER MANAGEMENT','SYSTEM ANALYSIS AND DESIGN','SOFT SKILLS','NETWORKING-I'],
#             'Practical_subjects': ['ADVANCE DATABASE LAB', 'NETWORKING LAN', 'SOFTSKILLS LAB']
#         },
#         'Sem-5': {
#             'Theory_subjects': ['ADVANCED WEB TECHNOLOGY','OPERATING SYSTEM','E-SECURITY & CYBER LAW','INFORMATION SECURITY','FUNDAMENTALS OF ANDROID DEVELOPMENT','CYBER SECURITY'],
#             'Practical_subjects': ['WEB TECH LAB', 'SYSTEM DEVELOPMENT PROJECT-I']
#         }
#     },
#     'Bsc': {
#         'Sem-1': {
#             'Theory_subjects': ['INTRODUCTION TO PROGRAMMING-I','OFFICE AUTOMATION TOOLS','WEB DESIGNING-1','INFORMATION TECHNOLOGY','FUNDAMENTAL OF MATHEMATICS','LANGUAGE AND COMMUNICATION SKILLS - I'],
#             'Practical_subjects': ['PROGRAMMING LAB', 'AUTOMATION TOOLS LAB']
#         },
#         'Sem-3': {
#             'Theory_subjects': ['DATA STRUCTURE','OBJECT ORIENTED CONCEPTS AND PROGRAMMING','DATABASE MANAGEMENT SYSTEM','SYSTEM ANALYSIS AND DESIGN','OPERATION RESEARCH','ENVIRONMENT DISASTER MANAGEMENT'],
#             'Practical_subjects': ['OOP LAB', 'RESEARCH LAB']
#         },
#         'Sem-5': {
#             'Theory_subjects':['WEB TECHNOLOGY- I','BASIC WEB PROGRAMMING AND DESIGNING','OPERATING SYSTEM','NETWORK TECHNOLOGY - II','BUSINESS ANALYSIS AND ANALYTICS'],
#             'Practical_subjects': ['INDUSTRIAL PROJECT - I', 'PROGRAMMING LAB']
#         }
#     }
# }

# teachers = {
#     'MBA': ['H.K. Patel', 'P.J. Jha', 'G.S. Desai', 'A.R. Rao', 'P.K. Solanki','J.P. Jaganiya','H.K. Shrivastav'],
#     'MCA': ['R.S. Prajapati', 'V.P. Paul', 'S.K. Mishra', 'D.G. Patel', 'S.I. Shah','I.M.Khare', 'P.K. Patel'],
#     'BCA': ['A.N. Murmu', 'H.S. Solanki', 'J.V. Raval','P.H. Chaudhri', 'R.S. Chavod', 'K.T. Iyer', 'L.K. Mehta', 'S.T Prajapati', 'A.P. Pandey', 'T.P. Agrawal'],
#     'Bsc': ['K.S. Yadav', 'M.N. Shah', 'H.H. Khatri', 'H.S. Vyas', 'D.K. Desai', 'H.H. Rathod', 'P.M. Patel', 'A.M. Joshi', 'A.T. Bhide', 'T.Y. Gupta', 'P.R. Patel']
# }

# subject_with_teacher = {
#     'PRINCIPLES OF MANAGEMENT' : ['H.K. Patel', 'P.J. Jha'],
#     'MANAGERIAL ACCOUNTING' : ['J.P. Jaganiya','H.K. Shrivastav'],
#     'PERSONALITY GROWTH LAB' : ['A.R. Rao', 'P.K. Solanki'],
#     'COMPUTER FUNDAMENTALS AND NETWORKING' : [ 'S.K. Mishra', 'D.G. Patel', 'S.I. Shah'],
#     'PYTHON PROGRAMMING LAB' : ['I.M.Khare', 'P.K. Patel'],
#     'OFFICE AUTOMATION TOOLS' : ['H.S. Solanki', 'J.V. Raval'],
#     'COMPUTER NETWORK' : ['S.T Prajapati', 'A.P. Pandey', 'T.P. Agrawal'],
#     'INFORMATION SECURITY' : ['K.T. Iyer', 'L.K. Mehta', 'S.T Prajapati'],
#     'WEB DESIGNING-1' : ['M.N. Shah', 'H.H. Khatri'],
#     'RESEARCH LAB' : ['D.K. Desai', 'H.H. Rathod'],
#     'OPERATING SYSTEM' : ['A.M. Joshi', 'A.T. Bhide']
# }

# recess_times = {
#     'MBA': (time(12, 0), time(12, 30)),
#     'MCA': (time(12, 0), time(12, 30)),
#     'BCA': (time(14, 0), time(14, 30)),
#     'Bsc': (time(11, 30), time(12, 0))
# }

# # Session lengths are different for Theory and Practical
# session_lengths = {
#     'MBA': {
#         'Theory': timedelta(hours=1),
#         'Practical': timedelta(hours=2)
#     },
#     'MCA': {
#         'Theory': timedelta(hours=1),
#         'Practical': timedelta(hours=2)
#     },
#     'BCA':{
#         'Theory': timedelta(minutes=45),
#         'Practical': timedelta(minutes=90)
#     },
#     'Bsc':{
#         'Theory': timedelta(minutes=45),
#         'Practical': timedelta(minutes=90)
#     }
# }

# time_slots = {
#     'MBA': (time(9, 0), time(16, 0)),
#     'MCA': (time(9, 0), time(16, 0)),
#     'BCA': (time(11, 0), time(17, 0)),
#     'Bsc': (time(7, 0), time(14, 0))
# }

# # Function to increment time
# def increment_time(current_time, delta):
#     try:
#         new_time = (datetime.combine(datetime.today(), current_time) + delta).time()
#         return new_time
#     except Exception as e:
#         logging.info("Error occured in increment_time")
#         raise CustomException(e, sys)


# # Helper function to create timetable
# def create_timetable():
#     timetable = {}

#     session_types = 70 * ['Theory'] + 30 * ['Practical']
    

#     try:

#         for course in courses:
#             for semester in courses[course]:
#                 timetable[f"{course}-{semester}"] = {'time_slots': []}
#                 for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']:
#                     logging.info(f"Creating timetable for {course}-{semester} on {day}")
#                     timetable[f"{course}-{semester}"][day] = []
#                     current_time = time_slots[course][0]
#                     end_time = time_slots[course][1]
#                     recess_start, recess_end = recess_times[course]


#                     # Create time slots
#                     time_slots_list = []
#                     while current_time < end_time:
#                         try: 
#                             next_time = increment_time(current_time, session_lengths[course]['Theory'])  # For one-hour slot
#                             time_slots_list.append(f"{current_time.strftime('%H:%M')} - {next_time.strftime('%H:%M')}")
#                             current_time = next_time  # Move current time to next slot
#                             if current_time == recess_start:
#                                 time_slots_list.append(f"{recess_start.strftime('%H:%M')} - {recess_end.strftime('%H:%M')}")
#                                 current_time = increment_time(current_time, timedelta(minutes=30))  # Recess for 30 minutes
#                         except Exception as e:
#                                 logging.info(f"Error in creating time slots for {course}-{semester} on {day}")
#                                 raise CustomException(e, sys)


#                     timetable[f"{course}-{semester}"]['time_slots'] = time_slots_list

#                     # Reset current_time to the start of the day
#                     current_time = time_slots[course][0]

#                     while current_time < end_time:
#                         try:
#                             if current_time == recess_start:
#                                 # Adding recess to timetable
#                                 timetable[f"{course}-{semester}"][day].append('Recess')
#                                 current_time = increment_time(current_time, timedelta(minutes=30))  # Recess for 30 minutes
#                             else:

#                                 #teacher = random.choice(teachers[course])

#                                 # Check time left for practical sessions
#                                 time_to_recess = (datetime.combine(datetime.today(), recess_start) - datetime.combine(datetime.today(), current_time)).seconds / 3600
#                                 time_to_end = (datetime.combine(datetime.today(), end_time) - datetime.combine(datetime.today(), current_time)).seconds / 3600
                                
#                                 if time_to_recess >= 2 and time_to_end >= 2:
#                                     # Randomly choose session type (Theory or Practical)
#                                     session_type = random.choice(session_types)
#                                 else:
#                                     # Not enough time for Practical, choose Theory
#                                     session_type = 'Theory'
                                
#                                 next_time = increment_time(current_time, session_lengths[course]['Theory'])  # Write for one-hour slot first
                                
#                                 # timetable[f"{course}-{semester}"][day].append(
#                                 #     f"{subject} ({teacher}) [{session_type}]"

#                                 if session_type == 'Theory':
#                                     subject = random.choice(courses[course][semester]['Theory_subjects'])
#                                     if subject in subject_with_teacher:
#                                         teacher = random.choice(subject_with_teacher[subject])
#                                     else:
#                                         teacher = random.choice(teachers[course])
#                                     timetable[f"{course}-{semester}"][day].append(
#                                         f"{subject}\n({teacher})\n[{session_type}]")
#                                 else:
#                                     subject = random.choice(courses[course][semester]['Practical_subjects'])
#                                     if subject in subject_with_teacher:
#                                         teacher = random.choice(subject_with_teacher[subject])
#                                     else:
#                                         teacher = random.choice(teachers[course])
#                                     timetable[f"{course}-{semester}"][day].append(
#                                         f"{subject}\n({teacher})\n[{session_type}]")
                                    
                                
#                                 current_time = next_time  # Move current time to next slot
                                
#                                 # If session is Practical (2 hours), fill the second hour slot with the same Practical info
#                                 if session_type == 'Practical':
#                                     next_time = increment_time(current_time, session_lengths[course]['Theory'])  # Advance another hour
#                                     timetable[f"{course}-{semester}"][day].append(
#                                         f"{subject}\n({teacher})\n[{session_type}]"
#                                     )
                                   
#                                     current_time = next_time  # Move current time to next available slot

#                         except Exception as e:
#                                 logging.info(f"Error while assigning session for {course}-{semester} on {day}")
#                                 raise CustomException(e, sys)
#     except Exception as e:
#         logging.info("Failed to create timetable")
#         raise CustomException(e, sys)

#     return timetable


# @app.route('/')
# def index():
#     try:
#         timetable = create_timetable()
#         return render_template('timetable.html', timetable=timetable)
#     except Exception as e:
#         logging.info('An error occurred while generating the timetable.')
#         raise CustomException(e,sys)

# if __name__ == '__main__':
#     app.run(debug=True)

































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

    return courses, teachers, credit_points, time_slots

# Path to your Excel file
file_path = 'C:\\Users\\HANI PATEL\\Desktop\\timetable excel.xlsx'

# Load data from Excel
courses, teachers, credit_points, time_slots = load_data_from_excel(file_path)

# Function to increment time
def increment_time(current_time, delta):
    try:
        new_time = (datetime.combine(datetime.today(), current_time) + delta).time()
        return new_time
    except Exception as e:
        logging.info("Error occurred in increment_time")
        raise CustomException(e, sys)

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

                        # Assign subject and teacher
                        if subject_idx >= len(weighted_subjects):
                            subject_idx = 0  # Reset index if we run out of subjects
                            logging.info('subject index reset second time')

                        subject = weighted_subjects[subject_idx]
                        # teacher = random.choice(teachers[course])
                        session_length = theory_length if subject in courses[course][semester]['Theory_subjects'] else practical_length
                        next_time = increment_time(current_time, timedelta(minutes=session_length))
                    

                        # If practical subject, allocate additional consecutive slots as required
                        while subject in courses[course][semester]['Practical_subjects'] and session_length > theory_length:
                            timetable[f"{course}-{semester}"][day].append(f"{subject}")
                            session_length -= theory_length
                            current_time = increment_time(current_time, timedelta(minutes=theory_length))
                            if current_time >= end_time_dt or current_time == recess_start_dt:
                                continue
                        else:
                            timetable[f"{course}-{semester}"][day].append(f"{subject}")
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

# @app.route('/<course_name>')
# def course_timetable(course_name):
#     try:
#         if course_name in timetable_data:
#             course_timetable = timetable_data[course_name]
#             return render_template('timetable.html', course_name=course_name, timetable=course_timetable)
#         else:
#             return f"Timetable for {course_name} not found.", 404
#     except Exception as e:
#         logging.info(f"Error displaying timetable for {course_name}")
#         raise CustomException(e, sys)

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

# @app.route('/')
# def index():
#     try:
#         timetable = create_timetable()
#         return render_template('timetable.html', timetable=timetable)
#     except Exception as e:
#         logging.info('An error occurred while generating the timetable.')
#         raise CustomException(e, sys)

# if __name__ == '__main__':
#     app.run(debug=True)





