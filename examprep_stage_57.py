# === Stage 57: Add structured result objects for command handlers ===
# Project: ExamPrep
class ExamResult:
    def __init__(self, topic_id, score, total, time_spent, correct_count):
        self.topic_id = topic_id
        self.score = score
        self.total = total
        self.time_spent = time_spent
        self.correct_count = correct_count

    def to_dict(self):
        return {
            "topic_id": self.topic_id,
            "score": self.score,
            "total": self.total,
            "time_spent": self.time_spent,
            "correct_count": self.correct_count,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            topic_id=data["topic_id"],
            score=data["score"],
            total=data["total"],
            time_spent=data["time_spent"],
            correct_count=data["correct_count"],
        )

    def __repr__(self):
        return (
            f"ExamResult(topic={self.topic_id}, score={self.score}/{self.total}, "
            f"time={self.time_spent}, correct={self.correct_count})"
        )
