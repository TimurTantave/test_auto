
import pytest


def test_get_grades_stats_count(grades_service, grades_test_data):
    student = grades_test_data["student"]
    expected = len(grades_test_data["grades"])

    actual = grades_service.get_grades_stats(
        student_id=student.id
    ).count

    assert actual == expected, (
        f"Grades count mismatch: actual={actual}, expected={expected}"
    )


def test_get_grades_stats_min(grades_service, grades_test_data):
    student = grades_test_data["student"]
    expected = min(grades_test_data["grades"])

    actual = grades_service.get_grades_stats(
        student_id=student.id
    ).min

    assert actual == expected, (
        f"Minimum grade mismatch: actual={actual}, expected={expected}"
    )


def test_get_grades_stats_max(grades_service, grades_test_data):
    student = grades_test_data["student"]
    expected = max(grades_test_data["grades"])

    actual = grades_service.get_grades_stats(
        student_id=student.id
    ).max

    assert actual == expected, (
        f"Maximum grade mismatch: actual={actual}, expected={expected}"
    )


def test_get_grades_stats_avg(grades_service, grades_test_data):
    student = grades_test_data["student"]
    grades = grades_test_data["grades"]
    expected = sum(grades) / len(grades)

    actual = grades_service.get_grades_stats(
        student_id=student.id
    ).avg

    assert actual == pytest.approx(expected), (
        f"Average grade mismatch: actual={actual}, expected={expected}"
    )


def test_get_grades_stats_filter_by_student(
    grades_service,
    grades_test_data,
    student_factory,
    grade_creator,
):
    student_1 = grades_test_data["student"]
    teacher = grades_test_data["teacher"]
    group = grades_test_data["group"]

    student_2 = student_factory(group.id)

    grade_creator(
        teacher_id=teacher.id,
        student_id=student_2.id,
        grade=1,
    )

    actual = grades_service.get_grades_stats(
        student_id=student_1.id
    ).count

    expected = 3

    assert actual == expected, (
        f"Student filter count mismatch: actual={actual}, expected={expected}"
    )


def test_get_grades_stats_filter_by_teacher(
    grades_service,
    grades_test_data,
    teacher_factory,
    grade_creator,
):
    student = grades_test_data["student"]
    teacher_1 = grades_test_data["teacher"]
    teacher_2 = teacher_factory()

    grade_creator(
        teacher_id=teacher_2.id,
        student_id=student.id,
        grade=1,
    )

    actual = grades_service.get_grades_stats(
        teacher_id=teacher_1.id
    ).count

    expected = 3

    assert actual == expected, (
        f"Teacher filter count mismatch: actual={actual}, expected={expected}"
    )


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

    group_2 = group_factory()
    student_2 = student_factory(group_2.id)

    grade_creator(
        teacher_id=teacher.id,
        student_id=student_2.id,
        grade=1,
    )

    actual = grades_service.get_grades_stats(
        group_id=group_1.id
    ).count

    expected = 3

    assert actual == expected, (
        f"Group filter count mismatch: actual={actual}, expected={expected}"
    )


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
    ).count

    expected = 3

    assert actual == expected, (
        f"Combined filters count mismatch: actual={actual}, expected={expected}"
    )
