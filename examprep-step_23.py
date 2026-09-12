# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: ExamPrep
def tag_add_remove(tags, topic):
    if topic not in tags:
        tags.append(topic)
    return tags

def tag_summary(tags):
    return ', '.join(tags) if tags else 'no tags'
