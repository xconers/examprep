# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: ExamPrep
import json

def load_planner_data(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Malformed JSON in '{path}'. Details: {e}")
        return None
    except PermissionError:
        print(f"Error: Permission denied when reading '{path}'.")
        return None
    except Exception as e:
        print(f"Unexpected error reading '{path}': {e}")
        return None
