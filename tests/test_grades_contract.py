import pytest


def test_get_grades_stats_success(grades_helper):
    response = grades_helper.get_grades_stats(params={})

    assert response.status_code == 200, (
        f"Unexpected status code: actual={response.status_code}, expected=200. "
        f"Response: {response.text}"
    )

    actual_fields = set(response.json().keys())
    expected_fields = {"count", "min", "max", "avg"}

    assert actual_fields == expected_fields, (
        f"Unexpected response fields: actual={actual_fields}, "
        f"expected={expected_fields}. Response: {response.text}"
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
