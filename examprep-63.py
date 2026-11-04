# === Stage 63: Add relationships between records where useful ===
# Project: ExamPrep
def link_records(records):
    """Attach useful cross-references between records."""
    topics = [r for r in records if r.get("type") == "topic"]
    sessions = [r for r in records if r.get("type") == "session"]
    for topic in topics:
        topic["practiced_by"] = [s["id"] for s in sessions if s.get("topic") == topic["id"]]
        topic["last_practiced"] = max([s["date"] for s in sessions if s.get("topic") == topic["id"]], default=None)
    for session in sessions:
        session["topic_info"] = next((t for t in topics if t["id"] == session.get("topic")), None)
        session["reviewed"] = False
    return records
