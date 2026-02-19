import sqlite3

DB_NAME = "badminton.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # ตารางผู้ใช้
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            role TEXT
        )
    """)

    # ตารางการจอง
    c.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            court INTEGER,
            date TEXT,
            time TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)

    conn.commit()
    conn.close()

def get_connection():
    return sqlite3.connect(DB_NAME)
