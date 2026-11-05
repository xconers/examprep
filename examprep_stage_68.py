# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: ExamPrep
def generate_changelog(activity_log):
    if not activity_log:
        return "No activity recorded yet."
    lines = ["ExamPrep Changelog"]
    entries = sorted(set(activity_log), key=lambda e: e[0], reverse=True)
    for date, items in entries:
        lines.append(f"\n{date}")
        for item in items:
            lines.append(f"  - {item}")
    return "\n".join(lines)
