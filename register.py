import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database Connection
conn = sqlite3.connect("database/attendance.db")
cursor = conn.cursor()

# Save Student
def save_student():
    student_id = entry_id.get()
    name = entry_name.get()
    course = entry_course.get()
    section = entry_section.get()

    if student_id == "" or name == "" or course == "" or section == "":
        messagebox.showerror("Error", "Please Fill All Fields")
        return

    try:
        cursor.execute("""
        INSERT INTO students(student_id,name,course,section)
        VALUES(?,?,?,?)
        """,(student_id,name,course,section))

        conn.commit()

        messagebox.showinfo("Success","Student Registered Successfully")

        entry_id.delete(0,tk.END)
        entry_name.delete(0,tk.END)
        entry_course.delete(0,tk.END)
        entry_section.delete(0,tk.END)

    except:
        messagebox.showerror("Error","Student ID Already Exists")

# GUI
root = tk.Tk()
root.title("Student Registration")
root.geometry("400x350")
root.resizable(False,False)

tk.Label(root,text="Student ID").pack(pady=5)
entry_id=tk.Entry(root,width=35)
entry_id.pack()

tk.Label(root,text="Name").pack(pady=5)
entry_name=tk.Entry(root,width=35)
entry_name.pack()

tk.Label(root,text="Course").pack(pady=5)
entry_course=tk.Entry(root,width=35)
entry_course.pack()

tk.Label(root,text="Section").pack(pady=5)
entry_section=tk.Entry(root,width=35)
entry_section.pack()

tk.Button(root,text="Register Student",
command=save_student,
bg="green",
fg="white",
width=20).pack(pady=20)

root.mainloop()

conn.close()