import streamlit as st
from booking import get_all_bookings
from database import get_connection
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

st.title("📊 ดูสถานะสนาม")

# กันคนยังไม่ login
if not st.session_state.get("logged_in"):
    st.warning("กรุณาเข้าสู่ระบบ")
    st.stop()

selected_date = st.date_input("เลือกวันที่", value=date.today())

# เวลาทั้งหมดที่เปิดให้จอง
time_slots = ["17:00", "18:00", "19:00", "20:00"]
courts = [1, 2, 3, 4]

conn = get_connection()
c = conn.cursor()

st.subheader(f"สถานะวันที่ {selected_date}")

for court in courts:
    st.markdown(f"### 🏸 สนาม {court}")
    
    cols = st.columns(len(time_slots))
    
    for i, time in enumerate(time_slots):
        c.execute(
            "SELECT * FROM bookings WHERE court=? AND date=? AND time=?",
            (court, str(selected_date), time)
        )
        booking = c.fetchone()
        
        if booking:
            cols[i].error(f"{time}\n❌ จองแล้ว")
        else:
            cols[i].success(f"{time}\n✅ ว่าง")

conn.close()
