import streamlit as st
from database import get_connection

def register(username, password):
    conn = get_connection()
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                  (username, password, "student"))
        conn.commit()
        st.success("สมัครสมาชิกสำเร็จ")
    except:
        st.error("Username ซ้ำ")
    conn.close()

def login(username, password):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT id, role FROM users WHERE username=? AND password=?",
              (username, password))
    user = c.fetchone()
    conn.close()

    if user:
        st.session_state.logged_in = True
        st.session_state.user_id = user[0]
        st.session_state.role = user[1]
        st.session_state.username = username
        return True
    return False
