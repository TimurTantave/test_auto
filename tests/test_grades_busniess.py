import pytest

from services.university.models.grades_stats_response import GradesStatsResponse


@pytest.mark.parametrize(
    ("filters", "use_other_group", "expected"),
    [
        pytest.param(
            ("student_id",),
            False,
            GradesStatsResponse(count=2, min=2, max=4, avg=3),
            id="student_includes_multiple_teachers",
        ),
        pytest.param(
            ("teacher_id",),
            False,
            GradesStatsResponse(count=3, min=3, max=5, avg=4),
            id="teacher_includes_multiple_groups",
        ),
        pytest.param(
            ("group_id",),
            False,
            GradesStatsResponse(count=3, min=2, max=4, avg=3),
            id="group_includes_multiple_students_and_teachers",
        ),
        pytest.param(
            ("student_id", "teacher_id"),
            False,
            GradesStatsResponse(count=1, min=4, max=4, avg=4),
            id="student_and_teacher",
        ),
        pytest.param(
            ("student_id", "group_id"),
            True,
            GradesStatsResponse(count=0, min=None, max=None, avg=None),
            id="student_and_other_group",
        ),
        pytest.param(
            ("teacher_id", "group_id"),
            False,
            GradesStatsResponse(count=2, min=3, max=4, avg=3.5),
            id="teacher_and_group",
        ),
        pytest.param(
            ("student_id", "teacher_id", "group_id"),
            False,
            GradesStatsResponse(count=1, min=4, max=4, avg=4),
            id="all_filters_match",
        ),
        pytest.param(
            ("student_id", "teacher_id", "group_id"),
            True,
            GradesStatsResponse(count=0, min=None, max=None, avg=None),
            id="all_filters_with_other_group",
        ),
    ],
)
def test_get_grades_stats_applies_filters(
    grades_service,
    grades_filter_ids,
    filters,
    use_other_group,
    expected,
):
    ids, other_group_id = grades_filter_ids
    params = {field: ids[field] for field in filters}
    if use_other_group:
        params["group_id"] = other_group_id

    actual = grades_service.get_grades_stats(**params)

    assert actual == expected, (
        f"Unexpected grades stats for filters {params}: "
        f"actual={actual}, expected={expected}"
    )