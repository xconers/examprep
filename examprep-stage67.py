# === Stage 67: Add a function that returns key project metrics ===
# Project: ExamPrep
def get_project_metrics(topics, practice_sessions, scores, reminders):
    total_topics = len(topics)
    completed_topics = sum(1 for t in topics if t.get("completed", False))
    total_sessions = len(practice_sessions)
    completed_sessions = sum(1 for s in practice_sessions if s.get("completed", False))
    total_scores = [s.get("score", 0) for s in scores if s.get("score", 0) is not None]
    overall_score = (sum(total_scores) / len(total_scores)) if total_scores else 0.0
    active_reminders = sum(1 for r in reminders if r.get("due") and r["due"] > datetime.now().date())
    overdue_reminders = sum(1 for r in reminders if r.get("due") and r["due"] < datetime.now().date())
    return {
        "total_topics": total_topics,
        "completed_topics": completed_topics,
        "topic_progress": (completed_topics / total_topics) if total_topics else 0.0,
        "total_sessions": total_sessions,
        "completed_sessions": completed_sessions,
        "overall_score": round(overall_score, 2),
        "active_reminders": active_reminders,
        "overdue_reminders": overdue_reminders,
    }
