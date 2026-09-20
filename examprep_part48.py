# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: ExamPrep
import unittest
from exam_prep import create_topic, validate_score, create_session, create_reminder


class TestHelpers(unittest.TestCase):
    def test_create_topic(self):
        topic = create_topic("Algebra", "quadratic equations")
        self.assertEqual(topic.name, "Algebra")
        self.assertEqual(topic.description, "quadratic equations")

    def test_validate_score_pass(self):
        self.assertTrue(validate_score(85, "Algebra"))
        self.assertTrue(validate_score(0, "Algebra"))
        self.assertTrue(validate_score(100, "Algebra"))

    def test_validate_score_fail(self):
        self.assertFalse(validate_score(-1, "Algebra"))
        self.assertFalse(validate_score(101, "Algebra"))
        self.assertFalse(validate_score("N/A", "Algebra"))

    def test_create_session(self):
        session = create_session("Algebra", "quadratic equations", 45)
        self.assertEqual(session.topic, "Algebra")
        self.assertEqual(session.description, "quadratic equations")
        self.assertEqual(session.duration_minutes, 45)

    def test_create_reminder(self):
        reminder = create_reminder("Algebra", "quadratic equations", "2024-12-01")
        self.assertEqual(reminder.topic, "Algebra")
        self.assertEqual(reminder.description, "quadratic equations")
        self.assertEqual(reminder.date, "2024-12-01")


if __name__ == "__main__":
    unittest.main()
