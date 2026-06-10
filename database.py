import sqlite3
from datetime import date

conn = sqlite3.connect("quoter.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY
)
""")

conn.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usage (
    user_id INTEGER,
    date TEXT,
    count INTEGER,
    PRIMARY KEY (user_id, date)
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

def check_limit(user_id):

    today = str(date.today())

    cursor.execute(
        """
        SELECT count
        FROM usage
        WHERE user_id=? AND date=?
        """,
        (user_id, today)
    )

    row = cursor.fetchone()

    if row is None:

        cursor.execute(
            """
            INSERT INTO usage
            (user_id, date, count)
            VALUES (?, ?, 1)
            """,
            (user_id, today)
        )

        conn.commit()

        return True

    count = row[0]

    if count >= 3:
        return False

    cursor.execute(
        """
        UPDATE usage
        SET count=count+1
        WHERE user_id=? AND date=?
        """,
        (user_id, today)
    )

    conn.commit()

    return True