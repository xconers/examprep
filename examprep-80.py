# === Stage 80: Polish user-facing messages, names, and examples for consistency ===
# Project: ExamPrep
def show_reminder_message(topic_name, days_until_due):
    if days_until_due <= 0:
        message = (
            f"Urgent: your revision for {topic_name} is due today. "
            "Open your session list and start practicing now."
        )
    elif days_until_due == 1:
        message = (
            f"Heads up: {topic_name} is due tomorrow. "
            "Spend a little time today to stay on track."
        )
    else:
        message = (
            f"Reminder: {topic_name} is due in {days_until_due} days. "
            "Plan a short practice session so it stays fresh."
        )
    return message

def show_score_message(score, target):
    if score >= target:
        label = "excellent"
        message = (
            f"Great work on your last practice session: {score} out of {target}. "
            "You are well prepared for this topic."
        )
    elif score >= target // 2:
        label = "good"
        message = (
            f"Nice progress: {score} out of {target}. "
            "Keep practicing to push your score even higher."
        )
    else:
        message = (
            f"You scored {score} out of {target}. "
            "Review the key points and try again to build confidence."
        )
    return message

def show_session_message(topic_name, minutes):
    message = (
        f"Thanks for your focus on {topic_name}. "
        f"You just practiced for {minutes} minutes."
    )
    if minutes < 15:
        message += " Aim for longer sessions to make real progress."
    elif minutes < 30:
        message += " A solid session. Try adding a few more questions next time."
    else:
        message += " Excellent dedication. Keep the momentum going."
    return message
