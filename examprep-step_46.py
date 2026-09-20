# === Stage 46: Add a schema version field and migration helper ===
# Project: ExamPrep
SCHEMA_VERSION = 3

def migrate_to_v3(records):
    """Upgrade any older record dicts to the current schema."""
    updated = []
    for r in records:
        if "schema_version" not in r:
            r["schema_version"] = 1
        if "last_practiced" not in r:
            r["last_practiced"] = ""
        if "last_score" not in r:
            r["last_score"] = 0
        if "total_practiced" not in r:
            r["total_practiced"] = 0
        if "last_revision" not in r:
            r["last_revision"] = 0.0
        updated.append(r)
    return updated
