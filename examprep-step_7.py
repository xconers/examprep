# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: ExamPrep
def format_session(s):
    return f"[{s['topic']}] Score: {s['score']}/10 | Time: {s['duration']} min"

def format_reminder(r):
    return f"Revise '{r['topic']}' in {r['days']} days ({r['next_date']})"

def format_summary(stats):
    lines = [f"Total Sessions: {stats['total']}",
             f"Avg Score: {stats['avg_score']:.1f}",
             f"Topics Covered: {', '.join(stats['topics'])}"]
    return "\n".join(lines)
