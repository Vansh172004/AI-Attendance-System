import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
import cv2
import numpy as np

from recognize import recognize_face


# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="AI Smart Attendance System",
    page_icon="🎓",
    layout="wide"
)



# =========================
# LOGIN CHECK
# =========================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


if not st.session_state.logged_in:
    st.warning("Please Login First")
    st.stop()



# =========================
# LOGOUT
# =========================

if st.button("🚪 Logout"):

    st.session_state.logged_in = False
    st.rerun()



# =========================
# TITLE
# =========================

st.title("🎓 AI Smart Attendance Dashboard")

st.subheader("📷 Face Recognition")



# =========================
# CAMERA
# =========================

img_file = st.camera_input(
    "Click Face Photo"
)



if img_file is not None:


    try:


        bytes_data = img_file.getvalue()


        img_array = np.frombuffer(
            bytes_data,
            np.uint8
        )


        frame = cv2.imdecode(
            img_array,
            cv2.IMREAD_COLOR
        )



        if frame is None:

            st.error(
                "Image Decode Failed"
            )


        else:


            st.success(
                "Photo Captured"
            )


            # Original Image

            rgb_original = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2RGB
            )


            st.image(
                rgb_original,
                caption="Original Photo",
                width=400
            )



            # Face Recognition

            result = recognize_face(
                frame
            )



            result_rgb = cv2.cvtColor(
                result,
                cv2.COLOR_BGR2RGB
            )



            st.image(
                result_rgb,
                caption="Recognition Result",
                width=400
            )



    except Exception as e:


        st.error(
            "Recognition Error"
        )

        st.exception(e)




# =========================
# DATABASE
# =========================

try:


    conn = sqlite3.connect(
        "database/attendance.db"
    )


    students = pd.read_sql_query(
        "SELECT * FROM students",
        conn
    )


    attendance = pd.read_sql_query(
        "SELECT * FROM attendance",
        conn
    )


    conn.close()



except Exception as e:

    st.error(
        "Database Error"
    )

    st.exception(e)

    st.stop()




# =========================
# CARDS
# =========================

st.divider()


col1,col2 = st.columns(2)


with col1:

    st.metric(
        "👨 Total Students",
        len(students)
    )


with col2:

    st.metric(
        "✅ Total Attendance",
        len(attendance)
    )




# =========================
# STUDENTS
# =========================

st.subheader(
    "👨‍🎓 Students"
)


st.dataframe(
    students,
    use_container_width=True
)



# =========================
# ATTENDANCE
# =========================

st.subheader(
    "📋 Attendance Records"
)


st.dataframe(
    attendance,
    use_container_width=True
)




# =========================
# CHART
# =========================

if not attendance.empty:


    data = attendance.groupby(
        "status"
    ).size().reset_index(
        name="Count"
    )


    fig = px.pie(
        data,
        values="Count",
        names="status",
        title="Attendance"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )