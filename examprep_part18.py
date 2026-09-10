# === Stage 18: Add an activity log with timestamps and action names ===
# Project: ExamPrep
import datetime


class ActivityLog:
    def __init__(self):
        self.entries = []

    def log(self, action, detail=""):
        self.entries.append(
            {"timestamp": datetime.datetime.now().isoformat(), "action": action, "detail": detail}
        )

    def __str__(self):
        lines = ["=== ExamPrep Activity Log ==="]
        for e in self.entries:
            lines.append(f"[{e['timestamp']}] {e['action']}: {e['detail']}")
        return "\n".join(lines)


# Example usage
log = ActivityLog()
log.log("User started ExamPrep", detail="Version 1.0")
log.log("Topic created", detail="Algebra 101")
log.log("Practice session completed", detail="Score: 85/100")
print(log)
