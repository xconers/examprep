# === Stage 42: Add CSV export without external dependencies ===
# Project: ExamPrep
import csv, io

def export_csv(self, filename="examprep_export.csv"):
    lines = []
    lines.append("Topic,Category,Progress,LastPracticed,NextRevision,Notes")
    for topic in self.topics:
        lines.append(
            f"{topic['name']},{topic.get('category','General')},{topic.get('progress',0)},"
            f"{topic.get('last_practiced','')},{topic.get('next_revision','')},{topic.get('notes','')}"
        )
    with open(filename, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(lines)
    print(f"Exported {len(self.topics)} topics to {filename}")
