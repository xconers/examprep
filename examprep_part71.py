# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: ExamPrep
def seed_demo_data(store):
    if not store.get("topics"):
        store["topics"] = [
            {"id": "t1", "name": "Algebra", "status": "active"},
            {"id": "t2", "name": "Calculus", "status": "active"},
            {"id": "t3", "name": "Geometry", "status": "review"},
        ]
    if not store.get("sessions"):
        store["sessions"] = [
            {"id": "s1", "topic_id": "t1", "score": 85},
            {"id": "s2", "topic_id": "t2", "score": 70},
        ]
    if not store.get("reminders"):
        store["reminders"] = [
            {"id": "r1", "topic_id": "t2", "days_until": 3},
            {"id": "r2", "topic_id": "t3", "days_until": 7},
        ]
    return store
