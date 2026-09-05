# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: ExamPrep
from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import List, Optional

@dataclass
class Topic:
    name: str
    difficulty: str  # 'easy', 'medium', 'hard'
    description: str = ""
    tags: List[str] = field(default_factory=list)

@dataclass
class PracticeSession:
    topic: Topic
    date: date
    duration_minutes: int = 30
    score: float = 0.0
    notes: str = ""

@dataclass
class RevisionReminder:
    topic: Topic
    due_date: date
    notes: str = ""

@dataclass
class ExamPlan:
    topics: List[Topic] = field(default_factory=list)
    sessions: List[PracticeSession] = field(default_factory=list)
    reminders: List[RevisionReminder] = field(default_factory=list)
    created: Optional[date] = None

    def add_session(self, topic: Topic, date: date, duration: int = 30, score: float = 0.0, notes: str = ""):
        self.sessions.append(PracticeSession(topic=topic, date=date, duration_minutes=duration, score=score, notes=notes))

    def add_reminder(self, topic: Topic, due_date: date, notes: str = ""):
        self.reminders.append(RevisionReminder(topic=topic, due_date=due_date, notes=notes))

    def upcoming_reminders(self, today: Optional[date] = None) -> List[RevisionReminder]:
        if today is None:
            today = date.today()
        return [r for r in self.reminders if r.due_date <= today]
