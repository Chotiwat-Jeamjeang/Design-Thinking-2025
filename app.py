import requests
from PIL import Image
from io import BytesIO
import streamlit as st
from database import init_db
from auth import login, register
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

init_db()

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get("https://dsq.up.ac.th/shapen/images/logo-dsq-color.png", headers=headers)
img = Image.open(BytesIO(response.content))

st.image(img, width=885)

st.set_page_config(page_title="สนามแบดมินตัน", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.title("🏸 ระบบจองสนามแบดมินตัน")

if not st.session_state.logged_in:

    menu = st.radio("เลือกเมนู", ["เข้าสู่ระบบ", "สมัครสมาชิก"])

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if menu == "สมัครสมาชิก":
        if st.button("สมัครสมาชิก"):
            register(username, password)

    else:
        if st.button("เข้าสู่ระบบ"):
            if login(username, password):
                st.success("เข้าสู่ระบบสำเร็จ")
                st.rerun()
            else:
                st.error("Username หรือ Password ไม่ถูกต้อง")

else:
    st.success(f"สวัสดี {st.session_state.username}")
    st.page_link("pages/1_จองสนาม.py", label="🏟️ จองสนาม")
    st.page_link("pages/2_ดูสถานะ.py", label="📊 ดูสถานะสนาม")
    st.page_link("pages/3_ประวัติ.py", label="📜 ประวัติการจอง")

    if st.session_state.role == "admin":
        st.page_link("pages/4_Admin.py", label="⚙️ Admin Panel")

    if st.button("ออกจากระบบ"):
        st.session_state.clear()
        st.rerun()
