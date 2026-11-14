# === Stage 84: Add final cleanup for unused helpers and duplicate code ===
# Project: ExamPrep
def prune_revisions(topic_scores):
    cleaned = {}
    for topic, scores in topic_scores.items():
        valid = [s for s in scores if isinstance(s, (int, float))]
        if valid:
            cleaned[topic] = max(valid)
    return cleaned

def dedupe_scores(records):
    seen = set()
    unique = []
    for record in records:
        key = tuple(sorted(record.items()))
        if key not in seen:
            seen.add(key)
            unique.append(record)
    return unique

def normalize_scores(records):
    result = []
    for record in records:
        if isinstance(record, dict) and 'score' in record:
            result.append({k: v for k, v in record.items() if k != 'score' and v is not None})
        elif isinstance(record, (int, float)):
            result.append(record)
    return result

def merge_score_lists(a, b):
    return list(a) + list(b)

def format_score(value):
    if isinstance(value, float):
        return round(value, 2)
    return value
