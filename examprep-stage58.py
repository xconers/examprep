# === Stage 58: Add bulk update behavior for selected records ===
# Project: ExamPrep
def bulk_update_records(self, updates: dict) -> list:
    """Apply a single update rule to every record and return the affected rows."""
    affected = []
    for record in self._records:
        new_fields = {}
        for key, value in updates.items():
            if key in record.fields and value != record.fields[key]:
                new_fields[key] = value
                record.fields[key] = value
        if new_fields:
            affected.append(record)
    return affected
