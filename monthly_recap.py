
from collections import defaultdict
from datetime import datetime
import csv
import glob

def monthly_recap():
    # List of CSV files
    file_pattern = "data/daily_report/*.csv"  # Update the path to your CSV files

    # Open the output CSV file for writing
    with open("data/monthly_recap.csv", mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        
        # Flag to check if the header has been written
        header_written = False

        # Iterate over all CSV files
        for filename in glob.glob(file_pattern):
            with open(filename, mode='r') as infile:
                reader = csv.reader(infile)
                header = next(reader)  # Read the header

                if not header_written:
                    writer.writerow(header)  # Write header to output file
                    header_written = True

                for row in reader:
                    writer.writerow(row)  # Write rows from each file

    with open('data/monthly_recap.csv', 'r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            
    # Initialize a defaultdict to hold monthly attendance summary for each student
    monthly_report = defaultdict(lambda: {'classes': 0, 'name of students': 0, 'total days attended': 0, 'number of time late': 0, 'number of absences': 0, 'total minutes (late)': 0})

    # Iterate over the data to process attendance
    for entry in data:
        student_class = entry['class']
        student_name = entry['name']
        attendance_status = entry['attendance_status']
        minutes_late = int(entry['minutes_late'])  # Convert minutes late to an integer for aggregation
        date = entry['date']
        
        # Extract year and month from the date
        year_month = datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m")  # Format as 'YYYY-MM'
        
        # Update the count and minutes late for the student in the specific month
        if attendance_status == 'late':
            monthly_report[(student_class, student_name, year_month)]['total days attended'] += 1
            monthly_report[(student_class, student_name, year_month)]['number of time late'] += 1
            monthly_report[(student_class, student_name, year_month)]['total minutes (late)'] += minutes_late
        elif attendance_status == 'abstain':
            monthly_report[(student_class, student_name, year_month)]['number of absences'] += 1
        elif attendance_status == 'on time':
            monthly_report[(student_class, student_name, year_month)]['total days attended'] += 1
            monthly_report[(student_class, student_name, year_month)]['on_time_count'] += 1

    data_final = list()
    # Print the summary for each student, grouped by month
    for (student_class, student_name, year_month), report in monthly_report.items():
        data_final.append({
                        'month': year_month,
                        'classes':student_class,
                        'name of student':student_name,
                        'total days attended':report['total days attended'],
                        'number of time late':report['number of time late'],
                        'number of absences':report['number of absences'],
                        'total minutes (late)':report['total minutes (late)']
                                                    }
                        )

    return data_final