# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: ExamPrep
# Demo scenario: exercises the main workflow
import datetime

# 1. Create a topic
topic = Topic("Algebra", description="Quadratic equations", difficulty="medium")

# 2. Create a practice session for the topic
session = PracticeSession(topic, duration_minutes=30, start_time=datetime.datetime.now(), notes="Focus on factorization")

# 3. Add a score
score = Score(18, 20, session)

# 4. Create a revision reminder for tomorrow
reminder = RevisionReminder(topic, date=datetime.date.today() + datetime.timedelta(days=1))

# 5. Execute the planner to generate a schedule
planner = Planner()
schedule = planner.generate_schedule([topic], [session], [reminder])

# 6. Display the generated schedule
print("=== ExamPrep Demo Schedule ===")
for day, tasks in schedule.items():
    print(f"\nDay: {day.strftime('%A, %Y-%m-%d')}")
    for task in tasks:
        if isinstance(task, Topic):
            print(f"  - Topic: {task.name} ({task.difficulty})")
        elif isinstance(task, Session):
            print(f"  - Practice: {task.topic.name} ({task.duration_minutes} min)")
        elif isinstance(task, Score):
            print(f"  - Score: {task.topic.name} -> {task.score}/{task.total}")
        elif isinstance(task, Reminder):
            print(f"  - Reminder: Review {task.topic.name} ({task.date})")
