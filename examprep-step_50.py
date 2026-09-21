# === Stage 50: Add unit tests for import and export behavior ===
# Project: ExamPrep
import json
import tempfile
import os
from unittest.mock import patch

from exam_prep import App, Topic, PracticeSession, RevisionReminder


def test_app_import_export():
    app = App("Math", "Final Exam", "2024-06-15")
    topic = Topic("Algebra", 5, 80)
    session = PracticeSession(topic, 45, 90)
    reminder = RevisionReminder(topic, "2024-06-10")

    app.add_topic(topic)
    app.add_session(session)
    app.add_reminder(reminder)

    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "export.json")
        app.export(path)

        with open(path) as f:
            data = json.load(f)

        assert data["title"] == "Math"
        assert len(data["topics"]) == 1
        assert data["topics"][0]["name"] == "Algebra"
        assert len(data["sessions"]) == 1
        assert data["sessions"][0]["duration"] == 45
        assert len(data["reminders"]) == 1
        assert data["reminders"][0]["topic"] == "Algebra"

        app2 = App.from_json(data)
        assert app2.title == "Math"
        assert app2.due_date == "2024-06-15"
        assert app2.topics[0].name == "Algebra"
        assert app2.topics[0].difficulty == 5
        assert app2.sessions[0].duration == 45
        assert app2.sessions[0].score == 90
        assert app2.reminders[0].topic == "Algebra"
        assert app2.reminders[0].date == "2024-06-10"
