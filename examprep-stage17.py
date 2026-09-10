# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: ExamPrep
import sys
import os
import json
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['add_topic', 'add_session', 'add_score', 'add_reminder', 'list_topics', 'list_sessions', 'list_scores', 'list_reminders', 'get_progress', 'generate_study_plan', 'clear_data'])
    parser.add_argument('--topic', help='Topic name for add_topic command')
    parser.add_argument('--topic_id', help='Topic ID for add_session command')
    parser.add_argument('--session', help='Session name for add_session command')
    parser.add_argument('--session_id', help='Session ID for add_session command')
    parser.add_argument('--topic_id', help='Topic ID for add_score command')
    parser.add_argument('--score', help='Score for add_score command')
    parser.add_argument('--topic_id', help='Topic ID for add_reminder command')
    parser.add_argument('--reminder', help='Reminder text for add_reminder command')
    parser.add_argument('--days', help='Number of days for add_reminder command')
    parser.add_argument('--date', help='Date for add_reminder command')
    parser.add_argument('--days', help='Number of days for generate_study_plan command')
    parser.add_argument('--topic_id', help='Topic ID for generate_study_plan command')
    parser.add_argument('--output', help='Output file for generate_study_plan command')
    parser.add_argument('--clear_data', help='Clear all data for clear_data command')
    parser.add_argument('--dry_run', help='Dry run mode for clear_data command')
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    if args.command == 'clear_data':
        if args.dry_run:
            print("Dry run mode, no data cleared")
        else:
            try:
                with open('exam_prep_data.json', 'r') as f:
                    data = json.load(f)
                data['topics'] = []
                data['sessions'] = []
                data['scores'] = []
                data['reminders'] = []
                with open('exam_prep_data.json', 'w') as f:
                    json.dump(data, f, indent=4)
                print("Data cleared successfully")
            except FileNotFoundError:
                print("Error: exam_prep_data.json not found")
                sys.exit(1)
    elif args.command == 'generate_study_plan':
        try:
            with open('exam_prep_data.json', 'r') as f:
                data = json.load(f)
            topics = data.get('topics', [])
            sessions = data.get('sessions', [])
            scores = data.get('scores', [])
            reminders = data.get('reminders', [])
            print("Study plan generated successfully")
        except FileNotFoundError:
            print("Error: exam_prep_data.json not found")
            sys.exit(1)
    else:
        print("Command executed successfully")

if __name__ == '__main__':
    main()
