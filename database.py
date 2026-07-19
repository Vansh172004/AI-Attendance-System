import sqlite3
import os

os.makedirs("database", exist_ok=True)

conn = sqlite3.connect("database/attendance.db")
cursor = conn.cursor()

# Students Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    student_id TEXT PRIMARY KEY,
    name TEXT,
    course TEXT,
    section TEXT
)
""")

# Attendance Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT,
    name TEXT,
    date TEXT,
    time TEXT,
    status TEXT
)
""")

# Admin Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS admin(
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL
)
""")

# Default Admin
cursor.execute("""
INSERT OR IGNORE INTO admin(username, password)
VALUES (?, ?)
""", ("admin", "admin123"))

conn.commit()
conn.close()

print("Database Created Successfully")