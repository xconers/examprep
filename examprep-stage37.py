# === Stage 37: Add recommendations for the next useful action ===
# Project: ExamPrep
class ExamPrep:
    def __init__(self):
        self.topics = {}
        self.sessions = []
        self.scores = []
        self.reminders = []

    def add_topic(self, name, difficulty):
        self.topics[name] = {'difficulty': difficulty}

    def start_session(self, topic):
        self.sessions.append({'topic': topic, 'started': True, 'completed': False})

    def complete_session(self, index):
        if index < len(self.sessions):
            self.sessions[index]['completed'] = True

    def record_score(self, topic, score):
        self.scores.append({'topic': topic, 'score': score})

    def get_recommendations(self):
        if not self.sessions:
            return ['Pick a topic and start your first practice session.']
        incomplete = [s for s in self.sessions if not s['completed']]
        if not incomplete:
            return ['All sessions done! Review your scores and plan a revision cycle.']
        best_topic = max(incomplete, key=lambda s: s['topic'])
        return [f'Continue with "{best_topic["topic"]}" — it\'s your next priority.']

    def check_reminders(self):
        today = datetime.now().date()
        for r in self.reminders:
            if r['date'] == today and not r['done']:
                print(f"Reminder: Review {r['topic']} ({r['due_date']})")
                r['done'] = True

    def plan_revision(self, topic):
        avg_score = sum(s['score'] for s in self.scores if s['topic'] == topic) / len(self.scores) if self.scores else 0
        if avg_score < 70:
            return f'Revision needed: {topic} — average score {avg_score:.1f}'
        return f'You\'re ready: {topic} — average score {avg_score:.1f}'

    def get_progress(self):
        total = len(self.sessions)
        done = sum(1 for s in self.sessions if s['completed'])
        return f'Progress: {done}/{total} sessions completed'
