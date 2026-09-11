# === Stage 20: Add duplicate detection for newly created records ===
# Project: ExamPrep
def find_duplicates(records):
    """Return list of record dicts that share an identical (topic, date, session_type) tuple."""
    seen = {}
    duplicates = []
    for r in records:
        key = (r.get('topic', ''), r.get('date', ''), r.get('session_type', ''))
        if key in seen:
            duplicates.append(r)
        else:
            seen[key] = r
    return duplicates
