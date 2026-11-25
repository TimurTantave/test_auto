
import pytest

from faker import Faker

from services.auth.auth_service import AuthService
from services.auth.models.login_request import LoginRequest
from services.auth.models.register_request import RegisterRequest
from services.university.models.teacher_request import TeacherRequest
from services.university.helpers.grades_helper import GradesHelper
from services.university.grades_service import GradesService
from services.university.models.base_student import DegreeEnum
from services.university.models.group_request import GroupRequest
from services.university.models.student_request import StudentRequest
from services.university.university_service import UniversityService

from utils.session_utils import ApiUtils


faker = Faker()


@pytest.fixture(scope="function")
def auth_api_utils_anonym():
    api_utils = ApiUtils(url=AuthService.SERVICE_URL)
    return api_utils


@pytest.fixture(scope="function")
def university_api_utils_anonym():
    api_utils = ApiUtils(url=UniversityService.UNIVERSITY_URL)
    return api_utils


@pytest.fixture(scope="function")
def auth_service_anonym(auth_api_utils_anonym):
    auth_service = AuthService(auth_api_utils_anonym)
    return auth_service


@pytest.fixture(scope="function")
def access_token(auth_service_anonym):
    username = faker.user_name()
    password = faker.password(
        length=30,
        special_chars=True,
        digits=True,
        upper_case=True,
        lower_case=True,
    )

    auth_service_anonym.register_user(
        register_request=RegisterRequest(
            username=username,
            password=password,
            password_repeat=password,
            email=faker.email(),
        )
    )

    login_response = auth_service_anonym.login_user(
        login_request=LoginRequest(
            username=username,
            password=password,
        )
    )

    return login_response.access_token


@pytest.fixture(scope="function")
def auth_api_utils_admin(access_token):
    api_utils = ApiUtils(
        url=AuthService.SERVICE_URL,
        headers={"Authorization": f"Bearer {access_token}"},
    )
    return api_utils


@pytest.fixture(scope="function")
def uni_api_utils_admin(access_token):
    api_utils = ApiUtils(
        url=UniversityService.UNIVERSITY_URL,
        headers={"Authorization": f"Bearer {access_token}"},
    )
    return api_utils


@pytest.fixture
def university_service(uni_api_utils_admin):
    return UniversityService(uni_api_utils_admin)


@pytest.fixture
def grades_service(uni_api_utils_admin):
    return GradesService(uni_api_utils_admin)


@pytest.fixture
def grades_helper(uni_api_utils_admin):
    return GradesHelper(uni_api_utils_admin)


# Test data fixtures


@pytest.fixture
def test_group(university_service):
    group_request = GroupRequest(
        name=f"Test group {faker.unique.word()}"
    )

    return university_service.create_group(group_request)


@pytest.fixture
def test_student(university_service, test_group):
    student_request = StudentRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.unique.email(),
        degree=DegreeEnum.BACHELOR,
        phone=f"+1{faker.numerify('##########')}",
        group_id=test_group.id,
    )

    return university_service.create_student(student_request)


@pytest.fixture
def grade_creator(grades_service):
    def create_grade(
        teacher_id: int,
        student_id: int,
        grade: int,
    ):
        response = grades_service.create_grade(
            teacher_id=teacher_id,
            student_id=student_id,
            grade=grade,
        )

        assert response.status_code == 201, (
            f"Failed to create grade: actual={response.status_code}, "
            f"expected=201. Response: {response.text}"
        )

        return response

    return create_grade

@pytest.fixture
def test_teacher(university_service):
    teacher_request = TeacherRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        subject="History",
    )
    return university_service.create_teacher(teacher_request)
@pytest.fixture
def group_factory(university_service):
    def create_group():
        group_request = GroupRequest(
            name=faker.unique.word()
        )
        return university_service.create_group(group_request)

    return create_group


@pytest.fixture
def student_factory(university_service):
    def create_student(group_id: int):
        student_request = StudentRequest(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.unique.email(),
            degree=DegreeEnum.BACHELOR,
            phone=f"+1{faker.numerify('##########')}",
            group_id=group_id,
        )
        return university_service.create_student(student_request)

    return create_student


@pytest.fixture
def teacher_factory(university_service):
    def create_teacher():
        teacher_request = TeacherRequest(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            subject="History",
        )
        return university_service.create_teacher(teacher_request)

    return create_teacher

@pytest.fixture
def grades_test_data(
    group_factory,
    student_factory,
    teacher_factory,
    grade_creator,
):
    group = group_factory()
    student = student_factory(group.id)
    teacher = teacher_factory()

    grades = [2, 4, 5]

    for grade in grades:
        grade_creator(
            teacher_id=teacher.id,
            student_id=student.id,
            grade=grade,
        )

    return {
        "group": group,
        "student": student,
        "teacher": teacher,
        "grades": grades,
    }