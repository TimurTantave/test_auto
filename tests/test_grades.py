
import pytest

from services.university.models.grades_stats_response import GradesStatsResponse


def test_get_grades_stats_returns_response_model(grades_service):
    actual = grades_service.get_grades_stats()

    assert actual.count >= 0, (
        f"Unexpected count: actual={actual.count}, expected >= 0"
    )


@pytest.mark.parametrize(
    "filter_params",
    [
        {"student_id": 1},
        {"teacher_id": 1},
        {"group_id": 1},
    ],
    ids=["by_student", "by_teacher", "by_group"],
)
def test_get_grades_stats_with_filter(grades_service, filter_params):
    actual = grades_service.get_grades_stats(**filter_params)

    assert actual.count >= 0, (
        f"Unexpected count for filter {filter_params}: "
        f"actual={actual.count}, expected >= 0"
    )
