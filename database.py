import sqlite3

conn = sqlite3.connect("quoter.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY
)
""")

conn.commit()

import sqlite3

conn = sqlite3.connect("quoter.db")
cursor = conn.cursor()


def add_user(user_id):
    cursor.execute(
        "INSERT OR IGNORE INTO users (user_id) VALUES (?)",
        (user_id,)
    )
    conn.commit()


def remove_user(user_id):
    cursor.execute(
        "DELETE FROM users WHERE user_id=?",
        (user_id,)
    )
    conn.commit()


def get_users():
    cursor.execute(
        "SELECT user_id FROM users"
    )

    return [row[0] for row in cursor.fetchall()]