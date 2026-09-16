# === Stage 36: Add templates for quickly creating common records ===
# Project: ExamPrep
def create_topic(name, category, difficulty, duration_min):
    return {'name': name, 'category': category, 'difficulty': difficulty, 'duration_min': duration_min}

def create_session(topic, date, duration_min, score):
    return {'topic': topic, 'date': date, 'duration_min': duration_min, 'score': score}

def create_reminder(topic, date, duration_min):
    return {'topic': topic, 'date': date, 'duration_min': duration_min}
