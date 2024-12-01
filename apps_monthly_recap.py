import tkinter as tk
from tkinter import ttk
from main import StudentAttendance
from monthly_recap import monthly_recap

def tree_monthly_recap(popup_window):
    # Add a label or other widgets to the popup window
    tree2 = ttk.Treeview(popup_window)
    columns = ("month", "classes", "name of student", "total days attended", "number of time late", "number of absences","total minutes (late)")
    tree2['columns'] = columns
    # Format our columns
    tree2.column("#0", width=0, stretch=tk.NO)
    tree2.column("month", anchor=tk.W, width=80)
    tree2.column("classes", anchor=tk.W, width=80)
    tree2.column("name of student", anchor=tk.W, width=120)
    tree2.column("total days attended", anchor=tk.W, width=120)
    tree2.column("number of time late", anchor=tk.W, width=120)
    tree2.column("number of absences", anchor=tk.W, width=120)
    tree2.column("total minutes (late)", anchor=tk.W, width=120)

    # Create headings
    tree2.heading("#0", text="", anchor=tk.W)
    tree2.heading("month", text="month", anchor=tk.W)
    tree2.heading("classes", text="classes", anchor=tk.W)
    tree2.heading("name of student", text="name of student", anchor=tk.W)
    tree2.heading("total days attended", text="total days attended", anchor=tk.W)
    tree2.heading("number of time late", text="number of time late", anchor=tk.W)
    tree2.heading("number of absences", text="number of absences", anchor=tk.W)
    tree2.heading("total minutes (late)", text="total minutes (late)", anchor=tk.W)

    # Fetch updated data
    updated_data = monthly_recap()

    # Insert updated data into the Treeview
    for item in updated_data:
        tree2.insert(
            "",
            tk.END,
            values=(item["month"],
                    item["classes"],
                    item["name of student"],
                    item["total days attended"],
                    item["number of time late"],
                    item["number of absences"],
                    item["total minutes (late)"],
                    )
        )
    return tree2

