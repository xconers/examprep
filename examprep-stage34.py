# === Stage 34: Add support for multiple local user profiles ===
# Project: ExamPrep
import json
from pathlib import Path

PROFILE_DIR = Path(__file__).parent / "profiles"
PROFILE_DIR.mkdir(exist_ok=True)

DEFAULT_PROFILE = {
    "name": "default",
    "topics": [],
    "scores": {},
    "revision_reminders": [],
}

def load_profile(name: str) -> dict:
    data = DEFAULT_PROFILE.copy()
    if not name:
        return data
    path = PROFILE_DIR / f"{name}.json"
    if path.exists():
        data.update(json.loads(path.read_text()))
    return data

def save_profile(name: str, profile: dict) -> None:
    path = PROFILE_DIR / f"{name}.json"
    path.write_text(json.dumps(profile, indent=2))

def get_profiles() -> list[dict]:
    return [load_profile(p) for p in sorted(PROFILE_DIR.glob("*.json"))]
