# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: ExamPrep
import json
from pathlib import Path

# ExamPrep: bulk delete topics
TOPIC_FILE = Path("topics.json")

def bulk_delete_topics(topic_ids, confirm=False):
    """Delete multiple topics by ID. If confirm is False, raise a RuntimeError
    to prevent accidental bulk removals."""
    if not confirm:
        raise RuntimeError("Bulk delete requires explicit confirmation.")
    if not topic_ids:
        return
    with open(TOPIC_FILE, "r") as f:
        topics = json.load(f)
    for tid in topic_ids:
        topics = [t for t in topics if t["id"] != tid]
    with open(TOPIC_FILE, "w") as f:
        json.dump(topics, f, indent=2)
    print(f"Deleted {len(topic_ids)} topic(s): {', '.join(topic_ids)}")
