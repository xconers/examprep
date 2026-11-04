# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: ExamPrep
def merge_imports(existing_lines, new_lines):
    """Merge new import lines into existing ones, dropping obvious duplicates.

    Handles three common cases:
      * identical `import x` lines
      * identical `from module import name` lines
      * `import a, b, c` where the new line only adds names already present
    """
    if not existing_lines:
        return new_lines

    normalized = []
    seen = set()

    def normalize(line):
        return line.strip().lstrip("from ").strip().split("import")[0].strip()

    for line in existing_lines:
        stripped = line.strip()
        if not stripped:
            continue
        prefix = stripped.split("import")[0].strip()
        if prefix in seen:
            continue
        seen.add(prefix)
        normalized.append(stripped)

    for line in new_lines:
        stripped = line.strip()
        if not stripped:
            continue
        prefix = stripped.split("import")[0].strip()
        if prefix in seen:
            continue
        seen.add(prefix)
        normalized.append(stripped)

    return normalized
