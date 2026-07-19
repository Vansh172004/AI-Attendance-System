import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE_PATH = os.path.join(BASE_DIR, "database", "attendance.db")

DATASET_PATH = os.path.join(BASE_DIR, "dataset")

MODEL_PATH = os.path.join(BASE_DIR, "models", "face_encodings.pkl")

ATTENDANCE_PATH = os.path.join(BASE_DIR, "attendance")