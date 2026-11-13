# === Stage 82: Add an end-to-end demo function that prints a complete walkthrough ===
# Project: ExamPrep
def demo_end_to_end():
    print("=== ExamPrep Demo ===")
    planner = ExamPrep("Mathematics")
    planner.add_topic("Algebra", 5)
    planner.add_topic("Geometry", 4)
    planner.add_topic("Statistics", 3)
    planner.add_session("Algebra", "Fractions", 85)
    planner.add_score("Algebra", 90)
    planner.add_reminder("Statistics", "Friday", 14)
    planner.print_topics()
    planner.print_sessions()
    planner.print_scores()
    planner.print_reminders()
    planner.print_summary()
