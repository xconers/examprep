# === Stage 45: Add restore from backup with validation ===
# Project: ExamPrep
import os
import json
from datetime import datetime

def load_plan():
    with open("plan.json", "r") as f:
        return json.load(f)

def save_plan(plan):
    with open("plan.json", "w") as f:
        json.dump(plan, f, indent=2)

def restore_backup(backup_path, validate=True):
    if not os.path.exists(backup_path):
        print(f"Backup file not found: {backup_path}")
        return False
    try:
        with open(backup_path, "r") as f:
            backup = json.load(f)
        if validate:
            if not isinstance(backup, dict):
                print("Invalid backup format")
                return False
            if "topics" not in backup or "sessions" not in backup:
                print("Backup missing required fields")
                return False
            for topic in backup["topics"]:
                if not isinstance(topic, dict) or "name" not in topic:
                    print("Invalid topic in backup")
                    return False
            for session in backup["sessions"]:
                if not isinstance(session, dict) or "topic" not in session:
                    print("Invalid session in backup")
                    return False
        current = load_plan()
        if current["topics"] == backup["topics"] and current["sessions"] == backup["sessions"]:
            print("Backup is identical to current plan")
            return False
        save_plan(backup)
        print(f"Restored from {backup_path}")
        return True
    except Exception as e:
        print(f"Restore failed: {e}")
        return False

# Usage
backup_path = "plan_backup.json"
if os.path.exists(backup_path):
    restore_backup(backup_path)
