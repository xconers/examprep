# === Stage 32: Add pagination helpers for long console output ===
# Project: ExamPrep
def page(lines, page_size=20):
    """Yield chunks of lines for paginated console output."""
    for i in range(0, len(lines), page_size):
        yield lines[i:i + page_size]

def print_page(lines, page_size=20, show_progress=True):
    """Print a single page of output and wait for user input before next page."""
    print()
    print(f"--- Page {1 if show_progress else 1} ---")
    for line in lines[:page_size]:
        print(line)
    if show_progress:
        input("Press Enter to continue...")
