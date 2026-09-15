# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: ExamPrep
def get_settings():
    return {
        "study_hours_per_day": 3,
        "break_duration_minutes": 15,
        "revision_frequency_days": 3,
        "notification_enabled": True,
        "font_size": "medium",
        "theme": "light",
        "language": "en",
        "default_difficulty": "medium",
        "max_attempts_per_topic": 5,
        "passing_score": 70,
        "auto_save_interval_seconds": 60,
        "last_updated": "2024-01-15T10:30:00"
    }

def update_settings(key, value):
    settings = get_settings()
    if key in settings:
        settings[key] = value
        print(f"Setting '{key}' updated to {value}")
    else:
        print(f"Error: Unknown setting '{key}'")
        return False
    return True

def reset_settings():
    settings = get_settings()
    for key in settings:
        if key != "last_updated":
            settings[key] = settings["default"] if "default" in settings else None
    print("All settings reset to defaults")
    return settings
