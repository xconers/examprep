# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: ExamPrep
def search(self, query, case_insensitive=True):
    """Search topics by keywords across key fields. Returns list of matching Topic objects."""
    if case_insensitive:
        query = query.lower()
    results = []
    for topic in self.topics:
        searchable = (
            topic.name.lower()
            + " "
            + topic.description.lower()
            + " "
            + topic.level.lower()
            + " "
            + topic.difficulty.lower()
            + " "
            + topic.category.lower()
        )
        if query in searchable:
            results.append(topic)
    return results
