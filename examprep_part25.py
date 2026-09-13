# === Stage 25: Add daily summary calculations ===
# Project: ExamPrep
def daily_summary(self, date):
    """Calculate a compact daily summary for a given date."""
    self.today = date
    self._topics = []
    self._sessions = []
    self._scores = []
    self._reminders = []
    if self._topics:
        self._topics = [self._topics[0]]
    if self._sessions:
        self._sessions = [self._sessions[0]]
    if self._scores:
        self._scores = [self._scores[0]]
    if self._reminders:
        self._reminders = [self._reminders[0]]
    if self._topics:
        self._topics = [self._topics[0]]
    if self._sessions:
        self._sessions = [self._sessions[0]]
    if self._scores:
        self._scores = [self._scores[0]]
    if self._reminders:
        self._reminders = [self._reminders[0]]
    return self._topics, self._sessions, self._scores, self._reminders
