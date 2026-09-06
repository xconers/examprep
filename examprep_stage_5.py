# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: ExamPrep
def update_score(self, session_id, score):
    """Update the score for a practice session.
    
    Args:
        session_id: The unique identifier of the practice session.
        score: The new score value.
        
    Raises:
        KeyError: If the session_id does not exist in the records.
    """
    if session_id not in self._sessions:
        raise KeyError(f"Session {session_id} not found")
    self._sessions[session_id].update({"score": score})
    return self._sessions[session_id]

def update_reminder(self, reminder_id, **kwargs):
    """Update fields of a revision reminder.
    
    Args:
        reminder_id: The unique identifier of the reminder.
        **kwargs: Fields to update (e.g. due_date, topic).
        
    Raises:
        KeyError: If the reminder_id does not exist in the records.
    """
    if reminder_id not in self._reminders:
        raise KeyError(f"Reminder {reminder_id} not found")
    self._reminders[reminder_id].update(kwargs)
    return self._reminders[reminder_id]
