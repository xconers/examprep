# === Stage 81: Add final README text as a module string with usage examples ===
# Project: ExamPrep
import os
from datetime import datetime, date

TOPICS = ["algebra", "geometry", "calculus", "statistics"]
SESSIONS = []
SCORES = []
REMINDERS = []


def add_topic(name):
    if name not in TOPICS:
        TOPICS.append(name)


def record_session(topic, minutes):
    SESSIONS.append({"topic": topic, "minutes": minutes, "date": datetime.now().strftime("%Y-%m-%d")})


def record_score(topic, score):
    if 0 <= score <= 100:
        SCORES.append({"topic": topic, "score": score, "date": datetime.now().strftime("%Y-%m-%d")})


def add_reminder(topic, days):
    REMINDERS.append({"topic": topic, "days": days})


def is_due(reminder):
    return (date.today() - date.fromisoformat(reminder["date"])).days >= reminder["days"]


def generate_reminders():
    return [r for r in REMINDERS if is_due(r)]


def show_progress():
    total = len(SCORES)
    if total == 0:
        print("No scores recorded yet.")
        return
    best = max(SCORES, key=lambda s: s["score"])
    print(f"Topics: {', '.join(TOPICS)}")
    print(f"Sessions: {len(SESSIONS)}  Scores: {total}")
    print(f"Best score: {best['topic']} = {best['score']}%")
    print("Due reminders:", ", ".join(generate_reminders()) if generate_reminders() else "None")


if __name__ == "__main__":
    add_topic("trigonometry")
    record_session("algebra", 25)
    record_score("algebra", 87)
    add_reminder("calculus", 2)
    show_progress()
