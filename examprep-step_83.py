# === Stage 83: Add regression tests for the final demo workflow ===
# Project: ExamPrep
def test_full_demo_workflow():
    from examprep import Planner

    planner = Planner("Math", ["Algebra", "Geometry"])

    planner.add_topic("Algebra", 5, 3)
    planner.add_topic("Geometry", 4, 4)

    planner.schedule_session("Algebra")
    planner.record_score("Algebra", 4)
    planner.schedule_session("Geometry")
    planner.record_score("Geometry", 3)

    planner.add_restriction("Algebra", "Monday", "Wednesday")
    planner.add_restriction("Geometry", "Tuesday", "Thursday")

    planner.set_revision("Algebra", 2)
    planner.set_revision("Geometry", 3)

    planner.set_target("Algebra", 4.5)
    planner.set_target("Geometry", 4.0)

    planner.update_progress("Algebra", 1)
    planner.update_progress("Geometry", 1)

    planner.mark_complete("Algebra")

    assert planner.topics["Algebra"]["status"] == "complete"
    assert planner.topics["Geometry"]["status"] == "in_progress"
    assert planner.topics["Geometry"]["progress"] == 2
    assert planner.topics["Algebra"]["progress"] == 1
    assert planner.topics["Algebra"]["target"] == 4.5
    assert planner.topics["Algebra"]["revision_days"] == 2
    assert planner.topics["Geometry"]["revision_days"] == 3
    assert planner.topics["Algebra"]["restrictions"] == ["Monday", "Wednesday"]
    assert planner.topics["Geometry"]["restrictions"] == ["Tuesday", "Thursday"]
    assert planner.topics["Algebra"]["scores"] == [4]
    assert planner.topics["Geometry"]["scores"] == [3]
