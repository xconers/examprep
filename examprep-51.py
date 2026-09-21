# === Stage 51: Add unit tests for search and filter behavior ===
# Project: ExamPrep
import unittest
from examprep.models import Topic, PracticeSession, Score, RevisionReminder

class TestSearchFilter(unittest.TestCase):
    def setUp(self):
        self.topics = [
            Topic("Algebra", "Basics", 5, "2024-01-01"),
            Topic("Calculus", "Limits", 7, "2024-01-05"),
            Topic("Algebra", "Functions", 8, "2024-01-10"),
        ]

    def test_search_by_name(self):
        result = Topic.search(self.topics, "Algebra")
        self.assertEqual(len(result), 2)
        self.assertIn("Algebra", [t.name for t in result])

    def test_search_case_insensitive(self):
        result = Topic.search(self.topics, "algebra")
        self.assertEqual(len(result), 2)

    def test_filter_by_difficulty(self):
        result = Topic.filter(self.topics, "hard")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Calculus")

    def test_filter_by_date(self):
        result = Topic.filter(self.topics, "2024-01-01")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Algebra")

    def test_filter_empty_result(self):
        result = Topic.filter(self.topics, "nonexistent")
        self.assertEqual(len(result), 0)

    def test_search_empty_list(self):
        result = Topic.search([], "test")
        self.assertEqual(len(result), 0)

    def test_filter_empty_list(self):
        result = Topic.filter([], "test")
        self.assertEqual(len(result), 0)

    def test_search_nonexistent_topic(self):
        result = Topic.search(self.topics, "Physics")
        self.assertEqual(len(result), 0)

    def test_filter_nonexistent_date(self):
        result = Topic.filter(self.topics, "2025-01-01")
        self.assertEqual(len(result), 0)

    def test_search_partial_match(self):
        result = Topic.search(self.topics, "Alg")
        self.assertEqual(len(result), 2)

    def test_filter_nonexistent_difficulty(self):
        result = Topic.filter(self.topics, "easy")
        self.assertEqual(len(result), 0)

if __name__ == "__main__":
    unittest.main()
