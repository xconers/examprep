# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: ExamPrep
def run_self_check(db_path="exam_prep.db"):
    import sqlite3

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    topics = cur.execute("SELECT COUNT(*) FROM topics").fetchone()[0]
    sessions = cur.execute("SELECT COUNT(*) FROM practice_sessions").fetchone()[0]
    scores = cur.execute("SELECT COUNT(*) FROM scores").fetchone()[0]
    reminders = cur.execute("SELECT COUNT(*) FROM revision_reminders").fetchone()[0]

    print("ExamPrep Self-Check")
    print("Topics:", topics)
    print("Practice sessions:", sessions)
    print("Scores:", scores)
    print("Revision reminders:", reminders)

    if topics == 0:
        cur.execute("INSERT INTO topics (name) VALUES ('Algebra')")
        print("Added default topic: Algebra")

    if sessions == 0:
        cur.execute(
            "INSERT INTO practice_sessions (topic_id, score) "
            "SELECT id, 85 FROM topics WHERE name = 'Algebra' LIMIT 1"
        )
        print("Added a sample practice session")

    if scores == 0:
        cur.execute(
            "INSERT INTO scores (topic_id, date, score) "
            "SELECT id, date('now'), 85 FROM practice_sessions LIMIT 1"
        )
        print("Added a sample score")

    if reminders == 0:
        cur.execute(
            "INSERT INTO revision_reminders (topic_id, next_review) "
            "SELECT id, date('now', '+7 days') FROM topics WHERE name = 'Algebra' LIMIT 1"
        )
        print("Added a sample revision reminder")

    conn.commit()

    avg = cur.execute(
        "SELECT AVG(score) FROM scores WHERE score IS NOT NULL"
    ).fetchone()[0]
    print("Average score:", round(avg, 2) if avg else None)

    pending = cur.execute(
        "SELECT COUNT(*) FROM revision_reminders WHERE next_review <= date('now')"
    ).fetchone()[0]
    print("Overdue revisions:", pending)

    conn.close()
    return True
