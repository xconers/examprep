# === Stage 56: Add compact error classes for domain failures ===
# Project: ExamPrep
class ExamError(Exception):
    """Base exception for all ExamPrep domain failures."""
    pass

class TopicNotFoundError(ExamError):
    """Raised when a topic does not exist in the planner."""
    def __init__(self, topic_id: str):
        super().__init__(f"Topic '{topic_id}' not found.")
        self.topic_id = topic_id

class SessionNotFoundError(ExamError):
    """Raised when a practice session cannot be located."""
    def __init__(self, session_id: str):
        super().__init__(f"Session '{session_id}' not found.")
        self.session_id = session_id

class ScoreOutOfRange(ExamError):
    """Raised when a score is outside the valid 0-100 range."""
    def __init__(self, score: int):
        super().__init__(f"Score {score} is out of range [0, 100].")
        self.score = score

class RevisionTooSoon(ExamError):
    """Raised when a revision reminder fires before the minimum interval."""
    def __init__(self, topic_id: str, minutes: int, min_interval: int):
        super().__init__(
            f"Topic '{topic_id}' needs {min_interval} min; only {minutes} elapsed."
        )
        self.topic_id = topic_id
        self.minutes = minutes
        self.min_interval = min_interval

class PlannerFullError(ExamError):
    """Raised when the planner has reached its session capacity."""
    def __init__(self, capacity: int):
        super().__init__(f"Planner is full (capacity {capacity}).")
        self.capacity = capacity
