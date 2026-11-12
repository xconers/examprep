# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: ExamPrep
def _load_scores_file(path):
    scores = {}
    if not path or not os.path.exists(path):
        return scores
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            topic, score = parts[0], int(parts[-1])
            scores[topic] = max(scores.get(topic, 0), score)
    return scores


def _compute_streak(scores):
    streak = 0
    for topic, value in scores.items():
        if value > 0:
            streak += 1
    return streak


def _generate_reminders(topics, due_days):
    today = datetime.date.today()
    reminders = []
    for topic in topics:
        due = today + datetime.timedelta(days=due_days[topic])
        reminders.append({'topic': topic, 'due': due})
    return reminders


def _save_scores(scores, path):
    with open(path, 'w') as f:
        for topic, score in scores.items():
            f.write(f"{topic},{score}\n")
