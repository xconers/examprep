# === Stage 11: Add JSON export for the current application state ===
# Project: ExamPrep
def export_state(path="state.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)
    print(f"State exported to {path}")
