import streamlit as st
import sqlite3


def login_page():

    st.title("🔐 AI Smart Attendance Login")

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )


    if st.button("Login"):


        conn = sqlite3.connect(
            "database/attendance.db"
        )

        cursor = conn.cursor()


        cursor.execute(
            """
            SELECT *
            FROM admin
            WHERE username=? AND password=?
            """,
            (
                username,
                password
            )
        )


        result = cursor.fetchone()


        conn.close()



        if result:


            st.session_state.logged_in = True

            st.success(
                "Login Successful"
            )

            st.rerun()



        else:

            st.error(
                "Invalid Login"
            )