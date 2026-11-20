import pytest

from services.university.helpers.grades_helper import GradesHelper
from services.university.grades_service import GradesService
from services.auth.auth_service import AuthService
from services.auth.models.login_request import LoginRequest
from services.auth.models.register_request import RegisterRequest
from services.university.university_service import UniversityService
from utils.session_utils import ApiUtils
from faker import Faker

faker = Faker()


@pytest.fixture(scope="function", autouse=False)
def auth_api_utils_anonym():
    api_utils = ApiUtils(url=AuthService.SERVICE_URL)
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def university_api_utils_anonym():
    api_utils = ApiUtils(url=UniversityService.UNIVERSITY_URL)
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def auth_service_anonym(auth_api_utils_anonym):
    auth_service = AuthService(auth_api_utils_anonym)
    return auth_service


@pytest.fixture(scope="function", autouse=False)
def access_token(auth_service_anonym):
    username = faker.user_name()
    password = faker.password(length=30,
                              special_chars=True,
                              digits=True,
                              upper_case=True,
                              lower_case=True)
    auth_service_anonym.register_user(register_request=RegisterRequest(username=username,
                                                                       password=password,
                                                                       password_repeat=password,
                                                                       email=faker.email()))
    login_response = auth_service_anonym.login_user(login_request=LoginRequest(username=username, password=password))
    return login_response.access_token


@pytest.fixture(scope="function", autouse=False)
def auth_api_utils_admin(access_token):
    api_utils = ApiUtils(url=AuthService.SERVICE_URL, headers={"Authorization": f"Bearer {access_token}"})
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def uni_api_utils_admin(access_token):
    api_utils = ApiUtils(url=UniversityService.UNIVERSITY_URL, headers={"Authorization": f"Bearer {access_token}"})
    return api_utils


@pytest.fixture
def grades_service(uni_api_utils_admin):
    return GradesService(uni_api_utils_admin)


@pytest.fixture
def grades_helper(uni_api_utils_admin):
    return GradesHelper(uni_api_utils_admin)
