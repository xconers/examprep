# === Stage 64: Add validation for relationship references ===
# Project: ExamPrep
def validate_references(db):
    if not db.get('topics'):
        return

    topic_ids = {t['id'] for t in db['topics']}
    session_ids = {s['id'] for s in db['sessions']}
    reminder_ids = {r['id'] for r in db['revision_reminders']}

    for session in db['sessions']:
        if session['topic_id'] not in topic_ids:
            raise ValueError(f"session {session['id']} references missing topic {session['topic_id']}")
        if session['score'] is not None and not (0 <= session['score'] <= 100):
            raise ValueError(f"session {session['id']} has invalid score {session['score']}")

    for reminder in db['revision_reminders']:
        if reminder['topic_id'] not in topic_ids:
            raise ValueError(f"reminder {reminder['id']} references missing topic {reminder['topic_id']}")
        if reminder['session_id'] not in session_ids:
            raise ValueError(f"reminder {reminder['id']} references missing session {reminder['session_id']}")
