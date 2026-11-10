# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: ExamPrep
def generate_validation_report(topics, sessions, scores, reminders):
    warnings = []
    errors = []

    for topic in topics:
        if topic.get('due_date') is None:
            warnings.append(f"Topic '{topic.get('name')}' has no due date.")
        if topic.get('status') not in ('planned', 'in_progress', 'completed', 'revision'):
            warnings.append(f"Topic '{topic.get('name')}' has unknown status '{topic.get('status')}'.")

    for session in sessions:
        if session.get('date') is None:
            errors.append("A practice session is missing a date.")
        if session.get('duration', 0) <= 0:
            warnings.append(f"Session on {session.get('date')} has non-positive duration.")

    total_attempts = len(scores)
    if total_attempts > 0:
        for i, score in enumerate(scores):
            if score.get('score') is None:
                warnings.append(f"Score record {i} has no score value.")
            elif not (0 <= score.get('score', -1) <= 100):
                errors.append(f"Score record {i} has out-of-range score.")
    else:
        warnings.append("No practice scores recorded yet.")

    for reminder in reminders:
        if reminder.get('due_date') is None:
            errors.append("A revision reminder has no due date.")
        elif reminder.get('reminder_days', 0) <= 0:
            warnings.append(f"Reminder for {reminder.get('due_date')} has non-positive lead time.")

    report = {
        'warnings': warnings,
        'errors': errors,
        'counts': {
            'topics': len(topics),
            'sessions': len(sessions),
            'scores': len(scores),
            'reminders': len(reminders),
            'warnings': len(warnings),
            'errors': len(errors),
        }
    }
    return report
