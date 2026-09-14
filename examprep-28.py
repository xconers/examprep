# === Stage 28: Add overdue item detection based on due dates ===
# Project: ExamPrep
def detect_overdue_items(items):
    """Returns a list of items whose due date has passed."""
    overdue = []
    for item in items:
        if item.get("due_date") is None:
            continue
        due = datetime.fromisoformat(item["due_date"].replace("Z", "+00:00"))
        if due < datetime.now(timezone.utc):
            overdue.append(item)
    return overdue
