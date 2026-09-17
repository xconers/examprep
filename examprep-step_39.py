# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: ExamPrep
def repair_data(self):
    """Fix simple integrity issues: normalize topic names, ensure session scores are numeric, and rebuild missing revision dates."""
    for topic in self.topics.values():
        topic["name"] = topic["name"].strip().lower()
    for session in self.sessions:
        if not isinstance(session["score"], (int, float)):
            session["score"] = 0
        if not session["score"] or session["score"] < 0:
            session["score"] = 0
        if not session["date"]:
            session["date"] = datetime.now().strftime("%Y-%m-%d")
        if not session["duration"]:
            session["duration"] = 60
    for topic in self.topics.values():
        if not topic["revision_date"]:
            topic["revision_date"] = datetime.now().strftime("%Y-%m-%d")
    return self
