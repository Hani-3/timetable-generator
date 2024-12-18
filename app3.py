from flask import Flask, render_template, request
import random
from datetime import time, timedelta, datetime
import sys
from src.exception import CustomException
from src.logger import logging

app = Flask(__name__)

# Helper function to increment time
def increment_time(current_time, delta):
    try:
        new_time = (datetime.combine(datetime.today(), current_time) + delta).time()
        return new_time
    except Exception as e:
        logging.info("Error occurred in increment_time")
        raise CustomException(e, sys)

courses = [
    {
        "name": "MCA",
        "url": "mca",
        "semesters": [
            {"sem_no": 1},
            {"sem_no": 3}
        ]
    },
    {
        "name": "MBA",
        "url": "mba",
        "semesters": [
            {"sem_no": 1},
            {"sem_no": 3}
        ]
    },
    {
        "name": "BCA",
        "url": "bca",
        "semesters": [
            {"sem_no": 1},
            {"sem_no": 3},
            {"sem_no": 5}
        ]
    }
]

# Route to display the form
@app.route('/')
def timetable_form():
    return render_template("form3.html", courses=courses)

# Routes to handle form submissions
@app.route('/generate-timetable/<course_url>', methods=['POST'])
def generate_timetable_route(course_url):
    return generate_timetable(course_url.upper())

# Track teacher time slots to avoid conflicts
teacher_schedule = {
    'Monday': {},
    'Tuesday': {},
    'Wednesday': {},
    'Thursday': {},
    'Friday': {},
    'Saturday': {}
}

# Function to generate the timetable for any course
def generate_timetable(course_name):
    try:
        # Get course-wide data
        teachers = request.form['teachers'].split(',')
        recess_start = request.form['recess_start']
        recess_end = request.form['recess_end']
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        theory_length = int(request.form['theory_length'])
        practical_length = int(request.form['practical_length'])
       
        # Handling semesters and multiple subject-teacher combinations
        if course_name in ['MCA', 'MBA']:
            semesters = {
                'Sem-1': {
                    'theory_subjects': request.form['theory_subjects_sem1'].split(','),
                    'practical_subjects': request.form['practical_subjects_sem1'].split(','),
                    'subject_combine': [request.form.get(f'subject_combine_sem1_{i}', '').split(',') for i in range(7)],
                    'teacher_combine': [request.form.get(f'teacher_combine_sem1_{i}', None) for i in range(7)],
                    'practical_combine': [request.form.get(f'practical_combine_sem1', '').split(',')],
                    'teacher_practical_combine': [request.form.get(f'teacher_practical_combine_sem1', None)]
                },
                'Sem-3': {
                    'theory_subjects': request.form['theory_subjects_sem3'].split(','),
                    'practical_subjects': request.form['practical_subjects_sem3'].split(','),
                    'subject_combine': [request.form.get(f'subject_combine_sem3_{i}', '').split(',') for i in range(7)],
                    'teacher_combine': [request.form.get(f'teacher_combine_sem3_{i}', None) for i in range(7)],
                    'practical_combine': [request.form.get(f'practical_combine_sem3', '').split(',')],
                    'teacher_practical_combine': [request.form.get(f'teacher_practical_combine_sem3', None)]
                }
            }

        else: 
            semesters = {
                'Sem-1': {
                    'theory_subjects': request.form['theory_subjects_sem1'].split(','),
                    'practical_subjects': request.form['practical_subjects_sem1'].split(','),
                    'subject_combine': [request.form.get(f'subject_combine_sem1_{i}', '').split(',') for i in range(7)],
                    'teacher_combine': [request.form.get(f'teacher_combine_sem1_{i}', None) for i in range(7)],
                    'practical_combine': [request.form.get(f'practical_combine_sem1', '').split(',')],
                    'teacher_practical_combine': [request.form.get(f'teacher_practical_combine_sem1', None)]
                },
                'Sem-3': {
                    'theory_subjects': request.form['theory_subjects_sem3'].split(','),
                    'practical_subjects': request.form['practical_subjects_sem3'].split(','),
                    'subject_combine': [request.form.get(f'subject_combine_sem3_{i}', '').split(',') for i in range(7)],
                    'teacher_combine': [request.form.get(f'teacher_combine_sem3_{i}', None) for i in range(7)],
                    'practical_combine': [request.form.get(f'practical_combine_sem3', '').split(',')],
                    'teacher_practical_combine': [request.form.get(f'teacher_practical_combine_sem3', None)]
                },
                'Sem-5':{
                    'theory_subjects': request.form['theory_subjects_sem5'].split(','),
                    'practical_subjects': request.form['practical_subjects_sem5'].split(','),
                    'subject_combine': [request.form.get(f'subject_combine_sem5_{i}', '').split(',') for i in range(7)],
                    'teacher_combine': [request.form.get(f'teacher_combine_sem5_{i}', None) for i in range(7)],
                    'practical_combine': [request.form.get(f'practical_combine_sem5', '').split(',')],
                    'teacher_practical_combine': [request.form.get(f'teacher_practical_combine_sem5', None)]
                }
            }

        # Debugging: Log missing subject/teacher combinations
        for sem, data in semesters.items():
            logging.info(f"Semester: {sem}")
            logging.info(f"Subject Combines: {data['subject_combine']}")
            logging.info(f"Teacher Combines: {data['teacher_combine']}")

        # Generate the timetable for all semesters
        timetable = {}
        for semester, data in semesters.items():
            timetable.update(create_timetable(
                course_name,
                semester,
                data['theory_subjects'],
                data['practical_subjects'],
                teachers,
                recess_start,
                recess_end,
                start_time,
                end_time,
                theory_length,
                practical_length,
                data['subject_combine'],
                data['teacher_combine'],
                data['practical_combine'],
                data['teacher_practical_combine']
            ))

        return render_template('timetable.html', timetable=timetable)

    except Exception as e:
        logging.info('An error occurred while generating the timetable.')
        raise CustomException(e, sys)

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

def create_timetable(course_name, semester, theory_subjects, practical_subjects, teachers, recess_start, recess_end, start_time, end_time, theory_length, practical_length, subject_combine, teacher_combine, practical_combine, teacher_practical_combine):
    timetable = {f"{course_name}-{semester}": {'time_slots': []}}

    session_types = 70 * ['Theory'] + 30 * ['Practical']

    try:
        for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']:
            logging.info(f"Creating timetable for {course_name}-{semester} on {day}")
            timetable[f"{course_name}-{semester}"][day] = []
            current_time = datetime.strptime(start_time, '%H:%M').time()
            end_time_dt = datetime.strptime(end_time, '%H:%M').time()
            recess_start_dt = datetime.strptime(recess_start, '%H:%M').time()
            recess_end_dt = datetime.strptime(recess_end, '%H:%M').time()

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
                    logging.info(f"Error in creating time slots for {course_name}-{semester} on {day}")
                    raise CustomException(e, sys)

            timetable[f"{course_name}-{semester}"]['time_slots'] = time_slots_list

            current_time = datetime.strptime(start_time, '%H:%M').time()

            while current_time < end_time_dt:
                try:
                    if current_time == recess_start_dt:
                        timetable[f"{course_name}-{semester}"][day].append('Recess')
                        current_time = recess_end_dt
                    else:
                        # Check time left for practical sessions
                        time_to_recess = (datetime.combine(datetime.today(), recess_start_dt) - datetime.combine(datetime.today(), current_time)).seconds / 3600
                        time_to_end = (datetime.combine(datetime.today(), end_time_dt) - datetime.combine(datetime.today(), current_time)).seconds / 3600

                        if time_to_recess >= 2 and time_to_end >= 2:
                            # Randomly choose session type (Theory or Practical)
                            session_type = random.choice(session_types)
                        else:
                            # Not enough time for Practical, choose Theory
                            session_type = 'Theory'
                        
                        teacher = random.choice(teachers)

                        if session_type == 'Theory':
                            
                            
                            # Check if the teacher is available for this time slot
                            if not is_teacher_available(teacher, day, current_time, increment_time(current_time, timedelta(minutes=theory_length))):
                                logging.info(f"{teacher} is already booked for {current_time} on {day}. Finding a new teacher.")
                                continue  # Skip this time slot if the teacher is booked
                                
                            
                            book_teacher(teacher, day, current_time, increment_time(current_time, timedelta(minutes=theory_length)))

                            if teacher in teacher_combine:
                                index = teacher_combine.index(teacher)
                                subject = random.choice(subject_combine[index])

                                logging.info(f"got {teacher} in teacher combine, selected subject is {subject}")

                            else:
                                subject = random.choice(theory_subjects)


                            timetable[f"{course_name}-{semester}"][day].append(
                                f"{subject}\n({teacher})\n[{session_type}]"
                            )
                        else:
                            # Check if the teacher is part of a practical combination
                            if teacher in teacher_practical_combine:
                                index = teacher_practical_combine.index(teacher)
                                subject = random.choice(practical_combine[index])

                                logging.info(f"Got {teacher} in practical teacher combine, selected subject is {subject}")
                            else:
                                teacher = random.choice(teachers)
                                subject = random.choice(practical_subjects)
                            

                            if not is_teacher_available(teacher, day, current_time, increment_time(current_time, timedelta(minutes=practical_length))):
                                logging.info(f"{teacher} is already booked for {current_time} on {day}. Finding a new teacher.")
                                continue  # Skip this time slot if the teacher is booked
                                

                            book_teacher(teacher, day, current_time, increment_time(current_time, timedelta(minutes=practical_length)))

                            timetable[f"{course_name}-{semester}"][day].append(
                                f"{subject}\n({teacher})\n[{session_type}]"
                            )

                        current_time = increment_time(current_time, timedelta(minutes=theory_length))

                        # If session is Practical (2 hours), fill the second hour slot with the same Practical info
                        if session_type == 'Practical':
                            next_time = increment_time(current_time, timedelta(minutes=theory_length))
                            timetable[f"{course_name}-{semester}"][day].append(
                                f"{subject}\n({teacher})\n[{session_type}]"
                            )
                            current_time = next_time  # Move current time to next slot

                except Exception as e:
                    logging.info(f"Error in processing sessions for {course_name}-{semester} on {day}")
                    raise CustomException(e, sys)

    except Exception as e:
        logging.info("Error occurred in create_timetable")
        raise CustomException(e, sys)
    return timetable


if __name__ == '__main__':
    app.run(debug=True)