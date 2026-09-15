# === Stage 31: Add compact table rendering for long lists ===
# Project: ExamPrep
def render_compact_table(rows, header=None):
    if not rows:
        return "No data"
    cols = len(rows[0])
    widths = [max(len(str(row[i])) for row in rows) for i in range(cols)]
    if header:
        widths = [max(len(str(header[i])), widths[i]) for i in range(cols)]
    lines = []
    sep = "+".join("-" * (w + 2) for w in widths)
    lines.append(sep)
    if header:
        lines.append("| " + " | ".join(str(h).ljust(widths[i]) for i, h in enumerate(header)) + " |")
        lines.append(sep)
    for row in rows:
        lines.append("| " + " | ".join(str(cell).ljust(widths[i]) for i, cell in enumerate(row)) + " |")
    lines.append(sep)
    return "\n".join(lines)
