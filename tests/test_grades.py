import pytest

from services.university.models.grades_stats_request import GradesStatsRequest
from services.university.models.grades_stats_response import GradesStatsResponse


def test_get_grades_stats_returns_response_model(grades_service):
    grades_request = GradesStatsRequest()

    actual = grades_service.get_grades_stats(grades_request)

    assert isinstance(actual, GradesStatsResponse), (
        f"Unexpected response type: actual={type(actual)}, "
        f"expected={GradesStatsResponse}"
    )

    assert actual.count >= 0, (
        f"Unexpected grades count: actual={actual.count}, expected>=0"
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
    grades_request = GradesStatsRequest(**filter_params)

    actual = grades_service.get_grades_stats(grades_request)

    assert isinstance(actual, GradesStatsResponse), (
        f"Unexpected response type: actual={type(actual)}, "
        f"expected={GradesStatsResponse}"
    )
