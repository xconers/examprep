# === Stage 4: Implement create operations for the primary records ===
# Project: ExamPrep
def create_topic(self, name, description, difficulty="medium", tags=None):
    if tags is None:
        tags = []
    topic = {
        "name": name,
        "description": description,
        "difficulty": difficulty,
        "tags": tags,
        "created_at": datetime.now().isoformat(),
    }
    self.topics[topic["name"]] = topic
    return topic

def create_session(self, topic_name, duration_minutes, start_time=None):
    if start_time is None:
        start_time = datetime.now().isoformat()
    session = {
        "topic": topic_name,
        "duration_minutes": duration_minutes,
        "started_at": start_time,
        "completed": False,
    }
    self.sessions.append(session)
    return session

def create_score(self, topic_name, score, total=None):
    if total is None:
        total = 100
    score_record = {
        "topic": topic_name,
        "score": score,
        "total": total,
        "date": datetime.now().isoformat(),
    }
    self.scores[topic_name] = score_record
    return score_record

def create_reminder(self, topic_name, due_date=None, priority="normal"):
    if due_date is None:
        due_date = datetime.now() + timedelta(days=7)
    reminder = {
        "topic": topic_name,
        "due_date": due_date.isoformat(),
        "priority": priority,
        "read": False,
    }
    self.reminders.append(reminder)
    return reminder
