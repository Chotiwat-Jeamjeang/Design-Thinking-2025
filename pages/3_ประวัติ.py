import streamlit as st
from booking import get_bookings_by_user
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
st.title("📜 ประวัติการจอง")

data = get_bookings_by_user(st.session_state.user_id)

for court, date, time in data:
    st.write(f"สนาม {court} | {date} | {time}")
