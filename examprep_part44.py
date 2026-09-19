# === Stage 44: Add backup creation for the data file ===
# Project: ExamPrep
def create_backup(data_path, backup_dir="backups"):
    """Create a timestamped backup of the data file."""
    import shutil
    import os
    from datetime import datetime
    backup_path = os.path.join(backup_dir, f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    try:
        shutil.copy2(data_path, backup_path)
        print(f"Backup created at: {backup_path}")
    except Exception as e:
        print(f"Backup failed: {e}")
