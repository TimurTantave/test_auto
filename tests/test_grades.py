import pytest

@pytest.mark.parametrize(
    "filter_type",
    ["student_id", "teacher_id", "group_id"],
    ids=["by_student", "by_teacher", "by_group"],
)
def test_get_grades_stats_with_filter(
    grades_service,
    grades_test_data,
    filter_type,
):
    filter_params = {
        "student_id": grades_test_data["student"].id,
        "teacher_id": grades_test_data["teacher"].id,
        "group_id": grades_test_data["group"].id,
    }

    actual = grades_service.get_grades_stats(
        **{filter_type: filter_params[filter_type]}
    )

    assert actual.count == len(grades_test_data["grades"]), (
        f"Unexpected count for filter {filter_type}: "
        f"actual={actual.count}, expected={len(grades_test_data['grades'])}"
    )