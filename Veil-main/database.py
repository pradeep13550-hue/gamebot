import sqlite3


conn = sqlite3.connect("data/veil.db", check_same_thread=False)
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
user_id INTEGER PRIMARY KEY,
username TEXT,
games INTEGER DEFAULT 0,
wins INTEGER DEFAULT 0
)
""")


conn.commit()
