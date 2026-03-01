import streamlit as st
from booking import get_all_bookings
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
        background-color: #265e20;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("⚙️ Admin Panel")

if st.session_state.role != "admin":
    st.error("ไม่มีสิทธิ์เข้าถึง")
    st.stop()

data = get_all_bookings()

for username, court, date, time in data:
    st.write(f"{username} | สนาม {court} | {date} | {time}")
