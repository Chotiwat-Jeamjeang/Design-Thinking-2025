from database import get_connection

def create_booking(user_id, court, date, time):
    conn = get_connection()
    c = conn.cursor()

    # เช็คซ้ำ
    c.execute("SELECT * FROM bookings WHERE court=? AND date=? AND time=?",
              (court, date, time))
    if c.fetchone():
        conn.close()
        return False

    c.execute("INSERT INTO bookings (user_id, court, date, time) VALUES (?, ?, ?, ?)",
              (user_id, court, date, time))
    conn.commit()
    conn.close()
    return True

def get_bookings_by_user(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT court, date, time FROM bookings WHERE user_id=?",
              (user_id,))
    data = c.fetchall()
    conn.close()
    return data

def get_all_bookings():
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        SELECT users.username, court, date, time
        FROM bookings
        JOIN users ON bookings.user_id = users.id
    """)
    data = c.fetchall()
    conn.close()
    return data
