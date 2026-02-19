import streamlit as st
from database import get_connection

# -------------------------
# 🔐 Login
# -------------------------
def login(username, password):

    # 🔥 Admin พิเศษ (Hardcode)
    if username == "admin" and password == "123456789":
        st.session_state.logged_in = True
        st.session_state.user_id = 0
        st.session_state.role = "admin"
        st.session_state.username = "admin"
        return True

    # 👤 User ปกติจาก database
    conn = get_connection()
    c = conn.cursor()

    c.execute(
        "SELECT id, role FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = c.fetchone()
    conn.close()

    if user:
        st.session_state.logged_in = True
        st.session_state.user_id = user[0]
        st.session_state.role = user[1]
        st.session_state.username = username
        return True

    return False


# -------------------------
# 📝 Register (student เท่านั้น)
# -------------------------
def register(username, password):
    conn = get_connection()
    c = conn.cursor()

    try:
        c.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            (username, password, "student")
        )
        conn.commit()
        st.success("สมัครสมาชิกสำเร็จ")

    except:
        st.error("Username ซ้ำ")

    conn.close()
