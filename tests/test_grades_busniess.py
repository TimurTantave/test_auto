
import pytest


def test_get_grades_stats_count(
    group_factory,
    student_factory,
    teacher_factory,
    grade_creator,
    grades_service,
):
    group = group_factory()
    student = student_factory(group.id)
    teacher = teacher_factory()

    for grade in [2, 4, 5]:
        grade_creator(
            teacher_id=teacher.id,
            student_id=student.id,
            grade=grade,
        )

    actual = grades_service.get_grades_stats(
        student_id=student.id
    ).count
    expected = 3

    assert actual == expected, (
        f"Grades count mismatch: actual={actual}, expected={expected}"
    )


def test_get_grades_stats_min(
    group_factory,
    student_factory,
    teacher_factory,
    grade_creator,
    grades_service,
):
    group = group_factory()
    student = student_factory(group.id)
    teacher = teacher_factory()

    for grade in [2, 4, 5]:
        grade_creator(
            teacher_id=teacher.id,
            student_id=student.id,
            grade=grade,
        )

    actual = grades_service.get_grades_stats(
        student_id=student.id
    ).min
    expected = 2

    assert actual == expected, (
        f"Minimum grade mismatch: actual={actual}, expected={expected}"
    )


def test_get_grades_stats_max(
    group_factory,
    student_factory,
    teacher_factory,
    grade_creator,
    grades_service,
):
    group = group_factory()
    student = student_factory(group.id)
    teacher = teacher_factory()

    for grade in [2, 4, 5]:
        grade_creator(
            teacher_id=teacher.id,
            student_id=student.id,
            grade=grade,
        )

    actual = grades_service.get_grades_stats(
        student_id=student.id
    ).max
    expected = 5

    assert actual == expected, (
        f"Maximum grade mismatch: actual={actual}, expected={expected}"
    )


def test_get_grades_stats_avg(
    group_factory,
    student_factory,
    teacher_factory,
    grade_creator,
    grades_service,
):
    group = group_factory()
    student = student_factory(group.id)
    teacher = teacher_factory()

    for grade in [2, 4, 5]:
        grade_creator(
            teacher_id=teacher.id,
            student_id=student.id,
            grade=grade,
        )

    actual = grades_service.get_grades_stats(
        student_id=student.id
    ).avg
    expected = 11 / 3

    assert actual == pytest.approx(expected), (
        f"Average grade mismatch: actual={actual}, expected={expected}"
    )


def test_get_grades_stats_filter_by_student(
    group_factory,
    student_factory,
    teacher_factory,
    grade_creator,
    grades_service,
):
    group = group_factory()
    student_1 = student_factory(group.id)
    student_2 = student_factory(group.id)
    teacher = teacher_factory()

    for grade in [2, 4]:
        grade_creator(
            teacher_id=teacher.id,
            student_id=student_1.id,
            grade=grade,
        )

    grade_creator(
        teacher_id=teacher.id,
        student_id=student_2.id,
        grade=5,
    )

    actual = grades_service.get_grades_stats(
        student_id=student_1.id
    ).count
    expected = 2

    assert actual == expected, (
        f"Student filter count mismatch: actual={actual}, expected={expected}"
    )


def test_get_grades_stats_filter_by_teacher(
    group_factory,
    student_factory,
    teacher_factory,
    grade_creator,
    grades_service,
):
    group = group_factory()
    student = student_factory(group.id)
    teacher_1 = teacher_factory()
    teacher_2 = teacher_factory()

    for grade in [2, 4]:
        grade_creator(
            teacher_id=teacher_1.id,
            student_id=student.id,
            grade=grade,
        )

    grade_creator(
        teacher_id=teacher_2.id,
        student_id=student.id,
        grade=5,
    )

    actual = grades_service.get_grades_stats(
        teacher_id=teacher_1.id
    ).count
    expected = 2

    assert actual == expected, (
        f"Teacher filter count mismatch: actual={actual}, expected={expected}"
    )


def test_get_grades_stats_filter_by_group(
    group_factory,
    student_factory,
    teacher_factory,
    grade_creator,
    grades_service,
):
    group_1 = group_factory()
    group_2 = group_factory()

    student_1 = student_factory(group_1.id)
    student_2 = student_factory(group_2.id)
    teacher = teacher_factory()

    for grade in [2, 4]:
        grade_creator(
            teacher_id=teacher.id,
            student_id=student_1.id,
            grade=grade,
        )

    grade_creator(
        teacher_id=teacher.id,
        student_id=student_2.id,
        grade=5,
    )

    actual = grades_service.get_grades_stats(
        group_id=group_1.id
    ).count
    expected = 2

    assert actual == expected, (
        f"Group filter count mismatch: actual={actual}, expected={expected}"
    )


def test_get_grades_stats_filter_by_multiple_params(
    group_factory,
    student_factory,
    teacher_factory,
    grade_creator,
    grades_service,
):
    group = group_factory()
    student_1 = student_factory(group.id)
    student_2 = student_factory(group.id)

    teacher_1 = teacher_factory()
    teacher_2 = teacher_factory()

    for grade in [2, 4]:
        grade_creator(
            teacher_id=teacher_1.id,
            student_id=student_1.id,
            grade=grade,
        )

    grade_creator(
        teacher_id=teacher_2.id,
        student_id=student_1.id,
        grade=5,
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
    expected = 2

    assert actual == expected, (
        f"Combined filters count mismatch: actual={actual}, expected={expected}"
    )
