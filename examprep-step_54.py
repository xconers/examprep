# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: ExamPrep
def print_report(results):
    """Print a colorized summary of practice results."""
    if not results:
        return
    print("\033[1m" + "=" * 50 + "\033[0m")
    print("\033[1m" + "  EXAM PREP REPORT" + "\033[0m")
    print("=" * 50)
    for topic in results:
        name = topic["topic"]
        score = topic["score"]
        status = "passed" if score >= 80 else "needs more practice"
        color = "\033[32m" if status == "passed" else "\033[31m"
        print(color + f"  {name}: {score:.0f}% ({status})" + "\033[0m")
    print("=" * 50)
