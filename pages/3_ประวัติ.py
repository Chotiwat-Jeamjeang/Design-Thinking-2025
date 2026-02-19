import streamlit as st
from booking import get_bookings_by_user

st.title("📜 ประวัติการจอง")

data = get_bookings_by_user(st.session_state.user_id)

for court, date, time in data:
    st.write(f"สนาม {court} | {date} | {time}")
