import streamlit as st
from booking import create_booking
from datetime import date
import requests
from PIL import Image
from io import BytesIO

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(
    "https://dsq.up.ac.th/shapen/images/logo-dsq-color.png",
    headers=headers
)
img = Image.open(BytesIO(response.content))

st.image(img, width=885)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #af94d1;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🏟️ จองสนาม")

if not st.session_state.get("logged_in"):
    st.warning("กรุณาเข้าสู่ระบบ")
    st.stop()

court = st.selectbox("เลือกสนาม", [1, 2, 3, 4])
booking_date = st.date_input("เลือกวันที่", min_value=date.today())
booking_time = st.selectbox("เลือกเวลา", ["17:00", "18:00", "19:00", "20:00"])

if st.button("ยืนยันการจอง"):
    success = create_booking(
        st.session_state.user_id,
        court,
        str(booking_date),
        booking_time
    )
    if success:
        st.success("จองสำเร็จ 🎉")
    else:
        st.error("เวลานี้ถูกจองแล้ว")
