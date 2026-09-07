# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: ExamPrep
def sort_sessions(sessions, key):
    if key == 'title':
        return sorted(sessions, key=lambda s: s.get('title', ''))
    elif key == 'date':
        return sorted(sessions, key=lambda s: s.get('date', ''), reverse=True)
    elif key == 'priority':
        return sorted(sessions, key=lambda s: s.get('priority', 'medium'))
    elif key == 'last_update':
        return sorted(sessions, key=lambda s: s.get('last_update', ''), reverse=True)
    else:
        return sessions
