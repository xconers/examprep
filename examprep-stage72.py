# === Stage 72: Add Markdown report export ===
# Project: ExamPrep
def export_markdown_report(db, filename="exam_prep_report.md"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("# ExamPrep Report\n\n")
        f.write(f"Generated: {datetime.now().isoformat()}\n\n")
        f.write("## Topics\n")
        for topic in db["topics"]:
            f.write(f"- {topic['name']} (sessions: {topic['count']})\n")
        f.write("\n## Practice Sessions\n")
        for session in db["sessions"]:
            score = session["score"]
            f.write(f"- {session['topic']} - {score}/100\n")
        f.write("\n## Revision Reminders\n")
        for reminder in db["reminders"]:
            f.write(f"- {reminder['topic']} on {reminder['date']} ({reminder['days']})\n")
