# === Stage 27: Add monthly summary calculations ===
# Project: ExamPrep
def monthly_summary(practice_log):
    """
    Compute a compact monthly summary from the practice_log list of dicts.
    Each entry: {"date": str, "topic": str, "score": int}
    Returns a dict: {"months": {month_name: {"sessions": int, "avg_score": float, "best_topic": str}},
    "overall_avg": float, "best_month": str}
    """
    from datetime import datetime
    month_data = {}
    total_score = 0.0
    for entry in practice_log:
        date = datetime.strptime(entry["date"], "%Y-%m-%d")
        month_key = date.strftime("%Y-%m")
        if month_key not in month_data:
            month_data[month_key] = {"sessions": 0, "scores": [], "topics": []}
        month_data[month_key]["sessions"] += 1
        month_data[month_key]["scores"].append(entry["score"])
        month_data[month_key]["topics"].append(entry["topic"])
        total_score += entry["score"]
    summary = {"months": {}, "overall_avg": 0.0, "best_month": ""}
    for month, info in month_data.items():
        avg = sum(info["scores"]) / len(info["scores"])
        best_topic = max(set(info["topics"]), key=lambda t: info["topics"].count(t))
        summary["months"][month] = {"sessions": info["sessions"], "avg_score": round(avg, 1), "best_topic": best_topic}
    if summary["months"]:
        summary["overall_avg"] = round(total_score / len(practice_log), 1)
        best_month = max(summary["months"], key=lambda m: summary["months"][m]["avg_score"])
        summary["best_month"] = best_month
    return summary
