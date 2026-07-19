## Final GitHub Folder Structure

```text
AI-Attendance-System/
│
├── app.py
├── capture.py
├── config.py
├── dashboard.py
├── database.py
├── recognize.py
├── register.py
├── train.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── database/
│   └── attendance.db   (optional - ya empty database)
│
├── dataset/
│   └── .gitkeep
│
├── models/
│   ├── trainer.yml
│   └── labels.txt
│
├── pages/
│   ├── login.py
│   ├── add_student.py
│   ├── edit_student.py
│   ├── attendance.py
│   └── ...
│
├── assets/
│   ├── logo.png
│   └── banner.png
│
└── screenshots/
    ├── login.png
    ├── dashboard.png
    ├── register.png
    └── attendance.png
```

---

## `.gitignore`

```gitignore
# Virtual Environment
venv/
env/

# Python Cache
__pycache__/
*.py[cod]
*.pyo

# IDE
.vscode/
.idea/

# OS Files
.DS_Store
Thumbs.db

# Logs
*.log

# Streamlit
.streamlit/secrets.toml

# Face Dataset (Private)
dataset/*

# Database (Optional)
database/attendance.db
```


---

## Git Commands

```bash
git init
git add .
git commit -m "Initial Commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/AI-Attendance-System.git
git push -u origin main
```

---


* 🎯 Face Recognition Attendance
* 📷 OpenCV + LBPH Face Recognizer
* 🗄 SQLite Database
* 🌐 Streamlit Dashboard
* 📊 Attendance Analytics
* 👨‍🎓 Student Management
* 📸 Face Registration
* 📈 Real-time Attendance Tracking

---
* Login Page
* Dashboard
* Student Registration
* Attendance Report
* Face Recognition Window

---Login Page
Username: Admin
Password: Admin123 Or 12345
