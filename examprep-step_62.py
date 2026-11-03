# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: ExamPrep
def recommend_priority(topics):
    """Return topics sorted by priority (weight * (1 - score/100))."""
    for topic in topics:
        if topic.get("complete"):
            topic["priority"] = 0
        else:
            topic["priority"] = topic.get("weight", 1) * (1 - topic.get("score", 0) / 100)
    return sorted(topics, key=lambda t: t["priority"], reverse=True)


def recommend_scores(scores):
    """Return a rating string for a list of session scores."""
    if not scores:
        return "No data yet"
    avg = sum(scores) / len(scores)
    if avg >= 80:
        return "Excellent"
    if avg >= 60:
        return "Good"
    if avg >= 40:
        return "Needs work"
    return "Focus here"


def recommend_reminders(sessions):
    """Return topics due for revision based on last practice date."""
    import datetime
    today = datetime.date.today()
    due = []
    for s in sessions:
        if s.get("last_practiced"):
            days = (today - datetime.date.fromisoformat(s["last_practiced"])).days
            if days >= 3:
                due.append(s.get("topic", "unknown"))
    return due
