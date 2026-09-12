# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: ExamPrep
def archive_records(records, cutoff=None):
    """Move records older than cutoff (or all if None) to an 'archived' list."""
    if cutoff is None:
        archived = records[:]
        records.clear()
        return archived
    archived = [r for r in records if (r.get("last_practiced") or r.get("created")) < cutoff]
    for r in archived:
        r["_archived"] = True
    records = [r for r in records if not r.get("_archived")]
    return archived

def restore_records(archived, cutoff=None):
    """Put records back; keep only those newer than cutoff if given."""
    if cutoff is None:
        return archived[:]
    return [r for r in archived if (r.get("last_practiced") or r.get("created")) >= cutoff]
