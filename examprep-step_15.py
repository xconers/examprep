# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: ExamPrep
class Dispatcher:
    def __init__(self):
        self._handlers = {}

    def register(self, command, handler):
        self._handlers[command] = handler

    def dispatch(self, text):
        text = text.strip().lower()
        for cmd, handler in self._handlers.items():
            if text.startswith(cmd):
                args = text[len(cmd):].strip()
                return handler(args)
        return None
