import tkinter as tk
from tkinter import ttk

from main import StudentAttendance
sa = StudentAttendance()

from apps_daily_status import refresh_treeview,tree_daily_status
from apps_monthly_recap import tree_monthly_recap


if __name__ == '__main__':
    def submit_id():
        student_id = id_entry.get()
        msg, status = sa.attendance(student_id)  # Replace this with your actual function

        # Set label text and color based on the message
        if status == 'late':
            msg_label.config(text=msg, fg="red")
        elif status == 'on time':
            msg_label.config(text=msg, fg="green")
        else:
            msg_label.config(text=msg, fg="black")  # Default color for other messages

        # Refresh the Treeview with updated data
        refresh_treeview(tree)

    def open_popup():
        # Create a new Toplevel window (popup)
        popup_window = tk.Toplevel(window)
        popup_window.title("Monthly Recap")
        popup_window.geometry("800x450")

        #tree
        tree2 = tree_monthly_recap(popup_window)
        tree2.pack(side='top', anchor='nw', pady=10)

        # Add a button to close the popup window
        close_button = tk.Button(popup_window, text="Close", command=popup_window.destroy)
        close_button.pack(side='top', anchor='nw', pady=5)


    # Create the main window
    window = tk.Tk()
    window.title("Student Attendance")

    window.geometry('600x450')

    # Create a label and entry field for the ID
    id_label = tk.Label(window, text="Student ID")
    id_label.pack(side='top', anchor='nw', pady=5)
    id_entry = tk.Entry(window)
    id_entry.pack(side='top', anchor='nw', pady=5)

    # Create a submit button
    submit_button = tk.Button(window, text="Submit", command=submit_id)
    submit_button.pack(side='top', anchor='nw', pady=5)

    # Create a label to display the message
    msg_label = tk.Label(window, text="", wraplength=500, anchor='nw', justify='left')
    msg_label.pack(side='top', anchor='nw', pady=10)

    #daily status
    tree= tree_daily_status(window)
    tree.pack(side='top', anchor='nw', pady=10)

    # Add a button to the main window
    open_button = tk.Button(window, text="Check Montly Recap", command=open_popup)
    open_button.pack(side='top', anchor='nw', pady=10)

    window.mainloop()


