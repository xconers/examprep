# === Stage 41: Add plain text import for a simple line-based format ===
# Project: ExamPrep
class LineImporter:
    """Reads a simple key=value text format, one entry per line.
    Supports comments starting with # and blank lines.
    Lines with an '=' sign are treated as key=value pairs.
    Values are stripped of whitespace.
    """

    def __init__(self, path: str):
        self.path = path
        self.data = {}

    def load(self) -> dict:
        with open(self.path, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if '=' in line:
                    key, value = line.split('=', 1)
                    self.data[key.strip()] = value.strip()
        return self.data

    def get(self, key: str, default=None):
        return self.data.get(key, default)
