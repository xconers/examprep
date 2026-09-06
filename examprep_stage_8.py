# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: ExamPrep
def filter_sessions(sessions, status=None, category=None, owner=None, tag=None):
    result = sessions
    if status is not None:
        result = [s for s in result if s.get("status") == status]
    if category is not None:
        result = [s for s in result if s.get("category") == category]
    if owner is not None:
        result = [s for s in result if s.get("owner") == owner]
    if tag is not None:
        result = [s for s in result if tag in s.get("tags", [])]
    return result
