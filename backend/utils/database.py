import sqlite3

DB_NAME = "fingerprint.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        voter_id TEXT UNIQUE,
        template TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_user(voter_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO users(voter_id, template)
    VALUES (?, ?)
    """, (voter_id, voter_id + ".npy"))

    conn.commit()
    conn.close()


def get_user(voter_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE voter_id=?",
        (voter_id,)
    )

    user = cursor.fetchone()

    conn.close()

    return user


def voter_exists(voter_id):
    return get_user(voter_id) is not None