import tkinter as tk
from tkinter import ttk
from main import StudentAttendance
sa = StudentAttendance()

def refresh_treeview(tree):
    # Clear all rows in the Treeview
    for row in tree.get_children():
        tree.delete(row)

    # Fetch updated data
    updated_data = sa.check_today_status()

    # Insert updated data into the Treeview
    for item in updated_data:
        if item["attendance_status"] == 'late':
            tags = ('late',)
        elif item["attendance_status"] == 'on time':
            tags = ('on time',)
        else:
            tags = ()  # No tag for other statuses

        tree.insert(
            "",
            tk.END,
            values=(item["date"], item["student_id"], item["name"], item["class"], item["attendance_status"],
                    item["minutes_late"]),
            tags=tags
        )

def tree_daily_status(window):
    tree = ttk.Treeview(window)

    # Define columns
    columns = ("date", "student_id", "name", "class", "attendance_status", "minutes_late")
    tree['columns'] = columns

    # Format our columns
    tree.column("#0", width=0, stretch=tk.NO)  # Don't display the first column
    tree.column("date", anchor=tk.W, width=80)
    tree.column("student_id", anchor=tk.W, width=120)
    tree.column("name", anchor=tk.W, width=80)
    tree.column("class", anchor=tk.W, width=80)
    tree.column("attendance_status", anchor=tk.W, width=120)
    tree.column("minutes_late", anchor=tk.W, width=80)

    # Create headings
    tree.heading("#0", text="", anchor=tk.W)
    tree.heading("date", text="Date", anchor=tk.W)
    tree.heading("student_id", text="Student ID", anchor=tk.W)
    tree.heading("name", text="Name", anchor=tk.W)
    tree.heading("class", text="Class", anchor=tk.W)
    tree.heading("attendance_status", text="Attendance Status", anchor=tk.W)
    tree.heading("minutes_late", text="Minutes Late", anchor=tk.W)

    # Define tags for late and on time
    tree.tag_configure('late', foreground='red')
    tree.tag_configure('on time', foreground='green')

    # Initial population of the Treeview
    refresh_treeview(tree)

    return tree
