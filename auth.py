def register(username, password):
    conn = get_connection()
    c = conn.cursor()

    # เช็คว่ามี admin แล้วหรือยัง
    c.execute("SELECT * FROM users WHERE role='admin'")
    admin_exists = c.fetchone()

    role = "admin" if not admin_exists else "student"

    try:
        c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                  (username, password, role))
        conn.commit()

        if role == "admin":
            st.success("สมัครสำเร็จ (คุณคือแอดมินคนแรก)")
        else:
            st.success("สมัครสมาชิกสำเร็จ")

    except:
        st.error("Username ซ้ำ")

    conn.close()
