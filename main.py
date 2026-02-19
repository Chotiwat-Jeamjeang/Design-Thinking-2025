import streamlit as st

from datetime import datetime



# ตั้งค่าหน้าเว็บ

st.set_page_config(

    page_title="สนามแบดมินตัน - แออดมิ้น&นิสิต",

    page_icon="🏸",

    layout="wide",

    initial_sidebar_state="expanded"

)



# สีหลัก

YELLOW = "#FFCC00"

DARK_YELLOW = "#E6B800"

BLACK = "#000000"

WHITE = "#FFFFFF"

ACCENT = "#FF6B00"  # สีส้มสำหรับปุ่มเด่น / ล็อกอิน



# CSS

st.markdown(

    f"""

    <style>

    .stApp {{

        background: linear-gradient(135deg, {YELLOW} 0%, #FFD966 100%);

    }}



    header {{

        background-color: {YELLOW} !important;

        border-bottom: 4px solid {BLACK} !important;

    }}



    /* ล็อกอินปุ่ม ขวาบน */

    .login-container {{

        position: absolute;

        top: 10px;

        right: 20px;

        z-index: 999;

    }}



    .login-btn {{

        background-color: {ACCENT};

        color: white;

        border: none;

        padding: 10px 20px;

        border-radius: 30px;

        font-weight: bold;

        font-size: 1.1rem;

        cursor: pointer;

        box-shadow: 0 4px 8px rgba(0,0,0,0.2);

        transition: all 0.3s;

    }}



    .login-btn:hover {{

        background-color: #E55A00;

        transform: translateY(-2px);

        box-shadow: 0 6px 12px rgba(0,0,0,0.25);

    }}



    .main-title {{

        color: {BLACK};

        font-size: 4.2rem;

        font-weight: 900;

        text-align: center;

        margin: 60px 0 50px 0;

        letter-spacing: 2px;

        text-shadow: 3px 3px 0 {YELLOW}, 6px 6px 0 rgba(0,0,0,0.15);

    }}



    .menu-container {{

        display: flex;

        flex-direction: column;

        align-items: center;

        gap: 25px;

        margin: 0 auto;

        max-width: 700px;

        padding: 0 20px;

    }}



    .menu-card {{

        background: white;

        width: 100%;

        max-width: 500px;

        padding: 20px;

        border-radius: 30px;

        border: 4px solid {BLACK};

        box-shadow: 0 10px 20px rgba(0,0,0,0.15);

        transition: all 0.3s ease;

        cursor: pointer;

        position: relative;

        overflow: hidden;

    }}



    .menu-card:hover {{

        transform: translateY(-8px);

        box-shadow: 0 20px 30px rgba(0,0,0,0.25);

    }}



    .menu-card::before {{

        content: "";

        position: absolute;

        top: 0; left: 0; right: 0; bottom: 0;

        background: linear-gradient(45deg, transparent, rgba(255,255,255,0.4));

        opacity: 0;

        transition: opacity 0.4s;

    }}



    .menu-card:hover::before {{

        opacity: 1;

    }}



    .menu-text {{

        font-size: 1.9rem;

        font-weight: bold;

        color: {BLACK};

        text-align: center;

    }}



    .footer-text {{

        text-align: center;

        font-size: 2rem;

        font-weight: bold;

        color: {BLACK};

        margin: 80px 0 40px;

        opacity: 0.9;

    }}

    </style>

    """,

    unsafe_allow_html=True

)



# ----------------------------------------------------------------

# ระบบล็อกอินง่าย ๆ (ตัวอย่าง)

# ----------------------------------------------------------------

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False

    st.session_state.username = None



# ฟังก์ชันล็อกอิน/ออก

def login():

    st.session_state.logged_in = True

    st.session_state.username = "นิสิตตัวอย่าง"  # หรือดึงจากฟอร์มจริง



def logout():

    st.session_state.logged_in = False

    st.session_state.username = None



# ปุ่มล็อกอิน ขวาบน

with st.container():

    st.markdown('<div class="login-container">', unsafe_allow_html=True)

    

    if not st.session_state.logged_in:

        if st.button("เข้าสู่ระบบ / สมัครสมาชิก", key="login_btn", help="ล็อกอินเพื่อจองและดูประวัติ"):

            login()  # ในของจริงให้เปิดฟอร์ม

            st.rerun()

    else:

        st.write(f"สวัสดี! {st.session_state.username}")

        if st.button("ออกจากระบบ", key="logout_btn"):

            logout()

            st.rerun()

    

    st.markdown('</div>', unsafe_allow_html=True)



# ----------------------------------------------------------------

# เนื้อหาหลัก

# ----------------------------------------------------------------

st.markdown('<div class="main-title">แออดมิ้น&นิสิต 🏸</div>', unsafe_allow_html=True)



with st.container():

    st.markdown('<div class="menu-container">', unsafe_allow_html=True)



    # เมนูแบบการ์ด

    menu_items = [

        ("🏟️ จองสนาม", "จองสนาม"),

        ("📊 ดูสถานะสนาม", "ดูสถานะ"),

        ("📜 ประวัติการจอง", "ประวัติ"),

        ("💰 ราคา & กฎกติกา", "ข้อมูล"),

        ("📞 ติดต่อเรา", "ติดต่อ")

    ]



    for emoji, title in menu_items:

        with st.container():

            st.markdown('<div class="menu-card">', unsafe_allow_html=True)

            if st.button(title, key=f"menu_{title}", use_container_width=True):

                if not st.session_state.logged_in and title in ["จองสนาม", "ประวัติ"]:

                    st.warning("กรุณาเข้าสู่ระบบก่อนใช้งานฟังก์ชันนี้")

                else:

                    st.info(f"กำลังไปที่หน้า: {title} ... (เพิ่มหน้าได้ที่นี่)")

            st.markdown(f'<div class="menu-text">{emoji} {title}</div>', unsafe_allow_html=True)

            st.markdown('</div>', unsafe_allow_html=True)



    st.markdown('</div>', unsafe_allow_html=True)



# Footer

st.markdown('<div class="footer-text">แออดมิ้น&นิสิต 🏸</div>', unsafe_allow_html=True)



st.caption(f"อัพเดทล่าสุด: {datetime.now().strftime('%d/%m/%Y %H:%M')} • เชียงใหม่")
