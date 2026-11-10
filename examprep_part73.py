# === Stage 73: Add a lightweight HTML report export ===
# Project: ExamPrep
def export_html_report(path, topics, sessions, scores, reminders):
    with open(path, "w", encoding="utf-8") as f:
        f.write("<!DOCTYPE html>\n<html><head><meta charset='utf-8'><title>ExamPrep Report</title></head>\n<body>\n")
        f.write("<h1>ExamPrep Progress Report</h1>\n")
        f.write("<h2>Topics</h2>\n<ul>\n")
        for t in topics:
            f.write("<li>" + t + "</li>\n")
        f.write("</ul>\n")
        f.write("<h2>Sessions</h2>\n<ul>\n")
        for s in sessions:
            f.write("<li>" + s + "</li>\n")
        f.write("</ul>\n")
        f.write("<h2>Scores</h2>\n<ul>\n")
        for sc in scores:
            f.write("<li>" + sc + "</li>\n")
        f.write("</ul>\n")
        f.write("<h2>Revision Reminders</h2>\n<ul>\n")
        for r in reminders:
            f.write("<li>" + r + "</li>\n")
        f.write("</ul>\n")
        f.write("</body></html>\n")
