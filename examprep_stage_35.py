# === Stage 35: Add active user switching and user-specific records ===
# Project: ExamPrep
import json, os, uuid
DATA = "data.json"

def load():
    if os.path.exists(DATA):
        with open(DATA) as f:
            return json.load(f)
    return {"users": [], "topics": [], "sessions": [], "scores": []}

def save(data):
    with open(DATA, "w") as f:
        json.dump(data, f, indent=2)

def register_user(name):
    data = load()
    if any(u["name"] == name for u in data["users"]):
        return
    data["users"].append({"name": name, "id": str(uuid.uuid4()), "topics": [], "sessions": [], "scores": []})
    save(data)
    return data

def login_user(name):
    data = load()
    for u in data["users"]:
        if u["name"] == name:
            return u
    return None

def active_user():
    return login_user("current_user")
