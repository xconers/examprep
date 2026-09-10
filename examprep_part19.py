# === Stage 19: Add undo support for the last simple mutation ===
# Project: ExamPrep
def undo_last():
    """Undo the last simple mutation (add/remove topic, add session, update score).
    Uses the undo log maintained alongside the data structures."""
    if not _undo_log:
        print("Nothing to undo.")
        return
    entry = _undo_log.pop()
    action, payload = entry
    if action == "add_topic":
        topics.remove(payload["topic"])
    elif action == "remove_topic":
        topics.append(payload["topic"])
    elif action == "add_session":
        sessions.append(payload["session"])
    elif action == "update_score":
        for s in sessions:
            if s["topic"] == payload["topic"] and s["session"] == payload["session"]:
                s["score"] = payload["old_score"]
                break
    print(f"Undid: {action} — {payload}")
