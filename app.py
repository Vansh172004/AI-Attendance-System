import streamlit as st

from login import login_page


st.set_page_config(
    page_title="AI Smart Attendance System",
    page_icon="🎓",
    layout="wide"
)


# Session
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False



if st.session_state.logged_in:

    import dashboard


else:

    login_page()