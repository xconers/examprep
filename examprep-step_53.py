# === Stage 53: Add command help text and usage examples ===
# Project: ExamPrep
# ExamPrep – command help text and usage examples
HELP_TEXT = """
ExamPrep – Exam Preparation Planner
Usage:
  python exam_prep.py <command> [options]

Commands:
  add-topic    <name> <description> [days]   Add a new topic.
  add-session  <topic> <date> <score> [minutes]  Record a practice session.
  add-score    <topic> <score> [minutes]       Record a single score for a topic.
  revision     <topic> [days]                  Show upcoming revision reminders.
  list         [topic]                        List topics, sessions, or scores.
  stats        [topic]                        Summary statistics.
  plan        <topic> <date> [days]           Create a study plan.
  help                        Show this help message.

Examples:
  python exam_prep.py add-topic "Algebra" "Study quadratic equations" 7
  python exam_prep.py add-session "Algebra" "2025-01-15" 85 45
  python exam_prep.py add-score "Calculus" 90 60
  python exam_prep.py revision "Trigonometry"
  python exam_prep.py list topics
  python exam_prep.py stats
  python exam_prep.py plan "Geometry" "2025-02-01" 3
  python exam_prep.py help
"""
