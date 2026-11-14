# === Stage 85: Add final readiness report summarizing features and known limits ===
# Project: ExamPrep
def readiness_report(planner):
    topics = planner.topics()
    sessions = planner.sessions()
    scores = planner.scores()
    due = planner.due_reminders()

    print("=" * 40)
    print("ExamPrep Readiness Report")
    print("=" * 40)
    print(f"Topics tracked:      {len(topics)}")
    print(f"Practice sessions:   {len(sessions)}")
    print(f"Achieved scores:     {len(scores)}")
    print(f"Revision reminders:  {len(due)}")

    if sessions:
        avg = sum(s.score for s in sessions) / len(sessions)
        print(f"Average practice score: {avg:.1f}%")
    if scores:
        best = max(scores, key=lambda s: s.score)
        print(f"Highest score:         {best.topic} - {best.score}%")
    if due:
        print("Urgent revisions:")
        for d in due:
            print(f"  - {d.topic} (due {d.date})")
    else:
        print("All revisions up to date. Well done!")

    print("=" * 40)


if __name__ == "__main__":
    from examprep import Planner
    p = Planner()
    readiness_report(p)
