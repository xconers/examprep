# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: ExamPrep
def _normalize_score(raw: float) -> float:
    """Clamp a raw score to the [0, 100] range and round to two decimals."""
    return round(max(0.0, min(100.0, raw)), 2)


def _format_date_iso(dt: datetime) -> str:
    """Return an ISO 8601 date string (YYYY-MM-DD) from any datetime."""
    return dt.strftime("%Y-%m-%d")


def _count_remaining_days(target: datetime, now: datetime) -> int:
    """Return the number of days left until *target*, or 0 if already past."""
    delta = (target - now).days
    return max(0, delta)


def _build_revision_reminder(topic: str, target_date: datetime) -> dict:
    """Create a revision-reminder record for a given topic and target date."""
    return {
        "type": "revision_reminder",
        "topic": topic,
        "target_date": target_date,
        "status": "pending",
    }


def _load_scores_from_file(path: str) -> dict[str, dict]:
    """Load the topic-scores mapping from a JSON file (returns empty dict on error)."""
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def _save_scores_to_file(path: str, scores: dict[str, dict]) -> None:
    """Persist the topic-scores mapping to a JSON file, creating parent dirs if needed."""
    parent_dir = os.path.dirname(path)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(scores, fh, indent=2, sort_keys=True)
