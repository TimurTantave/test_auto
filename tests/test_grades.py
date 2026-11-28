import pytest

from services.university.models.grades_stats_response import GradesStatsResponse


@pytest.mark.parametrize(
    ("grades", "expected"),
    [
        pytest.param(
            (),
            GradesStatsResponse(count=0, min=None, max=None, avg=None),
            id="student_without_grades",
        ),
        pytest.param(
            (0,),
            GradesStatsResponse(count=1, min=0, max=0, avg=0),
            id="single_zero",
        ),
        pytest.param(
            (2, 5, 0, 2),
            GradesStatsResponse(count=4, min=0, max=5, avg=2.25),
            id="repeated_grade_and_fractional_average",
        ),
    ],
)
def test_get_grades_stats_aggregates_student_grades(
    grades_service,
    test_student,
    test_teacher,
    grade_creator,
    grades,
    expected,
):
    for grade in grades:
        grade_creator(
            teacher_id=test_teacher.id,
            student_id=test_student.id,
            grade=grade,
        )

    actual = grades_service.get_grades_stats(student_id=test_student.id)

    assert actual == expected, (
        f"Unexpected grades stats for student {test_student.id} "
        f"with grades {grades}: "
        f"actual={actual}, expected={expected}"
    )