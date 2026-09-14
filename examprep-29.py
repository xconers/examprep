# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: ExamPrep
def upcoming_reminders(start_date, days_ahead=30):
    """Return list of upcoming revision items within a given window.

    Args:
        start_date: datetime.date representing today.
        days_ahead: number of days to look ahead.

    Returns:
        List of dicts with keys: topic, due_date, days_until_due, priority.
    """
    from datetime import timedelta

    end_date = start_date + timedelta(days=days_ahead)
    upcoming = []
    for item in revision_queue:
        due = item['due_date']
        if due >= start_date and due <= end_date:
            days_until = (due - start_date).days
            upcoming.append({
                'topic': item['topic'],
                'due_date': due,
                'days_until_due': days_until,
                'priority': item.get('priority', 'medium')
            })
    upcoming.sort(key=lambda x: x['days_until_due'])
    return upcoming
