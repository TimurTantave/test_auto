
import pytest
import pytest_check as check


def assert_grades_stats(actual, grades):
    expected = {
        "count": len(grades),
        "min": min(grades),
        "max": max(grades),
        "avg": pytest.approx(sum(grades) / len(grades)),
    }

    check.equal(
        actual.count,
        expected["count"],
        f"Grades count mismatch: actual={actual.count}, expected={expected['count']}",
    )
    check.equal(
        actual.min,
        expected["min"],
        f"Minimum grade mismatch: actual={actual.min}, expected={expected['min']}",
    )
    check.equal(
        actual.max,
        expected["max"],
        f"Maximum grade mismatch: actual={actual.max}, expected={expected['max']}",
    )
    check.equal(
        actual.avg,
        expected["avg"],
        f"Average grade mismatch: actual={actual.avg}, expected={expected['avg']}",
    )


def test_get_grades_stats(grades_service, grades_test_data):
    student = grades_test_data["student"]
    grades = grades_test_data["grades"]

    actual = grades_service.get_grades_stats(
        student_id=student.id
    )

    assert_grades_stats(actual, grades)


def test_get_grades_stats_filter_by_student(
    grades_service,
    grades_test_data,
    student_factory,
    grade_creator,
):
    student_1 = grades_test_data["student"]
    teacher = grades_test_data["teacher"]
    group = grades_test_data["group"]
    grades = grades_test_data["grades"]

    student_2 = student_factory(group.id)

    grade_creator(
        teacher_id=teacher.id,
        student_id=student_2.id,
        grade=1,
    )

    actual = grades_service.get_grades_stats(
        student_id=student_1.id
    )

    assert_grades_stats(actual, grades)


def test_get_grades_stats_filter_by_teacher(
    grades_service,
    grades_test_data,
    teacher_factory,
    grade_creator,
):
    student = grades_test_data["student"]
    teacher_1 = grades_test_data["teacher"]
    grades = grades_test_data["grades"]

    teacher_2 = teacher_factory()

    grade_creator(
        teacher_id=teacher_2.id,
        student_id=student.id,
        grade=1,
    )

    actual = grades_service.get_grades_stats(
        teacher_id=teacher_1.id
    )

    assert_grades_stats(actual, grades)


def test_get_grades_stats_filter_by_group(
    grades_service,
    grades_test_data,
    group_factory,
    student_factory,
    grade_creator,
):
    group_1 = grades_test_data["group"]
    student_1 = grades_test_data["student"]
    teacher = grades_test_data["teacher"]
    grades = grades_test_data["grades"]

    group_2 = group_factory()
    student_2 = student_factory(group_2.id)

    grade_creator(
        teacher_id=teacher.id,
        student_id=student_2.id,
        grade=1,
    )

    actual = grades_service.get_grades_stats(
        group_id=group_1.id
    )

    assert_grades_stats(actual, grades)


def test_get_grades_stats_filter_by_multiple_params(
    grades_service,
    grades_test_data,
    student_factory,
    teacher_factory,
    grade_creator,
):
    group = grades_test_data["group"]
    student_1 = grades_test_data["student"]
    teacher_1 = grades_test_data["teacher"]
    grades = grades_test_data["grades"]

    student_2 = student_factory(group.id)
    teacher_2 = teacher_factory()

    grade_creator(
        teacher_id=teacher_2.id,
        student_id=student_1.id,
        grade=1,
    )

    grade_creator(
        teacher_id=teacher_1.id,
        student_id=student_2.id,
        grade=1,
    )

    actual = grades_service.get_grades_stats(
        student_id=student_1.id,
        teacher_id=teacher_1.id,
        group_id=group.id,
    )

    assert_grades_stats(actual, grades)
