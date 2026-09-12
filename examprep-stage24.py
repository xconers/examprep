# === Stage 24: Add grouped summaries by category or status ===
# Project: ExamPrep
def grouped_summaries(records):
    from collections import defaultdict
    grouped = defaultdict(list)
    for r in records:
        grouped[r.get("category", "Uncategorized")].append(r)
    return [
        {"category": cat, "count": len(items), "entries": items}
        for cat, items in grouped.items()
    ]
