# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: ExamPrep
def compare_snapshots(before, after):
    before = before or {}
    after = after or {}
    keys = set(before) | set(after)
    added = {k: after[k] for k in keys if k not in before}
    removed = {k: before[k] for k in keys if k not in after}
    changed = {}
    for k in keys:
        if k in before and k in after and before[k] != after[k]:
            changed[k] = (before[k], after[k])
    return {"added": added, "removed": removed, "changed": changed}
