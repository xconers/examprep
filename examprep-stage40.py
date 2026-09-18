# === Stage 40: Add plain text report export ===
# Project: ExamPrep
def export_report(planner):
    """Export the planner data to a plain text summary report."""
    lines = []
    lines.append("=== ExamPrep Progress Report ===")
    lines.append(f"Planned topics: {len(planner.topics)}")
    for topic in planner.topics:
        lines.append(f"  Topic: {topic.name}")
        lines.append(f"    Status: {topic.status}")
        if topic.status == "done":
            lines.append(f"    Score: {topic.score}")
            lines.append(f"    Completed on: {topic.completed_date}")
        elif topic.status == "in_progress":
            lines.append(f"    Current session: {topic.current_session}")
            lines.append(f"    Last score: {topic.last_score}")
    lines.append(f"Total sessions completed: {planner.sessions_completed}")
    lines.append(f"Overall average score: {planner.overall_average:.1f}%")
    lines.append(f"Revision reminders: {planner.reminders_left}")
    lines.append("=== End of Report ===")
    return "\n".join(lines)
