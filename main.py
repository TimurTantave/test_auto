from faker import Faker
import random

from helpers.Auth_helper import AuthorizationHelper
from services.university.helpers.group_helper import GroupHelper
from services.university.helpers.student_helper import StudentHelper
from helpers.user_helper import UserHelper
from utils.session_utils import ApiUtils

AUTH_URL = "http://127.0.0.1:8000"
UNIVERSITY_URL = "http://127.0.0.1:8001"

REGISTER_ENDPOINT = "/auth/register/"
LOGIN_ENDPOINT = "/auth/login/"
ME_ENDPOINT = "/users/me/"
GROUPS_ENDPOINT = "/groups/"
STUDENTS_ENDPOINT = "/students/"

faker = Faker()

username = faker.user_name()
password = "aZ!$123" + faker.word()

auth_helper = AuthorizationHelper(api_utils=ApiUtils(AUTH_URL))

response = auth_helper.post_reigister(
    data={"username": username,
          "password": password,
          "password_repeat": password,
          "email": faker.email()})

response = auth_helper.post_login(
    data={"username": username,
    "password": password}
)

access_token = response.json()["access_token"]

auth_admin_helper = AuthorizationHelper(api_utils=ApiUtils(AUTH_URL,headers={"Authorization": f"Bearer {access_token}"}))
admin_university_api = api_utils=ApiUtils(UNIVERSITY_URL,headers={"Authorization": f"Bearer {access_token}"})
group_admin_helper = GroupHelper(admin_university_api)
student_admin_helper = StudentHelper(admin_university_api)
user_admin_helper = UserHelper(ApiUtils(AUTH_URL, headers={"Authorization": f"Bearer {access_token}"}))

response = user_admin_helper.get_me()

response = group_admin_helper.post_group(json={"name": faker.name()},)
response = student_admin_helper.post_student(
                         json={"first_name": faker.first_name(),
                               "last_name": faker.last_name(),
                               "email": faker.email(),
                         "degree": random.choice(["Associate", "Bachelor", "Master", "Doctorate"]),
                               "phone": faker.numerify("+7##########"),
                               "group_id": response.json()["id"]})


