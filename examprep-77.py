# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: ExamPrep
def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def average(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def normalize_score(raw: int, max_score: int) -> float:
    return clamp((raw / max_score) * 100.0, 0.0, 100.0)


def days_until(target: int) -> int:
    return max(0, target - days_passed())


def score_rank(score: float) -> str:
    if score >= 90:
        return "Excellent"
    if score >= 75:
        return "Good"
    if score >= 60:
        return "Satisfactory"
    if score >= 40:
        return "Needs Improvement"
    return "Fail"


def format_date(date: datetime.date) -> str:
    return date.strftime("%Y-%m-%d")


def parse_date(date_str: str) -> datetime.date:
    return datetime.date.fromisoformat(date_str.strip())


def is_due(revision_date: datetime.date, today: datetime.date | None = None) -> bool:
    today = today or datetime.date.today()
    return today >= revision_date


def sort_by_score(sessions: list[PracticeSession]) -> list[PracticeSession]:
    return sorted(sessions, key=lambda session: session.score, reverse=True)


def group_by_topic(sessions: list[PracticeSession]) -> dict[str, list[PracticeSession]]:
    grouped: dict[str, list[PracticeSession]] = {}
    for session in sessions:
        grouped.setdefault(session.topic, []).append(session)
    return grouped


def recent_sessions(sessions: list[PracticeSession], limit: int) -> list[PracticeSession]:
    return sessions[-limit:] if limit else []


def progress_percentage(completed: int, total: int) -> float:
    return round((completed / total) * 100.0, 2) if total else 0.0
