import csv
from datetime import datetime, date
today = date.today().strftime("%Y-%m-%d")


def find_student_data(student_id):
    with open('data/student.csv', 'r') as file:
        reader = csv.DictReader(file)
        data = list()
        student = 'Not Found'
        for row in reader:
            if row['student_id'] == student_id:
                student = row
        return student

def check_daily_attendance(student_id):
    with open('data/daily_attendance.csv', 'r') as file:
        reader = csv.DictReader(file)
        find = False
        for row in reader:
            if row['student_id'] == student_id:
                find = True
        return find

def write_daily_attendance(student,status,minutes_late):
    with open('data/daily_attendance.csv', 'a', newline='') as csvfile:
        fieldnames = ['date', 'student_id', 'name', 'class', 'attendance_status', 'minutes_late']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        data ={  'date': date.today().strftime("%Y-%m-%d"),
                 'student_id': student['student_id'],
                 'name': student['name'],
                 'class': student['class'],
                 'attendance_status': status,
                 'minutes_late': minutes_late}

        if csvfile.tell() == 0:
            writer.writeheader()
        try:
            writer.writerow(data)
        except:
            None

def read_student_data():
    with open('data/student.csv', 'r') as file:
        reader = csv.DictReader(file)
        data = dict()
        for row in reader:
            data[row['student_id']] = row
    return data

def read_daily_attendance_log():
    with open('data/daily_attendance.csv', 'r') as file:
        reader = csv.DictReader(file)
        data = dict()
        for row in reader:
            if row['date'] == date.today().strftime("%Y-%m-%d"):
                data[row['student_id']] = row
        return data

def clear_daily_attendace():
    with open('data/daily_attendance.csv', 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
        try:
            if data[0]['date'] < date.today().strftime("%Y-%m-%d"):
                with open('data/daily_attendance.csv', 'w', newline='') as csvfile:
                    fieldnames = ['date', 'student_id', 'name', 'class', 'attendance_status', 'minutes_late']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
        except:
            None

def daily_status():
    student_data = read_student_data()
    attendace_log = read_daily_attendance_log()

    daily_status = list()
    for student in student_data:
        if student not in attendace_log:
            daily_status.append({
                'date':date.today().strftime("%Y-%m-%d"),
                'student_id':student_data[student]['student_id'],
                'name':student_data[student]['name'],
                'class':student_data[student]['class'],
                'attendance_status':'abstain',
                'minutes_late':0})
        else:
            daily_status.append({
                'date':date.today().strftime("%Y-%m-%d"),
                'student_id':attendace_log[student]['student_id'],
                'name':attendace_log[student]['name'],
                'class':attendace_log[student]['class'],
                'attendance_status':attendace_log[student]['attendance_status'],
                'minutes_late':attendace_log[student]['minutes_late']})

        with open(f'data/daily_report/{today}.csv', 'w', newline='') as csvfile:
                    fieldnames = ['date', 'student_id', 'name', 'class', 'attendance_status', 'minutes_late']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()

                    for data in daily_status:
                        writer.writerow(data)
    return daily_status

class StudentAttendance:
    def attendance(self,student_id):
        clear_daily_attendace()
        while True:
            status = None
            student = find_student_data(student_id)
            if student =='Not Found':
                msg = 'Error! Student ID Not Found'
                return  msg, status

            check_daily_attendcae = check_daily_attendance(student['student_id'])

            if check_daily_attendcae == True:
                msg = 'Error! Today Attendance Already Recorded'
                return msg, status

            student_schedule = datetime.strptime(student['schedule'], "%H:%M:%S").time()
            if datetime.now().time() < student_schedule:
                status = 'on time'
                minutes_late = 0
                msg = f"""Name : {student['name']}, Level : {student['level']}, Class : {student['class']}, Status : {status}"""

            else:
                student_schedule = datetime.combine(datetime(1, 1, 1), student_schedule)
                current_datetime = datetime.combine(datetime(1, 1, 1), datetime.now().time())
                status = 'late'
                minutes_late = round((current_datetime - student_schedule).total_seconds() / 60)
                msg = f"""Name : {student['name']}, Level : {student['level']}, Class : {student['class']}, Status : {status}, Minutes Late : {minutes_late}"""

            write_daily_attendance(student,status, minutes_late)

            return  msg, status

    def check_today_status(self):
        return daily_status()

