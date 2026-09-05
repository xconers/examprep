# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: ExamPrep
class ExamPrep:
    def __init__(self):
        self.topics = {
            "Algebra": {"sessions": 0, "scores": [], "last_review": None},
            "Calculus": {"sessions": 0, "scores": [], "last_review": None},
            "Statistics": {"sessions": 0, "scores": [], "last_review": None},
        }
        self.reminders = []
