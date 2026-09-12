# === Stage 22: Add favorite records and quick favorite listing ===
# Project: ExamPrep
import sqlite3

conn = sqlite3.connect("exam_prep.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS favorites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic_id INTEGER NOT NULL,
    session_id INTEGER NOT NULL,
    score INTEGER,
    FOREIGN KEY(topic_id) REFERENCES topics(id),
    FOREIGN KEY(session_id) REFERENCES sessions(id)
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS favorite_list (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    topic_id INTEGER NOT NULL,
    session_id INTEGER NOT NULL,
    score INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(topic_id) REFERENCES topics(id),
    FOREIGN KEY(session_id) REFERENCES sessions(id)
)
""")

def add_favorite(user_id=None, topic_id=None, session_id=None, score=None):
    if user_id is None:
        c.execute("SELECT id FROM users WHERE id = ?", (user_id,))
        row = c.fetchone()
        if row is None:
            raise ValueError("User not found")
        user_id = row[0]
    c.execute(
        "INSERT INTO favorite_list (user_id, topic_id, session_id, score) VALUES (?, ?, ?, ?)",
        (user_id, topic_id, session_id, score)
    )
    conn.commit()

def get_favorites(user_id=None):
    if user_id is None:
        c.execute("SELECT topic_id, session_id, score FROM favorites ORDER BY score DESC")
    else:
        c.execute("SELECT topic_id, session_id, score FROM favorite_list WHERE user_id = ? ORDER BY score DESC", (user_id,))
    return c.fetchall()
