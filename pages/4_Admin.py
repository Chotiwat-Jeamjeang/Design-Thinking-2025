import streamlit as st
from booking import get_all_bookings

st.title("⚙️ Admin Panel")

if st.session_state.role != "admin":
    st.error("ไม่มีสิทธิ์เข้าถึง")
    st.stop()

data = get_all_bookings()

for username, court, date, time in data:
    st.write(f"{username} | สนาม {court} | {date} | {time}")
