# === Stage 43: Add CSV import for the primary record type ===
# Project: ExamPrep
import csv

def import_csv(filename, delimiter=","):
    topics = []
    with open(filename, "r", newline="") as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        for row in reader:
            topics.append({
                "name": row["name"],
                "description": row["description"],
                "difficulty": row["difficulty"],
                "status": row["status"],
            })
    return topics
