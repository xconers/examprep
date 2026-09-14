# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: ExamPrep
def parse_date(date_str, fmt=None):
    """Parse a date string with clear error messages."""
    if not date_str or not isinstance(date_str, str):
        raise ValueError("Invalid date string: must be a non-empty string")
    date_str = date_str.strip()
    if not date_str:
        raise ValueError("Invalid date string: empty string after stripping")
    try:
        if fmt:
            return datetime.strptime(date_str, fmt)
        else:
            for pattern in ["%Y-%m-%d", "%m/%d/%Y", "%d-%m-%Y", "%Y/%m/%d"]:
                try:
                    return datetime.strptime(date_str, pattern)
                except ValueError:
                    continue
            raise ValueError(f"Unsupported date format: {date_str!r}")
    except ValueError:
        raise ValueError(f"Cannot parse date: {date_str!r}")
