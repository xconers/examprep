# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: ExamPrep
def validate_required(value, field_name):
    if not value or not value.strip():
        raise ValueError(f"{field_name} is required and cannot be empty.")
    return value.strip()

def validate_alphanumeric(value, field_name):
    if not value or not value.strip():
        raise ValueError(f"{field_name} is required and cannot be empty.")
    cleaned = value.strip()
    if not cleaned.isalnum():
        raise ValueError(f"{field_name} must contain only letters and digits.")
    return cleaned

def validate_short_text(value, field_name, max_length=50):
    if not value or not value.strip():
        raise ValueError(f"{field_name} is required and cannot be empty.")
    cleaned = value.strip()
    if len(cleaned) > max_length:
        raise ValueError(f"{field_name} must not exceed {max_length} characters.")
    return cleaned
