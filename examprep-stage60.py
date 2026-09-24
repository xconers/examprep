# === Stage 60: Add saved views for frequently used filters ===
# Project: ExamPrep
class SavedView:
    def __init__(self, name, filters, columns):
        self.name = name
        self.filters = filters
        self.columns = columns

    def apply(self, planner):
        for key, value in self.filters.items():
            setattr(planner, key, value)
        planner.show_columns = list(self.columns)

    def __str__(self):
        return f"SavedView({self.name}, filters={self.filters}, columns={self.columns})"
