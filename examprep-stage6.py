# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: ExamPrep
def delete_topic(topic_id: str, confirm: bool = False) -> bool:
    """Delete a topic by ID. If confirm is False, the operation is skipped."""
    if not confirm:
        print(f"⚠️  Deletion of topic '{topic_id}' cancelled (no confirmation).")
        return False
    topics = load_topics()
    if topic_id not in topics:
        print(f"Topic '{topic_id}' not found.")
        return False
    del topics[topic_id]
    save_topics(topics)
    print(f"Topic '{topic_id}' deleted.")
    return True

def delete_session(session_id: str, confirm: bool = False) -> bool:
    """Delete a practice session by ID. Requires confirmation."""
    if not confirm:
        print(f"⚠️  Deletion of session '{session_id}' cancelled (no confirmation).")
        return False
    sessions = load_sessions()
    if session_id not in sessions:
        print(f"Session '{session_id}' not found.")
        return False
    del sessions[session_id]
    save_sessions(sessions)
    print(f"Session '{session_id}' deleted.")
    return True

def delete_score(score_id: str, confirm: bool = False) -> bool:
    """Delete a recorded score by ID. Requires confirmation."""
    if not confirm:
        print(f"⚠️  Deletion of score '{score_id}' cancelled (no confirmation).")
        return False
    scores = load_scores()
    if score_id not in scores:
        print(f"Score '{score_id}' not found.")
        return False
    del scores[score_id]
    save_scores(scores)
    print(f"Score '{score_id}' deleted.")
    return True

def delete_reminder(reminder_id: str, confirm: bool = False) -> bool:
    """Delete a reminder by ID. Requires confirmation."""
    if not confirm:
        print(f"⚠️  Deletion of reminder '{reminder_id}' cancelled (no confirmation).")
        return False
    reminders = load_reminders()
    if reminder_id not in reminders:
        print(f"Reminder '{reminder_id}' not found.")
        return False
    del reminders[reminder_id]
    save_reminders(reminders)
    print(f"Reminder '{reminder_id}' deleted.")
    return True
