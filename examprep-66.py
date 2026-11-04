# === Stage 66: Add export of a short status dashboard ===
# Project: ExamPrep
def export_status_dashboard(data):
    topics = data.get("topics", [])
    sessions = data.get("sessions", [])
    scores = data.get("scores", [])
    reminders = data.get("reminders", [])

    total_topics = len(topics)
    completed_topics = sum(1 for t in topics if t.get("done"))
    total_sessions = len(sessions)
    total_correct = sum(s.get("correct", 0) for s in sessions)
    total_questions = sum(s.get("total", 0) for s in sessions)
    accuracy = round(total_correct / total_questions, 1) if total_questions else 0
    upcoming = [r for r in reminders if r.get("due", 0) >= 0]

    lines = ["ExamPrep Status Dashboard", "=" * 24]
    lines.append(f"Topics: {completed_topics}/{total_topics} complete")
    lines.append(f"Practice sessions: {total_sessions}")
    lines.append(f"Accuracy: {accuracy}%")
    lines.append(f"Upcoming revisions: {len(upcoming)}")
    lines.append("")
    for r in upcoming[:5]:
        topic = r.get("topic", "unknown")
        due = r.get("due", 0)
        lines.append(f"  - {topic} revisable in {due} day(s)")
    if not upcoming:
        lines.append("  No upcoming revisions scheduled")
    return "\n".join(lines)
