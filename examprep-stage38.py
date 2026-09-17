# === Stage 38: Add data integrity checks for broken references ===
# Project: ExamPrep
def check_data_integrity(data):
    """
    Perform data integrity checks for broken references.
    Checks:
    1. All topic IDs referenced in practice sessions exist in topics.
    2. All session IDs referenced in scores exist in sessions.
    3. All topic IDs referenced in revision_reminders exist in topics.
    4. All session IDs referenced in revision_reminders exist in sessions.
    5. All topic IDs referenced in revision_notes exist in topics.
    """
    errors = []

    # Check that all topic references in practice_sessions are valid
    topic_ids_in_sessions = set()
    for session in data.get('practice_sessions', []):
        topic_ids_in_sessions.add(session['topic_id'])

    for session in data.get('practice_sessions', []):
        if session['topic_id'] not in data.get('topics', []):
            errors.append(f"Broken reference: session {session['id']} references non-existent topic {session['topic_id']}")

    # Check that all session references in scores are valid
    session_ids_in_scores = set()
    for score in data.get('scores', []):
        session_ids_in_scores.add(score['session_id'])

    for score in data.get('scores', []):
        if score['session_id'] not in data.get('sessions', []):
            errors.append(f"Broken reference: score {score['id']} references non-existent session {score['session_id']}")

    # Check that all topic references in revision_reminders are valid
    for reminder in data.get('revision_reminders', []):
        if reminder['topic_id'] not in data.get('topics', []):
            errors.append(f"Broken reference: revision_reminder {reminder['id']} references non-existent topic {reminder['topic_id']}")

        if reminder['session_id'] not in data.get('sessions', []):
            errors.append(f"Broken reference: revision_reminder {reminder['id']} references non-existent session {reminder['session_id']}")

    # Check that all topic references in revision_notes are valid
    for note in data.get('revision_notes', []):
        if note['topic_id'] not in data.get('topics', []):
            errors.append(f"Broken reference: revision_note {note['id']} references non-existent topic {note['topic_id']}")

    return errors
