# === Stage 13: Add file save support using a configurable path ===
# Project: ExamPrep
import os

def save_exam_data(exam_data, filepath):
    """Save exam data to a file."""
    with open(filepath, 'w') as f:
        f.write(str(exam_data))
    print(f"Data saved to {filepath}")
