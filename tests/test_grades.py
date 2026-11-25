import pytest

from tests.test_grades_busniess import assert_grades_stats


@pytest.mark.parametrize(
    ("filter_type", "filter_key"),
    [
        ("student_id", "student"),
        ("teacher_id", "teacher"),
        ("group_id", "group"),
    ],
    ids=["by_student", "by_teacher", "by_group"],
)
def test_get_grades_stats_with_filter(
    grades_service,
    grades_test_data,
    filter_type,
    filter_key,
):
    grades = grades_test_data["grades"]
    filter_value = grades_test_data[filter_key].id

    actual = grades_service.get_grades_stats(
        **{filter_type: filter_value}
    )

    assert_grades_stats(actual, grades)