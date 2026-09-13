# === Stage 26: Add weekly summary calculations ===
# Project: ExamPrep
def weekly_summary(weekly_scores):
    """Calculate weekly summary statistics from a list of weekly score records.
    
    Each record should be a dict with 'date', 'topic', 'score' keys.
    
    Returns a dict with total_score, avg_score, best_score, worst_score,
    and a list of topics sorted by average score.
    """
    if not weekly_scores:
        return {
            'total_score': 0,
            'avg_score': 0,
            'best_score': 0,
            'worst_score': 0,
            'topic_rankings': []
        }

    total_score = sum(record['score'] for record in weekly_scores)
    best_score = max(record['score'] for record in weekly_scores)
    worst_score = min(record['score'] for record in weekly_scores)
    avg_score = total_score / len(weekly_scores)

    topic_scores = {}
    for record in weekly_scores:
        topic = record['topic']
        if topic not in topic_scores:
            topic_scores[topic] = []
        topic_scores[topic].append(record['score'])

    topic_rankings = []
    for topic, scores in topic_scores.items():
        avg = sum(scores) / len(scores)
        topic_rankings.append({'topic': topic, 'avg_score': avg, 'count': len(scores)})

    topic_rankings.sort(key=lambda x: x['avg_score'], reverse=True)

    return {
        'total_score': total_score,
        'avg_score': avg_score,
        'best_score': best_score,
        'worst_score': worst_score,
        'topic_rankings': topic_rankings
    }
