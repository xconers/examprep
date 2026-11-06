# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: ExamPrep
def cmd_clear_state():
    if not confirm("Are you sure you want to reset all data?"):
        print("Clear cancelled.")
        return
    topics.clear()
    sessions.clear()
    scores.clear()
    reminders.clear()
    save_state()
    print("State cleared.")
