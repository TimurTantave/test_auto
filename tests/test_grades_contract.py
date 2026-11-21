import pytest

from services.university.models.grades_stats_response import GradesStatsResponse


def test_get_grades_stats_success(grades_helper):
    response = grades_helper.get_grades_stats(params={})

    assert response.status_code == 200, (
        f"Unexpected status code: actual={response.status_code}, expected=200. "
        f"Response: {response.text}"
    )


def test_get_grades_stats_response_model(grades_helper):
    response = grades_helper.get_grades_stats(params={})

    assert response.status_code == 200, (
        f"Unexpected status code: actual={response.status_code}, expected=200. "
        f"Response: {response.text}"
    )

    try:
        actual = GradesStatsResponse(**response.json())
    except Exception as error:
        pytest.fail(
            f"Response does not match GradesStatsResponse: {error}. "
            f"Response: {response.text}"
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
def test_get_grades_stats_with_filter(grades_helper, filter_params):
    response = grades_helper.get_grades_stats(params=filter_params)

    assert response.status_code == 200, (
        f"Unexpected status code for filter {filter_params}: "
        f"actual={response.status_code}, expected=200. "
        f"Response: {response.text}"
    )


def test_get_grades_stats_invalid_student_id(grades_helper):
    response = grades_helper.get_grades_stats(
        params={"student_id": "invalid"}
    )

    assert response.status_code == 422, (
        f"Unexpected status code: actual={response.status_code}, expected=422. "
        f"Response: {response.text}"
    )


def test_get_grades_stats_with_all_filters(grades_helper):
    params = {
        "student_id": 1,
        "teacher_id": 1,
        "group_id": 1,
    }

    response = grades_helper.get_grades_stats(params=params)

    assert response.status_code == 200, (
        f"Unexpected status code: actual={response.status_code}, "
        f"expected=200. Response: {response.text}"
    )


def test_get_grades_stats_with_nonexistent_student_id(grades_helper):
    response = grades_helper.get_grades_stats(
        params={"student_id": 999999999}
    )

    assert response.status_code == 200, (
        f"Unexpected status code: actual={response.status_code}, "
        f"expected=200. Response: {response.text}"
    )


def test_get_grades_stats_empty_result(grades_helper):
    response = grades_helper.get_grades_stats(
        params={"student_id": 999999999}
    )

    assert response.status_code == 200, (
        f"Unexpected status code: actual={response.status_code}, "
        f"expected=200. Response: {response.text}"
    )

    actual = GradesStatsResponse(**response.json())

    expected = {
        "count": 0,
        "min": None,
        "max": None,
        "avg": None,
    }

    actual_stats = actual.model_dump()

    assert actual_stats == expected, (
        f"Unexpected statistics: actual={actual_stats}, expected={expected}"
    )
