# === Stage 16: Add argparse support for the most common commands ===
# Project: ExamPrep
import argparse

def main():
    parser = argparse.ArgumentParser(description="ExamPrep - Exam Preparation Planner")
    subparsers = parser.add_subparsers(dest="command")

    p_topic = subparsers.add_parser("topic", help="Manage topics")
    p_topic.add_argument("action", choices=["add", "list", "detail"], nargs="?", default="list")
    p_topic.add_argument("--name", help="Topic name (for add)")
    p_topic.add_argument("--status", choices=["planned", "in_progress", "done"], default="planned")
    p_topic.add_argument("--id", help="Topic ID (for detail)")

    p_session = subparsers.add_parser("session", help="Manage practice sessions")
    p_session.add_argument("action", choices=["start", "end", "list"], nargs="?", default="list")
    p_session.add_argument("--topic-id", help="Topic ID to start session for")
    p_session.add_argument("--score", help="Score achieved (for end)")

    p_score = subparsers.add_parser("score", help="Record scores")
    p_score.add_argument("--topic-id", required=True)
    p_score.add_argument("--sessions", required=True, help="Comma-separated session IDs")
    p_score.add_argument("--scores", required=True, help="Comma-separated scores")

    p_revision = subparsers.add_parser("revision", help="Check revision reminders")
    p_revision.add_argument("--days", type=int, default=1, help="Days since last revision")
    p_revision.add_argument("--topic-id", help="Specific topic ID")

    args = parser.parse_args()
    if args.command in ("topic", "session", "score", "revision"):
        print(f"ExamPrep: {args.command} command invoked")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
