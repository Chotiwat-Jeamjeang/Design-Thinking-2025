import streamlit as st
import pandas as pd
from database import get_connection
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

st.title("🗄️ ดูฐานข้อมูล (Admin Only)")

if st.session_state.get("role") != "admin":
    st.error("ไม่มีสิทธิ์เข้าถึง")
    st.stop()

conn = get_connection()

# ตาราง users
st.subheader("ตาราง Users")
users_df = pd.read_sql_query("SELECT * FROM users", conn)
st.dataframe(users_df)

# ตาราง bookings
st.subheader("ตาราง Bookings")
bookings_df = pd.read_sql_query("SELECT * FROM bookings", conn)
st.dataframe(bookings_df)

conn.close()
