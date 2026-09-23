# === Stage 55: Add a setting to disable colorized output ===
# Project: ExamPrep
import sys

class ExamPrep:
    def __init__(self):
        self.topics = []
        self.practice_sessions = []
        self.scores = []
        self.revision_reminders = []
        self._color_enabled = True

    def set_color_enabled(self, enabled: bool) -> None:
        self._color_enabled = enabled

    @staticmethod
    def _colorize(text: str, fg: str = "green") -> str:
        if not ExamPrep._color_enabled:
            return text
        codes = {
            "green": "\033[32m",
            "red": "\033[31m",
            "yellow": "\033[33m",
            "blue": "\033[34m",
            "cyan": "\033[36m",
            "white": "\033[37m",
            "reset": "\033[0m",
        }
        return f"{codes.get(fg, '')}{text}{codes['reset']}"

    def add_topic(self, name: str, difficulty: str = "medium") -> None:
        self.topics.append({"name": name, "difficulty": difficulty})

    def add_practice_session(self, topic: str, duration_minutes: int) -> None:
        self.practice_sessions.append({"topic": topic, "duration_minutes": duration_minutes})

    def record_score(self, topic: str, score: float) -> None:
        self.scores.append({"topic": topic, "score": score})

    def add_revision_reminder(self, topic: str, days_until: int) -> None:
        self.revision_reminders.append({"topic": topic, "days_until": days_until})

    def _print_topics(self) -> None:
        print(self._colorize("\n=== Topics ===", "blue"))
        for t in self.topics:
            print(f"  - {self._colorize(t['name'], 'green')} [{t['difficulty']}]")

    def _print_sessions(self) -> None:
        print(self._colorize("\n=== Practice Sessions ===", "blue"))
        for s in self.practice_sessions:
            print(f"  - {self._colorize(s['topic'], 'green')} ({s['duration_minutes']} min)")

    def _print_scores(self) -> None:
        print(self._colorize("\n=== Scores ===", "blue"))
        for s in self.scores:
            print(f"  - {self._colorize(s['topic'], 'green')}: {s['score']:.1f}%")

    def _print_reminders(self) -> None:
        print(self._colorize("\n=== Revision Reminders ===", "blue"))
        for r in self.revision_reminders:
            print(f"  - {self._colorize(r['topic'], 'green')} in {r['days_until']} days")

    def print_all(self) -> None:
        self._print_topics()
        self._print_sessions()
        self._print_scores()
        self._print_reminders()
