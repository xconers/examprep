# === Stage 14: Add file load support with fallback demo data ===
# Project: ExamPrep
def load_data(filename="exam_prep.json", fallback=True):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            data = {"topics": [], "sessions": [], "scores": [], "reminders": []}
        return data
    except FileNotFoundError:
        if fallback:
            return {"topics": [], "sessions": [], "scores": [], "reminders": []}
        raise
    except json.JSONDecodeError:
        if fallback:
            print("Warning: invalid JSON, using fallback data")
            return {"topics": [], "sessions": [], "scores": [], "reminders": []}
        raise
