# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: ExamPrep
import unittest
from app import ExamPrep

class TestUpdateDelete(unittest.TestCase):
    def setUp(self):
        self.app = ExamPrep()

    def test_update_nonexistent_topic(self):
        with self.assertRaises(ValueError):
            self.app.update_topic("nonexistent", "math", 100)

    def test_delete_nonexistent_topic(self):
        with self.assertRaises(ValueError):
            self.app.delete_topic("nonexistent")

    def test_update_score(self):
        self.app.add_topic("math", 80)
        self.app.update_topic("math", 90)
        self.assertEqual(self.app.get_topic("math").score, 90)

    def test_delete_topic(self):
        self.app.add_topic("math", 80)
        self.app.delete_topic("math")
        with self.assertRaises(KeyError):
            self.app.get_topic("math")

    def test_update_invalid_score(self):
        self.app.add_topic("math", 80)
        with self.assertRaises(ValueError):
            self.app.update_topic("math", "invalid", 80)

    def test_delete_last_topic(self):
        self.app.add_topic("math", 80)
        self.app.add_topic("science", 70)
        self.app.delete_topic("math")
        self.assertEqual(self.app.get_topics(), ["science"])

if __name__ == "__main__":
    unittest.main()
