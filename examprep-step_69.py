# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: ExamPrep
def reset_demo_data(db):
    """Reset demo data for manual testing."""
    with db.cursor() as cur:
        cur.execute("DELETE FROM revision_reminders")
        cur.execute("DELETE FROM practice_sessions")
        cur.execute("DELETE FROM scores")
        cur.execute("DELETE FROM topics")
        topics = [
            ("Algebra", "2024-01-05"),
            ("Geometry", "2024-01-10"),
            ("Trigonometry", "2024-01-15"),
        ]
        cur.executemany("INSERT INTO topics (name, created) VALUES (%s, %s)", topics)
        for topic_id, session_id, score in [
            (1, 1, 85),
            (2, 1, 70),
            (1, 2, 90),
        ]:
            cur.execute(
                "INSERT INTO scores (topic_id, session_id, score, scored_at) "
                "VALUES (%s, %s, %s, NOW())",
                (topic_id, session_id, score),
            )
        reminders = [
            ("Algebra", "2024-01-20"),
            ("Geometry", "2024-01-25"),
        ]
        cur.executemany(
            "INSERT INTO revision_reminders (topic_name, due_date) VALUES (%s, %s)",
            reminders,
        )
    db.commit()
    print("Demo data reset.")
